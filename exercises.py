# -*- coding: utf-8 -*-
"""
Library of Crazyflie-guided breathing exercises.
"""

from time import sleep, time

from helpers import cf_hover_safely, cf_is_safe, cf_pulsate_led, remap


def box_breathing(cf, mr, z_min, z_max, count=4.0, ts=1.5, n=3):
    """
    Executes 'n' cycles of box breathing, moving the Crazyflie vertically
    between specified z values. Each movement (inhale, hold, exhale, hold)
    lasts for 'count' counts, and each count lasts for 'ts' seconds.
    ('ts' stands for 'time stretch'.)
    """
    # Calculate period of one movement in sec
    per = count * ts
    # Execute n cycles of "inhale, hold, exhale, hold"
    for i in range(n):
        print(f'Box breathing, cycle {i + 1} of {n}.')    
        for j in range(4):
            # State movement
            if j == 0:
                print(f'Inhale for {int(count)}...')
            if j == 2:
                print(f'Exhale for {int(count)}...')
            if j in [1, 3]:
                print(f'Hold for {int(count)}...')
            # Reset timer
            t = time()
            dt = 0
            while dt < per:
                # Compute z based on time and movement
                dt = time() - t
                if j == 0: # Inhale
                    z = remap(dt, 0, per, z_min, z_max)
                if j == 1: # Hold inhale
                    z = z_max
                if j == 2: # Exhale
                    z = remap(dt, 0, per, z_max, z_min)
                if j == 3: # Hold exhale
                    z = z_min
                # Safety check
                if not cf_is_safe(mr):
                    return
                # Actuate
                cf_hover_safely(cf, mr, z)
                cf_pulsate_led(cf, dt, ts)
                sleep(0.01)
    print(f'Exercise completed.')


def water_breathing(cf, mr, z_min, z_max, count=4.0, ts=3.75, n=3):
    """
    Executes 'n' cycles of water breathing, moving the Crazyflie vertically
    between specified z values. Each movement (inhale, exhale)
    lasts for 'count' counts, and each count lasts for 'ts' seconds.
    ('ts' stands for 'time stretch'.)
    """
    # Calculate period of one movement in sec
    per = count * ts
    # Execute n cycles of "inhale, hold, exhale, hold"
    for i in range(n):
        print(f'Water breathing, cycle {i + 1} of {n}.')    
        for j in range(4):
            # State movement
            if j == 0:
                print(f'Inhale for {int(count)}...')
            if j == 1:
                print(f'Exhale for {int(count)}...')
            # Reset timer
            t = time()
            dt = 0
            while dt < per:
                # Compute z based on time and movement
                dt = time() - t
                if j == 0: # Inhale
                    z = remap(dt, 0, per, z_min, z_max)
                if j == 1: # Exhale
                    z = remap(dt, 0, per, z_max, z_min)
                # Safety check
                if not cf_is_safe(mr):
                    return
                # Actuate
                cf_hover_safely(cf, mr, z)
                cf_pulsate_led(cf, dt, ts)
                sleep(0.01)
    print(f'Exercise completed.')  
