# Computer Vision App - All-in-One
# Aplikasi Computer Vision dengan 3 fitur utama:
# 1. Face Detection
# 2. Hand Skeleton Detection
# 3. Face Recognition (dengan Create Dataset, Training, dan Recognition)

import os
import sys
import threading
import time

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_loading(message="Loading", duration=0.5):
    """Menampilkan animasi loading"""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    idx = 0
    while time.time() < end_time:
        print(f"\r{frames[idx % len(frames)]} {message}...", end="", flush=True)
        idx += 1
        time.sleep(0.1)
    print(f"\r✓ {message}... Selesai!" + " " * 20)

def loading_with_task(message, task_func, *args, **kwargs):
    """Menjalankan task dengan loading indicator"""
    result = {'done': False, 'data': None, 'error': None}
    
    def run_task():
        try:
            result['data'] = task_func(*args, **kwargs)
        except Exception as e:
            result['error'] = e
        finally:
            result['done'] = True
    
    # Jalankan task di thread terpisah
    thread = threading.Thread(target=run_task)
    thread.daemon = True
    thread.start()
    
    # Tampilkan loading animation
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    idx = 0
    while not result['done']:
        print(f"\r{frames[idx % len(frames)]} {message}...", end="", flush=True)
        idx += 1
        time.sleep(0.08)
    
    print(f"\r✓ {message}... Selesai!" + " " * 20)
    
    if result['error']:
        raise result['error']
    
    return result['data']

def print_banner():
    """Menampilkan banner aplikasi"""
    print("=" * 60)
    print(" " * 15 + "COMPUTER VISION APP")
    print(" " * 15 + "All-in-One Solution")
    print("=" * 60)

def print_menu():
    """Menampilkan menu utama"""
    print("\n📋 MENU UTAMA:")
    print("1. Face Detection (Deteksi Wajah)")
    print("2. Hand Skeleton Detection (Deteksi Kerangka Tangan)")
    print("3. Face Recognition - Create Dataset (Buat Dataset Wajah)")
    print("4. Face Recognition - Training Model (Latih Model)")
    print("5. Face Recognition - Recognize Face (Kenali Wajah)")
    print("0. Keluar")
    print("-" * 60)

def run_face_detection():
    """Menjalankan Face Detection"""
    print("\n🎯 Mempersiapkan Face Detection...")
    try:
        # Import dengan loading indicator
        print("⏳ Memuat modul...")
        from face_detection import start_face_detection
        
        print("📷 Menginisialisasi kamera...")
        print("Tekan 'q' untuk kembali ke menu utama\n")
        
        start_face_detection()
    except ImportError as e:
        print(f"❌ Error: Module tidak ditemukan - {e}")
        print("Pastikan file face_detection.py ada di folder yang sama")
    except Exception as e:
        print(f"❌ Error: {e}")
    input("\nTekan Enter untuk kembali ke menu...")

def run_hand_skeleton():
    """Menjalankan Hand Skeleton Detection"""
    print("\n✋ Mempersiapkan Hand Skeleton Detection...")
    try:
        # Import dengan loading indicator
        print("⏳ Memuat modul MediaPipe (ini mungkin memakan waktu beberapa detik)...")
        from hand_skeleton import start_hand_skeleton
        
        print("📷 Menginisialisasi kamera...")
        print("Tekan 'q' untuk kembali ke menu utama\n")
        
        start_hand_skeleton()
    except ImportError as e:
        print(f"❌ Error: Module tidak ditemukan - {e}")
        print("Pastikan file hand_skeleton.py ada di folder yang sama")
    except Exception as e:
        print(f"❌ Error: {e}")
    input("\nTekan Enter untuk kembali ke menu...")

def run_create_dataset():
    """Menjalankan Face Recognition - Create Dataset"""
    print("\n📸 Face Recognition - Create Dataset")
    print("=" * 60)
    
    try:
        person_name = input("Masukkan nama orang: ").strip()
        if not person_name:
            print("❌ Nama tidak boleh kosong!")
            input("\nTekan Enter untuk kembali ke menu...")
            return
        
        person_id = input("Masukkan ID (angka): ").strip()
        if not person_id.isdigit():
            print("❌ ID harus berupa angka!")
            input("\nTekan Enter untuk kembali ke menu...")
            return
        
        from face_create_dataset import create_dataset
        create_dataset(int(person_id), person_name)
        
        # Reminder untuk training
        print("\n" + "=" * 60)
        print("⚠️  PENTING! LANGKAH SELANJUTNYA:")
        print("=" * 60)
        print("📌 Dataset berhasil dibuat, tapi model BELUM diperbarui!")
        print("📌 Agar sistem bisa mengenali wajah baru, Anda HARUS:")
        print("   1️⃣  Kembali ke menu utama")
        print("   2️⃣  Pilih menu 4 (Training Model)")
        print("   3️⃣  Tunggu training selesai")
        print("   4️⃣  Baru bisa gunakan Face Recognition (menu 5)")
        print("\n💡 Tips: Training hanya perlu dilakukan sekali setelah")
        print("   menambah/mengubah dataset!")
        print("=" * 60)
    except ImportError as e:
        print(f"❌ Error: Module tidak ditemukan - {e}")
        print("Pastikan file face_create_dataset.py ada di folder yang sama")
    except Exception as e:
        print(f"❌ Error: {e}")
    input("\nTekan Enter untuk kembali ke menu...")

def run_training():
    """Menjalankan Face Recognition - Training"""
    print("\n🧠 Face Recognition - Training Model")
    print("=" * 60)
    print("Memulai training model...")
    print("Proses ini akan memakan waktu beberapa detik.\n")
    
    try:
        from face_training import train_model
        train_model()
    except ImportError as e:
        print(f"❌ Error: Module tidak ditemukan - {e}")
        print("Pastikan file face_training.py ada di folder yang sama")
    except Exception as e:
        print(f"❌ Error: {e}")
    input("\nTekan Enter untuk kembali ke menu...")

def run_recognition():
    """Menjalankan Face Recognition"""
    print("\n🔍 Face Recognition - Recognize Face")
    print("=" * 60)
    
    # Cek apakah model sudah ada
    import os
    if not os.path.exists("face-model.yml"):
        print("❌ Error: Model belum ada!")
        print("\n💡 Langkah yang harus dilakukan:")
        print("   1️⃣  Buat dataset dulu (menu 3)")
        print("   2️⃣  Training model (menu 4)")
        print("   3️⃣  Baru bisa gunakan Face Recognition")
        input("\nTekan Enter untuk kembali ke menu...")
        return
    
    # Cek jumlah orang di database vs peringatan
    try:
        import json
        if os.path.exists("names_database.json"):
            with open("names_database.json", "r") as f:
                names_dict = json.load(f)
                num_people = len(names_dict)
                if num_people > 0:
                    print(f"📊 Dataset berisi {num_people} orang: {', '.join(names_dict.values())}")
                    print("\n⚠️  PERHATIAN:")
                    print("   Jika Anda baru saja menambah dataset baru,")
                    print("   pastikan sudah melakukan TRAINING ULANG (menu 4)!")
                    print("   Jika tidak, sistem akan salah mengenali wajah.\n")
    except:
        pass
    
    print("⏳ Memuat modul dan model...")
    print("📷 Menginisialisasi kamera...")
    print("Tekan 'q' untuk kembali ke menu utama\n")
    
    try:
        from face_recognition_module import start_recognition
        start_recognition()
    except ImportError as e:
        print(f"❌ Error: Module tidak ditemukan - {e}")
        print("Pastikan file face_recognition_module.py ada di folder yang sama")
    except Exception as e:
        print(f"❌ Error: {e}")
    input("\nTekan Enter untuk kembali ke menu...")

def main():
    """Fungsi utama aplikasi"""
    while True:
        clear_screen()
        print_banner()
        print_menu()
        
        choice = input("Pilih menu (0-5): ").strip()
        
        if choice == '1':
            run_face_detection()
        elif choice == '2':
            run_hand_skeleton()
        elif choice == '3':
            run_create_dataset()
        elif choice == '4':
            run_training()
        elif choice == '5':
            run_recognition()
        elif choice == '0':
            clear_screen()
            print("\n👋 Terima kasih telah menggunakan Computer Vision App!")
            print("=" * 60)
            sys.exit(0)
        else:
            print("\n❌ Pilihan tidak valid! Silakan pilih 0-5.")
            input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
