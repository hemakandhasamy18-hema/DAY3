# Day 3 - Iteration + Core Data Structures

numbers = [10, 20, 30, 20, 10, 40, 20]

# -------------------------
# 1. Find Sum
# -------------------------

total = 0

for num in numbers:
    total += num

print("Numbers:", numbers)
print("Sum:", total)


# -------------------------
# 2. Find Maximum
# -------------------------

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum:", maximum)


# -------------------------
# 3. Find Minimum
# -------------------------

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum:", minimum)


# -------------------------
# 4. Count Frequency
# -------------------------

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency:", frequency)


# -------------------------
# 5. Bonus - Reverse List
# Without using reverse()
# -------------------------

reversed_list = []

i = len(numbers) - 1

while i >= 0:
    reversed_list.append(numbers[i])
    i -= 1

print("Reversed List:", reversed_list)