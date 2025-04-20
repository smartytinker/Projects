@echo off
:: Set paths
set "PROC_PATH=C:\Program Files\ProcessMonitor\Procmon64a.exe"
set "LOG_PATH=C:\Users\rajes\Desktop\Project 1\procmon_log.pml"

:: Start Procmon with logging
powershell -Command "Start-Process -FilePath '%PROC_PATH%' -ArgumentList '/BackingFile \"%LOG_PATH%\"', '/Quiet', '/Minimized'"

:: Wait 30 seconds
timeout /t 5 /nobreak > nul

:: Kill Procmon
taskkill /IM Procmon64a.exe /F

: Time to shutdown Procmon safely
timeout /t 2

echo [*] Procmon capture completed.
pause



