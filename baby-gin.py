def baby_gin(card):
    count = [0] * 10

    for i in range(len(card)):
        count[card[i]] += 1

    run = 0
    triplet = 0
    for i in range(len(card)):
        if count[i] + count[i+1] + count[i+2] == 3 and count[i]>0 and count[i+1]>0 and count[i+2]>0:
            run += 1
            
        elif count[i]>=3:

            triplet += 1

    if run + triplet == 2:
        print("baby-gin")
    else: 
        print("NOT baby-gin")

card = list(map(int, input().split()))
baby_gin(card))