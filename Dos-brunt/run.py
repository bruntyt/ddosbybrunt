import os
os.system("clear")
print("""
    ###    #####                     ###                                   ##
     ##   ##   ##                     ##                                   ##
     ##   ##   ##   #####             ##      ######   ##  ##   #####     #####
  #####   ##   ##  ##       ######    #####    ##  ##  ##  ##   ##  ##     ##
 ##  ##   ##   ##   #####             ##  ##   ##      ##  ##   ##  ##     ##
 ##  ##   ##   ##       ##            ##  ##   ##      ##  ##   ##  ##     ## ##
  ######   #####   ######            ######   ####      ######  ##  ##      ###


""")
os.system("chmod +x brunt.c")
os.system("gcc brunt.c -o brunt")
a = input("\n Insira o endereço do site, por exemplo >>> www.xvideos.com \n insira a url do site>>> : ")
os.system("./brunt "+a+" 80")
