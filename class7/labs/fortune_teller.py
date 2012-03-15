"""
fortune_teller.py
===
1. Create a list of fortunes: 'you will write a program', 'you have a lot of tabs in your future', 
'boo!' and store it in a variable called fortunes
2. Use random to print out a random fortune when you run the program
3. Run the program several times

Expected Output:

$ python fortune_teller.py 
boo!
$ python fortune_teller.py 
you have a lot of tabs in your future
$ python fortune_teller.py 
you have a lot of tabs in your future
"""
import random 

lof = ["You will write many programs in your future", "you will eat a cookie...a forture cookie",
"You will never know the magic word", "The sun rises in the east and beats your ass in the west",
"You will break it and you will buy it", "Your assumptions are wrong", " If a pigeon poops on you, do not blame the pigeon, blame the poop.",
"Ninety-five percent of the things you worry about will never happen. The other five percent will kill you.",
"You are sitting on gum.", "The lesser of two evils is still evil.", " Ancient Chinese secret: You're screwed.",
"I know I am, but what am I? —Descartes, on the playground", " Be decisive. Maybe. If you want to.",
"If a man slaps you in the face, turn the other cheek and shoot him.","2,390,670,980 fortunes=one tree. Please recycle."]
index = random.randint(0,11)
print lof[index]