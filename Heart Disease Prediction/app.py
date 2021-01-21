
from flask import Flask, request, render_template, jsonify
#from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
@app.route("/home")
# @cross_origin()
def home():
    return render_template("index.html")


@app.route("/test")
# @cross_origin()
def test():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
# @cross_origin()
def predict():
    if request.method == "POST":

        age = float(request.form["age"])

        gender = int(request.form['gender'])

        height = float(request.form["height"])

        weight = float(request.form["weight"])

        systolic = float(request.form["systolic"])

        diastolic = float(request.form["diastolic"])

        cholesterol = int(request.form["cholesterol"])

        glucose = int(request.form["glucose"])

        smoke = int(request.form['smoke'])

        alcohol = int(request.form['alcohol'])

        active = int(request.form['active'])

        prediction = model.predict([[
            age,
            gender,
            height,
            weight,
            systolic,
            diastolic,
            cholesterol,
            glucose,
            smoke,
            alcohol,
            active
        ]])

        output = round(prediction[0])

        if output == 0:
            ans = "You don't have Heart Disease"
        else:
            ans = "You have Heart Disease"

        return render_template('index.html',prediction_text="{}".format(ans))


    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
