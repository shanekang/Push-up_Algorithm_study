ticket_list = list(map(int,list(input())))
answer = 0
for i in range(len(ticket_list)):
    for j in range(i+1,len(ticket_list),2):
        sub = ticket_list[i:j+1]
        if sum(sub[:len(sub)//2]) == sum(sub[len(sub)//2:]):
            if answer < len(sub):
                answer = len(sub)
print(answer)