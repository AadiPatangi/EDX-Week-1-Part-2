sequence = [1,6,45,987]


#sequences
print(sequence[1])
print(sequence[-1])  #prints last element in sequence
print(sequence[0:2]) #returns objects 0 and 1, not 2 or the last object specified

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

#tuples
