def solve(n):
    st = []
    for _ in range(n):
        command = input().split()
        query = int(command[0])
        if query == 1:
            st.append(int(command[1]))
        elif query == 2:
            if len(st) > 0:
                st.pop()
        elif query == 3:
            if len(st) > 0:
                print(max(st))
        elif query == 4:
            if len(st) > 0:
                print(min(st))

    print(', '.join([str(x) for x in reversed(st)]))


solve(int(input()))
