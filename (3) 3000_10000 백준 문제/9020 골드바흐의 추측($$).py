# 내가 한거 오래걸림
case = int(input())

for _ in range(case):
    n = int(input())
    prime_list = [True] * (n+1)
    prime_list[0] = False
    prime_list[1] = False

    for i in range(2, int(n**0.5)+1):
        if prime_list[i]:
            for j in range(i*2, n+1, i):
                prime_list[j] = False
    
    num = n // 2
    ans1 = num
    ans2 = num

    if prime_list[ans1] == False and prime_list[ans2] == False:
        while True:
            ans1 -= 1
            ans2 += 1
            
            if prime_list[ans1] == True and prime_list[ans2] == True:
                break

    print(ans1, ans2)            

#시간 제일 빠름

def case(x):    
    if x==1:   
        return False
    for i in range(2,int(x**0.5)+1):    
        if x%i==0:  
            return False
    return True 

test=int(input())

for i in range(test):
    n=int(input())
    
    a=n//2
    b=n//2

    while a>0:
        if case(a) and case(b): 
            print(a,b)
            break
        else:
            a-=1
            b+=1
        
