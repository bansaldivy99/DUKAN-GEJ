import pandas as pd
import numpy as np
import csv 

from operator import itemgetter

df = pd.read_csv('DUKAN_GEJ.csv')

place = df.Place.unique() #Print Different Places
print('These Are all Places :' , place)
gauge = df.Gauge.unique() #Print Different Places
print('These Are all Gauge :' , gauge)
meena = df.Meena.unique() #Print Different Places
print('These Are all Meena :' , meena)

order = [] #list of Piece no.
print("Enter Piece No. ")
while True:
    inp = input()
    if inp == "":
        break
    order.append(int(inp))
#print(order)

#numpy_df = df.to_numpy() #converting df to 2D Array

C =[]
H =[]
RD =[]
B=[]
X=[] #pata nahi kiska piece hai
WO=[] #these piece not in caltalogue 
FullOrder=[] #This list has the list of full order

s=set()
for i in range(0,len(df.axes[0])):
	s.add(df.iloc[i,0])
#print(s) #Set of all the design Numbers in stock

for i in range(0,len(order)) :

	for row in range(0,len(df.axes[0])) :
		if df.iloc[row,0] == order[i] :

			if df.iloc[row,1] == 'C':
				C.append([df.iloc[row,0],df.iloc[row,2],df.iloc[row,3]])
				FullOrder.append([df.iloc[row,0],df.iloc[row,2],df.iloc[row,3]])
				break
			elif df.iloc[row,1] == 'H':
				H.append([df.iloc[row,0],df.iloc[row,2],df.iloc[row,3]])
				FullOrder.append([df.iloc[row,0],df.iloc[row,2],df.iloc[row,3]])
				break
			elif df.iloc[row,1] == 'RD':
				RD.append([df.iloc[row,0],df.iloc[row,2],df.iloc[row,3]])
				FullOrder.append([df.iloc[row,0],df.iloc[row,2],df.iloc[row,3]])
				break
			elif df.iloc[row,1] == 'B':
				B.append([df.iloc[row,0],df.iloc[row,2],df.iloc[row,3]])
				FullOrder.append([df.iloc[row,0],df.iloc[row,2],df.iloc[row,3]])
				break
			elif df.iloc[row,1] == 'X':
				X.append([df.iloc[row,0],df.iloc[row,2],df.iloc[row,3]])
				FullOrder.append([df.iloc[row,0],df.iloc[row,2],df.iloc[row,3]])
				break	
			else :
				WO.append([df.iloc[row,0]])
				break

C.sort(key=lambda x: (x[1],x[0]))  # Sorting According to Gauge each List
H.sort(key=lambda x: (x[1],x[0]))
RD.sort(key=lambda x: (x[1],x[0]))
B.sort(key=lambda x: (x[1],x[0]))
X.sort(key=lambda x: (x[1],x[0]))
FullOrder.sort(key=lambda x: (x[1],x[0]))


C.insert(0,['S_No','Gauge','Meena/sada'])
H.insert(0,['S_No','Gauge','Meena/sada'])
RD.insert(0,['S_No','Gauge','Meena/sada'])
B.insert(0,['S_No','Gauge','Meena/sada'])
X.insert(0,['S_No','Gauge','Meena/sada'])
FullOrder.insert(0,['S_No','Gauge','Meena/sada'])

print(C)
print(H)
print(RD)
print(B)
print(X)
print(WO)

with open("order.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')

    my_csv.write(" \nC Ka Order \n")
    csvWriter.writerows(C)
    my_csv.write(" \nH Ka Order \n")
    csvWriter.writerows(H)
    my_csv.write("\nRD Ka Order \n")
    csvWriter.writerows(RD)
    my_csv.write("\nB Ka Order \n")
    csvWriter.writerows(B)
    my_csv.write("\nX Ka Order \n")
    csvWriter.writerows(X)
    my_csv.write("\nWrong Order \n")
    csvWriter.writerows(WO)
    my_csv.write(" \n\n\nFULL Order \n\n")
    csvWriter.writerows(FullOrder)
# Cases like 1,,*,* Wont show up

''' TEST CASE
10
11
1
14
19
20
21
48
39
251
1082
1051
1405
1201
1401
1402
1440
1442
2140
2149
2146
4
5
6
'''