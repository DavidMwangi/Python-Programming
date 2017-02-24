# dir function returns all function that can be used with the datatype

# Lets take an example of a string

name = "My name is David"

# Lets find out what are the functions we can use with the string

print (dir(name))

# In the case that you do not know what any of the function with the datatype does help function is helpful

# From dir, one of the function we could use with the string name is upper

# Suppose we do not know what the upper function does

# help function can help us find out

print(help(name.upper))

print(name.upper())


# Lets try it out with a dictionary

dic = {"key":"value"}

print(dir(dic))

print(help(dic.fromkeys))

print(help(dic.get))

print(help(dic.pop))

print(help(dic.setdefault))
