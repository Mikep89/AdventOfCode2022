file = open('data/day1.txt')

d = file.readlines()
elves = {}
elf_id = 1
for i in d:
    i = i[:-1]
    if i == '':
        elf_id += 1
    elif elf_id in elves.keys():
        elves[elf_id].append(int(i))
    else:
        elves[elf_id] = [int(i)]

max_list = [sum(values) for key, values in elves.items()]
max_list.sort()

# largest
print(f"Maximum Calories carried by an elf: {max_list[-1]}")
#part 2
print(f"Total calories carried by the top 3: {sum(max_list[-3:])}")