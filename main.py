# 12 table in a list
tw=[12,24,36,48,60,72,84,96,108,120]
# printing 12 table list
print(f"12 table in a list = {tw}")
# creating multiplier of 12 for 14 table
lst=[]
for j in range(2,21,2):
    lst.append(j)
print(f"multiplier of 14 tabel from 12 tabel = {lst}")
# length of lst
lenLst=len(lst)
# creating 14 table from 12 table
for i in range(0,lenLst):
    tw[i]+=lst[i]
print(tw)