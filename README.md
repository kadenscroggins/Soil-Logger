# Soil-Logger
A microcontroller script that logs soil moisture!


## Parts used
* [Adafruit ESP32-S3 Feather with 4MB Flash 2MB PSRAM - STEMMA QT / Qwiic](https://www.adafruit.com/product/5477)
    * [Lithium Ion Polymer Battery Ideal For Feathers - 3.7V 400mAh](https://www.adafruit.com/product/3898)
* [Adalogger FeatherWing - RTC + SD Add-on For All Feather Boards](https://www.adafruit.com/product/2922)
    * [512MB micro SD Memory Card](https://www.adafruit.com/product/5252)
    * [CR1220 12mm Diameter - 3V Lithium Coin Cell Battery - CR1220](https://www.adafruit.com/product/380)
    * [Header Kit for Feather - 12-pin and 16-pin Female Header Set](https://www.adafruit.com/product/2886)
* [Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor - JST PH 2mm](https://www.adafruit.com/product/4026)
    * [4-pin JST PH to JST SH Cable - STEMMA to QT / Qwiic - 200mm long](https://www.adafruit.com/product/4424)


## Assembly
1. Solder the included male headers onto the ESP32-S3 feather board. The black plastic should be on the bottom of the board with the short ends going up into the board and the long end going down.
    * I used my Miniware TS80P soldering iron for all soldering on this project, which was perfect for these small boards.
2. Solder the female header kit onto the RTC featherwing board. The black plastic should be on the top of the board.
3. Insert the coin cell into the RTC featherwing board.
4. Solder the AD0 pads on the back of the STEMMA soil sensor together to increase the i2c address by one.
    * The default address of the soil sensor conflicts with the address of the battery monitor on the microcontroller
5. Sandwich the battery between the two boards - it should be a pretty snug fit, they are designed to accomodate the specific battery on the parts list. The cable should stick out just under the battery port on the top board. The battery can stay disconnected until assembly is done.
6. Push the male headers of the top board all the way into the female headers in the bottom board.
7. Connect the larger end (JST PH) of the 4-pin cable to the STEMMA soil sensor, and the smaller end (JST SH) to the port in the center of the top board.
8. Plug the top board into your computer and [install the CircuitPython firmware](https://learn.adafruit.com/adafruit-esp32-s3-feather/circuitpython) used by this project.
9. Copy the code into the CIRCUITPYTHON drive that appears when plugging in the microcontroller, and install all libraries
    * adafruit_max1704x
    * adafruit_pcf8523
    * adafruit_seesaw
    * neopixel
10. Plug in the SD card to the bottom board
