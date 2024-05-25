#/usr/bin/python3

import jtag_debugmode
import os


current_dir = os.getcwd()

print("----------------------------------------------------------------------")
print("--    iDEAFD - The iOS Data Extraction / Acquisition / Forensics    --")
print("--              .... and Debugging ToolKit by comalmot              --")
print("----------------------------------------------------------------------")

print("\n")

print("Select Option Numbers  : ")
print("[1] Backup Data Extraction")
print("[2] Passcode Brute Force (Disable Passcode Attempts)")
print("[3] Full File System Extraction (Passcode is required)")
print("[4] JTAG Debug Mode (JTAG/SWD Cable is required)")

op = int(input("Enter your option number : "))

if op == 1:
	print("Backup Data Extraction")
elif op ==  2:
	print("Passcode Brute Force")
elif op == 3:
	print("Full File System Extraction")
elif op == 4:
	print("JTAG Debug Mode is started")
	obj_jtag_debugmode = jtag_debugmode.JTAGDebugMode("t8010", current_dir)
else:
	print("Invaild Option")


while True:
	print('', end='') # for do not terminate Subprocess
