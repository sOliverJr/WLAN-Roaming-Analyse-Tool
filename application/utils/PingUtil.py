import os


class PingUtil:
    ip = ''
    file_writer: None

    def __init__(self, ip, file_writer):
        self.ip = ip
        self.file_writer = file_writer

    def ping(self):
        """Pings IP and returns shell response."""
        return os.popen(f"ping -c 1 {self.ip}").read()

    def extract_ping_info(self, array):
        """Extract relevant information out of the shell response."""
        for element in array:
            if 'bytes from' in element:
                return element

    def iterate_once(self):
        """Executes one full iteration."""
        ping_res = self.ping().split("\n")
        self.file_writer.add_response(self.extract_ping_info(ping_res))
