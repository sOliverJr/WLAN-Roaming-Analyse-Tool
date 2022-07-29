import subprocess

# 'sudo', weil sonst die BSSID nicht angezeigt wird
command = '/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I'
command = command.split()

pc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result = pc.decode('UTF-8')      # Nur erste Tupel-Element ist Interessant und wird decodet

# print(result)

for item in result.split("\n"):
    if "BSSID" in item:
        print(item.strip())
