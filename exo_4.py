Code=input(str("Code:"))
inverse=Code[::-1]
somme=0
for i in range(1,len(inverse),2):
  int (i)
  i*=2
  if i>9:
   i-=9
  somme+=i
for i in range (0,len(inverse),2):
 somme +=int(i)
if somme%10 == 0:
 print('Valide')
else:
 print('Invalide')
