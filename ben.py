import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet TREANGLE :)")
naber = input("Termux İçin Hacker Animasyon Başlatılsınmı y/n : ")
if naber == "y":
    os.system("cmatrix")
    print("Başlamadıysa 'pkg install cmatrix' yazabilirsiniz ...")

else:
    print("Hacker Animasyon Başlatılmayacaktır...")