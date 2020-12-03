from os import path
import collections


soubor = input("Zadejte název dokumentu. Pokud soubor neexistuje, vytvoří se nový: \n")
print(".............................................................")


# work with file
if(path.exists(soubor)):
    x = open(soubor, "r")
    print(x.read())
else:
	x = open(soubor, "w")
	x.write(input("Napište text, který chcete mít v novém souboru:\n\n"))
	x.close()


#insert text into variable
with open(soubor, "r") as file:
    text = file.read().replace("\n", "")
    
print("-------------------------------------------------------------")
 

#number of characters
celkem = 0
for i in text:
    celkem += 1
print("Počet znaků je ", celkem)
        

#counting most used char
most = collections.Counter(text.lower()).most_common(1)[0]
print("Nejpoužívanější znak je ", most)


#finding least used char
all_freq = {}
for i in text.lower():
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
least = min(all_freq, key = all_freq.get)
print("Nejménně použitý znak je ", least)

for prumer in text:
    data = []
    with open(soubor) as f:
        for slovo in f:
            fields = slovo.split()
            radky = map(str, fields)
            data.extend(radky)
#print([char for char in text])  
print('Počet znaků v textu')
c = collections.Counter(text.lower())
for CislaPrumeros in 'abcdefghijklmnopqrstuvwxyz 1234567890':   
    print(CislaPrumeros,':' ,c[CislaPrumeros], ', ', sep='', end='', flush=True)
for i in c:
       c.pop(CislaPrumeros)

print('')
input("\nKlávesou ENTER ukončíte program...")
