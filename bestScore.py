# Akshaya Ravi
import sys
#import timeit

'''
file       score    Approx time (timeit)
zero       1        0.0004
1000       1488     0.4789
oily       406026   4901.16
random.    410777   5645.5
binary     203742   7977.07
total.     1022032. 18524.2
'''


#start=timeit.default_timer()
class Painting():
     def __init__(self,pid,paintingtype,noofkeys,keys):
        self.pid=pid    
        self.paintingtype=paintingtype
        self.noofkeys=noofkeys
        self.keys=keys


inputfile=sys.argv[1]
outputfile=sys.argv[2]

my_objects = []
#read from input file
with open(inputfile,mode='r') as f:
    line=f.readline()
    totalpainting=str(line)
    line=f.readline()
    temp_potr=[]
    t=0
    while line:
        string_split=line.strip().split(" ")
        if string_split[0]=='L':
            my_objects.append(Painting(t,string_split[0], string_split[1], set(string_split[2:])))
        else:
            if(len(temp_potr)==0):
                temp_potr.append(Painting(t,string_split[0], string_split[1], set(string_split[2:])))
            elif (len(temp_potr)==1):
                temp_potr.append(Painting(t,string_split[0], string_split[1], set(string_split[2:])))
                my_objects.append(temp_potr)
                temp_potr=[]
                
        t=t+1
        line=f.readline()
    if(len(temp_potr)==1):
        my_objects.append(temp_potr)


new_objlist=[]
checker=0

#compare to get best output
for idx,i in enumerate(my_objects):
    best_obj=idx+1
    score=0
    if idx != len(my_objects)-1:
        if isinstance(i,list):
            frame1=i[0].keys | i[1].keys
        else:
            frame1=i.keys
        for j in range(idx+1,len(my_objects)):
            if isinstance(my_objects[j],list):
                frame2=my_objects[j][0].keys| my_objects[j][1].keys
                
            else:
                frame2=my_objects[j].keys
            intersection = list(frame1.intersection(frame2))
            val1 = len(intersection)
            val2 = len(frame1)-len(intersection)
            val3 = len(frame2)-len(intersection)
            scorepair = min(val1,val2,val3)
            
            if(scorepair>score):
                checker=checker+1
                score=scorepair
                best_obj=j
            #if checker==2:
                #break
        temp=my_objects[idx+1]
        my_objects[idx+1]=my_objects[best_obj]
        my_objects[best_obj]=temp
        
    new_objlist.append(i) 

    

#write output
with open(outputfile,mode='w') as f:
    str1=str(len(new_objlist))+" \n"
    f.write(str1)
    for i in new_objlist :
        if isinstance(i,list):
            if(len(i)==1):
                str1=str(i[0].pid)+" \n"
                f.write(str1)
            else:
                str1=str(i[0].pid)+" "+str(i[1].pid)+" \n"
                f.write(str1)
                
        else:
            str1=str(i.pid)+" \n"
            f.write(str1)
#stop=timeit.default_timer()
#print('time',stop-start)