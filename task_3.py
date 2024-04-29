from collections import UserList


class Stack(UserList):
    def __init__(self, name):
        super().__init__()
        self.name = name


def move_disks(n, source, target, helper):
    if n > 0:
        move_disks(n - 1, source, helper, target)
        disk = source.pop()
        target.append(disk)
        print(f"  Transfer disk {disk} from pilar {source.name} to pilar {target.name} ",end="-> ")
        print("A:", pilarA, "B:", pilarB, "C:", pilarC)
        move_disks(n - 1, helper, target, source)


pilarA = Stack('A')
pilarB = Stack('B')
pilarC = Stack('C')

print('')
print('Hanoi towers puzzle solver')
print('')
n = input('How many disks do you want to use?(1 - infinite) ')
if n.isdigit():
    n = int(n)
else:
    n = 0

if n > 0:

    for i in range(n, 0, -1):
        pilarA.append(i)

    print('')
    print(f'Puzzle starts with {n} disks on pilar A', end=' -> ')
    print("A:", pilarA, "B:", pilarB, "C:", pilarC)
    print('To solve this puzzle follow the instruction:')
    move_disks(n, pilarA, pilarC, pilarB)
