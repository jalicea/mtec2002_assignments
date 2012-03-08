"""
tuples.py
===
1. Tuples are lists that cannot be changed
2. Just like lists they are comma separated values
3. However, instead of square brackets, tuples are enclosed by parentheses
4. This means that:
	a. Elements can be accessed like regular lists (0 based start index, using brackets to index into an element)
	b. However, you can't assign any new values
	c. They don't have an append or extend method
	d. They don't have a remove method
	e. They don't have an index method

Examples:
(3, 7)
("hello", "how", "are", "you")

Where you've seen them before / why would you use one:
1. When creating constant set of values - for example, one could represent the origin of a two dimensional plane as: origin = (0, 0)
2. When you need to make sure your set of values cannot be changed or overridden
3. In string formatting/string interpolation
"""
# create a tuple with 2 strings
t = ("two", "strings")
# print out the tuple
print t
# define a tuple with 5 numbers
num = (1,2,3,4,5)
# print out the tuple
print num
# print out the 2nd element in the tuple
print num[2]
# try to change the value of the second element
#num[1] = 222
# what happened?  comment out the line you just wrote to continue....

# try using append() on a tuple to add another element
#num.append(1212)
# what happened?  comment out the line you just wrote to continue....

# let's compare to lists: try creating a list and changing a value, it should work
list = range(10)
# try appending an element to a list
print list.append
# try using the tuple you created above in string formatting
print "%s %s" % ("hi", "hello")
# let's do another... without using a variable

# tuples can also be items in a list!
crazy_list = [(1,2), (4,5), (4,4)]
print crazy_list
# let's iterate through them
for x in crazy_list