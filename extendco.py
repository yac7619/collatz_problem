from os import write
import sys


option=int(input('file format(csv:0,txt:1,dat:2)->'))
file=str(input('output filename(Does not include extention)->'))
s_num=int(input('calclation start->'))
e_num=int(input('calclation limit->'))
csv=".csv"
txt=".txt"
dat=".dat"
ct=0

def collatz(x):
    global ct
    ct+=1
    if x%2==0:
        x/=2
        if x!=1:
            return collatz(x)
    else:
        x=(x*3)+1
        return collatz(x)
if option==0:
    f=open(file+csv,'x')
elif option==1:
    f=open(file+txt,'x')
elif option==2:
    f=open(file+dat,'x')
else:
    print('option:{0} is Illegal.'.format(option))
    sys.exit()

f.write('"num","times"\n')
for t in range(s_num,e_num+1):
    collatz(t)
    f.write('"{0}","{1}"\n'.format(t,ct))
    ct=0
f.close()