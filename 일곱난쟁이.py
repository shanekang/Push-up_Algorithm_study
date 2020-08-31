def seven_short(height):
    first_inx = 0
    last_inx = len(height)-1
    height.sort()

    while (first_inx != last_inx):
        if (sum(height)-height[first_inx]-height[last_inx])== 100:
            remove_first = height[first_inx]
            remove_last = height[last_inx]
            height.remove(remove_first)
            height.remove(remove_last)
            break
        elif (sum(height)-height[first_inx]-height[last_inx])> 100:             
            first_inx+=1
        else:
            last_inx-=1
        
    for i in height:
        print(i)
    

height = [20, 7, 23, 19, 10, 15, 25, 8, 13]
print(seven_short(height))