from flask import Flask, render_template, redirect, request, jsonify
from simulation import simulationWithoutDrug, simulationWithDrug
import pylab


app = Flask(__name__)
# data = []

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/without_drug", methods=['GET', 'POST'])
def without_drug():
	# return pylab.plot(simulationWithoutDrug(1, 1000, 0.1, 0.05, 1), label = "SimpleVirus")
	data = []
	numViruses = int(request.form.get("numViruses"))
	maxPop = int(request.form.get("maxPop"))
	maxBirthProb = float(request.form.get("maxBirthProb"))
	clearProb = float(request.form.get("clearProb"))
	numTrials = int(request.form.get("numTrials"))
	data.extend(simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials))
	# return render_template("plot.html")
	# return render_template("plot.html", data=data)
	# return redirect("/plot")
	# return numViruses
	# return jsonify(numViruses)
	return jsonify(simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials))
	# return jsonify(simulationWithoutDrug(100, 1000, 0.1, 0.05, 1))

@app.route("/with_drug", methods=['GET', 'POST'])
def with_drug():
	if request.method == 'GET':
		return jsonify(simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1))
# resistance 選單

if __name__ == "__main__":
	app.run(debug=True)