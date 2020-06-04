# Name :Akshaya Ravi
import sys
import timeit
 
'''
file       score        time (sec)
zero      1             0.0007
1000      803           0.049
oily      222552        7.716
random.   224522        711.34
binary    83133        1216.337
total.    531011.       1935.443
'''
#start=timeit.default_timer()
totalpainting=0
lanscapeId=0
high_in=0



class Painting():
     def __init__(self,pid,paintingtype,noofkeys,keys):
        self.pid=pid    
        self.paintingtype=paintingtype
        self.noofkeys=noofkeys
        self.keys=keys

def get_keys(input_obj):
        frame=set()
        if isinstance(input_obj,list) and len(input_obj)==2:
            frame=input_obj[0].keys | input_obj[1].keys
        else:
            frame=input_obj.keys
        
        return frame


def readfile(inputfile):
    global totalpainting
    global lanscapeId
    global high_in
    my_objects_L=[]
    with open(inputfile,mode='r') as f:
        line=f.readline()
        totalpainting=str(line)
        line=f.readline()
        temp_potr=[]
        t=0
        keys_list=[]
        list_used=[]
        while line:
            string_split=line.strip().split(" ")
            if string_split[0]=='L':
                my_objects_L.append(Painting(t,string_split[0], string_split[1], set(string_split[2:])))
                keys_list.append(set(string_split[2:]))
            else:
                if(len(temp_potr)==0):
                    temp_potr.append(Painting(t,string_split[0], string_split[1], set(string_split[2:])))
                
                elif (len(temp_potr)==1):
                    temp_potr.append(Painting(t,string_split[0], string_split[1], set(string_split[2:])))
                    my_objects_L.append(temp_potr)
                

                    temp_potr=[]
                
            t=t+1
            line=f.readline()

        if(len(temp_potr)==1):
            my_objects_L.append(temp_potr)
        if(int(totalpainting)> 1000):
            high_in=1
        if(len(my_objects_L)==int(totalpainting)):
            lanscapeId=1
            list_used=keys_list    
        else:
            list_used=my_objects_L
    return list_used



def getOrder(list_used):
    new_objlist=[]
    p=0
    q=p+1
    k=p+1 
    if(lanscapeId==1):
        new_objlist.append(p)    
    else:
        new_objlist.append(list_used[p])
    while p<len(list_used)-1:
        p_obj=list_used[p]
        q_obj=list_used[q]
        val1=0
        condition=0

        if lanscapeId  != 1:
            frame1=get_keys(p_obj)
            frame2=get_keys(q_obj)
            intersection=list(frame1.intersection(frame2))
            val1=len(intersection)            
            if high_in == 1:
                condition=4

        else:
            
            val1=len(list(p_obj.intersection(q_obj)))
        if val1 > condition:
            if lanscapeId  != 1:
                new_objlist.append(q_obj)
            else:
                new_objlist.append(q)

            if k!=q:
                temp=list_used[k]
                list_used[k]=list_used[q]
                list_used[q]=temp
            p=p+1
            q=p+1
            k=p+1
        else:
            if q != len(list_used)-1 :
                q=q+1
            else:
                p=p+1
                q=p+1
                k=p+1
    return new_objlist
        





        
def writeOutput(outputfile,new_objlist):
    with open(outputfile,mode='w') as f:
        str1=str(len(new_objlist))+" \n"
        f.write(str1)
        if lanscapeId !=1 :
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
        else:
            for i in new_objlist :
                str1=str(i)+" \n"
                f.write(str1)
    
    






def main():
    inputfile=sys.argv[1]
    outputfile=sys.argv[2]
    my_objects=readfile(inputfile)
    new_objlist=getOrder(my_objects)
    writeOutput(outputfile,new_objlist)


if __name__ == "__main__":
    main()
    #stop=timeit.default_timer()
    #print('Time',stop-start)

