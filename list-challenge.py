#!/usr/bin/env python3
"""Alta3 Research | Gaurav Banjade
   List - challenge"""
import random
wordbank= ["indentation", "spaces"]

tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

wordbank.append(4)
#num = int(input("Input a number between 0 and 18"))

student_name =random.randint(0,18)
print(f"{tlgstudents[student_name]} always uses {wordbank[2]} {wordbank[1]} to indent")


