# Hand Skeleton Detection Module
# Modul untuk mendeteksi kerangka tangan secara real-time menggunakan webcam

import cv2
import mediapipe as mp

def start_hand_skeleton():
    """
    Fungsi untuk memulai hand skeleton detection
    Mendeteksi tangan dan menggambar landmark (titik-titik kerangka tangan)
    """
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
    
    # Inisialisasi solusi Hands dari Mediapipe
    hands_detector = mp.solutions.hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )
    drawing_utils = mp.solutions.drawing_utils
    
    print("✅ Hand Skeleton Detection dimulai!")
    print("✋ Letakkan tangan Anda di depan kamera")
    print("⌨️  Tekan 'q' untuk keluar\n")
    
    while True:
        # Membaca frame dari kamera
        success, frame = cap.read()
        
        if not success:
            print("❌ Error: Tidak dapat membaca frame dari webcam")
            break
        
        # Mengubah warna frame dari BGR ke RGB karena Mediapipe menggunakan RGB
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        hand_obj = hands_detector.process(frameRGB)
        
        # Cek jika ada tangan yang terdeteksi
        hands_detected = 0
        if hand_obj.multi_hand_landmarks:
            hands_detected = len(hand_obj.multi_hand_landmarks)
            # Loop untuk setiap tangan yang terdeteksi
            for hand_landmarks in hand_obj.multi_hand_landmarks:
                # Menggambar landmark dan koneksinya
                drawing_utils.draw_landmarks(
                    frame, 
                    hand_landmarks,
                    mp.solutions.hands.HAND_CONNECTIONS,
                    drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                    drawing_utils.DrawingSpec(color=(255, 0, 0), thickness=2)
                )
        
        # Tampilkan jumlah tangan yang terdeteksi
        cv2.putText(frame, f"Tangan Terdeteksi: {hands_detected}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Menampilkan hasil di jendela "Hand Skeleton"
        cv2.imshow("Hand Skeleton - Tekan 'q' untuk keluar", frame)
        
        # Berhenti jika tombol 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Melepaskan kamera dan menutup semua jendela
    cap.release()
    cv2.destroyAllWindows()
    hands_detector.close()
    print("\n✅ Hand Skeleton Detection selesai!")

if __name__ == "__main__":
    start_hand_skeleton()
