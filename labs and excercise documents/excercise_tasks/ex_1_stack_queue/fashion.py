def arrange_clothes(arr_clothes,capacity):
    racks = 1
    current_rack = 0

    while arr_clothes:

        cloth = arr_clothes.pop()
        current_rack += cloth
        if current_rack <= capacity:
            current_rack = current_rack
        else:
            racks += 1
            current_rack = cloth
    return racks


clothes = [int(cloth) for cloth in input().split()]
rack_capacity = int(input())
print(arrange_clothes(arr_clothes = clothes, capacity= rack_capacity))
