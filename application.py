from flask import Flask, render_template, redirect, request, jsonify
from simulation import simulationWithoutDrug, simulationWithDrug
# import pylab


app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/without_drug", methods=['GET', 'POST'])
def without_drug():
	data = []
	try:
		numViruses = int(request.form.get("numViruses"))
		maxPop = int(request.form.get("maxPop"))
		maxBirthProb = float(request.form.get("maxBirthProb"))
		clearProb = float(request.form.get("clearProb"))
		numTrials = int(request.form.get("numTrials"))
		if numViruses < 0 or maxPop < 0 or maxBirthProb < 0 or maxBirthProb > 1 or clearProb < 0 or clearProb > 1 or numTrials < 0:
				return ""
		data.extend(simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials))
	except:
		return ""
	return jsonify(simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials))

if __name__ == "__main__":
	# app.run(debug=False)
	app.run(debug=True)