x = []
for a in range(1,101):
    x.append(a)
    if a%3== 0 and a%5==0:
        print('fizzbuzz')
    elif a%3 == 0:
        print('buzz')
    elif a%5 == 0:
        print('fizz')
    else:
        print(a)
        

