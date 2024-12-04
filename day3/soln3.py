import re

def multiply(token):
    matches = re.findall("[0-9]+", token)
    nums = [int(item) for item in matches]
    return nums[0] * nums[1]


regex = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
do = re.compile(r"do\(\)")
dont = re.compile(r"don't\(\)")
with open("inputd3.txt", 'r') as f:
    mem = f.read()

mults = regex.finditer(mem)
mults_list = [match for match in mults]
dos = do.finditer(mem)
dos_list = [match for match in dos]
donts = dont.finditer(mem)
donts_list = [match for match in donts]


flag = 0
real_products = []
i = 0
while i < len(mem):
    if flag == 0:
        for j in mults_list:
            if j.start() == i:
                real_products.append(j.group())
        
    for c in donts_list:
        if i == c.start():
            flag = 1
    
    for y in dos_list:
        if i == y.start():
            flag = 0
    i += 1

r = re.findall(regex, mem)
products = 0
for p in r:
    products += multiply(p)
print(products)

p2 = 0
for p in real_products:
    p2 += multiply(p)
print(p2)
