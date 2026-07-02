@echo off
title Picture Styler Pro
cd /d "%~dp0"
py -3.10 -m streamlit run app.py
pause