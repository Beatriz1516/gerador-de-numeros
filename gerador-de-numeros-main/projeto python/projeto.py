print("******************************************")
print("*Bem-vindo ao jogo de descobrir números*")
print("******************************************")

#definindo a variável do número secreto
numero_secreto = 22
#definindo a entrado da entrada (input)
chute = int(input("Digite o seu número: "))

print ("Você digitou ", chute)

acertou     = chute == numero_secreto
chute_menor = chute > numero_secreto
chute_maior = chute < numero_secreto

if (acertou):
    print ("Você acertou! :)")
else:
    if (chute_menor):
      print("O número é menor que ", chute )
    elif(chute_maior):
      print("O número é maior que", chute )
