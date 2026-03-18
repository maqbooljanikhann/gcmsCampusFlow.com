@echo off
title GCMS CampusFlow
echo Starting GCMS CampusFlow...
echo Open browser at: http://localhost:5000
echo Press Ctrl+C to stop.
pip install flask Pillow reportlab python-dotenv -q
python app.py
pause
