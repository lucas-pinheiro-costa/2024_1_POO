'''
Flavinho sabe que a chance de ganhar na loteria é bem pequena. Ele gosta muito de estudar probabilidade!
Mas, justamente por entender de probabilidades, Flavinho segue o ditado, “quem não arrisca, não petisca!”,
 e faz um jogo toda semana.

Na loteria preferida dele, o jogador aposta seis números entre 1 e 99. No sorteio, também são escolhidos 
seis números ganhadores entre 1 e 99. Quem acerta 3, 4, 5 ou 6 números ganha como prêmio, respectivamente,
 um “terno”, uma “quadra”, uma “quina” ou uma “sena”.

Nesta tarefa, você deve escrever um programa que diga qual foi o prêmio que Flavinho ganhou, dados os 
seis números que ele apostou e os seis números que foram sorteados.

Entrada
A entrada consiste de duas linhas apenas. Na primeira linha são dados seis números inteiros distintos 
entre 1 e 99, representando a aposta do Flavinho. A segunda linha contém os seis números inteiros 
distintos sorteados.

Saída
Seu programa deve imprimir uma linha contendo uma palavra: “terno”, “quadra”, “quina” ou “sena”; 
caso Flavinho tenha acertado, respectivamente, 3, 4, 5, ou 6 números. Caso ele tenha acertado menos 
do que 3 números, imprima a palavra “azar”.
'''

aposta = list(map(int, input().split()))
sorteio = list(map(int, input().split()))

aposta.sort()
sorteio.sort()
contador = 0

for i in range(len(aposta)):
    for j in range(len(sorteio)):
        if aposta[i] == sorteio[j]:
            contador += 1
            break

if contador == 6:
    print('sena')
elif contador == 5:
    print('quina')
elif contador == 4:
    print('quadra')
elif contador == 3:
    print('terno')
else:
    print('azar')