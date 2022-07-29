# CURRENTLY, ONLY WORKING ON MAC
# Needs to be run as superuser to get BSSID
from utils.RoaminUtil import RoamingUtil
import time


if __name__ == '__main__':
    roaming_util = RoamingUtil()
    roaming_threat = roaming_util.main()
    roaming_threat.join()
