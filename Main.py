class Stack():
def init (self,Range):
self.Range = Range
self.array = list()
self.top = -1
def Push(self,value):
self.top += 1
self.array.append(value)
if(len(self.array) > self.Range):
print("The Stack is in the OverFlow is condition")

2

def pop(self):
if(self.top ==
-1):

print("Stack is a empty")
else:
self.top
-= 1
self.array.pop()
def peek(self):
print(self.array[self.top])
def display(self):
if(len(self.array) == 0):
print("Stack is Empty")
else:
print(self.array)
Range
= int(input("Enter the Range of the Stack:"))
obj
= Stack(Range)
while(1):
print("Press 1 for Push")
print("Press 2 for Pop")
print("Press 3 for Peek")
print("Press

4 for Display")

op
= int(input("Enter the option:"))
if(op == 1): x = int(input("Enter the element to push:"))
obj.Push(x)
elif(op == 2):
obj.pop()
elif(op == 3):
obj.peek()
elif(op == 4):
obj.display()
else:
print("Error")
