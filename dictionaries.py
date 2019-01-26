# Finding data using dictionaries
# Python dictionaries are software implementation of a data structure called hash table
# Key:Value pairs
# Key must be unique
# Key must be immutable (can be string, numbers, tuples but not lists)
Colors = {"Sam": "Blue", "Amy": "Red", "Sarah": "Yellow"}
print(Colors["Sarah"])
print(Colors.keys())

for Item in Colors.keys():
    print("{0} likes the color {1}.".format(Item, Colors[Item]))

Colors["Sarah"] = "Purple"
print(Colors)
Colors.update({"Harry": "Orange"})
print(Colors)
del Colors["Sam"]
print(Colors)