import subprocess
import os

PROC_PATH = r"C:\Program Files\ProcessMonitor\Procmon64a.exe"
CSV_PATH = r"C:\Users\rajes\Desktop\Project 1\capture.csv"
PML_PATH = r"C:\Users\rajes\Desktop\Project 1\procmon_log.pml"

def convert():
    if not os.path.exists(PML_PATH):
        print("No pml log found")
        return False

    
    subprocess.run([PROC_PATH, "/OpenLog", PML_PATH, "/SaveAs", CSV_PATH])
    print(f"CSV saved to {CSV_PATH}")
    return True

