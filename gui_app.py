# Computer Vision App - GUI Version
# Aplikasi Computer Vision dengan GUI menggunakan Tkinter

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import threading
import os
import sys

class ComputerVisionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Vision App - All-in-One")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Set icon jika ada
        try:
            self.root.iconbitmap('icon.ico')
        except:
            pass
        
        # Warna tema
        self.bg_color = "#2c3e50"
        self.fg_color = "#ecf0f1"
        self.btn_color = "#3498db"
        self.btn_hover = "#2980b9"
        
        self.root.configure(bg=self.bg_color)
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg="#34495e", height=80)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tk.Label(
            header_frame,
            text="🎯 COMPUTER VISION APP",
            font=("Arial", 20, "bold"),
            bg="#34495e",
            fg="#ecf0f1"
        )
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(
            header_frame,
            text="All-in-One Solution - GUI Edition",
            font=("Arial", 10),
            bg="#34495e",
            fg="#bdc3c7"
        )
        subtitle_label.pack()
        
        # Main content frame
        content_frame = tk.Frame(self.root, bg=self.bg_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        # Section 1: Detection
        self.create_section(content_frame, "📹 DETECTION", [
            ("Face Detection", "Deteksi wajah real-time", self.run_face_detection, "#e74c3c"),
            ("Hand Skeleton", "Deteksi kerangka tangan", self.run_hand_skeleton, "#9b59b6")
        ])
        
        # Separator
        ttk.Separator(content_frame, orient='horizontal').pack(fill=tk.X, pady=15)
        
        # Section 2: Face Recognition
        self.create_section(content_frame, "🔐 FACE RECOGNITION", [
            ("Create Dataset", "Buat dataset wajah baru", self.run_create_dataset, "#27ae60"),
            ("Training Model", "Latih model pengenalan", self.run_training, "#f39c12"),
            ("Recognize Face", "Kenali wajah real-time", self.run_recognition, "#16a085")
        ])
        
        # Separator
        ttk.Separator(content_frame, orient='horizontal').pack(fill=tk.X, pady=15)
        
        # Info panel
        info_frame = tk.Frame(content_frame, bg="#34495e", relief=tk.RIDGE, bd=2)
        info_frame.pack(fill=tk.X, pady=10)
        
        info_label = tk.Label(
            info_frame,
            text="💡 Tips: Pastikan webcam tersedia dan pencahayaan cukup terang",
            font=("Arial", 9),
            bg="#34495e",
            fg="#ecf0f1",
            wraplength=500,
            justify=tk.LEFT
        )
        info_label.pack(padx=15, pady=10)
        
        # Exit button
        exit_btn = tk.Button(
            content_frame,
            text="❌ KELUAR",
            command=self.exit_app,
            font=("Arial", 16, "bold"),
            bg="#c0392b",
            fg="white",
            activebackground="#a93226",
            cursor="hand2",
            relief=tk.RAISED,
            bd=6,
            height=3,
            width=25,
            padx=10,
            pady=10
        )
        exit_btn.pack(fill=tk.X, pady=16)
        
        # Footer
        footer_label = tk.Label(
            self.root,
            text="Version 2.2 - Optimized Edition | 2025",
            font=("Arial", 8),
            bg=self.bg_color,
            fg="#7f8c8d"
        )
        footer_label.pack(side=tk.BOTTOM, pady=5)
    
    def create_section(self, parent, title, buttons):
        """Membuat section dengan judul dan tombol-tombol"""
        # Section title
        title_label = tk.Label(
            parent,
            text=title,
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg="#ecf0f1",
            anchor=tk.W
        )
        title_label.pack(fill=tk.X, pady=(10, 10))
        
        # Buttons
        for btn_text, description, command, color in buttons:
            btn_frame = tk.Frame(parent, bg=self.bg_color)
            btn_frame.pack(fill=tk.X, pady=5)
            
            btn = tk.Button(
                btn_frame,
                text=btn_text,
                command=command,
                font=("Arial", 11, "bold"),
                bg=color,
                fg="white",
                activebackground=self.adjust_color(color, -20),
                cursor="hand2",
                relief=tk.RAISED,
                bd=2,
                height=2,
                width=20
            )
            btn.pack(side=tk.LEFT, padx=(0, 10))
            
            desc_label = tk.Label(
                btn_frame,
                text=description,
                font=("Arial", 9),
                bg=self.bg_color,
                fg="#bdc3c7",
                anchor=tk.W
            )
            desc_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    def adjust_color(self, hex_color, adjustment):
        """Adjust color brightness"""
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        r = max(0, min(255, r + adjustment))
        g = max(0, min(255, g + adjustment))
        b = max(0, min(255, b + adjustment))
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def run_in_thread(self, func):
        """Jalankan fungsi di thread terpisah agar GUI tidak freeze"""
        thread = threading.Thread(target=func, daemon=True)
        thread.start()
    
    def run_face_detection(self):
        """Jalankan Face Detection"""
        def task():
            try:
                from face_detection import start_face_detection
                messagebox.showinfo("Face Detection", "Kamera akan terbuka.\nTekan 'q' untuk keluar.")
                start_face_detection()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
        
        self.run_in_thread(task)
    
    def run_hand_skeleton(self):
        """Jalankan Hand Skeleton Detection"""
        def task():
            try:
                from hand_skeleton import start_hand_skeleton
                messagebox.showinfo("Hand Skeleton", "Kamera akan terbuka.\nTekan 'q' untuk keluar.")
                start_hand_skeleton()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
        
        self.run_in_thread(task)
    
    def run_create_dataset(self):
        """Jalankan Create Dataset"""
        # Dialog untuk input nama
        person_name = simpledialog.askstring(
            "Create Dataset",
            "Masukkan nama orang:",
            parent=self.root
        )
        
        if not person_name:
            return
        
        # Dialog untuk input ID
        person_id = simpledialog.askinteger(
            "Create Dataset",
            "Masukkan ID (angka):",
            parent=self.root,
            minvalue=1,
            maxvalue=999
        )
        
        if not person_id:
            return
        
        # Konfirmasi
        confirm = messagebox.askyesno(
            "Konfirmasi",
            f"Nama: {person_name}\nID: {person_id}\n\n"
            f"Akan mengambil 150 foto.\n"
            f"Estimasi waktu: 2-3 menit.\n\n"
            f"Apakah Anda sudah siap?"
        )
        
        if not confirm:
            return
        
        def task():
            try:
                from face_create_dataset import create_dataset
                # Buat fungsi wrapper untuk skip konfirmasi
                import cv2
                import os
                import json
                
                # Load classifier
                faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                if faceCascade.empty():
                    messagebox.showerror("Error", "Tidak dapat memuat haarcascade file!")
                    return
                
                # Init kamera
                cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
                
                if not cap.isOpened():
                    messagebox.showerror("Error", "Tidak dapat mengakses webcam!")
                    return
                
                # Warm-up
                for _ in range(5):
                    cap.read()
                
                # Buat folder dataset
                dataset_path = "dataset/"
                if not os.path.exists(dataset_path):
                    os.mkdir(dataset_path)
                
                # Simpan nama
                names_db = {}
                if os.path.exists("names_database.json"):
                    with open("names_database.json", "r") as f:
                        names_db = json.load(f)
                
                names_db[str(person_id)] = person_name
                with open("names_database.json", "w") as f:
                    json.dump(names_db, f, indent=4)
                
                TOTAL_PHOTOS = 150
                count = 0
                
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
                    
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        count += 1
                        filename = f"{dataset_path}Person-{person_id}-{count}.jpg"
                        cv2.imwrite(filename, gray[y:y + h, x:x + w])
                    
                    # Progress
                    progress_text = f"Foto: {count}/{TOTAL_PHOTOS} ({int((count/TOTAL_PHOTOS)*100)}%)"
                    cv2.putText(frame, progress_text, (10, 30), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    cv2.putText(frame, f"Nama: {person_name}", (10, 60), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    
                    # Instruksi
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
                    
                    cv2.imshow("Create Dataset - Tekan 'q' untuk batal", frame)
                    
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    elif count >= TOTAL_PHOTOS:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                
                if count >= TOTAL_PHOTOS:
                    messagebox.showinfo(
                        "Berhasil!",
                        f"✅ {TOTAL_PHOTOS} foto untuk '{person_name}' berhasil disimpan!\n\n"
                        f"⚠️ JANGAN LUPA:\n"
                        f"Lakukan TRAINING MODEL (menu Training Model)\n"
                        f"sebelum menggunakan Face Recognition!"
                    )
                else:
                    messagebox.showwarning(
                        "Dibatalkan",
                        f"Foto yang tersimpan: {count}/{TOTAL_PHOTOS}"
                    )
            
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
        
        self.run_in_thread(task)
    
    def run_training(self):
        """Jalankan Training Model"""
        confirm = messagebox.askyesno(
            "Training Model",
            "Akan memulai training model.\n"
            "Proses ini akan memakan waktu beberapa detik.\n\n"
            "Lanjutkan?"
        )
        
        if not confirm:
            return
        
        def task():
            try:
                from face_training import train_model
                train_model()
                messagebox.showinfo(
                    "Berhasil!",
                    "✅ Training model berhasil!\n\n"
                    "Sekarang Anda bisa menggunakan Face Recognition."
                )
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
        
        self.run_in_thread(task)
    
    def run_recognition(self):
        """Jalankan Face Recognition"""
        # Cek apakah model sudah ada
        if not os.path.exists("face-model.yml"):
            messagebox.showerror(
                "Error",
                "Model belum ada!\n\n"
                "Langkah yang harus dilakukan:\n"
                "1. Buat dataset (Create Dataset)\n"
                "2. Training model (Training Model)\n"
                "3. Baru bisa Face Recognition"
            )
            return
        
        def task():
            try:
                from face_recognition_module import start_recognition
                messagebox.showinfo("Face Recognition", "Kamera akan terbuka.\nTekan 'q' untuk keluar.")
                start_recognition()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
        
        self.run_in_thread(task)
    
    def exit_app(self):
        """Keluar dari aplikasi"""
        if messagebox.askyesno("Keluar", "Apakah Anda yakin ingin keluar?"):
            self.root.destroy()
            sys.exit(0)

def main():
    root = tk.Tk()
    app = ComputerVisionGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
