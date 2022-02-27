import os


# this will return a tuple of root and extension
split_tup = os.path.splitext('hello.python')
print(split_tup)

# extract the file name and extension
file_name = split_tup[0]
file_extension = split_tup[1]

if file_extension == ".py":
    file_extension = "python"


print("File Name: ", file_name)
print("File Extension: ", file_extension)