a, b, c= map(float,input('Введите коэф-ты a, b, c: ').strip().split())

D = b**2 - 4*a*c
if D < 0:
    print('корней нет')
    exit()

if a == 0: print('x = ', -1*c/b)

elif b == 0:
    if c < 0: print('x = ', (-1*c)**0.5)
    else: print('Корней нет')

elif c == 0: print('x = ', -1*b/a)

else:
    if (-1*b + D**0.5)/(2*a) == (-1*b - D**0.5)/(2*a): print('x == '(-1*b + D**0.5)/(2*a)) 
    else:
        print('x1 = ', (-1*b + D**0.5)/(2*a))
        print('x2 = ', (-1*b - D**0.5)/(2*a))