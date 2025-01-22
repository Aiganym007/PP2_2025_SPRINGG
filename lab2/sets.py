#1
thisset = {"apple", "banana", "cherry"}
print(thisset)
#2
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#4
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#5
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#6
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)