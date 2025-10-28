import mcp3021_driver as mcp
import adc_plot
import time

adc = mcp.MCP3021(5.18)
voltage_values=[]
time_values=[]
duration = 3.0
try:
    time_start=time.time()
    while time.time()-time_start<=duration:
        time_current = time.time()
        voltage_values.append(adc.get_voltage())
        time_values.append(time_current-time_start)
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, 5.18)
    adc_plot.plot_sampling_period_hist(time_values)
finally:
    adc.deinit()