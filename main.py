import random 

Welcome_message = "welcome to game!"
tupai_position = random.randint(1, 4)


print('''************************''')
print('''*** ''' + Welcome_message + ''' ***''')
print('''************************''') 

nama_user = input("masukan nama:")
print(f'''
HALOO {nama_user} coba lihat gua di bawah ini!

           |_| |_| |_| |_|
''')
pilihan_user =int(input('menurut kamu di goa no berapa tupai berada? [1/2/3/4:]'))

confirm_answer = input(f"apakah kamu yakin jawabannya {pilihan_user}? [y/n]")

if confirm_answer == "n":
   print('program selsai!')
   exit()
elif confirm_answer == "y":
    if pilihan_user == tupai_position:
         print(f"WOAAAA {nama_user} YOU WIN!!! posisi tupai ada di gua {tupai_position} dan pilihan kamu adalah {pilihan_user}")
    else:
        print(f"YOU LOSE!!! tupai berada di no {tupai_position} kamu memilih {pilihan_user}")
else:
    print("mohon ulangi program")
    exit()