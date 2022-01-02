from collections import deque


def solve(food):
    order = deque([int(x) for x in input().split(' ')])
    print(max(order))

    while order:
        current_order = order.popleft()
        if current_order <= food:
            food -= current_order
        else:
            order.appendleft(current_order)
            print(f"Orders left: {' '.join([str(x) for x in order])}")
            break
    if not order:
        print("Orders complete")


solve(int(input()))
