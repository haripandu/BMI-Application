# bmi.py

# get user input for height and weight
def user_input():
    height = float(input("Height (cm): "))
    weight = float(input("Weight (kg): "))
    return height, weight

user_height, user_weight = user_input()

# calculate BMI based on user weight and height
def bmi_calculation():
    bmi = round(user_weight / (user_height/100)**2, 2)
    return bmi

user_bmi = bmi_calculation()
# print user BMI
print("BMI: " + str(user_bmi))

# set BMI label based on user BMI
def bmi_label():
    label = "-"
    if user_bmi < 18.5:
        label = "Underweight"
    elif user_bmi >= 18.5 and user_bmi <= 24.9:
        label = "Normal weight"
    elif user_bmi >= 25.0:
        label= "Overweight"
    return label

user_bmi_label = bmi_label()
print("BMI Label: " + str(user_bmi_label))