fruits=["Apple", "Orange", "Pineapple","Tomato"]
print(fruits[1], end="\n")
fruit_pies=[];
for fruit in fruits:
 #for sm variable that ww call fruit in list fruits
  print(fruit)
  pie=fruit+"Pie"
  print(pie, end="\n \n")
  fruit_pies.append(pie)
print(fruit_pies)
