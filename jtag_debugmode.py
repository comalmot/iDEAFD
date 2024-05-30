#!/usr/bin/python3

import subprocess
import time
import sys

class JTAGDebugMode:
	def __init__(self, devCode, current_dir):		
		self.devCode = devCode
		self.current_dir = current_dir
		self.commands = [
			['python', 'ipwndfu', '-p', '--demote', '--disable-wdt'],
			['openocd', '-f', 'Modules/bonobo-configs/t8010.cfg'],
			['nc', '127.0.0.1 4444'],
			['gdb', '-q']
		]
		
		print("Ready DFU Mode. we will wait 10 seconds..")
		time.sleep(10)
	
		for command in self.commands:
			if "ipwndfu" in command:
				script = f'tell application "Terminal" to do script "cd {self.current_dir}/Modules/ipwndfu-nowdt/ && {command[0]} {" ".join(command[1:])}"'			
			else:
				script = f'tell application "Terminal" to do script "cd {self.current_dir} && {command[0]} {" ".join(command[1:])}"'
			print("[+] Debug : " + script)
			subprocess.run(["osascript", "-e", script])	

		# Invoke GDB
		subprocess.run(['osascript', '-e', '''
    			tell application "Terminal"
        		activate
        		delay 1
        		do script "target remote :3333" in front window
        		delay 1
    			end tell
		'''])
