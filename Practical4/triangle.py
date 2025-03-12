# name the variable of triangular values in the triangular sequence as t
# variable i is in the range (1,11), indicating that we will generate 10 triangular values
# each time we add i to t, and print t (which is the triangular value for this layer)

t = 0 # initialzie "t"
for i in range (1 , 11):
    t += i
    print(t)