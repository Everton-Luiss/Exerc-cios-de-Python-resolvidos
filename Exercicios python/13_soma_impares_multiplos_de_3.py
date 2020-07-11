s = 0
count = 0
for c in range(1,500,2):
    #print(c,end=' ')
    if c % 3 == 0:
        #print(c)
        count = count +1
        s = s + c
print('A soma de todos os {} valores solicitados é de {}!'.format(count ,s))
print('FIM')