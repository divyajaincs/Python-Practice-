from heapq import nlargest
details={"John":86.5,"Jack":91.2,"Jill":84.5,"Harry":72.1,"Joe":80.5}
three_largest=nlargest(3,details,key=details.get);
print(three_largest)
sum=0
for value in details:
    sum+=details[value]
print(sum/len(details))    