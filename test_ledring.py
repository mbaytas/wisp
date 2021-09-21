# -*- coding: utf-8 -*-
"""
Program to test Crazyflie LED Ring deck.
Cycles through all available patterns.
"""


from time import sleep

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.utils import uri_helper

from helpers import cf_preflight_reset


# Init
cflib.crtp.init_drivers()
cf_uri = uri_helper.uri_from_env()
cf = Crazyflie()


print(f'Establishing synchronous connection to Crazyflie at "{cf_uri}"...')

with SyncCrazyflie(cf_uri, cf=cf) as scf:
    print(f'Connected to Crazyflie at "{cf_uri}"...')

    print('Pre-flight reset...')
    cf_preflight_reset(cf)

    ring_neffect = cf.param.get_value('ring.neffect')
    print(f'{ring_neffect} effects available on LED ring.')

    for i in range(int(ring_neffect)):
        try:
            print(f'Effect {i}:', end=' ')
            cf.param.set_value('ring.effect', i)
            sleep(1)
        except Exception as ex:
            print(f'{type(ex).__name__}')
        else:
            print('OK')