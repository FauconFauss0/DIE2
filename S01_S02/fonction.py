import math

def print_arrow(n_lines, symbol):
    for i in range (n_lines):
        print (f"{i*symbol}")
    print ("stop")
    
def solve_quadratic_eq(a, b, c):
    delta = b**2-4*a*c
    if (delta==0):
        r1 = -b/(2*a)
        r2 = r1
        print(f"delta = {delta}\t1 solution : {r1}")
    elif(delta>0):
        r1 = (-b-delta**0.5)/(2*a)
        r2 = (-b+delta**0.5)/(2*a)
        print(f"delta = {delta}\t2 solutions real : {r1}\t{r2}")
    else:
        r1 = (-b-delta**0.5)/(2*a)
        r2 = (-b+delta**0.5)/(2*a)
        print(f"delta = {delta}\t2 solutions non-real : {r1}\t{r2}")

    
print_arrow(5,"/")

solve_quadratic_eq(1, 2, 3)
solve_quadratic_eq(1, 2, 1)
solve_quadratic_eq(1, 10, 1)