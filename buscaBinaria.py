def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim )//2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio -1
    return -1

# exemplo de uso
nomes = ["Alice", "Amanda", "André", "Antonio", "Beatriz", "Bruno", "Camila", "Carlos", "Carolina", "Cecília", 
         "Clara", "Daniel", "Diego", "Eduarda", "Eduardo", "Elisa", "Emanuel", "Enzo", "Esther", "Felipe", 
         "Fernanda", "Francisco", "Gabriel", "Gabriela", "Guilherme", "Gustavo", "Heitor", "Helena", "Henrique", 
         "Hugo", "Isabel", "Isabella", "Isadora", "João", "Joaquim", "Júlia", "Lara", "Laura", "Leonardo", 
         "Letícia", "Lívia", "Lorena", "Lucas", "Luiza", "Manoel", "Marcelo", "Marcos", "Marina", "Mateus", 
         "Miguel", "Murilo", "Natália", "Nicolas", "Olívia", "Otávio", "Paula", "Pedro", "Rafaela", "Rafael", 
         "Ricardo", "Roberta", "Rodrigo", "Samuel", "Sara", "Sofia", "Stella", "Theo", "Thiago", "Vicente", 
         "Vinícius", "Vitor", "Yasmin", "Zoe", "Adriana", "Afonso", "Alexandre", "Alícia", "Aline", "Alonso", 
         "Álvaro", "Amélia", "Ana", "Anelise", "Angelina", "Antônia", "Aurora", "Bianca", "Breno", "Bruna", 
         "Caio", "Calebe", "Cássio", "Claudia", "Cristiano", "Davi", "Denise", "Diana", "Dylan", "Eliane", 
         "Eliseu", "Eloá", "Eva", "Evelyn", "Fausto", "Frederico", "Geovana", "Giovana", "Giovanni", "Gisele", 
         "Iara", "Igor", "Irene", "Isaque", "Ivan", "Janaina", "Jéssica", "Jonas", "Jorge", "José", "Juliana"]


elemento = "Rafael"
resutado = busca_binaria(nomes,elemento)

if resutado != -1:
            print(f"O elemento {elemento} está na posição {resutado} na lista.")
else: print(f"O elemento {elemento} não foi encontrado na lista.")
