def func_C():
    print("func_C1") # -- 5
    print("func_C2") # -- 6

def func_B():
    print("func_B1") # -- 3
    func_C() # -- 4
    print("func_B2") # -- 7

def func_A():
    print("func_A1") # -- 1
    func_B() # -- 2
    print("func_A2") # -- 8

func_A()