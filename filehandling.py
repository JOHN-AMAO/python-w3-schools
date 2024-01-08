f = open("demo.txt", "w")
"""
f = open("demo.txt", "w") will overwrite every content while "a" will append

"""
f.write("now this is time for somethig more interesting")
f.close()
g = open("demo.txt", "rt")
print(g.read())


"""
to create a new file use the parameter "x
eg
new = open("new.text", "x)
"""
new = open("new.txt", "x")