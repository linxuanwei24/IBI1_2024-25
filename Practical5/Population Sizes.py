import matplotlib.pyplot as plt

uk_countries = [57.11 , 3.13 , 1.91 , 5.45]
provinces = [65.77 , 41.88 , 45.28 , 61.27 , 85.15]
# sorting the two lists
print(sorted(uk_countries))
print(sorted(provinces))

# uk pie chart:
labels_uk = "England" , "Scotland" , "Wales" , "Northern Ireland"
sizes_uk = [57.11 , 5.45 , 3.13 , 1.91]
plt.pie(sizes_uk , labels = labels_uk , autopct = "%.2f%%" , shadow = False , startangle = 0)
plt.axis("equal")
plt.show()
# china's provinces pie chart:
labels_provinces = "Zhejiang" , "Fujian" , "Jiangxi" , "Anhui" , "Jiangsu"
sizes_provinces = [65.77 , 41.88 , 45.28 , 61.27 , 85.15]
plt.pie(sizes_provinces , labels = labels_provinces , autopct = "%.2f%%" , shadow = False , startangle = 0)
plt.axis("equal")
plt.show()