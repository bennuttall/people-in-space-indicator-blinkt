from blinkt import set_pixel, show
import requests
from time import sleep

url = "http://api.open-notify.org/astros.json"

def blink():
    for i in range(5):
        set_pixel(7, 255, 0, 0)
        show()
        sleep(1)
        set_pixel(7, 0, 0, 0)
        show()
        sleep(1)

while True:
    r = None
    while not r:
        try:
            r = requests.get(url)
        except:
            blink()
    j = r.json()
    n = j['number']

    for i in range(8):
        set_pixel(i, 0, 0, 0)
    show()

    sleep(1)
    for i in range(8):
        if n > i:
            set_pixel(i, 0, 0, 255)
        else:
            set_pixel(i, 0, 0, 0)
        show()
        sleep(1)
    sleep(60)
