from pyo import *
s = Server().boot().start()
sf = SfPlayer("Warm Rain Digital Master.wav").out()
s.gui(locals())