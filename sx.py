import os
import requests
import time
import pyfiglet
req = requests.get('https://google.com')
os.system('clear')
print ("Fuck Dunia Percintaan")
time.sleep(1)
os.system('clear')
print ("\33[36;1m")
text = pyfiglet.figlet_format("SantriXploiter")
print (text)
print
print ("[1] Tentang SantriXploiter")
print ("[2] Blog SantriXploiter")
print ("[3] Web SantriXploiter")
print ("[4] Instagram SntriXploiter")
print ("[5] Group Telegram ")
print ("[6] Channel Youtube ")
print ("[7] Fanspage Facebook")
print
pilih = int(input("pilih : "))
if pilih == 1:
  time.sleep(1)
  print("Komunitas dari Pelajar Biasa yang tertarik Pada Dunia IT Dan Blog Yang Membahas Seputar Dunia IT dan Agama")
elif pilih == 2:
  time.sleep(1)
  os.system('xdg-open https://santrixploiter.blogspot.com')
elif pilih == 3:
  time.sleep(1)
  os.system('xdg-open http://aliyajnck.000webhostapp.com')
elif pilih == 4:
  time.sleep(1)
  os.system('xdg-open https://www.instagram.com/santri.xploiter/')
elif pilih == 5:
  time.sleep(1)
  os.system('xdg-open http://t.me/santrixploiter')
elif pilih == 6:
  time.sleep(1)
  os.system('xdg-open https://www.youtube.com/channel/UCG8EAqQdcDzphpluzrJWt3Q')
elif pilih == 7:
  time.sleep(1)
  os.system('xdg-open https://www.facebook.com/santrixploiter/')
else:
  print ("Tidak Tersedia")