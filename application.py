from flask import Flask, render_template, redirect, url_for, request, jsonify
from simulation import simulationWithoutDrug, simulationWithDrug
import pylab


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/without_drug", methods=['GET', 'POST'])
def without_drug():
	# return pylab.plot(simulationWithoutDrug(1, 1000, 0.1, 0.05, 1), label = "SimpleVirus")
	if request.method == 'GET':
		return jsonify(simulationWithoutDrug(1, 1000, 0.1, 0.05, 1))
	else:
		return "post"

@app.route("/with_drug", methods=['GET', 'POST'])
def with_drug():
	if request.method == 'GET':
		return jsonify(simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1))


if __name__ == "__main__":
	app.run(debug=True)