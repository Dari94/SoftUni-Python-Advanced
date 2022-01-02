n = int(input())
chemical_elements = set()
for _ in range(n):
    elements = set(input().split(' '))
    chemical_elements |= elements
print('\n'.join(chemical_elements))