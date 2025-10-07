# Build Script untuk Convert Python ke EXE
# Menggunakan PyInstaller

# File: build_exe.bat
# Cara pakai: Double-click file ini atau jalankan di terminal

@echo off
echo ============================================================
echo  COMPUTER VISION APP - BUILD TO EXE
echo ============================================================
echo.

echo [1/4] Checking PyInstaller...
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller belum terinstall. Installing...
    pip install pyinstaller
) else (
    echo PyInstaller sudah terinstall!
)
echo.

echo [2/4] Cleaning previous build...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist "Computer Vision App.spec" del "Computer Vision App.spec"
echo Done!
echo.

echo [3/4] Building EXE file...
echo Ini akan memakan waktu 1-3 menit. Mohon tunggu...
echo.

pyinstaller --onefile ^
    --windowed ^
    --name "Computer Vision App" ^
    --icon=icon.ico ^
    --add-data "haarcascade_frontalface_default.xml;." ^
    --hidden-import=cv2 ^
    --hidden-import=mediapipe ^
    --hidden-import=PIL ^
    --hidden-import=numpy ^
    gui_app.py

echo.
echo [4/4] Finalizing...

if exist "dist\Computer Vision App.exe" (
    echo.
    echo ============================================================
    echo  BUILD SUCCESSFUL!
    echo ============================================================
    echo.
    echo File EXE telah dibuat di folder: dist\
    echo Nama file: Computer Vision App.exe
    echo.
    echo CATATAN PENTING:
    echo - Copy file haarcascade_frontalface_default.xml ke folder yang sama dengan EXE
    echo - Pastikan webcam tersedia saat menjalankan aplikasi
    echo.
    echo Tekan tombol apapun untuk membuka folder dist...
    pause >nul
    explorer dist
) else (
    echo.
    echo ============================================================
    echo  BUILD FAILED!
    echo ============================================================
    echo.
    echo Ada error saat building. Periksa pesan error di atas.
    echo.
    pause
)

echo.
echo Tekan tombol apapun untuk keluar...
pause >nul
