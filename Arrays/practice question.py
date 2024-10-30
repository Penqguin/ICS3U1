s = []
g = []


for i in range(5):
    s.append(str(input()))
    g.append(int(input()))

x, y = max(g), min(g)

xIndex, yIndex = g.index(x), g.index(y)

print(f'{s[xIndex]} has the highest mark of {x}')
print(f'{s[yIndex]} has the lowest mark of {y}')

for i in range(5):
    if g[i] < 50:
        print(f'{s[i]} is failing with a mark of {g[i]}')