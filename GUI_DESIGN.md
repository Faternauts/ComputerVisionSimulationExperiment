# 🎨 GUI Design Mockup - Computer Vision App

## 📱 **Main Window Design**

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║         🎯 COMPUTER VISION APP                            ║
║         All-in-One Solution - GUI Edition                 ║
║                                                           ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  📹 DETECTION                                             ║
║  ┌────────────────────┐                                  ║
║  │ Face Detection     │  Deteksi wajah real-time         ║
║  └────────────────────┘                                  ║
║  ┌────────────────────┐                                  ║
║  │ Hand Skeleton      │  Deteksi kerangka tangan         ║
║  └────────────────────┘                                  ║
║                                                           ║
║  ─────────────────────────────────────────────────────── ║
║                                                           ║
║  🔐 FACE RECOGNITION                                      ║
║  ┌────────────────────┐                                  ║
║  │ Create Dataset     │  Buat dataset wajah baru         ║
║  └────────────────────┘                                  ║
║  ┌────────────────────┐                                  ║
║  │ Training Model     │  Latih model pengenalan          ║
║  └────────────────────┘                                  ║
║  ┌────────────────────┐                                  ║
║  │ Recognize Face     │  Kenali wajah real-time          ║
║  └────────────────────┘                                  ║
║                                                           ║
║  ─────────────────────────────────────────────────────── ║
║                                                           ║
║  ┌─────────────────────────────────────────────────────┐ ║
║  │ 💡 Tips: Pastikan webcam tersedia dan pencahayaan  │ ║
║  │     cukup terang                                    │ ║
║  └─────────────────────────────────────────────────────┘ ║
║                                                           ║
║  ┌─────────────────────────────────────────────────────┐ ║
║  │                    ❌ KELUAR                         │ ║
║  └─────────────────────────────────────────────────────┘ ║
║                                                           ║
║         Version 2.2 - Optimized Edition | 2025            ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 🎨 **Color Scheme:**

### **Background:**

- Main Background: `#2c3e50` (Dark Blue Gray)
- Header: `#34495e` (Darker Blue Gray)
- Info Panel: `#34495e`

### **Text:**

- Primary Text: `#ecf0f1` (Almost White)
- Secondary Text: `#bdc3c7` (Light Gray)
- Footer Text: `#7f8c8d` (Medium Gray)

### **Buttons:**

- Face Detection: `#e74c3c` (Red)
- Hand Skeleton: `#9b59b6` (Purple)
- Create Dataset: `#27ae60` (Green)
- Training Model: `#f39c12` (Orange)
- Recognize Face: `#16a085` (Teal)
- Exit Button: `#c0392b` (Dark Red)

---

## 📋 **Dialog Examples:**

### **1. Input Nama (Create Dataset):**

```
┌────────────────────────────────────┐
│  Create Dataset                    │
├────────────────────────────────────┤
│                                    │
│  Masukkan nama orang:              │
│  ┌──────────────────────────────┐ │
│  │ [Fathan________________]     │ │
│  └──────────────────────────────┘ │
│                                    │
│        [  OK  ]    [ Cancel ]      │
│                                    │
└────────────────────────────────────┘
```

### **2. Input ID:**

```
┌────────────────────────────────────┐
│  Create Dataset                    │
├────────────────────────────────────┤
│                                    │
│  Masukkan ID (angka):              │
│  ┌──────────────────────────────┐ │
│  │ [1_____________________]     │ │
│  └──────────────────────────────┘ │
│                                    │
│        [  OK  ]    [ Cancel ]      │
│                                    │
└────────────────────────────────────┘
```

### **3. Konfirmasi Ready:**

```
┌────────────────────────────────────┐
│  Konfirmasi                        │
├────────────────────────────────────┤
│                                    │
│  Nama: Fathan                      │
│  ID: 1                             │
│                                    │
│  Akan mengambil 150 foto.          │
│  Estimasi waktu: 2-3 menit.        │
│                                    │
│  Apakah Anda sudah siap?           │
│                                    │
│        [  Yes  ]    [  No  ]       │
│                                    │
└────────────────────────────────────┘
```

### **4. Success Message:**

```
┌────────────────────────────────────┐
│  ℹ️ Berhasil!                      │
├────────────────────────────────────┤
│                                    │
│  ✅ 150 foto untuk 'Fathan'        │
│     berhasil disimpan!             │
│                                    │
│  ⚠️ JANGAN LUPA:                   │
│  Lakukan TRAINING MODEL            │
│  (menu Training Model) sebelum     │
│  menggunakan Face Recognition!     │
│                                    │
│            [  OK  ]                │
│                                    │
└────────────────────────────────────┘
```

### **5. Error Message:**

```
┌────────────────────────────────────┐
│  ❌ Error                          │
├────────────────────────────────────┤
│                                    │
│  Model belum ada!                  │
│                                    │
│  Langkah yang harus dilakukan:     │
│  1. Buat dataset (Create Dataset)  │
│  2. Training model (Training Model)│
│  3. Baru bisa Face Recognition     │
│                                    │
│            [  OK  ]                │
│                                    │
└────────────────────────────────────┘
```

---

## 🎯 **Button States:**

### **Normal:**

```
┌────────────────────┐
│  Face Detection    │
└────────────────────┘
Color: #e74c3c (Red)
```

### **Hover:**

```
┌────────────────────┐
│  Face Detection    │  ← Cursor berubah jadi "hand"
└────────────────────┘
Color: Slightly darker
Cursor: hand2
```

### **Pressed:**

```
┌────────────────────┐
│  Face Detection    │  ← Sedikit "push down" effect
└────────────────────┘
Relief: SUNKEN
```

---

## 📐 **Layout Specifications:**

### **Window Size:**

- Width: `600px`
- Height: `700px`
- Resizable: `No` (Fixed size)

### **Margins & Padding:**

- Main padding: `30px` (horizontal), `20px` (vertical)
- Button spacing: `5px` between buttons
- Section spacing: `15px` between sections

### **Font Sizes:**

- Title: `20pt` (Bold)
- Subtitle: `10pt`
- Button: `11pt` (Bold)
- Description: `9pt`
- Footer: `8pt`

### **Button Dimensions:**

- Width: `20 characters` (~180px)
- Height: `2 lines` (~50px)

---

## 🎨 **Icon Usage:**

| Element           | Icon | Purpose              |
| ----------------- | ---- | -------------------- |
| Title             | 🎯   | Main app identity    |
| Detection Section | 📹   | Video/Camera related |
| Face Recognition  | 🔐   | Security/Recognition |
| Tips Panel        | 💡   | Information          |
| Exit Button       | ❌   | Close action         |
| Success           | ✅   | Confirmation         |
| Warning           | ⚠️   | Important notice     |
| Error             | ❌   | Error message        |
| Info              | ℹ️   | Information          |

---

## 📱 **Responsive Behavior:**

### **On Different Screens:**

**Normal Display (600x700):**

```
Perfect fit, all elements visible
```

**Small Screen (< 600px):**

```
Window stays 600px (tidak resize)
User perlu scroll jika screen terlalu kecil
```

**Large Screen (> 1920px):**

```
Window tetap 600px (centered)
Background blur/dim optional
```

---

## 🎬 **Animation & Effects:**

### **Hover Effect:**

```python
Button Hover:
- Color: Slightly darker
- Cursor: Change to "hand2"
- Border: Slight glow (optional)
```

### **Click Effect:**

```python
Button Click:
- Relief: RAISED → SUNKEN
- Visual feedback
```

### **Dialog Appear:**

```python
Modal Dialog:
- Fade in effect (optional)
- Center of parent window
- Parent window disabled saat dialog open
```

---

## 🔧 **Accessibility:**

### **Keyboard Navigation:**

```
Tab: Move between buttons
Enter: Activate focused button
Escape: Close dialog/Exit (optional)
```

### **Screen Reader:**

```
All buttons have descriptive text
Dialog titles are clear
Error messages are explicit
```

---

## 🎯 **User Flow:**

```
START
  ↓
[Main Window Opens]
  ↓
User sees 5 main features + 1 exit
  ↓
User clicks button
  ↓
[Dialog/Camera Action]
  ↓
Process complete
  ↓
Return to main window
  ↓
User can click another button or exit
  ↓
END
```

---

## 📊 **Performance:**

### **Expected Metrics:**

| Metric                    | Target       | Notes                 |
| ------------------------- | ------------ | --------------------- |
| **Window Load**           | < 1 second   | GUI initialization    |
| **Button Click Response** | < 100ms      | UI feedback           |
| **Camera Open**           | 1-2 seconds  | With optimization     |
| **Thread Response**       | Non-blocking | Camera runs in thread |
| **Memory Usage**          | < 200MB      | GUI + loaded modules  |

---

## 🎨 **Design Philosophy:**

1. **Simple & Clean**

   - Minimalist design
   - No clutter
   - Focus on functionality

2. **Intuitive**

   - Clear button labels
   - Descriptive text
   - Logical flow

3. **Modern**

   - Dark theme
   - Colored buttons
   - Rounded corners (if possible)

4. **Accessible**
   - Good contrast
   - Readable fonts
   - Clear icons

---

**Design Version:** 1.0  
**Created:** 7 Oktober 2025  
**Status:** ✅ Implemented in gui_app.py
