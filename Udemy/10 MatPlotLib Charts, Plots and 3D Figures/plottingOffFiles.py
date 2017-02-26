from matplotlib import pyplot as plt

x = []
y = []

readFile = open("coordinates.txt", "r")

data = readFile.read().split("\n")

for item in data:
    
    value = item.split(",")
    
    x.append(int(value[0]))
    y.append(int(value[1]))
    
plt.plot(x,y)

plt.title("A GRAPH PLOTTED FROM FILE DATA")
plt.xlabel("The X-Axis")
plt.ylabel("The Y-Axis")

plt.show()