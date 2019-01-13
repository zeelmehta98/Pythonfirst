import sys
class school(object):
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def result(self,marks):
        self.result=marks
        if marks >= 35:
            print('Congratulations!YOU HAVE PASSED')
            sys.exit()
        else:
            print('SORRY! YOU HAVE NOT PASSED')
            sys.exit()
        return self.result
print('This program shows the result of students')
name=input('Enter name:')
roll=int(input('Enter Roll number:'))
s=school(name,roll)

while(True):
    print('Hello Student!')
    points=int(input('Enter marks obtained:'))
    s.result(points)
