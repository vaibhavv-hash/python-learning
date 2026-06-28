# ==========================================
# Multiple Table Generator
# Author: Vaibhav Kshirsagar
# Description:
# Generates multiplication tables for a given range
# and displays the total of each table.
# ==========================================

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("\n========== MULTIPLICATION TABLES ==========")

for table in range(start, end + 1):
    total = 0

    print("\n" + "=" * 30)
    print(f"      Table of {table}")
    print("=" * 30)

    for multiplier in range(1, 11):
        result = table * multiplier
        print(f"{table} x {multiplier:<2} = {result}")
        total += result

    print("-" * 30)
    print(f"Total = {total}")