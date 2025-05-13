# Criando arrays 
carros = ["HRV", "Golf", "Argo", "Focus"]
carros2 = ["Celta", "Brasilia"]

# Cada item da lista tem um índice inteiro, começando do 0
print(f"Primeiro item da lista: {carros[0]}")  # Saída: Primeiro item da lista: HRV

# Acessando o último item da lista (usando índice negativo)
print(f"Último item da lista: {carros[-1]}")  # Saída: Último item da lista: Focus

# Adicionando elementos no final da lista
carros.append("Fusca")
carros.append("Polo")

# Verificando o tamanho da lista (número de elementos)
print(f"Total de carros: {len(carros)}")  # Saída: Total de carros: 6

# Removendo um item específico pelo valor
carros.remove("Fusca")  # Remove "Fusca" se existir

# Removendo um item pelo índice
del carros[0]  # Remove o primeiro item da lista

# Removendo o último item da lista
carros.pop()  # Remove e retorna o último item

# Copiando a lista para outra (cria uma nova lista independente)
carros2 = list(carros)

# Fundindo duas listas (concatenando)
todos_carros = carros + carros2

# Exibindo as listas
print(f"Lista carros: {carros}")
print(f"Lista carros2 (cópia): {carros2}")
print(f"Todos os carros (união das listas): {todos_carros}")

# Limpando todos os elementos da lista original
carros.clear()
print(f"Lista carros após clear(): {carros}")  # Saída: []
