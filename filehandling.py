f = open("demo.txt", "w")
"""
f = open("demo.txt", "w") will overwrite every content while "a" will append

"""
f.write("now this is time for somethig more interesting")
f.close()
g = open("demo.txt", "rt")
print(g.read())