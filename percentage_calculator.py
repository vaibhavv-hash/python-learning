obtained = int(input("Enter the obtained marks: "))
total = int(input("Enter total marks : "))
if obtained > total:
    print("Invalid value")
else:
    percentage = obtained / total * 100
    if percentage >= 90:
     print("Grade: A ")

    elif percentage >= 75:
     print("Grade: B ")

    elif percentage >= 50:
     print("Grade: C ")

    if percentage >= 50:
     print("Congratulations you passed !!")
     
    else:
     print("Grade : Fail")
     print("Better luck next time !!")
    print("percentage :",percentage)
