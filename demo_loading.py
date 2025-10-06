"""
Demo Loading Indicator
Menampilkan contoh animasi loading yang ditambahkan ke aplikasi
"""

import time
import threading

def show_loading_demo(message="Loading", duration=2):
    """Demo animasi loading"""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    idx = 0
    while time.time() < end_time:
        print(f"\r{frames[idx % len(frames)]} {message}...", end="", flush=True)
        idx += 1
        time.sleep(0.1)
    print(f"\r✓ {message}... Selesai!" + " " * 20)

def simulate_camera_init():
    """Simulasi inisialisasi kamera"""
    time.sleep(1.5)  # Simulasi waktu loading
    return True

def loading_with_task_demo(message, task_func):
    """Demo loading dengan task"""
    result = {'done': False, 'data': None}
    
    def run_task():
        result['data'] = task_func()
        result['done'] = True
    
    thread = threading.Thread(target=run_task)
    thread.daemon = True
    thread.start()
    
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    idx = 0
    while not result['done']:
        print(f"\r{frames[idx % len(frames)]} {message}...", end="", flush=True)
        idx += 1
        time.sleep(0.08)
    
    print(f"\r✓ {message}... Selesai!" + " " * 20)
    return result['data']

if __name__ == "__main__":
    print("=" * 60)
    print(" " * 15 + "DEMO LOADING INDICATOR")
    print("=" * 60)
    
    print("\n1️⃣ Loading Sederhana:")
    show_loading_demo("Memuat modul", 2)
    
    print("\n2️⃣ Loading dengan Task (Simulasi):")
    result = loading_with_task_demo("Menginisialisasi kamera", simulate_camera_init)
    
    print("\n3️⃣ Simulasi Menu Face Detection:")
    print("\n🎯 Mempersiapkan Face Detection...")
    show_loading_demo("Memuat modul", 1)
    loading_with_task_demo("Menginisialisasi kamera", simulate_camera_init)
    print("📷 Kamera siap!")
    
    print("\n4️⃣ Simulasi Menu Hand Skeleton:")
    print("\n✋ Mempersiapkan Hand Skeleton Detection...")
    show_loading_demo("Memuat modul MediaPipe", 2)
    loading_with_task_demo("Menginisialisasi kamera", simulate_camera_init)
    print("✋ Kamera siap untuk deteksi tangan!")
    
    print("\n" + "=" * 60)
    print("Demo selesai! Ini adalah loading indicator yang sekarang")
    print("ada di aplikasi Computer Vision Anda.")
    print("=" * 60)
