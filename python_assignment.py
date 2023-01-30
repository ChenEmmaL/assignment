import random

def gen_random_A():
    return(random.randint(1, 9))

def gen_random_B():
    return(random.randint(1, 9))

if __name__ == "__main__":
    while(True):
        A = gen_random_A()
        B = gen_random_A()
        C = A*B
        if C == 4:
            print("Success!")
            print("A is:", A)
            print("B is:", B)
            break
        else:
            print("A is:", A)
            print("C is:", C)