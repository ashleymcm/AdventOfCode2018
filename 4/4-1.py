import os, sys


dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

##collect all input, or "timestamps"
with open(os.path.join(dirname, "input.txt")) as timestamp_list:
    timestamps = [timestamps.split() for timestamps in timestamp_list]

##sort list by time
timestamps = sorted(timestamps)
i = 0

#loop through timestamps to collect guard data
while i < len(timestamps):
    timestamp = timestamps[i]
    j = 1
    next_timestamp = timestamps[i + j]
    guard = timestamp[3]
    print(guard)

    while next_timestamp[2] != "Guard":
        if next_timestamp[2] == "falls":
            fall_timestamp = int(next_timestamp[1].split(":")[1][:-1])
            print(fall_timestamp)
            j += 1
            next_timestamp = timestamps[i + j]
            wake_timestamp = int(next_timestamp[1].split(":")[1][:-1])
            print(wake_timestamp)
        j += 1
        next_timestamp = timestamps[i + j]
    
    i += j