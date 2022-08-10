from dotenv import load_dotenv
from sys import platform
import subprocess
import os


class RoamingUtil:
    roaming_documented = False
    iterations = 0
    response: None
    bssid_1 = ''
    bssid_2 = ''

    def __init__(self, file_writer):
        self.command = self.get_correct_command().split()
        self.search_key = self.get_correct_rssid_key()
        self.bssid_1 = self.get_bssid(self.execute_command())
        self.counter = 0
        self.file_writer = file_writer

    def get_correct_command(self):
        """Extracts command to get network summary for the current OS from the .env-file."""
        load_dotenv()
        if platform == 'darwin':
            return os.getenv('OSX_COMMAND')
        elif platform == 'win32':
            return os.getenv('WIN_COMMAND')
        # elif platform == "linux" or platform == "linux2":
        #     print('linux')

    def get_correct_rssid_key(self):
        """Extracts rssi key-name for the current OS from the .env-file."""
        load_dotenv()
        if platform == 'darwin':
            return os.getenv('OSX_KEY')
        elif platform == 'win32':
            return os.getenv('WIN_KEY')
        # elif platform == "linux" or platform == "linux2":
        #     print('linux')

    def execute_command(self):
        """Executes shell-command and returns output."""
        # Needs to be run as superuser
        pc = subprocess.run(self.command, stdout=subprocess.PIPE)
        self.iterations += 1
        return pc.stdout.decode('UTF-8')

    def extract_bssid(self, response):
        """Extract BSSID of currently connected AP out of the shell response."""
        for item in response.split("\n"):
            if 'BSSID' in item:
                self.bssid_2 = item.strip().split()[1]  # Remove spaces -> split key/value into array -> only return value
                print('BSSID ' + str(self.iterations) + ': ' + self.bssid_2)
                return self.bssid_2

    def extract_rssi(self, response):
        """Extract current RSSI out of the shell response."""
        for item in response.split('\n'):
            if self.search_key in item:
                self.file_writer.add_response('RSSI: ' + item.strip().split()[1])  # Remove spaces -> split key/value into array -> only return value

    def bssid_has_changed(self):
        """Tests if the BSSID has changed in the last iteration."""
        if self.bssid_1 != self.bssid_2:
            if not self.roaming_documented:
                self.file_writer.add_response('#--------------   BSSID change detected!   --------------#')
                self.roaming_documented = True
            return True
        else:
            return False

    def iterate_once(self):
        """Executes one full iteration."""
        self.response = self.execute_command()
        self.extract_bssid(self.response)
        self.extract_rssi(self.response)
        return self.bssid_has_changed()
