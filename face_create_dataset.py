# Face Recognition - Create Dataset Module
# Modul untuk membuat dataset wajah dengan mengambil foto dari webcam

import cv2
import os
import json

def load_names_database():
    """Memuat database nama dari file JSON"""
    if os.path.exists("names_database.json"):
        with open("names_database.json", "r") as f:
            return json.load(f)
    return {}

def save_names_database(names_dict):
    """Menyimpan database nama ke file JSON"""
    with open("names_database.json", "w") as f:
        json.dump(names_dict, f, indent=4)

def create_dataset(person_id, person_name):
    """
    Fungsi untuk membuat dataset wajah
    
    Parameters:
    - person_id: ID unik untuk orang tersebut (integer)
    - person_name: Nama orang yang akan dideteksi
    """
    # Konfigurasi jumlah foto
    TOTAL_PHOTOS = 150
    
    # Konfirmasi kesiapan
    print("\n" + "=" * 60)
    print("📸 PERSIAPAN PENGAMBILAN FOTO")
    print("=" * 60)
    print(f"👤 Nama: {person_name}")
    print(f"🆔 ID: {person_id}")
    print(f"📷 Jumlah foto yang akan diambil: {TOTAL_PHOTOS} foto")
    print("\n💡 TIPS UNTUK HASIL TERBAIK:")
    print("   ✓ Pastikan pencahayaan cukup terang")
    print("   ✓ Hadapkan wajah langsung ke kamera")
    print("   ✓ Gerakkan kepala ke berbagai arah:")
    print("     - Kiri, kanan, atas, bawah")
    print("     - Sedikit miring")
    print("     - Berbagai ekspresi wajah")
    print("   ✓ Jarak ideal: 50-100 cm dari kamera")
    print("\n⏱️  Estimasi waktu: ~2-3 menit")
    print("=" * 60)
    
    # Tanya konfirmasi
    ready = input("\n❓ Apakah Anda sudah siap? (y/n): ").strip().lower()
    
    if ready != 'y' and ready != 'yes':
        print("\n⚠️  Pengambilan foto dibatalkan.")
        print("💡 Silakan persiapkan diri dan coba lagi nanti.")
        return
    
    print("\n⏳ Mempersiapkan kamera...")
    
    # Load classifier
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    # Cek apakah model berhasil dimuat
    if faceCascade.empty():
        print("❌ Error: Tidak dapat memuat haarcascade_frontalface_default.xml")
        return
    
    # Inisialisasi webcam dengan optimasi
    # Gunakan CAP_DSHOW di Windows untuk startup lebih cepat
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    # Set buffer size lebih kecil untuk mengurangi delay
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    
    # Cek apakah webcam berhasil dibuka
    if not cap.isOpened():
        print("❌ Error: Tidak dapat mengakses webcam")
        return
    
    # Warm-up kamera (buang beberapa frame pertama)
    for _ in range(5):
        cap.read()
    
    # Buat folder dataset jika belum ada
    dataset_path = "dataset/"
    if not os.path.exists(dataset_path):
        os.mkdir(dataset_path)
        print(f"📁 Folder '{dataset_path}' dibuat")
    
    # Simpan nama ke database
    names_db = load_names_database()
    names_db[str(person_id)] = person_name
    save_names_database(names_db)
    print(f"💾 Nama '{person_name}' disimpan dengan ID {person_id}")
    
    count = 0  # Penghitung untuk nama file gambar
    
    print(f"\n✅ Pengambilan foto dimulai!")
    print(f"📸 Target: {TOTAL_PHOTOS} foto")
    print("💡 Gerakkan kepala Anda ke berbagai arah untuk hasil lebih baik")
    print("⌨️  Tekan 'q' untuk membatalkan\n")
    
    while True:
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
            
            # Simpan gambar wajah yang dipotong (ROI - Region of Interest)
            count += 1
            filename = dataset_path + "Person-" + str(person_id) + "-" + str(count) + ".jpg"
            cv2.imwrite(filename, gray[y:y + h, x:x + w])
            
            # Tampilkan progress dengan persentase
            percentage = int((count / TOTAL_PHOTOS) * 100)
            print(f"✓ Foto {count}/{TOTAL_PHOTOS} tersimpan ({percentage}%)", end='\r')
        
        # Tampilkan progress di frame
        progress_text = f"Foto: {count}/{TOTAL_PHOTOS} ({int((count/TOTAL_PHOTOS)*100)}%)"
        cv2.putText(frame, progress_text, (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"Nama: {person_name}", (10, 60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Tampilkan instruksi
        if count < 30:
            instruction = "Hadap depan"
        elif count < 60:
            instruction = "Tengok kiri/kanan"
        elif count < 90:
            instruction = "Kepala atas/bawah"
        elif count < 120:
            instruction = "Miring kiri/kanan"
        else:
            instruction = "Berbagai ekspresi"
        
        cv2.putText(frame, instruction, (10, 90), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        
        # Tampilkan frame
        cv2.imshow("Create Dataset - Tekan 'q' untuk batal", frame)
        
        # Keluar jika 'q' ditekan atau sudah mencapai target
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("\n\n⚠️  Dibatalkan oleh pengguna")
            print(f"📊 Total foto yang tersimpan: {count}/{TOTAL_PHOTOS}")
            break
        elif count >= TOTAL_PHOTOS:
            print(f"\n\n🎉 BERHASIL! {TOTAL_PHOTOS} foto untuk '{person_name}' telah tersimpan")
            print(f"📁 Lokasi: {dataset_path}")
            print(f"🆔 ID: {person_id}")
            break
    
    # Bersihkan
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Contoh penggunaan
    name = input("Masukkan nama: ")
    id_num = int(input("Masukkan ID (angka): "))
    create_dataset(id_num, name)
