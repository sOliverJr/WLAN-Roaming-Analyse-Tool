from dotenv import load_dotenv
from sys import platform
import subprocess
import os


class RoamingUtil:
    command = ''
    bssid_1 = ''
    bssid_2 = ''
    key = ''
    written = False
    counter = 0
    iterations = 0
    file_writer: None
    response: None

    def __init__(self, file_writer):
        self.command = self.get_correct_command().split()
        self.key = self.get_correct_rssid_key()
        self.bssid_1 = self.get_bssid(self.execute_command())
        self.bssid_2 = ''
        self.counter = 0
        self.file_writer = file_writer

    def get_correct_command(self):
        load_dotenv()
        if platform == 'darwin':
            return os.getenv('OSX_COMMAND')
        elif platform == 'win32':
            return os.getenv('WIN_COMMAND')
        # elif platform == "linux" or platform == "linux2":
        #     print('linux')

    def get_correct_rssid_key(self):
        load_dotenv()
        if platform == 'darwin':
            return os.getenv('OSX_KEY')
        elif platform == 'win32':
            return os.getenv('WIN_KEY')
        # elif platform == "linux" or platform == "linux2":
        #     print('linux')

    def execute_command(self):
        # Needs to be run as superuser
        pc = subprocess.run(self.command, stdout=subprocess.PIPE)
        self.iterations += 1
        return pc.stdout.decode('UTF-8')

    def get_bssid(self, response):
        """Extract BSSID of currently connected AP"""
        for item in response.split("\n"):
            if 'BSSID' in item:
                self.bssid_2 = item.strip().split()[1]  # Remove spaces -> split key/value into array -> only return value
                print('BSSID ' + str(self.iterations) + ': ' + self.bssid_2)
                return self.bssid_2

    def get_rssi(self, response):
        """Extract RSSI of current connection"""
        for item in response.split('\n'):
            if self.key in item:
                self.file_writer.add_response('RSSI: ' + item.strip().split()[1])  # Remove spaces -> split key/value into array -> only return value

    def bssid_has_changed(self):
        if self.bssid_1 != self.bssid_2:
            if not self.written:
                self.file_writer.add_response('#--------------   BSSID change detected!   --------------#')
                self.written = True
            return True
        else:
            return False

    def iterate_once(self):
        self.response = self.execute_command()
        self.get_bssid(self.response)
        self.get_rssi(self.response)
        return self.bssid_has_changed()
