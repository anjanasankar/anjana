nl=[]
for x in ran(1500, 2701):
if (x%7==0) and (x%5==0):
nl.append(str(x))
print (','.join(nl))
