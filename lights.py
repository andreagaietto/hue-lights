#!/usr/bin/python

from phue import Bridge
import colorsys


b = Bridge('192.168.11.102')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

#lights = b.lights
light_names = b.get_light_objects('name')


# Print light names
# for l in lights:
#     print(l.name)

#light = light_names["Living Room Lamp"]
light = light_names["Andrea's Lamp"]

light.transitiontime = 1

# maxL = 254

#hsl
# sunriseHSLRange = [
#     [0,254,0],
#     [9600,164,254]]

sH = 0.0
sS = 254.0
sL = 0.0
eH = 9600.0
eS = 220.0
eL = 40.0 #254.0

sunriseHSL = []
steps = 200.0
m = (1.0 / steps)
hStep = (eH - sH) * m
sStep = (eS - sH) * m
lStep = (eL - sL) * m
print m, hStep, sStep, lStep

for i in range(0, int(steps)):
    sunriseHSL.append([int(hStep * i), int(sS) - int(sStep * i), int(lStep * i)])
    print i

for s in sunriseHSL:
    print s
    light.on = True
    light.hue = s[0]
    light.saturation = s[1]
    light.brightness = s[2]


# i = 0
# while i < len(sunriseHSL) and light.on:
#     print(i)
#     light.hue = sunriseHSL[i][0]
#     light.saturation = sunriseHSL[i][1]
#     light.brightness = sunriseHSL[i][2]
#     i = i+1



# hue = 0
# sat = 50
# bri = 254
# while hue <= 65535 and sat <= 254 and bri <= 254 and light.on:
#     print(hue)

#     light.hue = hue
#     light.saturation = sat
#     light.brightness = bri
#     hue += 100


# Andrea's Lamp
# Living Room Lamp
# Neil's Lamp
