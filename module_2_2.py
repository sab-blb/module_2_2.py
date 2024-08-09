first = int(input('first: '))
second = int(input('second: '))
third = int(input('third: '))
if first == second and first == third and second == third:
    print(3)
elif first == second != third or first == third != second or second == third != first:
    print(2)
else:
    print(0)