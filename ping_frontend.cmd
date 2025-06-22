@echo off
setlocal enabledelayedexpansion
set FRONTEND_URL1=https://xoltar-v1.onrender.com/health
set PING_INTERVAL=300

echo Starting ping to !FRONTEND_URL1! every 5 minutes...

:loop
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /format:list') do set datetime=%%I
set TIMESTAMP=!datetime:~0,4!-!datetime:~4,2!-!datetime:~6,2! !datetime:~8,2!:!datetime:~10,2!:!datetime:~12,2!

curl -s -o nul -w "%%{http_code}" "!FRONTEND_URL1!" > temp.txt
set /p STATUS1=<temp.txt
del temp.txt

echo [!TIMESTAMP!] Pinged !FRONTEND_URL1! - Status: !STATUS1!
timeout /t !PING_INTERVAL! /nobreak > nul
goto loop