
slovo = ""
result = ""

user_input = input("Zadejte slovo: ")
slovo = user_input

with open('abeceda.txt', 'r') as f:
    lines = f.readlines()
    
    pismeno = []
    znaky = []
    
    for I in lines:
        as_list = I.strip().split(' ')
        pismeno.append(as_list[0])
        znaky.append(as_list[1])
    
   # print(pismeno)
   # print(znaky)

    
for char in slovo:
    result += znaky[pismeno.index(char)] + ' '

    
print (result)
        