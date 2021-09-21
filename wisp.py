# -*- coding: utf-8 -*-
"""
Breathing exercises guided by a Crazyflie.
Hardware:
- Crazyflie 2.1
- Crazyradio PA
- LED Ring Deck
- Multi-ranger Deck
- Flow Deck v2
"""

import sys
from time import sleep, time


import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.utils import uri_helper
from cflib.utils.multiranger import Multiranger

from helpers import bt_connect, cf_hover_safely, cf_is_safe, cf_land_safely, cf_preflight_reset, cf_pulsate_led, cf_reset_ledring, cf_takeoff_safely

from exercises import bitalino_follow, box_breathing, bitalino_follow, water_breathing


# Settings
bt_macAddress = "98:D3:71:FD:63:15" # BITalino MAC address, for Windows
bt_vcp = "/dev/tty.BITalino-63-15-DevB" ## BITalino virtual COM port, for Mac
bt_acqChannels = [0] # BITalino sensor channel
bt_samplingRate = 100 # BITalino sampling rate
cf_zMin = 0.6 # Minimum altitude (m)
cf_zMax = 1.3 # Maximum altitude (m)
ts = 1.2 # 'Time stretch' factor (s)


# Init
cflib.crtp.init_drivers()
cf_uri = uri_helper.uri_from_env()
cf = Crazyflie()

# Connect to BITalino and start acquisition
# COMMENT OUT IF NOT NEEDED
bt = bt_connect(bt_vcp, bt_samplingRate, bt_acqChannels)
#/COMMENT OUT IF NOT NEEDED

print(f'Establishing synchronous connection to Crazyflie at "{cf_uri}"...')
with SyncCrazyflie(cf_uri, cf=cf) as scf:
    with Multiranger(scf) as mr:
        print(f'Connected to Crazyflie at "{cf_uri}"...')

        print('Pre-flight reset...')
        cf_preflight_reset(cf)

        # Lift-off warning
        print('Lift-off in 3...')
        cf_reset_ledring(cf)
        _t = time()
        _dt = 0
        while _dt < 3 * ts:
            _dt = time() - _t
            cf_pulsate_led(cf, _dt, ts, pattern='triangle', color_key='ring.solidGreen')
            sleep(0.01)

        # Take off
        cf_takeoff_safely(cf, mr, cf_zMin)

        # Hover in place
        print('Exercise begins in 5...')
        cf_reset_ledring(cf)
        _t = time()
        _dt = 0
        while _dt < 5 * ts:
            _dt = time() - _t
            cf_hover_safely(cf, mr, cf_zMin)
            cf_pulsate_led(cf, _dt, ts, pattern='triangle', color_key='ring.solidGreen')
            sleep(0.01)
        
        # Exercise
        # SELECT VIA COMMENTS
        bitalino_follow(cf, mr, bt, cf_zMin, cf_zMax, duration=30) if 'bt' in locals() else print('No BITalino!')
        # box_breathing(cf, mr, cf_zMin, cf_zMax, ts=ts, n=2)
        # water_breathing(cf, mr, cf_zMin, cf_zMax, n=1)
        #/SELECT VIA COMMENTS

        # Hover in place
        print('Landing soon...')
        cf_reset_ledring(cf)
        _t = time()
        _dt = 0
        while _dt < 3 * ts:
            if not cf_is_safe:
                break
            _dt = time() - _t
            cf_hover_safely(cf, mr, cf_zMin)
            cf_pulsate_led(cf, _dt, ts, pattern='triangle', color_key='ring.solidGreen')
            sleep(0.01)

        # Land
        cf_land_safely(cf, mr, cf_zMin)
        # Program exits via landing funciton