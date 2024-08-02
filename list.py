fruit=['apple','banana','kiwi']
qty=[11,2,3]

print(fruit)
print(qty)
qty.sort()
#print (qty)
#print(fruit[::-1]) #descending

for fruits,qtys in zip(fruit,qty):
 print(fruits,'=',qtys)

basket=":".join(fruit)
print(basket)


bucket=[fruit,qty]
print (bucket)

bucket[0][2]='orange';
print (bucket)

print(bucket.pop())
print(bucket)
