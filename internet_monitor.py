import subprocess
from time import time, sleep
import re
from datetime import datetime

DEBUG = True # print out messages to terminal
TEST_IP = "8.8.8.8" # Google's DNS server
OUTAGE_DURATION_SEC = 60 # shortest detectable outage

ONLINE = "online"
OUTAGE = "outage"
UNREACHABLE = "network unreachable"

def main():
    poll_sec = OUTAGE_DURATION_SEC/2.0 # Nyquist sampling rate
    try:
        while True:
            ping_msg = get_ping_msg(TEST_IP)
            network_status = get_network_status(ping_msg)
            ping_time = get_ping_time(ping_msg)
            timestamp = time()
            date_str = get_date_str(timestamp)
            time_str = get_time_str(timestamp)
            s = "{}, {}, {}, {}, {}".format(timestamp, date_str, time_str, network_status, ping_time)
            if DEBUG:
                print(s)
            with open(get_filename(), "a") as logfile:
                logfile.write(s + "\n")
            sleep(poll_sec)
    except KeyboardInterrupt:
        exit()

def get_filename():
    timestamp = time()
    date_str = get_date_str(timestamp)
    filename = "{}.csv".format(date_str)
    return filename

def get_ping_msg(ip):
    ping_process = subprocess.Popen(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    pingp = str(ping_process.stdout.read())
    return pingp

def get_network_status(ping_msg):
    if re.search(r'100.0% packet loss|100% packet loss', ping_msg) != None:
        return OUTAGE
    elif re.search(r'Network is unreachable', ping_msg) != None:
        return UNREACHABLE
    else:
        return ONLINE

def get_ping_time(ping_msg):
    match = re.search(r'\/\d{2,4}\.\d{3}\/', ping_msg)
    if match is not None:
        ping_time = float(match.group(0).replace("/", ''))
    else:
        ping_time = None
    return ping_time

def get_date_str(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime("%Y-%m-%d")

def get_time_str(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime("%H:%M:%S")

if __name__=="__main__":
    main()
