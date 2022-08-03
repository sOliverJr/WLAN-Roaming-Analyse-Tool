import os


class PingUtil:
    ip = ''
    iterations = 0
    file_writer: None

    def __init__(self, ip, file_writer):
        self.ip = ip
        self.file_writer = file_writer

    def ping(self):
        """Pings IP and returns response."""
        return os.popen(f"ping -c 1 {self.ip}").read()

    def extract_ping_info(self, array):
        for element in array:
            if 'bytes from' in element:
                return element

    def iterate_once(self):
        ping_res = self.ping().split("\n")
        self.file_writer.add_response(self.extract_ping_info(ping_res))
        self.iterations += 1