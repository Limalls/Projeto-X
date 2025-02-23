import random

# If/Else
def verificar_numero():
    num = float(input("Digite um número: "))
    if num > 0:
        print(f"{num} é positivo.")
    elif num < 0:
        print(f"{num} é negativo.")
    else:
        print(f"{num} é zero.")

def maior_dos_dois():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num1 > num2:
        print(f"O maior número é {num1}.")
    elif num2 > num1:
        print(f"O maior número é {num2}.")
    else:
        print("Os números são iguais.")

def par_ou_impar():
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print(f"{num} é par.")
    else:
        print(f"{num} é ímpar.")

def verificar_ano_bissexto():
    ano = int(input("Digite um ano: "))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é bissexto.")
    else:
        print(f"{ano} não é bissexto.")

def verificar_idade_para_voto():
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Você pode votar.")
    else:
        print("Você não pode votar.")

def ordenar_numeros():
    numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(3)]
    numeros.sort()
    print("Os números em ordem crescente são:", numeros)

def sistema_de_notas():
    media = float(input("Digite a média do aluno: "))
    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

def sistema_de_desconto():
    preco = float(input("Digite o preço do produto: R$"))
    if preco > 100:
        desconto = preco * 0.10
        preco_com_desconto = preco - desconto
        print(f"Preço com 10% de desconto: R${preco_com_desconto:.2f}")
    else:
        print(f"Preço sem desconto: R${preco:.2f}")

def verificar_nome_comeca_com_a():
    nome = input("Digite um nome: ")
    if nome[0].lower() == "a":
        print(f"{nome} começa com a letra 'A'.")
    else:
        print(f"{nome} não começa com a letra 'A'.")

def verificar_triangulo():
    a = float(input("Digite o primeiro lado do triângulo: "))
    b = float(input("Digite o segundo lado do triângulo: "))
    c = float(input("Digite o terceiro lado do triângulo: "))
    if a == b == c:
        print("O triângulo é equilátero.")
    elif a == b or b == c or a == c:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")

# laços de reptiçoes
def numeros_1_a_10():
    for i in range(1, 11):
        print(i)

def numeros_1_a_10_while():
    i = 1
    while i <= 10:
        print(i)
        i += 1

def tabuada():
    numero = int(input("Digite um número para ver sua tabuada: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def fibonacci():
    a, b = 0, 1
    for _ in range(10):
        print(a, end=" ")
        a, b = b, a + b
    print()

def divisores():
    numero = int(input("Digite um número: "))
    print(f"Divisores de {numero}:")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)

def loop_ate_minus_um():
    while True:
        numero = int(input("Digite um número (-1 para sair): "))
        if numero == -1:
            break

def soma_numeros_ate_minus_um():
    soma = 0
    while True:
        numero = int(input("Digite um número (-1 para sair): "))
        if numero == -1:
            break
        soma += numero
    print(f"Soma dos números inseridos: {soma}")

def verificar_numero_primo():
    numero = int(input("Digite um número: "))
    if numero < 2:
        print(f"{numero} não é primo.")
        return
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"{numero} não é primo.")
            return
    print(f"{numero} é primo.")

def contar_numeros_pares():
    contador = 0
    for i in range(1, 101):
        if i % 2 == 0:
            contador += 1
    print(f"Quantidade de números pares entre 1 e 100: {contador}")

def jogo_adivinhacao():
    numero_aleatorio = random.randint(1, 50)
    while True:
        palpite = int(input("Tente adivinhar o número (1 a 50): "))
        if palpite < numero_aleatorio:
            print("Tente um número maior.")
        elif palpite > numero_aleatorio:
            print("Tente um número menor.")
        else:
            print("Parabéns! Você acertou!")
            break

# Listas
def exibir_nomes():
    nomes = ["Ana", "João", "Maria", "Carlos", "Pedro"]
    for nome in nomes:
        print(nome)

def exibir_nomes_invertido():
    nomes = ["Ana", "João", "Maria", "Carlos", "Pedro"]
    for nome in reversed(nomes):
        print(nome)

def soma_lista_de_numeros():
    numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
    print(f"A soma dos números é: {sum(numeros)}")

def maior_e_menor_lista():
    numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))
    print(f"O maior número é: {max(numeros)}")
    print(f"O menor número é: {min(numeros)}")

def contar_elementos_lista():
    lista = [1, 2, 2, 3, 3, 3, 4]
    elemento = int(input("Digite o número a ser contado: "))
    print(f"{elemento} aparece {lista.count(elemento)} vezes na lista.")

def remover_nome_lista():
    nomes = ["Ana", "João", "Maria", "Carlos", "Pedro"]
    nome = input("Digite o nome para remover da lista: ")
    if nome in nomes:
        nomes.remove(nome)
        print(f"{nome} foi removido da lista.")
    else:
        print(f"{nome} não encontrado na lista.")

def exibir_pares():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = [n for n in lista if n % 2 == 0]
    print("Números pares:", pares)

def multiplicar_lista_por_dois():
    lista = [1, 2, 3, 4, 5]
    lista_dobrada = [x * 2 for x in lista]
    print("Lista multiplicada por 2:", lista_dobrada)

def ordenar_lista_sem_sort():
    lista = [5, 2, 9, 1, 5, 6]
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    print("Lista ordenada:", lista)

def gerar_matriz():
    matriz = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
    for linha in matriz:
        print(linha)

# Juntar tudo
def dicionario_pessoa():
    pessoa = {"nome": "João", "idade": 25, "profissao": "engenheiro"}
    print(pessoa)

def dicionario_com_input_pessoa():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    profissao = input("Digite sua profissão: ")
    pessoa = {"nome": nome, "idade": idade, "profissao": profissao}
    print(pessoa)

def sistema_preco_produtos():
    produtos = {"Produto1": 10.0, "Produto2": 20.0, "Produto3": 30.0}
    print(produtos)

def contar_ocorrencias():
    frase = input("Digite uma frase: ").split()
    dicionario = {}
    for palavra in frase:
        dicionario[palavra] = dicionario.get(palavra, 0) + 1
    print(dicionario)

def carrinho_de_compras():
    carrinho = {"Produto1": 10.0, "Produto2": 20.0, "Produto3": 30.0}
    total = sum(carrinho.values())
    print(f"Total da compra: R${total:.2f}")

def sistema_notas():
    notas = {"Ana": 7.5, "João": 5.0, "Maria": 9.0}
    nome = input("Digite o nome do aluno para consultar a nota: ")
    if nome in notas:
        print(f"A nota de {nome} é {notas[nome]}")
    else:
        print("Aluno não encontrado.")

def agenda_telefones():
    agenda = {"Ana": "123456", "João": "654321", "Maria": "987654"}
    nome = input("Digite o nome do contato: ")
    if nome in agenda:
        print(f"O telefone de {nome} é {agenda[nome]}")
    else:
        print("Contato não encontrado.")

def dicionario_cidades():
    cidades = {"São Paulo": 12345678, "Rio de Janeiro": 6543210}
    cidade = input("Digite o nome de uma cidade: ")
    if cidade in cidades:
        print(f"A população de {cidade} é {cidades[cidade]}")
    else:
        print("Cidade não encontrada.")

def conversor_moeda():
    taxas = {"USD": 5.0, "EUR": 6.0}
    valor = float(input("Digite o valor em BRL: "))
    moeda = input("Digite a moeda para conversão (USD ou EUR): ").upper()
    if moeda in taxas:
        print(f"Valor convertido: {valor / taxas[moeda]:.2f} {moeda}")
    else:
        print("Moeda não suportada.")

def calcular_media_geral():
    notas = {"Ana": 7.5, "João": 5.0, "Maria": 9.0}
    media = sum(notas.values()) / len(notas)
    print(f"Média geral da turma: {media:.2f}")

# Menuzinho
def menu():
    while True:
        print("\nSelecione uma opção:")
        print("1 - Verificar número (Positivo, Negativo ou Zero)")
        print("2 - Maior dos dois números")
        print("3 - Par ou ímpar")
        print("4 - Verificar ano bissexto")
        print("5 - Verificar idade para votar")
        print("6 - Ordenar 3 números")
        print("7 - Sistema de notas")
        print("8 - Sistema de desconto")
        print("9 - Verificar se o nome começa com 'A'")
        print("10 - Verificar tipo de triângulo")
        print("11 - Exibir números de 1 a 10 (for)")
        print("12 - Exibir números de 1 a 10 (while)")
        print("13 - Tabuada")
        print("14 - Sequência Fibonacci")
        print("15 - Divisores")
        print("16 - Continuar até digitar -1")
        print("17 - Soma dos números até digitar -1")
        print("18 - Verificar número primo")
        print("19 - Contar números pares entre 1 e 100")
        print("20 - Jogo de adivinhação")
        print("21 - Exibir nomes")
        print("22 - Exibir nomes em ordem inversa")
        print("23 - Soma da lista de números")
        print("24 - Maior e menor número da lista")
        print("25 - Contar elementos na lista")
        print("26 - Remover nome da lista")
        print("27 - Exibir números pares da lista")
        print("28 - Multiplicar lista por 2")
        print("29 - Ordenar lista sem sort()")
        print("30 - Gerar matriz 3x3")
        print("31 - Dicionário pessoa")
        print("32 - Dicionário pessoa com input")
        print("33 - Sistema de preço de produtos")
        print("34 - Contar ocorrências de palavras")
        print("35 - Carrinho de compras")
        print("36 - Sistema de notas")
        print("37 - Agenda telefônica")
        print("38 - Dicionário de cidades")
        print("39 - Conversor de moeda")
        print("40 - Calcular média geral da turma")
        print("0 - Sair")
        
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 0:
            break
        elif opcao == 1:
            verificar_numero()
        elif opcao == 2:
            maior_dos_dois()
        elif opcao == 3:
            par_ou_impar()
        elif opcao == 4:
            verificar_ano_bissexto()
        elif opcao == 5:
            verificar_idade_para_voto()
        elif opcao == 6:
            ordenar_numeros()
        elif opcao == 7:
            sistema_de_notas()
        elif opcao == 8:
            sistema_de_desconto()
        elif opcao == 9:
            verificar_nome_comeca_com_a()
        elif opcao == 10:
            verificar_triangulo()
        elif opcao == 11:
            numeros_1_a_10()
        elif opcao == 12:
            numeros_1_a_10_while()
        elif opcao == 13:
            tabuada()
        elif opcao == 14:
            fibonacci()
        elif opcao == 15:
            divisores()
        elif opcao == 16:
            loop_ate_minus_um()
        elif opcao == 17:
            soma_numeros_ate_minus_um()
        elif opcao == 18:
            verificar_numero_primo()
        elif opcao == 19:
            contar_numeros_pares()
        elif opcao == 20:
            jogo_adivinhacao()
        elif opcao == 21:
            exibir_nomes()
        elif opcao == 22:
            exibir_nomes_invertido()
        elif opcao == 23:
            soma_lista_de_numeros()
        elif opcao == 24:
            maior_e_menor_lista()
        elif opcao == 25:
            contar_elementos_lista()
        elif opcao == 26:
            remover_nome_lista()
        elif opcao == 27:
            exibir_pares()
        elif opcao == 28:
            multiplicar_lista_por_dois()
        elif opcao == 29:
            ordenar_lista_sem_sort()
        elif opcao == 30:
            gerar_matriz()
        elif opcao == 31:
            dicionario_pessoa()
        elif opcao == 32:
            dicionario_com_input_pessoa()
        elif opcao == 33:
            sistema_preco_produtos()
        elif opcao == 34:
            contar_ocorrencias()
        elif opcao == 35:
            carrinho_de_compras()
        elif opcao == 36:
            sistema_notas()
        elif opcao == 37:
            agenda_telefones()
        elif opcao == 38:
            dicionario_cidades()
        elif opcao == 39:
            conversor_moeda()
        elif opcao == 40:
            calcular_media_geral()
        else:
            print("Opção inválida.")

# Rodar o menu
menu()