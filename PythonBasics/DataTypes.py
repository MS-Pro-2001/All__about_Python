# Let us learn about Datatype in python which is easy but very important building blocks
# So there are majorly 4 types of built in DataTypes in python
# Set,List,Tuple and Dictionary


########################### List ############################ 

#  -> List is the most basic dataStructure which is mutable( means that items can be changed maybe added or deleted even after the creation of the list)

# Program for a list in python

# creating an empty list
shoppingList = []

# Now to append data in the list, we have to use append() function

shoppingList.append("Hello world")
shoppingList.append("23")
shoppingList.append(34)

# ouput  :  ['Hello world', '23', 34]
print(shoppingList)



################### Dictionary ###################

# -> The dictionary basically consists of KEY-VALUE pairs and its value can be accessed by a unique key in the dictionary
# Let us demonstrate using a program


dic = dict();  # or dic = {}


# Adding key-value pair in the dictionary
dic["name"] = "mridul"
dic['class'] = "msc"

print(dic)

# printing keys and values only of dcitionary

print(dic.keys())
print(dic.values())

# Now let us try to iterate through the dictionary


for i in dic:
    print("%s %s" %( i, dic[i]))


############################ Tuples ################################