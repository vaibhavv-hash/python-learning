marks = [78, 92, 56, 88, 95, 61]
total = 0
pass_count = 0
highest = marks[0]
lowest = marks[0]
excellent = 0
for mark in marks:
    total += mark
    if mark > highest:
        highest = mark

    if mark >= 40:
        pass_count += 1

    if mark < lowest:
        lowest = mark

    if mark >= 90:
        excellent += 1

average = total / len(marks)

print(excellent)
print(total)
print(highest)
print(lowest)
print(pass_count)
print(average)