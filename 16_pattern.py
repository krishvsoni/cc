thickness = 5
c = 'H'
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

for i in range(thickness+1):  
    print((c*thickness).center(thickness*1)+(c*thickness).center(thickness*5))

for i in range((thickness+1)//2):
    print((c*thickness*4).center(thickness*5))    

for i in range(thickness+1): print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*5))    

for i in range(thickness):  print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*5))