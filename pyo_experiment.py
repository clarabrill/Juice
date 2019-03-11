from pyo import *
from time import sleep

s = Server().boot()
a = FM().out()
s.start()
sleep(1)
s.stop()
