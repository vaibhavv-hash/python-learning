total = 0
even_count = 0
odd_count = 0
even_total = 0
odd_total = 0
num = int(input("Enter a number : "))
print("All Numbers : ")
for i in range(1, num+1):
    print(i)
    total = total + i
print("Even Number : ")
for j in range(1 , num+1):
    if j % 2 == 0:
        print(j)
        even_count = even_count + 1
        even_total = even_total + j
print("Total even number : ")
print(even_count)
print("Sum of even number : ", even_total)
print("Odd Number : ")
for i in range(1, num+1):
    if i % 2 == 1:
        print(i)
        odd_count = odd_count + 1
        odd_total = odd_total + i
print("Total Odd numbers : ")
print(odd_count)
print("Sum of odd number : ", odd_total)
print("Sum of all number : ", total)