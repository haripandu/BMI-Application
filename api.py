# api.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api", methods=["POST", "GET"])
# Get user input and display bmi and label in json format
def input():
    height = float(request.args.get("height"))
    weight = float(request.args.get("weight"))
    bmi = bmi_calculation(height, weight)
    label = bmi_label(bmi)
    return jsonify({"bmi": bmi, "label": label})

# calculate BMI based on user weight and height
def bmi_calculation(height, weight):
    return round(weight / (height / 100) ** 2, 2)

# set BMI label based on user BMI
def bmi_label(bmi):
    if bmi < 18.5:
        label = "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        label = "Normal weight"
    elif bmi >= 25.0:
        label = "Overweight"
    return label

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)