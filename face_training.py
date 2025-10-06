# Face Recognition - Training Module
# Modul untuk melatih model pengenalan wajah dari dataset

import cv2
import numpy as np
import os
from PIL import Image

def getImagesAndLabels(path="dataset/"):
    """
    Membaca gambar dari folder dataset dan mengekstrak ID
    
    Returns:
    - faceSamples: List berisi gambar wajah
    - ids: Array berisi ID yang sesuai dengan setiap gambar
    """
    # Dapatkan semua path file gambar di folder dataset
    if not os.path.exists(path):
        print(f"❌ Error: Folder '{path}' tidak ditemukan!")
        print("💡 Silakan buat dataset terlebih dahulu menggunakan menu 3")
        return [], np.array([])
    
    imagePaths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
    
    if len(imagePaths) == 0:
        print(f"❌ Error: Tidak ada file gambar (.jpg) di folder '{path}'")
        print("💡 Silakan buat dataset terlebih dahulu menggunakan menu 3")
        return [], np.array([])
    
    faceSamples = []
    ids = []
    
    # Load face cascade untuk deteksi wajah
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    if faceCascade.empty():
        print("❌ Error: Tidak dapat memuat haarcascade_frontalface_default.xml")
        return [], np.array([])
    
    print(f"📁 Memproses {len(imagePaths)} gambar dari folder '{path}'...")
    
    processed = 0
    for imagePath in imagePaths:
        try:
            # Buka gambar dan konversi ke grayscale
            PIL_img = Image.open(imagePath).convert('L')  # 'L' untuk grayscale
            img_numpy = np.array(PIL_img, 'uint8')
            
            # Ekstrak ID dari nama file (format: Person-ID-count.jpg)
            filename = os.path.split(imagePath)[-1]
            id = int(filename.split("-")[1])
            
            # Deteksi wajah dari gambar
            faces = faceCascade.detectMultiScale(img_numpy)
            
            # Tambahkan setiap wajah yang terdeteksi ke dataset
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y+h, x:x+w])
                ids.append(id)
                processed += 1
            
            # Progress indicator
            print(f"  ✓ Diproses: {len(faceSamples)} wajah dari {len(imagePaths)} gambar", end='\r')
            
        except Exception as e:
            print(f"\n⚠️  Warning: Gagal memproses {imagePath}: {e}")
            continue
    
    print(f"\n✅ Total {len(faceSamples)} wajah berhasil diproses dari {len(np.unique(ids))} orang")
    
    return faceSamples, np.array(ids, dtype="int32")

def train_model():
    """
    Melatih model LBPH Face Recognizer dan menyimpannya
    """
    print("\n" + "="*60)
    print("🧠 FACE RECOGNITION - TRAINING MODEL")
    print("="*60)
    
    # Inisialisasi recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    
    print("\n[INFO] Mulai training model...")
    print("[INFO] Ini akan memakan waktu beberapa detik. Mohon tunggu...\n")
    
    # Dapatkan data training
    faces, ids = getImagesAndLabels("dataset/")
    
    if len(faces) == 0 or len(ids) == 0:
        print("\n❌ Training dibatalkan: Tidak ada data untuk dilatih")
        return
    
    # Train model
    try:
        recognizer.train(faces, ids)
        print("\n[INFO] Training selesai!")
        
        # Simpan model
        model_path = 'face-model.yml'
        recognizer.write(model_path)
        
        print(f"\n✅ Model berhasil disimpan sebagai '{model_path}'")
        print(f"📊 Statistik:")
        print(f"   - Jumlah orang: {len(np.unique(ids))}")
        print(f"   - Total foto: {len(faces)}")
        print(f"   - ID yang dilatih: {sorted(np.unique(ids))}")
        
    except Exception as e:
        print(f"\n❌ Error saat training model: {e}")

if __name__ == "__main__":
    train_model()
