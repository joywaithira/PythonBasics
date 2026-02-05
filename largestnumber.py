first = int(input("First number:"))
second = int(input("Second number:"))
third = int(input("Third number:"))

if first > second and first > third:
    print(first, "is the greatest number")

elif second > first and second > third:
    print(second, "is the greatest number")

else:
    print(third, "is the greatest number")

print()

