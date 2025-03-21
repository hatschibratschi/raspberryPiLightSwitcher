# Project

## Task

Use RaspberryPi 3 to switch USB 5V powered lights. 

1. Use web page to switch USB power on and off.
1. Use motion detection to switch USB power.
1. Use motion detection and light sensor to switch USB power.

## Switch USB port (5V)

On the Raspberry Pi 4 and 3B+, you can toggle the power to the USB ports via software. This is done by controlling the USB hub chip. 

```
# Turn off USB power
echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/unbind

# Turn USB power back on
echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/bind
```

### Switch USB power off at start up

Set crontab with reboot to switch power of at startup.

```
sudo crontab -e
@reboot echo '1-1' > /sys/bus/usb/drivers/usb/unbind
```

## pi-pinout
`pinout`

```
,--------------------------------.
| oooooooooooooooooooo J8     +====
| 1ooooooooooooooooooo        | USB
|                             +====
| o1 RUN  Pi Model 3B  V1.2      |
| |D      +---+               +====
| |S      |SoC|               | USB
| |I      +---+               +====
| |0               C|            |
|                  S|       +======
|                  I| |A|   |   Net
| pwr      |HDMI|  0| |u|   +======
`-| |------|    |-----|x|--------'

J8:
   3V3  (1) (2)  5V    
 GPIO2  (3) (4)  5V    
 GPIO3  (5) (6)  GND   
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND   
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND   
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8 
   GND (25) (26) GPIO7 
 GPIO0 (27) (28) GPIO1 
 GPIO5 (29) (30) GND   
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND   
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21
```

## Get environment light

### Circuit Schematic

Below is the schematic for connecting the LDR and resistor to the Raspberry Pi GPIO pins:

```
3.3V (Pin 1)
           |
           |
          [LDR]
           |
           |--- GPIO (e.g., GPIO18, Pin 12)
           |
          [10kΩ Resistor]
           |
           |
         GND (Pin 6)
```
## Motion detection

### Circuit Diagram

PIR Sensor:
```
+----------------+
| VCC   OUT   GND|
+----------------+
```

Connections:
```
PIR VCC -> RPi 5V (Pin 2 or 4)
PIR GND -> RPi GND (Pin 6)
PIR OUT -> RPi GPIO17 (Pin 11)
```
