dict={'Name':'Divya','Age':'45'}
print("Name:",dict['Name'])
dict['Age']=19
print(dict)
del dict['Name']#remove entry with key Name
dict.clear()#remove all entry in disk
del dict#remove entire dictionary
print(dict)
#more than one entry per key is not allowed,when duplicate encountered last is means
#key must be mutable not like['Name']
dict1={'Name':'Divya','Age':'19'}
#print(len(dict))#no of items in dictonary



