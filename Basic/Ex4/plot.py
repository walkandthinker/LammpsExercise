import matplotlib.pyplot as plt

filename='Al_comp_100.def1.txt'
inp=open(filename,'r+')
line=inp.readline()
strain=[];stress1=[];stress2=[];stress3=[]
line=inp.readline()
while len(line)>1:
    linevalue=line.split(' ')
    strain.append(-float(linevalue[1-1]))
    stress1.append(-float(linevalue[2-1]))
    stress2.append(-float(linevalue[3-1]))
    stress3.append(-float(linevalue[4-1]))
    line=inp.readline()

plt.plot(strain,stress1,label=r'$\sigma_{1}$')
plt.plot(strain,stress2,label=r'$\sigma_{1}$')
plt.plot(strain,stress3,label=r'$\sigma_{1}$')

plt.legend()

plt.ylabel('$\sigma$ [GPa]',fontsize=15)
plt.xlabel('$\epsilon [-]$',fontsize=15)