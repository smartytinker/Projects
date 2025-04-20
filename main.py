import subprocess
import time
from malware_runner import run_sample
from log_parser import convert
from report_builder import parse_csv

def runprocmon(duration = 30):
	print("Starting Procmon..........")
	subprocess.run(["cmd", "/c", "run_procmon.bat", str(duration)], shell = True)
	print("Loading Procmon finished")

if __name__ == "__main__":
	malwarepath = r"C:\Users\rajes\Desktop\Project 1\dist\fake.exe"
	run_sample(malwarepath)
	runprocmon(30)

	if convert():
		report = parse_csv()
	
		print("Malware Behav iour Summary")
		
		print("\n[Files Written]\n")
		for item in report["files written"][:10]:
			print(f" - {item}")

		print("\n[Registery Modified]\n")
		for item in report["registry mods"][:10]:
			print(f" - {item}")

		print("\n[Network Access]\n")
		for item in report["network access"][:10]:
			print(f" - {item}")
	

