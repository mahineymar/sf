a=input()
substring=""
l=0
op=[]
if a==a[::-1]:
  op.append(0)
for i in range(len(a)-1):
  for j in range(i+1,len(a)):
    substring=s[i:j+1]
    if substring==substring[::-1]:
      op.append(len(a)-len(substring))
     
print(min(op))
