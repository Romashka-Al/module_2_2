first, second, third = map(int, input().split())
if first == second == third:
    print(3)
elif third == second or second == first or first == third:
    print(2)
else:
    print(0)
