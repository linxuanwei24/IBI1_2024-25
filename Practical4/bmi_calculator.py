# the value of weight and height are stored in the variables weight and height
# the BMI value are stored in the variable bmi
# calculate the BMI value then compare the value to the provided data

weight = float(input("please input your weight(in kg):"))
height = float(input("please input your height(in m):"))
bmi = weight / (height * height) 
bmi = round(bmi , 2) # round the BMI value so that it looks more concise
if bmi > 30:
    print("Your BMI is " , bmi , ", and you are considered obese.")
elif bmi < 18.5:
    print("Your BMI is " , bmi , ", and you are considered underweight.")
else:
    print("Your BMI is " , bmi , ", and you are considered normal weight.")