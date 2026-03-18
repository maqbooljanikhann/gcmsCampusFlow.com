@echo off
title GCMS CampusFlow — Building EXE
color 0A
echo.
echo ================================================================
echo   GCMS CampusFlow v10 — EXE Builder
echo   Government College of Management Sciences, Sangota Swat
echo ================================================================
echo.
python --version >nul 2>&1
if errorlevel 1 (echo ERROR: Install Python 3.9+ from python.org & pause & exit /b 1)
python --version
echo.
echo Installing packages...
pip install pyinstaller pywebview flask Pillow reportlab python-dotenv -q
echo.
echo Cleaning old build...
if exist build rmdir /s /q build
if exist dist  rmdir /s /q dist
echo.
echo Building EXE (3-5 minutes)...
pyinstaller GCMS_CampusFlow.spec --noconfirm
if errorlevel 1 (echo. & echo BUILD FAILED! Run: python app.py to see errors. & pause & exit /b 1)
echo.
if not exist "dist\static\uploads" mkdir "dist\static\uploads"
if not exist "dist\static\images"  mkdir "dist\static\images"
if exist "campus.db" copy "campus.db" "dist\campus.db" >nul
if exist "static\images\GCMSSANGOTA.jpg" copy "static\images\GCMSSANGOTA.jpg" "dist\static\images\GCMSSANGOTA.jpg" >nul
echo.
echo ================================================================
echo   BUILD SUCCESSFUL!
echo   Your EXE: dist\GCMS_CampusFlow.exe
echo   Share the entire dist\ folder (not just the .exe)
echo   Login: admin / admin123
echo ================================================================
pause
