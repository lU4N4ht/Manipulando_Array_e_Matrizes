# Criando matriz: Trabalha com dois índices (linhas e colunas)
carros = [
    ["Modelo: ", "HRV"], 
    ["Fabricante: ", "Honda"], 
    ["Ano: ", 2016]
]

# Imprimir um elemento específico 
print(carros[0][1])  # carros[liha][coluna]

# Modificando algum valor da matriz 
carros[2][1] = 2019

# Percorrer uma matriz por meio do laço de repetição for
for l,c in carros:  # Criando duas variáveis para os valores da linha e da coluna
    print(f"{l}{str(c)}\n") # Fazendo a conversão para string

# Adicionar nova lista na matriz
carros.append("Cor: ", "Prata")

# Criar matriz vazia com tamanho definido e adicionar elementos depois
matriz = [[0 for _ in range(3)] for _ in range(3)] # Criando uma matriz 3x3 com valores padrão (zeros)

# Adicionando valores manualmente
matriz[0][0] = 1
matriz[1][1] = 5
matriz[2][2] = 9

# Exibindo a matriz
for linha in matriz:
    print(linha)

# Preencher uma matriz com valores do usuário (input)
linhas = 2
colunas = 2
matriz = []

print("Preencha a matriz 2x2:")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz preenchida:")
for linha in matriz:
    print(linha)

# Soma de todos os elementos de uma matriz
soma = 0
for linha in matriz:
    for valor in linha:
        soma += valor
print(f"Soma de todos os elementos: {soma}")

# Soma de uma linha ou coluna específica
# Soma da linha 0
soma_linha0 = sum(matriz[0])
print(f"Soma da linha 0: {soma_linha0}")

# Soma da coluna 1
soma_coluna1 = sum(linha[1] for linha in matriz)
print(f"Soma da coluna 1: {soma_coluna1}")

# Matriz identidade (1 na diagonal principal, 0 no restante)
tamanho = 4
identidade = [[1 if i == j else 0 for j in range(tamanho)] for i in range(tamanho)]

print("Matriz identidade:")
for linha in identidade:
    print(linha)


# Multiplicando cada elemento por um valor fixo
multiplicador = 2
matriz_multiplicada = [[valor * multiplicador for valor in linha] for linha in matriz]

print("Matriz multiplicada por 2:")
for linha in matriz_multiplicada:
    print(linha)





