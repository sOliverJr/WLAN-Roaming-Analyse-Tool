import pandas as pd
import numpy as np
import threading
import time
import os


class PingUtil:
    ip = ''
    pinging = True
    responses = []
    bssid_changed = False
    bssid_change_written = False

    def __init__(self, ip):
        self.ip = ip
        self.pinging = True
        self.responses = []
        self.bssid_changed = False
        self.bssid_change_written = False

    def ping(self):
        """Pings IP and returns response."""
        return os.popen(f"ping -c 1 {self.ip}").read()

    def set_pinging(self, boolean: bool):
        self.pinging = boolean

    def set_bssid_changed(self, boolean: bool):
        self.bssid_changed = boolean

    def write_responses(self):
        to_write = np.asarray(self.responses)
        pd.DataFrame(to_write).to_csv("application/logs/pings.csv", index_label="Index", header=['Pings'])
        self.responses = []
        print('Wrote pings to file.')

    def remove_unnecessary_items(self, array):
        for element in array:
            if 'bytes from' in element:
                return element

    def start_ping_loop(self):
        self.responses = []
        while self.pinging:
            if self.bssid_changed and not self.bssid_change_written:
                self.responses.append('BSSID change detected!')
                self.bssid_change_written = True
            ping_res = self.ping().split("\n")
            self.responses.append(self.remove_unnecessary_items(ping_res))
            time.sleep(0.1)

        self.write_responses()

    def main(self):
        """Creates and starts roaming_threat."""
        ping_threat = threading.Thread(target=self.start_ping_loop, name='bssid_threat', args=())
        ping_threat.start()
        return ping_threat
