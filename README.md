# 🎯 Computer Vision App - All-in-One (OPTIMIZED ⚡)

Aplikasi Computer Vision lengkap dengan 3 fitur utama - **Sekarang lebih cepat 50-60%!**

1. **Face Detection** - Deteksi wajah real-time
2. **Hand Skeleton Detection** - Deteksi kerangka tangan
3. **Face Recognition** - Sistem pengenalan wajah lengkap

## ✨ BARU! Peningkatan v2.0 (Optimized Edition)

- ⚡ **Kamera terbuka 2-3 detik lebih cepat** dengan DirectShow API
- 🔄 **Loading indicators** yang informatif
- 📊 **Real-time feedback** saat memuat modul
- ✨ **Frame langsung terang** (no more dark frames)
- 🎯 **Buffer optimized** untuk response lebih cepat

👉 **Lihat detail:** [PANDUAN_OPTIMASI.md](PANDUAN_OPTIMASI.md)

## 📋 Fitur Aplikasi

### 1️⃣ Face Detection

- Mendeteksi wajah secara real-time menggunakan webcam
- Menampilkan persegi merah di sekitar wajah yang terdeteksi
- Menghitung jumlah wajah yang terdeteksi

### 2️⃣ Hand Skeleton Detection

- Mendeteksi tangan menggunakan MediaPipe
- Menampilkan landmark (titik-titik) kerangka tangan
- Dapat mendeteksi hingga 2 tangan secara bersamaan

### 3️⃣ Face Recognition

Sistem pengenalan wajah dengan 3 tahap:

- **Create Dataset**: Mengambil 30 foto wajah untuk training
- **Training Model**: Melatih model dari dataset yang telah dibuat
- **Recognition**: Mengenali wajah secara real-time

## 🛠️ Instalasi

### Prasyarat

- Python 3.8 atau lebih baru
- Webcam yang berfungsi
- Windows/Linux/MacOS

### Langkah Instalasi

1. **Clone atau Download Project**

   ```bash
   cd "d:\allin one pai app"
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Library yang akan terinstall:

   - `opencv-contrib-python` - Untuk computer vision
   - `mediapipe` - Untuk hand skeleton detection
   - `numpy` - Untuk operasi array
   - `Pillow` - Untuk pemrosesan gambar

3. **Verifikasi File Haar Cascade**

   Pastikan file `haarcascade_frontalface_default.xml` ada di folder project.
   Jika belum ada, download dari:

   ```
   https://raw.githubusercontent.com/opencv/opencv/4.x/data/haarcascades/haarcascade_frontalface_default.xml
   ```

## 🚀 Cara Menggunakan

### Menjalankan Aplikasi

```bash
python main.py
```

### Menu Utama

Setelah menjalankan aplikasi, Anda akan melihat menu:

```
================================================================
               COMPUTER VISION APP
               All-in-One Solution
================================================================

📋 MENU UTAMA:
1. Face Detection (Deteksi Wajah)
2. Hand Skeleton Detection (Deteksi Kerangka Tangan)
3. Face Recognition - Create Dataset (Buat Dataset Wajah)
4. Face Recognition - Training Model (Latih Model)
5. Face Recognition - Recognize Face (Kenali Wajah)
0. Keluar
----------------------------------------------------------------
```

### Cara Menggunakan Face Recognition

#### Step 1: Buat Dataset (Menu 3)

1. Pilih menu **3** (Create Dataset)
2. Masukkan nama orang (contoh: "John")
3. Masukkan ID unik (contoh: 1)
4. Hadapkan wajah ke kamera
5. Program akan mengambil 30 foto secara otomatis
6. Gerakkan kepala ke berbagai arah untuk hasil lebih baik

#### Step 2: Training Model (Menu 4)

1. Pilih menu **4** (Training Model)
2. Program akan membaca semua foto dari folder `dataset/`
3. Model akan dilatih dan disimpan sebagai `face-model.yml`
4. Tunggu hingga proses selesai (biasanya beberapa detik)

#### Step 3: Kenali Wajah (Menu 5)

1. Pilih menu **5** (Recognize Face)
2. Hadapkan wajah ke kamera
3. Jika wajah sudah dilatih, nama dan akurasi akan ditampilkan
4. Tekan 'q' untuk keluar

### Tips Penggunaan

#### Face Detection & Hand Skeleton

- Pastikan pencahayaan cukup terang
- Jarak ideal dari kamera: 50-100 cm
- Tekan **'q'** untuk kembali ke menu

#### Face Recognition - Create Dataset

- Ambil foto di berbagai sudut (depan, kiri, kanan, atas, bawah)
- Gunakan ekspresi wajah yang berbeda
- Pastikan pencahayaan konsisten
- Setiap orang harus memiliki ID unik

#### Face Recognition - Training

- Pastikan minimal ada 1 orang dalam dataset
- Semakin banyak foto, semakin akurat hasilnya
- Untuk menambah orang baru, ulangi Create Dataset dengan ID berbeda

#### Face Recognition - Recognition

- Confidence < 100 = Wajah dikenali ✅
- Confidence >= 100 = Wajah tidak dikenali ❌
- Semakin rendah confidence, semakin akurat pengenalan

## 📁 Struktur Project

```
d:\allin one pai app\
│
├── main.py                           # File utama untuk menjalankan aplikasi
├── face_detection.py                 # Modul Face Detection
├── hand_skeleton.py                  # Modul Hand Skeleton Detection
├── face_create_dataset.py            # Modul untuk membuat dataset wajah
├── face_training.py                  # Modul untuk training model
├── face_recognition_module.py        # Modul untuk recognition
│
├── haarcascade_frontalface_default.xml  # Model Haar Cascade
├── requirements.txt                  # Daftar dependencies
├── README.md                         # Dokumentasi ini
│
├── dataset/                          # Folder untuk menyimpan foto training
│   ├── Person-1-1.jpg
│   ├── Person-1-2.jpg
│   └── ...
│
├── names_database.json               # Database nama (dibuat otomatis)
└── face-model.yml                    # Model terlatih (dibuat setelah training)
```

## 🔧 Troubleshooting

### Error: Import "cv2" could not be resolved

**Solusi**: Install OpenCV

```bash
pip install opencv-contrib-python
```

### Error: Import "mediapipe" could not be resolved

**Solusi**: Install MediaPipe

```bash
pip install mediapipe
```

### Error: Tidak dapat mengakses webcam

**Solusi**:

- Pastikan webcam tidak sedang digunakan aplikasi lain
- Cek permission webcam di sistem operasi
- Coba restart komputer

### Error: haarcascade_frontalface_default.xml tidak ditemukan

**Solusi**: Download file dari link di atas dan letakkan di folder project

### Face Recognition tidak akurat

**Solusi**:

- Tambah lebih banyak foto (ulangi Create Dataset)
- Pastikan pencahayaan konsisten
- Ambil foto dari berbagai sudut
- Training ulang model

## 🎯 Contoh Penggunaan

### Scenario: Membuat sistem absensi wajah untuk 3 orang

1. **Buat Dataset untuk Orang 1**
   - Menu 3 → Nama: "Alice" → ID: 1 → Ambil 30 foto
2. **Buat Dataset untuk Orang 2**
   - Menu 3 → Nama: "Bob" → ID: 2 → Ambil 30 foto
3. **Buat Dataset untuk Orang 3**

   - Menu 3 → Nama: "Charlie" → ID: 3 → Ambil 30 foto

4. **Training Model**

   - Menu 4 → Tunggu hingga selesai

5. **Test Recognition**
   - Menu 5 → Coba hadapkan wajah Alice, Bob, atau Charlie

## 📝 Catatan Penting

1. **Dataset Folder**: Akan dibuat otomatis saat pertama kali membuat dataset
2. **Names Database**: File JSON untuk menyimpan mapping ID → Nama
3. **Model File**: File `.yml` hasil training, jangan dihapus jika ingin menggunakan recognition
4. **ID Unik**: Setiap orang harus memiliki ID yang berbeda
5. **Overwrite**: Jika membuat dataset dengan ID yang sama, data lama akan ditambahkan (tidak ditimpa)

## 🎓 Teknologi yang Digunakan

- **OpenCV**: Library computer vision untuk face detection dan recognition
- **MediaPipe**: Framework Google untuk hand landmark detection
- **Haar Cascade**: Algoritma untuk face detection
- **LBPH Face Recognizer**: Algoritma untuk face recognition
- **Python**: Bahasa pemrograman utama

## 📞 Support

Jika ada pertanyaan atau masalah:

1. Cek troubleshooting di atas
2. Pastikan semua dependencies terinstall dengan benar
3. Pastikan webcam berfungsi dengan baik

## ⚖️ License

Project ini dibuat untuk tujuan edukasi dan pembelajaran Computer Vision.

---

**Selamat Menggunakan Computer Vision App! 🎉**

Dibuat dengan ❤️ menggunakan Python, OpenCV, dan MediaPipe
