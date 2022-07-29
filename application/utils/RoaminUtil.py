import subprocess
import threading
import time


class RoamingUtil:
    command = '/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I'.split()
    bssid_1 = ''
    bssid_2 = ''
    counter = 0
    counting = False
    check_roaming = True

    def get_bssid(self):
        """Returns BSSID of currently connected AP"""
        # Needs to be run as superuser
        pc = subprocess.run(self.command, stdout=subprocess.PIPE)
        result = pc.stdout.decode('UTF-8')

        for item in result.split("\n"):
            if "BSSID" in item:
                return item.strip().split()[1]  # Remove spaces -> split key/value into array -> only return value

    def set_roaming_loop(self, boolean: bool):
        self.check_roaming = boolean

    def start_roaming_loop(self):
        """Checks every 0.1s the BSSID of the connected AP.
        Once the BSSID changes, it reads 50 more values and returns."""
        self.bssid_1 = self.get_bssid()
        self.counter = 0
        self.counting = False

        while self.check_roaming:
            self.bssid_2 = self.get_bssid()
            print('BSSID: ' + self.bssid_2)

            if self.bssid_1 != self.bssid_2 and not self.counting:
                self.counting = True
                print('Starting Counter')
            if self.counting:
                self.counter += 1
            if self.counter >= 50:
                print('counter = ' + str(self.counter) + ', exiting...')
                return

            time.sleep(0.1)
        print('returning')
        return

    def main(self):
        """Creates and starts roaming_threat."""
        roaming_threat = threading.Thread(target=self.start_roaming_loop, daemon=True, name='bssid_threat', args=())
        roaming_threat.start()
        return roaming_threat

