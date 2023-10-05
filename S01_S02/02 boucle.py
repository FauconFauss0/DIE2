
for i in range (6):
    #print(i)
    print((i**2)*"O")
symbol_ = " "
symbola = "*"
max = 20



for i in range (max):
    #print(i)
    print(f"{symbol_*(max-i)} {symbola*(i*2+1)}")
for i in range (max):
    #print(i)
    print(f"{symbol_*(i)} {symbola*(max*2-i*2+1)}")
    
print('end')