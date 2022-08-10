# CURRENTLY ONLY WORKING ON MAC
# Needs to be run as superuser to get BSSID

# Run 'sudo python3 -m main' in venv-terminal

from utils.RoamingUtil import RoamingUtil
from utils.FileWriter import FileWriter
from utils.PingUtil import PingUtil
from dotenv import load_dotenv
import time
import os


if __name__ == '__main__':

    # Gets informations from the '.env' file
    load_dotenv()
    ping_ip = os.getenv('IP')

    # Initialize utils
    file_writer = FileWriter()
    ping_util = PingUtil(ping_ip, file_writer)
    roaming_util = RoamingUtil(file_writer)

    running = True
    network_overview = None
    bssid_changed = False
    counting = False
    counter = 0

    while running:
        ping_util.iterate_once()
        bssid_changed = roaming_util.iterate_once()

        if bssid_changed and not counting:
            counting = True
            print("BSSID change detected, starting counter")
        if counting:
            counter += 1
        if counter >= 50:
            print("Counter = " + str(counter) + ", exiting...")
            running = False

        time.sleep(0.05)    # Sleep for 0.05 seconds -> 20 iterations/second

    # Writes the logs to a file
    file_writer.write_responses()
