print("******************************************")
print("*Bem-vindo ao jogo de descobrir números*")
print("******************************************")

#definição das variáveis do número secreto, das tentativas e do número de rodadas
numero_secreto = 22
numero_tentativas = 3
rodada = 1

#definição da função de laço para repetir a quantidade de rodadas (print das tentativas, definição do input, mostrar qual o número chutado e a função de acerto)
while (rodada <= numero_tentativas):
    print ("TENTATIVAS", rodada, "de", numero_tentativas)
    chute = int(input("Digite o seu número: "))
    print ("Você digitou ", chute)
    #definição de variáveis de acerto (acertou, maior ou menor)
    acertou = chute == numero_secreto
    chute_menor = chute > numero_secreto
    chute_maior = chute < numero_secreto
    #função de condição de acerto (acertou, maior que o número ou menor que o número)
    if (acertou):
          print ("Você acertou! :)")
    else:
        if (chute_menor):
          print("O número é menor que ", chute )
        elif(chute_maior):
          print("O número é maior que", chute )
    #definição da métrica do número de rodadas (a cada nova tentativa é mostrado em qual rodada a tentativa se encontra)      
    rodada = rodada + 1
