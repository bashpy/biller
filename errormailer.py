__author__ = 'jovin'
i=16
error=[]
errornw=[]
for line in open("debug.log"):

    if "ERROR" in line:
        j=line.split()
        f=j[1].split(",",1)
        z=j[0]+" "+f[0]
        for li in open("time.txt"):
            if li < z:
                w=open("time.txt","w")
                w.write(z)
                i=0

    if i<15:
        x=open("error.txt","a")
        errornw.append(line)
    i=i+1

if errornw != error:
    print errornw
else:
    error=errornw
