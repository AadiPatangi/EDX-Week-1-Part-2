sequence = [1,6,45,987]


#sequences
print(sequence[1])
print(sequence[-1])  #prints last element in sequence
print(sequence[0:2]) #returns objects 0 and 1, not 2 or the last object specified
print("**************************************")

#lists
numbers = [2,4,6,8]
print(numbers[0])
print(numbers[-1])
numbers.append(10) #adds 10 to the end of the list
print(numbers)
x = [12,14,16] 
numbers = numbers + x #adding list x to numbers
print(numbers)
print(type(numbers))
numbers.reverse  # reversing the list
print(numbers)
locations = ["New York","Albany","Brisbane","San Francisco"]
locations.sort() #sorts the locations list in alphabetical order
print(locations)
print(len(locations)) #returns amount of objects in the list
print("**************************************")

#tuples
T = (1,3,5,7)
print(len(T))
print(T +(9,11)) #adding elements to the tuple
print(T[1]) #accessing specific elements in the tuple
x = 12.23
y = 23.34
coordinate = (x,y)
print(type(coordinate)) #returns tuple; this is called tuple packing
(c1,c2) = coordinate #unpacking the tuple
print(c1,c2)
coordinate = (2,) #adding the comma will avoid python from classifying coordinate as an integer

#range
print(range(5))
a = list(range(5)) #doesn't include last value which is specified
print(a)
a = list(range(1,13,2)) #includes values 1-13 not including 13 with increments of 2

#strings
S = "Camera"
print(len(S))
print(S[0])
print(S[0:3])
print(S[-3:]) #string slicing
print("C" in S)

print("Hello"+" World") #addition of strings is called concatenation
print(3*S)
print(S.replace("C","c")) #replace 1st character with the second
S = "Nice Camera"
s = S.split #splits "Nice" and "Camera" into two different objects in a list

#Sets
#frozen sets are immutable while createed but normal ones are not

ids = set()
ids = set([2,4,6,8,10])
print(len(ids)) #gives number of members in the set
ids.add(12)

ids.pop() #removes an object
print(len(ids))
ids = set(range(10))
print(ids)
males = set ([1,3,5,7])
females = ids - males
print(type(females))
print(females)
everyone = males | females
print(everyone)
print(everyone & set([1,2,3])) #returns the intersection of both sets
word = ("antidisestablishmentarianism")
letters= set(word)
print(len(letters))

#dictionaries