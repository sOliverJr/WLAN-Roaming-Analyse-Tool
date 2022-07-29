# CURRENTLY, ONLY WORKING ON MAC
import subprocess

# 'sudo', weil sonst die BSSID nicht angezeigt wird
command = 'sudo -S /System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I'
command = command.split()

pc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result = pc.communicate(b'861553\n')    # Passwort eingeben -> Rückgabewert ist ein Tupel
result = result[0].decode('UTF-8')      # Nur erste Tupel-Element ist Interessant und wird decodet

# print(result)

for item in result.split("\n"):
    if "BSSID" in item:
        print(item.strip())
