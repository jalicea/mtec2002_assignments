x = "there are %d typoes of people" % 10 
binary = "Binary"
do_not = "don't"
y = "those who know %s and those who %s" % (binary, do_not)

print x 
print y
Print "I said: %r." %x
print "i also said: '%s'." % y

hilarious = False 
joke_evaluation = " Isn't that joke so funny?! %r" 

print joke_evaluation % hilarious 
w = "This is the left side of..."
e = "a string with a right side."

print w + e