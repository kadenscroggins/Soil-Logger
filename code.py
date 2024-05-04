'''
i2c addresses:
    PCF8523 (RTC):      0x68 / 104
    MAX17048 (Batt):    0x36 /  54
    STEMMA soil sensor: 0x37 /  55
'''
import alarm
import board
import neopixel
import time
import traceback
from sd_card_functions import sd_mount_append_unmount as sd_write
from adafruit_max1704x import MAX17048
from adafruit_pcf8523 import PCF8523
from adafruit_seesaw.seesaw import Seesaw

# Weekdays for RTC
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

# Set up i2c
i2c = board.I2C()
while not i2c.try_lock():
    pass
i2c_address_list = i2c.scan()
i2c.unlock()

# Assign i2c devices
batt = MAX17048(i2c)
soil = Seesaw(board.STEMMA_I2C(), addr=0x37)
rtc = PCF8523(board.I2C())

# Set up NeoPixel
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.05
pixel.fill((0, 255, 0))

# Collect timestamp
t = rtc.datetime
timestamp = f'[{t.tm_mon:02d}/{t.tm_mday:02d}/{t.tm_year:04d}-' + \
            f'{t.tm_hour:02d}:{t.tm_min:02d}:{t.tm_sec:02d}]'

# Collect battery info
batt_info = f'[{batt.cell_percent:.2f}% / {batt.cell_voltage:.1f}V]'

# Collect soil info
soil_temp_f = (soil.get_temp() * 1.8) + 32.0
soil_info = f'[{soil_temp_f:.2f}F {soil.moisture_read()}]'

print(f'Logging: {timestamp}{batt_info}{soil_info}')

try:
    sd_write(
        "soil_log.txt",
        f'\n{timestamp}{batt_info}{soil_info}',
        "Timestamp, Battery Info, Soil Info"
    )
except Exception as e:
    print("\nError reading SD card!\n")
    traceback.print_exception(e)
    print()
    for _ in range(4):
        pixel.fill((255, 0, 0))
        time.sleep(0.1)
        pixel.fill((0, 0, 0))
        time.sleep(0.1)

print("Sleepy time!")
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 20)
alarm.exit_and_deep_sleep_until_alarms(time_alarm)
