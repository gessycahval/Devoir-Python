
#Exo5- jenere yon SLUG 
text = "Fonksyon pou kreye yon fonksyon ki ap dekripte yon mo ki fet ak endex chak let nan alfabet a" 

word = '-'.join(text.split())
word=''.join ([i for i in word if i.isalnum() or i=='-'])

print(word)

#Exo6- Fonksyn pou separe pa yn vigil

text = "Fonksyon" 

mot = ','.join(text)
print(mot)