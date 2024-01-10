
slovo = ""
result = ""

user_input = input("Zadejte slovo: ")
slovo = user_input.upper()

with open('abeceda.txt', 'r') as f:
    lines = f.readlines()
    
    pismeno = []
    znaky = []
    
    for line in lines:
        as_list = line.strip().split(' ')

        if len(as_list) == 2:
            pismeno.append(as_list[0])
            znaky.append(as_list[1])
        else:
            pismeno.append(as_list[0])
            znaky.append(as_list[0])

for char in slovo:
    if char == ' ':
        result += " -.-.-.- "
    else:
        result += znaky[pismeno.index(char)] + ' '

print(result)