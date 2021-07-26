# main.py

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
# Get user input in form and render template in html
def index():
    bmi = ""
    label = ""
    try:
        if request.method == "POST" and "height" and "weight" in request.form:   
            height = float(request.form.get("height"))
            weight = float(request.form.get("weight"))
            bmi = bmi_calculation(height, weight)
            label = bmi_label(bmi)
        return render_template("index.html", bmi=bmi, label=label)
    except:
        return render_template("index_error.html")

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

# Get user input and display bmi and label in json format
@app.route("/api", methods=["POST", "GET"])
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