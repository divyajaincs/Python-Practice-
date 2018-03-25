def readData(kmeans):
    f=open("kmeans.txt","r");
    lines=f.read().splitlines();
    print(f)
    f.close();
    items=[]
    for i in range(1,len(lines)):
        line=lines[i].split(",");
        itemfeat=[]
        for j in range(1,len(lines)-1):
            v=float(lines[j]);
            itemfeat.append(v);


    items.append(itemfeat);
    suffle(items);
    return items;


            
