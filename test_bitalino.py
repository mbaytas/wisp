# -*- coding: utf-8 -*-
"""
Program to test BITalino board and PZT respiration sensor.
Reads and prints 8-bit sensor value and sensor strain
calculated via formula in datasheet (range [-50, 50]%).
"""

from time import sleep, time

from helpers import bt_connect

# Settings
bt_macAddress = "98:D3:71:FD:63:15" # BITalino MAC address, for Windows
bt_vcp = "/dev/tty.BITalino-63-15-DevB" ## BITalino virtual COM port, for Mac
bt_acqChannels = [0] # BITalino sensor channel
bt_samplingRate = 100 # BITalino sampling rate
bt_n_samples = 10 # Black magic
duration = 30 # Program duration in seconds


# Connect to BITalino and start acquisition
bt = bt_connect(bt_vcp)
bt.start(bt_samplingRate, bt_acqChannels)

# Init timer
t = time()
dt = 0

while dt < 30:
    dt = time() - t

    # Read a batch of samples sample from sensor at A0
    dataAcquired = bt.read(bt_n_samples)

    # ADC = digital sample value from sensor, range [0, 1023]
    adc = dataAcquired[0, 5]
    print("ADC: " + str(int(adc)))

    # PZT = sensor strain, range [-50, 50]% - see datasheet
    pzt = -((adc/1023.0) - (1.0/2.0)) * 100.0
    print("PZT:  " + str(int(pzt)))

    sleep(0.1)

# Stop acquisition & close connection
print('Closing connection to BITalino...')
bt.stop()
bt.close()
print(f'Exercise completed.')  