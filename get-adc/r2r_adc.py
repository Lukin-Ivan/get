import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        self.time_val=[]

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    
    def number_to_dac(self, number):
        a = [int(element) for element in bin(number)[2:].zfill(8)]
        for i in range(8):
            GPIO.output(self.bits_gpio[i],a[i])
    
    def sequential_counting_adc(self):
        time_start=time.time()
        for i in range(256):
            self.number_to_dac(i)
            time.sleep(self.compare_time)
            self.time_val.append(time.time()-time_start)
            if GPIO.input(self.comp_gpio) == 1:
                return i
        return 255
    
    def get_sc_voltage(self):
        return self.sequential_counting_adc()/255 * self.dynamic_range

    def successive_approximation_adc(self):
        time_start=time.time()
        GPIO.output(self.bits_gpio, 0)
        a=0
        for i in range(8):
            GPIO.output(self.bits_gpio[i],1)
            time.sleep(self.compare_time)
            self.time_val.append(time.time()-time_start)
            if GPIO.input(self.comp_gpio) == 1:
                GPIO.output(self.bits_gpio[i],0)
                time.sleep(self.compare_time)
            else:
                a+=2**(7-i)
        return a
    
    def get_sar_voltage(self):
        return self.successive_approximation_adc()/255 * self.dynamic_range
                
    

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.291)
        while True:
            voltage = adc.get_sc_voltage()
            print(f"Напряжение: {voltage:.3f}")
            #voltage = adc.get_sar_voltage()
            #print(f"Напряжение: {voltage:.3f}")
    finally:
        adc.deinit()


