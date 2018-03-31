N = int(raw_input())
for i in range(0,N):
string = raw_input()
evenlist = []
oddlist = []
for item, char in enumerate(strg):
if item % 2 == 0:
evenlist.append(char)
else:
oddlist.append(char)
print ''.join(evenlist), ''.join(oddlist)
