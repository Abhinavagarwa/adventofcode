with open("input.txt") as file:
    lines = file.readlines()

list1 = []
list2 = []

for line in lines:
    number1, number2 = line.split('   ')
    list1.append(number1)
    list2.append(number2)

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

match = []

for i in list1:
    c = 0
    for j in list2:
        if int(i) == int(j):
            c += 1
    match.append(c) 

sums = []

for a, b in zip(list1, match):
    sums.append(int(a) * int(b))

solution = (sum(sums))
print(f"\n\033[92m[+] Solution: {solution}\033[0m\n")