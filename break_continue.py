# Day 9: break and continue in Python

# break example
print("Break example:")
for i in range(1, 11):
    if i == 6:
        break
    print(i)

# continue example
print("\nContinue example:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# break with while loop
print("\nBreak in while loop:")
count = 1
while True:
    print(count)
    if count == 5:
        break
    count += 1

# continue in while loop
print("\nContinue in while loop:")
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)

# Real example: search number
numbers = [2, 4, 6, 8, 10]
search = int(input("Enter number to search: "))

for n in numbers:
    if n == search:
        print("Number found:", n)
        break
else:
    print("Number not found")
