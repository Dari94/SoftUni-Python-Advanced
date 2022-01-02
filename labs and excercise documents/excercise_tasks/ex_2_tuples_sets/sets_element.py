(n,m)= (input().split(' '))

n_elements = set()
m_elements = set()
[n_elements.add(input()) for _ in range(int(n))]
[m_elements.add(input()) for _ in range(int(m))]
elements = n_elements.intersection(m_elements)
[print(element) for element in elements]
