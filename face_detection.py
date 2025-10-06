# Face Detection Module
# Modul untuk mendeteksi wajah secara real-time menggunakan webcam

import cv2

def start_face_detection():
    """
    Fungsi untuk memulai face detection
    Mendeteksi wajah dan menggambar persegi merah di sekitarnya
    """
    # Path ke file model Haar Cascade
    cascade_path = "haarcascade_frontalface_default.xml"
    
    # Load classifier
    clf = cv2.CascadeClassifier(cascade_path)
    
    # Cek apakah model berhasil dimuat
    if clf.empty():
        print("❌ Error: Tidak dapat memuat haarcascade_frontalface_default.xml")
        print("Pastikan file ada di folder yang sama dengan script ini.")
        return
    
    # Inisialisasi webcam, ID 0 biasanya untuk webcam bawaan
    # Optimasi: gunakan CAP_DSHOW di Windows untuk startup lebih cepat
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    # Set buffer size lebih kecil untuk mengurangi delay
    camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    
    # Cek apakah webcam berhasil dibuka
    if not camera.isOpened():
        print("❌ Error: Tidak dapat mengakses webcam")
        return
    
    # Warm-up kamera (buang beberapa frame pertama yang biasanya gelap)
    for _ in range(5):
        camera.read()
    
    print("✅ Face Detection dimulai!")
    print("📹 Webcam aktif - Wajah akan dideteksi dengan persegi merah")
    print("⌨️  Tekan 'q' untuk keluar\n")
    
    while True:
        # Membaca frame dari kamera
        ret, frame = camera.read()
        
        if not ret:
            print("❌ Error: Tidak dapat membaca frame dari webcam")
            break
        
        # Mengubah frame menjadi grayscale untuk proses deteksi
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Mendeteksi wajah dalam gambar grayscale
        faces = clf.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            flags=cv2.CASCADE_SCALE_IMAGE,
            minSize=(30, 30)
        )
        
        # Menggambar persegi di setiap wajah yang terdeteksi
        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 0, 255), 2)
        
        # Tampilkan jumlah wajah yang terdeteksi
        cv2.putText(frame, f"Wajah Terdeteksi: {len(faces)}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Menampilkan hasil di jendela "Face Detection"
        cv2.imshow("Face Detection - Tekan 'q' untuk keluar", frame)
        
        # Berhenti jika tombol 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Melepaskan kamera dan menutup semua jendela
    camera.release()
    cv2.destroyAllWindows()
    print("\n✅ Face Detection selesai!")

if __name__ == "__main__":
    start_face_detection()
