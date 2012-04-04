"""
exceptions.py
=====
To handle errors, use a try/catch block:

-----
try:
	# do your stuff
except SomeError:
	# deal with some error
-----

optionally... you can continue catching more than one exception:

-----
.
.
except AnotherError:
	# deal with another error
-----

Substitute SomeError with the kind of error you want to handle - for example:

KeyError
ValueError
TypeError
IndexError
ZeroDivisionError
"""
#KeyError
d = {"shape":"circle"}
print d["shape"]
try:
	print d["color"]
except KeyError:
	print "it doesnt exist"
print "done"
#ValueError (conversion errors)
try:
	print int ("this is not a number")
except ValueError:
	print " Its is not a number"
print "done"

#TypeError
try:
	print "foo"*"bar"
except TypeError:
	print "It wont work"
print "done"
#IndexError
ls = ["some","stuff"]
try:
	print ls[3]
except IndexError:
	print "Your index is out of range"
print "done"
#ZeroDivisionError
try:
	1/0
except ZeroDivisionError:
	print "you cant divde by zero"
print "done"
#catching multiple possible exceptions - try possible KeyError AND TypeError like dictionary value divided by another value
#ex... which player do you want to add a score to, and add that score
