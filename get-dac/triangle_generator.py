import time
import numpy as np

def get_triangle_wave_amplitude(freq, time):
    a = (time * freq) % 1
    if 0<=a<=0.5:
        return 1-2*a
    else:
        return -1+2*a

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)

