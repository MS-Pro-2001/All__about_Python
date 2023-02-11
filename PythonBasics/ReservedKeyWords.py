# So before going ahead we should know little bit about the Keywords that are being reserved in python i.e we cannot use them creating variable names. They are basically inbuilt function

""" 
  Some of them are listed below:

  and	as	assert	break
class	continue	def	del
elif	else	except	False
finally	for	from	global
if	import	in	is
lambda	None	nonlocal	not
or	pass	raise	return
True	try	while	with
yield	

"""


# Now there is one interesting way to check whether a word is a reserved KeyWord or not, using python function.

import keyword
# Printing all keywords

print("The list of Keywords are:")
print(keyword.kwlist);

# Thats it
# Lets proceed further with some more important concepts in python