alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
smeshenie = int(input('Шаг шифровки: '))
message = input("Сообщение для дешифровки: ").upper()

itog = ''
for i in message:
    mesto = alfavit_EU.find(i)		 # Меняем знак + на знак - 
    new_mesto = mesto - smeshenie
    if i in alfavit_EU:
        itog += alfavit_EU[new_mesto]
    else:
        itog += i
print(itog)