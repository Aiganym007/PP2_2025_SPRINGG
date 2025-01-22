#1
thislist = ["apple", "banana", "cherry"]
print(thislist)
#2
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#4
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#5
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#6
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#7
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#8
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#9
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#10
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


