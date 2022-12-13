import random

#9.pemite de yon varyab

pemite1="Fonksyon ki pemute yn varyab"
pemite2="Fonksyon ki pa pemite yn varyab"

def permute(var1, var2):
         var1,var2=var2,var1
         print (f"Pemite1 = {var1}\nPemite2 = {var2}")
        
permute(pemite1,pemite2)

#10
name ="Jean-Baptiste Jean"
def pseudo_name(name):
    separasyon_name = name.split(" ")
    separasyon_name_san_tire= []
    initial_name= ""
    for name in separasyon_name:
        separasyon_name_san_tire += name.split("-")
    for name in separasyon_name_san_tire:
        initial_name += name[0]

    print(initial_name)
pseudo_name(name)