# -*- coding: utf-8 -*-
"""
Helper functions for close-range interactive Crazyflie applications.
"""


from math import sqrt
from time import sleep
import sys

from bitalino import BITalino


def bt_connect(bt_address, bt_samplingRate=100, bt_acqChannels=[0]):
    """
    Connect to bitalino at 'bt_address'.
    """
    print(f'Connecting to BITalino...')
    for i in range(0,10):
        print(f'Connection attempt {str(i+1)}/10...')
        try:
            bt = BITalino(bt_address, timeout=2)
        except:
            print("Failed! Retrying...")
            if i == 9:
                print("Failed to connect to BITalino. Exiting.")
                sys.exit()
        else:
            print("Connected to Bitalino " + bt_address)
            bt.start(bt_samplingRate, bt_acqChannels)
            return bt


def cf_hover_safely(cf, mr, z, cf_maxSpeed_xy = 0.5, cf_buffer_xy = 0.8):
    """
    Set hover setpoint while avoiding collisions.
    Recommended: check cf_is_safe() before calling this.
    """
    # Reset
    vx = 0.0
    vy = 0.0

    # Avoid obstacles
    if mr.front is not None:
        dvx = remap(mr.front, 0.0, cf_buffer_xy, cf_maxSpeed_xy, 0.0)
        vx -= dvx
        # print("FRONT: " + str(mr.front) + " --> " + str(dvx))
    if mr.back is not None:
        dvx = remap(mr.back,  0.0, cf_buffer_xy, cf_maxSpeed_xy, 0.0)
        vx += dvx
        # print("BACK: " + str(mr.back) + " --> " + str(dvx))
    if mr.left is not None:
        dvy = remap(mr.left,  0.0, cf_buffer_xy, cf_maxSpeed_xy, 0.0)
        vy -= dvy
        # print("LEFT: " + str(mr.left) + " --> " + str(dvy))
    if mr.right is not None:
        dvy = remap(mr.right, 0.0, cf_buffer_xy, cf_maxSpeed_xy, 0.0)
        vy += dvy
        # print("RIGHT: " + str(mr.right) + " --> " + str(dvy))

    led_r = int(remap(sqrt((vx ** 2) + (vy ** 2)), 0, cf_maxSpeed_xy, 10, 255))
    cf.param.set_value('ring.solidRed', str(led_r))

    cf.commander.send_hover_setpoint(vx, vy, 0, z)


def cf_is_safe(mr, d=0.06):
    """
    Performs critical safety checks and returns False if unsafe.
    """
    # Is the drone too close to anything from any direction?
    if mr.up is not None:
        if mr.up < d:
            print('PROXIMITY ALERT!')
            return False
    if mr.front is not None:
        if mr.front < d:
            print('PROXIMITY ALERT!')
            return False
    if mr.back is not None:
        if mr.back < d:
            print('PROXIMITY ALERT!')
            return False
    if mr.left is not None:
        if mr.left < d:
            print('PROXIMITY ALERT!')
            return False
    if mr.right is not None:
        if mr.right < d:
            print('PROXIMITY ALERT!')
            return False
    return True


def cf_land_safely(cf, mr, z0):
    """
    Land slowly using hover setpoints, while avoiding collisions.
    """
    print('Landing sequence initiated.')
    cf_reset_ledring(cf, brightness=100)
    z = z0
    while (z > 0):
        z -= 0.05
        print(f'z: {z}')
        cf_hover_safely(cf, mr, z)
        try:
            cf.param.set_value('ring.solidRed', str(int(z*10)))
            cf.param.set_value('ring.solidGreen', str(int(z*10)))
            cf.param.set_value('ring.solidBlue', str(int(z*10)))
        except Exception as e:
            pass
        sleep(0.1)
    print('Landed.')
    sys.exit()


def cf_preflight_reset(cf):
    """
    Pre-flight reset boilerplate.
    """
    sleep(0.5)
    cf.param.set_value('ring.effect', '0')
    sleep(0.5)
    cf.param.set_value('kalman.resetEstimation', '1')
    sleep(0.5)
    cf.param.set_value('kalman.resetEstimation', '0')
    sleep(0.5)


def cf_pulsate_led(cf, dt, per, pattern='sawtooth', color_key='ring.solidBlue'):
    """
    Pulsates LED in a specified period (in seconds) and pattern.
    Assumes 'ring.effect' parameter is set to 7 (solid color).
    Patterns: 'sawtooth' (default), 'triangle'
    """
    if pattern == 'triangle':
        if dt % per < per / 2:
            led_val = int(remap(dt % per, 0, per / 2, 10, 255))
        else:
            led_val = int(remap(dt % per, per / 2, per, 255, 10))
    else:
        led_val = int(remap(dt % per, per / 2, per, 255, 10))
    cf.param.set_value(color_key, str(led_val))


def cf_reset_ledring(cf, brightness=10):
        """
        Resets LED ring to solid while at specified brightness (range 0-255, default 10).
        """
        cf.param.set_value('ring.effect', '7')
        cf.param.set_value('ring.solidRed', str(10))
        cf.param.set_value('ring.solidGreen', str(10))
        cf.param.set_value('ring.solidBlue', str(10))


def cf_takeoff_safely(cf, mr, z0):
    """
    Take off slowly using hover setpoints, while avoiding collisions.
    """
    print('Take-off sequence initiated.')
    cf_reset_ledring(cf, brightness=0)
    z = z0
    while (z < z0):
        z += 0.1
        print(f'z: {z}')
        cf_hover_safely(cf, mr, z)
        try:
            cf.param.set_value('ring.solidRed', str(int(z*10)))
            cf.param.set_value('ring.solidGreen', str(int(z*10)))
            cf.param.set_value('ring.solidBlue', str(int(z*10)))
        except Exception as e:
            pass
        sleep(0.1)
    print('Hovering.')


def remap(val, inMin, inMax, outMin, outMax):
    """
    Clamps value 'val' to input range [inMin, inMax] and remaps the clamped
    value to output range [outMin, outMax]. Linear.
    """
    if val < inMin:
        val = inMin
    if val > inMax:
        val = inMax
    return outMin + (val - inMin) * (outMax - outMin) / (inMax - inMin)