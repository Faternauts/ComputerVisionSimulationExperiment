# Face Recognition Module
# Modul untuk mengenali wajah secara real-time menggunakan model yang telah dilatih

import cv2
import json
import os

def load_names_database():
    """Memuat database nama dari file JSON"""
    if os.path.exists("names_database.json"):
        with open("names_database.json", "r") as f:
            names_dict = json.load(f)
            # Konversi key menjadi integer untuk kemudahan akses
            return {int(k): v for k, v in names_dict.items()}
    return {}

def start_recognition():
    """
    Fungsi untuk memulai face recognition
    Mendeteksi dan mengenali wajah menggunakan model yang telah dilatih
    """
    # Cek apakah model sudah ada
    model_path = "face-model.yml"
    if not os.path.exists(model_path):
        print(f"❌ Error: Model '{model_path}' tidak ditemukan!")
        print("💡 Silakan latih model terlebih dahulu menggunakan menu 4")
        return
    
    # Load recognizer dan model
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    try:
        recognizer.read(model_path)
        print(f"✅ Model '{model_path}' berhasil dimuat")
    except Exception as e:
        print(f"❌ Error saat memuat model: {e}")
        return
    
    # Load face cascade
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    if faceCascade.empty():
        print("❌ Error: Tidak dapat memuat haarcascade_frontalface_default.xml")
        return
    
    # Load database nama
    names_dict = load_names_database()
    if not names_dict:
        print("⚠️  Warning: Database nama kosong")
        print("💡 Nama akan ditampilkan sebagai ID")
    else:
        print(f"✅ Database nama dimuat: {len(names_dict)} orang")
        for id, name in names_dict.items():
            print(f"   - ID {id}: {name}")
    
    # Font untuk menampilkan text
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # Inisialisasi webcam dengan optimasi
    # Gunakan CAP_DSHOW di Windows untuk startup lebih cepat
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    # Set buffer size lebih kecil untuk mengurangi delay
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    
    if not cap.isOpened():
        print("❌ Error: Tidak dapat mengakses webcam")
        return
    
    # Warm-up kamera (buang beberapa frame pertama)
    for _ in range(5):
        cap.read()
    
    print("\n✅ Face Recognition dimulai!")
    print("📹 Webcam aktif - Sistem akan mengenali wajah yang telah dilatih")
    print("⌨️  Tekan 'q' untuk keluar\n")
    
    while True:
        # Baca frame dari webcam
        ret, frame = cap.read()
        
        if not ret:
            print("❌ Error: Tidak dapat membaca frame dari webcam")
            break
        
        # Konversi ke grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Deteksi wajah
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        # Proses setiap wajah yang terdeteksi
        for (x, y, w, h) in faces:
            # Gambar persegi biru di sekitar wajah
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            
            # Prediksi identitas wajah
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            
            # Tentukan nama berdasarkan confidence
            # Semakin KECIL confidence = Semakin BAGUS (lebih yakin)
            if confidence < 100:
                # Wajah dikenali dengan baik
                if id in names_dict:
                    displayName = names_dict[id]
                else:
                    displayName = f"ID: {id}"
                
                # Tentukan kualitas match berdasarkan confidence
                if confidence < 50:
                    match_quality = "Excellent"
                    color = (0, 255, 0)  # Hijau untuk match sempurna
                elif confidence < 70:
                    match_quality = "Good"
                    color = (0, 200, 200)  # Cyan untuk match bagus
                else:
                    match_quality = "Fair"
                    color = (0, 255, 255)  # Kuning untuk match cukup
                
                confidenceText = f"Conf: {round(confidence, 1)} ({match_quality})"
            else:
                # Wajah tidak dikenali (confidence terlalu tinggi)
                displayName = "Unknown"
                confidenceText = f"Conf: {round(confidence, 1)}"
                color = (0, 0, 255)  # Merah untuk unknown
            
            # Tampilkan nama
            cv2.putText(frame, str(displayName), (x + 5, y - 10), 
                        font, 0.8, color, 2)
            
            # Tampilkan confidence dengan penjelasan
            cv2.putText(frame, str(confidenceText), (x + 5, y + h + 25), 
                        font, 0.6, color, 2)
        
        # Tampilkan jumlah wajah terdeteksi
        cv2.putText(frame, f"Wajah Terdeteksi: {len(faces)}", (10, 30), 
                    font, 0.7, (0, 255, 0), 2)
        
        # Tampilkan frame
        cv2.imshow("Face Recognition - Tekan 'q' untuk keluar", frame)
        
        # Keluar jika 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Bersihkan
    cap.release()
    cv2.destroyAllWindows()
    print("\n✅ Face Recognition selesai!")

if __name__ == "__main__":
    start_recognition()
