import winapps

for app in winapps.list_installed():
    print(str(app)+'\n')