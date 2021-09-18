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

from time import sleep, time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.utils import uri_helper
from cflib.utils.multiranger import Multiranger

from helpers import cf_hover_safely, cf_is_safe, cf_land_safely, cf_preflight_reset, cf_pulsate_led, cf_reset_ledring

from exercises import box_breathing, water_breathing


# Settings
cf_zMin = 0.6 # Minimum altitude
cf_zMax = 1.3 # Maximum altitude
ts = 1.4 # 'Time stretch' factor


# Init
cflib.crtp.init_drivers()
cf_uri = uri_helper.uri_from_env()
cf = Crazyflie(rw_cache='./cache')


print(f'Establishing synchronous connection to Crazyflie at "{cf_uri}"...')

with SyncCrazyflie(cf_uri, cf=cf) as scf:
    with Multiranger(scf) as mr:
        print(f'Connected to Crazyflie at "{cf_uri}"...')

        print('Pre-flight reset...')
        cf_preflight_reset(cf)

        # Lift-off warning
        print('Lift-off in 5...')
        cf_reset_ledring(cf)
        _t = time()
        _dt = 0
        while _dt < 5 * ts:
            _dt = time() - _t
            cf_pulsate_led(cf, _dt, ts, pattern='triangle', color_key='ring.solidGreen')
            sleep(0.01)

        cf_reset_ledring(cf)

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
        # box_breathing(cf, mr, cf_zMin, cf_zMax, ts=ts, n=1)
        water_breathing(cf, mr, cf_zMin, cf_zMax, n=1)

        # Hover in place
        if cf_is_safe:
            print('Landing in 5...')
            cf_reset_ledring(cf)
            _t = time()
            _dt = 0
            while _dt < 5 * ts:
                _dt = time() - _t
                cf_hover_safely(cf, mr, cf_zMin)
                cf_pulsate_led(cf, _dt, ts, pattern='triangle', color_key='ring.solidGreen')
                sleep(0.01)

        # Land
        cf_land_safely(cf, mr, cf_zMin)