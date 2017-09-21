def gradeScale():
    for i in range(10):
        score=random.randint(60,100)
        if score <= 70:
            print "score:", score,"; Your grade is D"
        elif score <= 80:
            print "score:", score,"; Your grade is C"
        elif score <= 90:
            print "score:", score,"; Your grade is B"
        elif score <= 100:
            print "score:", score,"; your grade is A"

gradeScale()

#import random="randint"
#import re="regular expression"
