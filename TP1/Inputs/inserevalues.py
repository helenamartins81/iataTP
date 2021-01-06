from pynput import keyboard

from Adafruit_IO import Client, Feed, RequestError

import calendar
import time

ADAFRUIT_IO_USERNAME = 'Barca88'
ADAFRUIT_IO_KEY = 'aio_KgtP88Z5IAEdT78vSQOfTQ6Zj7xK'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

adafeed = aio.feeds('workshop-somanalog')

while 1:
    value = input("Please enter a string:\n")
    aio.send(adafeed.key, value)
