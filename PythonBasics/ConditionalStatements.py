# The iteration Keywords are one of the crucial building blocks of python.
# for,while,break,continue,pass, range,for-else loop


# ################# For Loop #################

# iterating over  a list

list = ["Kaushik","Suryam","Mridul","Yogesh"]

for i in list:
    print(i)

# For loops with Dictionary

dic = {"name":"mridul","age":"22"}
for i in dic:
    print(i)

# Loops with strings

demoString = "Good"
for i in demoString:
    print(i)


# Now let us study some concepts in looping


# Continue Function

# Basically in continue statement we can skip some words or whatever we want while iterating thru loops using certain conditions

# printing all letters except 'e' and 's'

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print(letter)


# Break function

# WhereAs in break statement we can stop the loop iteration by applying certain conditions

for letter in "sigmaMale":
    if letter == 'm':
        break
    print(letter)


# Pass function
"""
When the user does not know what code to write, So user simply places pass at that line. Sometimes, pass is used when the user doesn’t want any code to execute. So user can simply place pass where empty code is not allowed, like in loops, function definitions, class definitions, or in if statements. So using pass statement user avoids this error.
"""

for i in "somefreakingword":
    pass
print(i)



# Range Functions

for i in range(20):
    print(i)


sum =0
for x in range(1,10):
    sum = sum + x
    print(sum)
print(sum)


for i in range(2,5):
    print(i)
else:
    print("loop ended")