# you can type different values of "weight", the code will not go on unless your value is in the correct range
# so do the strength of paracetamol
# after inputing the two parameters, the function will return a value, which is the answer to this question
# for example:
# entering "150", you will be asked to input weight again
# entering "80",  the code will go on
# entering "120mg/5ml", you will get the answer: "The colume of paracetamol required is 50.0 ml."


# input the weight
# the check point
def input_weight():
    weight = float(input("please input the body weight (in kg):"))
    if weight < 10 or weight > 100:
        print("Error! The weight should be between 10 and 100kg, please input again.")
        return input_weight()
    else:
        return weight
weight = input_weight()

# input the strength
# the check point
def input_strength():
    strength = str(input("please select the strength of paracetamol (120mg/5ml or 250mg/5ml):"))
    if strength != "120mg/5ml" and strength != "250mg/5ml":
        print('Error! please input "120mg/5ml" or "250mg/5ml"')
        return input_strength()
    else:
        strength = int(strength[:3])
        return strength
strength = input_strength()

# define a function to cacluate the need volume of paracetamol
def caculator(weight , strength):
    volume = 15 * weight / strength * 5
    return volume
volume = caculator(weight , strength)
print("The colume of paracetamol required is" , volume , "ml.")