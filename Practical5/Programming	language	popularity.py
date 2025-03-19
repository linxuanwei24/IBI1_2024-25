import numpy as np
import matplotlib.pyplot as plt

# you can modify the variables here:
JavaScript_Users , HTML_Useres , Python_Users , SQL_Users , TypeScript_Users = 62.3 , 52.9 , 51 , 51 , 38.5
language_popularity = {'JavaScript':JavaScript_Users , 'HTML':HTML_Useres , 'Python':Python_Users , 'SQL':SQL_Users , 'TypeScript':TypeScript_Users}

print(language_popularity) # print the dictionary

# bar graph:
x = np.arange(5) # x axis
y = (JavaScript_Users , HTML_Useres , Python_Users , SQL_Users , TypeScript_Users) # y axis
width = 0.35
plt.bar(x , y , width)
plt.ylabel("Users(percentage)")
plt.title("Population Popularity")
plt.xticks(x , ("JavaScript" , "HTML" , "Python" ,"SQL" , "TypeScript"))
plt.yticks(np.arange(0 , 101 , 10))
plt.show()
 
language = str(input("please input the language:"))
if language in language_popularity:
    print("The percentage of the developers using" , language , "is" , language_popularity[language] , "%.")
else:
    print("Error.")