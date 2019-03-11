from pyo import *
from flask import Flask, request

app = Flask(__name__)
s = Server().boot()

sf = SfPlayer("Warm Rain Digital Master.wav")
hr = Harmonizer(sf).out()
ch = Chorus(sf).out()


lfo1 = Sine(freq=.1, mul=500, add=1000)
lfo2 = Sine(freq=.4).range(2,8)
bpl = ButBP(sf, freq=lfo1, q=lfo2).out()



s.start()


@app.route("/temp", methods=['POST'])
def temp_input():
	temp = request.get_data(as_text=True)
	print("Got temperature " + temp)
	#lfo1.mul = lfo1.mul + (int(temp) % 40)
	mod = int(temp) % 100
	transpo = .1 * (mod - 50)
	print("setting transpo to " + str(transpo))
	hr.setTranspo(transpo)
	#print("LFO mul is " + str(lfo1.mul))
	return 'OK'