# Internet Connectivity Monitor

Python script that periodically pings an IP and logs the result to a CSV until you stop it with a KeyboardInterrupt.

### Example Output

**2020-04-30.csv**

```
1588288021.577121, 2020-04-30, 16:07:01, online, 21.74
1588288051.6037278, 2020-04-30, 16:07:31, online, 17.82
1588288081.629055, 2020-04-30, 16:08:01, outage, None
1588288111.652388, 2020-04-30, 16:08:31, outage, None
1588288141.675437, 2020-04-30, 16:09:01, online, 16.593
```

**Format:** timestamp, date string, time string, network status, ping time.

### Configurable Parameters

`DEBUG`: If `True` (default), will print each CSV row to the terminal as well as logging it to the file. If `False`, runs silently.

`TEST_IP`: The host that the script will try to ping. Default is `"8.8.8.8"` (Google's DNS server), but can be changed.

`OUTAGE_DURATION_SEC`: The shortest outage you want to be able to detect (in seconds). The polling rate will be automatically set based on this value. The default is `60`, which detects outages as small as one minute (polls every 30 seconds).
