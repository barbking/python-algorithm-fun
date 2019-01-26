# needing to store data in a certain order to access when needed
# stack (LI/FO)

MyStack = []
StackSize = 3

def DisplayStack():
    print("Stack currently contains: ")
    for item in MyStack:
        print(item)

def Push(value):
    if len(MyStack) < StackSize:
        MyStack.append(value)
    else:
        print("Stack is full!")

def Pop():
    if len(MyStack) > 0:
        print("Popping: ", MyStack.pop())
    else:
        print("Stack is empty!")

Push(1)
Push(2)
Push(3)
DisplayStack()
Push(4)

Pop()
DisplayStack()

Pop()
Pop()
Pop()

# Queues (FI/FO)
# like stacks can find predefined implementation in many pkgs such
# as NumPy and Pandas, also defined Python
import queue
MyQueue = queue.Queue(3)
print("Queue empty: ", MyQueue.empty())
MyQueue.put(1)
MyQueue.put(2)
MyQueue.put(3)
print("MyQueue: ", MyQueue)
print("Queue full: ", MyQueue.full())
print("Popping: ", MyQueue.get())
print("Queue full: ", MyQueue.full())
print("Popping: ", MyQueue.get())
print("Popping: ", MyQueue.get())
print("Queue empty: ", MyQueue.empty())


