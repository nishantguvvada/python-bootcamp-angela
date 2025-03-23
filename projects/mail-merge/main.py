# How to open, read, write and close files in python

# OPEN

file = open("my_file.txt", mode="r")

# with open("my_file.txt") as file: # with stores the exit method, closes automatically
#     contents = file.read()

# READING

contents = file.read()
print("original content: ", contents)

# WRITING

with open("my_file.txt", mode="a") as file:
    file.write("\nNew Text added to the file.")

with open("my_file.txt", mode="r") as file:
    contents = file.read()
    print("new content: ", contents)

# CLOSE

file.close()

