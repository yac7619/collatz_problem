from os import write
import sys
import datetime

deb=False

d_str=str(input('Enable debugging(y,n)->'))
option=int(input('File format(csv:0,txt:1,dat:2)->'))
file=str(input('Output filename(Does not include extention)->'))
s_num=int(input('Calclation start->'))
e_num=int(input('Calclation limit->'))
csv=".csv"
txt=".txt"
dat=".dat"
ct=0
max=0
m_num=0
typ=''

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
    if max<=ct:
        max=ct
        m_num=t
    ct=0
f.close()

if d_str=='y':
    deb=True

if option==0:
    typ=csv
elif option==1:
    typ=txt
elif option==2:
    typ=dat
else:
    file=''
    typ='<error>'
    
print('output file comleted:"{0}"\n'.format(file+typ))

#debug_file

    
if deb==True:
    d=open('debug.txt','w')
    now=datetime.datetime.now()
    d.write(now.strftime("%Y/%m/%d,%X\n"))
    d.write("Start number:{0}\n".format(s_num))
    d.write("End number:{0}\n".format(e_num))
    d.write("Filename:{0}\n".format(file+typ))
    d.write("Maximum calc:Num {0},{1}time(s)".format(m_num,max))
    d.close()
