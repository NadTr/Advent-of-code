class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

from pathlib import Path
print("advent of code 2016 day 19")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    number = int(f.read())

elf = Node(1)
head = elf
for i in range (2,number +1):
    elf.next = Node(i)
    elf = elf.next
elf.next = head

elf = head
while elf.next != elf:
    elf.next = elf.next.next
    elf = elf.next

print("The last elf is ", elf.val)