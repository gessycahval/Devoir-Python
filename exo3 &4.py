import random
 #Exo3- fonksyon ki jenere yon kod aleyatwa ki gen n karakte alfabetik san repetisyon

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def aleyatwa(nomb_fwa):
    if nomb_fwa>=1 and nomb_fwa <=26:
        random.shuffle(alphabet)
        text=alphabet[0:nomb_fwa]
        print(''.join(text))
    else : print("antre yon lot kod")


aleyatwa(25)


#Exo4- fonksyon ki jenere yon kod aleyatwa ki genn karakte alfanimerik san repetisyon

alfanumerik=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0','1','2','3','4','5','6','7','8','9']

def ale_alfa(nomb_fwa):
    if nomb_fwa>=1 and nomb_fwa <=26:
        random.shuffle(alfanumerik)
        text=alfanumerik[0:nomb_fwa]
        print(''.join(text))
    else : print("antre yon lot kod")

ale_alfa(20)