@echo off
title Computer Vision App - GUI
python gui_app.py
if errorlevel 1 (
    echo.
    echo Error: Python tidak ditemukan atau ada error dalam kode.
    echo Pastikan Python sudah terinstall dengan benar.
    pause
)
