import r2r_adc
import adc_plot
import time

adc = r2r_adc.R2R_ADC(3.291)
voltage_values=[]
time_values=[]
duration = 3.0
try:
    time_start=time.time()
    while time.time()-time_start<=duration:
        time_current = time.time()
        voltage_values.append(adc.get_sc_voltage())
        time_values.append(time_current-time_start)
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, 3.291)
    adc_plot.plot_sampling_period_hist(adc.time_val)
finally:
    adc.deinit()