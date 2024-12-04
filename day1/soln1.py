with open("inputd1.txt", 'r') as f:
    l1 = []
    l2 = []
    for line in f:
        location = line.split()
        l1.append(int(location[0]))
        l2.append(int(location[1]))

l1.sort()
l2.sort()

distance = 0

for i in range(len(l1)):
    distance += abs(l1[i] - l2[i])

print(distance)

sim = {}

for i in l1:
    if i not in sim:
        sim[i] = 0

for j in l2:
    if j in sim:
        sim[j] += 1

similarity = 0
for key in sim:
    similarity += key * sim[key]
print(similarity)