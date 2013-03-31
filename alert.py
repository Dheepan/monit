import subprocess
import fileinput

input_file="monit.log"
error_list=[]
prev_time=""
dtime=""

def compare_time(s1,s2):
    month={"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
    if(s1==s2):
        return True
    t1=s1.split(" ")
    t2=s2.split(" ")
    t1[0]=month[t1[0]]
    t2[0]=month[t2[0]]
    for i in range(0,len(t1)):
        delta=int(t1[i])-int(t2[i])
        if delta>0:
            return False
        if delta<0:
            return True
    return True

for line in fileinput.input("prevtime.txt"):
    prev_time=line

temp=""
for line in fileinput.input(input_file):
    temp=line.split(":")
    if temp[2].split(" ")[1]=="error":
        t=temp[:3]
        dtime=" ".join(t[0].split(" ")[1:])+" "+t[1]+" "+t[2].split("]")[0]
        if compare_time(prev_time,dtime):
            error_list.append(temp)

t=temp[:3]
dtime=" ".join(t[0].split(" ")[1:])+" "+t[1]+" "+t[2].split("]")[0]
last_time=dtime
f1=open("error.txt","w")
mode=""
line=""

for line in fileinput.input("status"):
    line=line.strip("\n\t")
    if line=="0":
    	mode="a" 
    if line=="1":
    	mode="w" 
    	s1=open("status","w")
    	s1.write("0\n")
    	s1.close()

f2=open("speak.txt",mode)
f3=open("prevtime.txt","w")
dtime=""
for ele in error_list:
    msg=ele[3:]
    alertstr=""
    for e in msg:
        alertstr+=e
    t=ele[:3]
    dtime=" ".join(t[0].split(" ")[1:])+" "+t[1]+" "+t[2].split("]")[0]
    f1.write(dtime+"\t"+alertstr+"\n")
    f2.write("Error! "+alertstr+"\n")
f3.write(last_time)
f1.close()
f2.close()
f3.close()
f4=open("All_Errors.txt","a")
for line in fileinput.input("error.txt"):
    f4.write(line)

f4.close()
#subprocess.call(['espeak','-s','120','-f','speak.txt'])
subprocess.call(['say','-f','speak.txt'])


