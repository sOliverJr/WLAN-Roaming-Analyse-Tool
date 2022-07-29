# CURRENTLY, ONLY WORKING ON MAC
# Needs to be run as superuser to get BSSID

# Run 'sudo python3 -m main' in venv-terminal

from utils.PingUtil import PingUtil
from utils.RoaminUtil import RoamingUtil
import time


if __name__ == '__main__':
    ping_util = PingUtil('8.8.8.8')
    roaming_util = RoamingUtil(ping_util)

    ping_threat = ping_util.main()
    roaming_threat = roaming_util.main()

    roaming_threat.join()

    ping_util.set_pinging(False)
