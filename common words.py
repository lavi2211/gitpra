line1=input("enter first line of text:")
line2=input("enter the second line of text:")
print("="*50)
print("line:{}".format(line1))
print("line:{}".format(line2))
print("="*50)
lst1=line1.split()
lst2=line2.split()
set1=set(lst1)
set2=set(lst2)
cw=set1&set2
print(" num of number common words={}".format(len(cw)))
print("list of common words={}".format(cw))