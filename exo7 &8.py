import random

#7. Kripte yon mon ak vale index li nan alfabe a

mesaj="ALO"
crypt=lambda mesaj: "-".join ([str(ord(elt)-97)for elt in mesaj.lower()])
print(crypt(mesaj))



#8-dekripte yon kod avek valel nan alfabea
 
KOD="0-11-14"
decrypt=lambda mesaj: "".join([chr(int(elt)+97) for elt in KOD.split("-")]) 

print(decrypt(KOD))