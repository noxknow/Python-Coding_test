while True:
    n = int(input())
    if n == 0:
        break

    prime_list = [True]*((2*n)+1) 
    prime_list[0] = False 
    prime_list[1] = False

    for i in range(2, int((2*n)**0.5)+1):
        if prime_list[i]:
            for j in range(i*2,(2*n)+1,i):
                prime_list[j] = False  
    
    cnt = 0
    for x in range(n+1,(2*n)+1):
        if prime_list[x]:
            cnt += 1
            
    print(cnt)
            