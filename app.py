########  imports  ##########
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

#############################
# Additional code goes here #
#############################

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def result():
    output = request.form.to_dict()
    departure = output["departure"]
    arrival = output["arrival"]
    time = output["time"]

    return render_template("index.html", departure = type(departure), arrival = type(arrival), time = type(time))

#########  run app  #########
app.run(debug=True)