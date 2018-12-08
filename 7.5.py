from math import sqrt
def square_root(x,a):
    epsilon=1e-7
    while True:
        y=(x+a/x)/2
        if abs(y-x)<epsilon:
            return y
            break
        x=y
# def giaithua(a):
# #     if a ==1:
# #         return 1
# #     else:
# #         return a*giaithua((a-1))
def giaithua(a):
    A=a
    if a==0:
        return 1
    while True:
        a=a-1

        if a<1:
            break
        A = A * a
    return A
# # # # for i in range(1,9,1):
# # # #     print('%f %f %f'%(i,sqrt(i),square_root(10,i)))
# def eval_loop():
#     string=input('Input equation require')
#     if  string =='Done':
#         return
#     else:
#         result=eval(string)
#         print('Result is: '+str(result))
# eval_loop()
## Evaluate PI
def Pi():
    HS=((2*square_root(2,2))/9801)
    epsilon= 1e-15
    k=-1
    A=0
    while True:
        k=k+1
        B=(giaithua(4*k)*(1103+26390*k))/(giaithua(k)**4*396**(4*k))
        A = A + B
        if B<epsilon:
            break
    return (HS*A)**-1
from math import pi
print('%f %f %f'%(pi,Pi(),pi-Pi()))