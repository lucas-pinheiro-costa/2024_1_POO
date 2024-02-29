# Função para verificar se uma sentença é um tautograma
def verificar_tautograma(sentenca):
    palavras = sentenca.split()  # Dividir a sentença em palavras
    primeira_letra = palavras[0][0].lower()  # Obter a primeira letra da primeira palavra
    for palavra in palavras:
        if palavra[0].lower() != primeira_letra:
            return 'N'  # Se a primeira letra de qualquer palavra for diferente, não é um tautograma
    return 'Y'  # Se todas as palavras começarem com a mesma letra, é um tautograma


# Processamento dos casos de teste
while True:
    sentenca = input()
    if sentenca == '*':
        break
    print(verificar_tautograma(sentenca))