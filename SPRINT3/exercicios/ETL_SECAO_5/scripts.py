# Função para dividir linhas em colunas
def split_line(line):
    return [column.strip().strip('"') for column in line.split(',')]

# Abrir e ler o arquivo actors.csv
with open('actors.csv', 'r', encoding='utf-8') as csv_file:
    # Ler o cabeçalho
    header = split_line(csv_file.readline().strip())
    data = []
    
    for line in csv_file:
        row = split_line(line.strip())
        # Verifica se o número de colunas está correto
        if len(row) == len(header):
            data.append(row)
        else:
            print("Erro na linha com número incorreto de colunas:", row)

# Etapa 1: Atores com maior número de filmes
movies_index = header.index('Number of Movies')
actor_movies = {}

for row in data:
    actor_name = row[0].strip()
    num_movies = int(row[movies_index].strip())
    
    actor_movies[actor_name] = num_movies

most_movies_actor = max(actor_movies, key=actor_movies.get)
most_movies_count = actor_movies[most_movies_actor]

with open('etapa-1.txt', 'w', encoding='utf-8') as file:
    file.write(f"{most_movies_actor} - {most_movies_count}\n")

# Etapa 2: Média de receita de bilheteira
gross_index = header.index('Gross')
total_gross = sum(float(row[gross_index].strip()) for row in data)
average_gross = total_gross / len(data)

with open('etapa-2.txt', 'w', encoding='utf-8') as file:
    file.write(f"Média de receita de bilheteira: {average_gross}\n")

# Etapa 3: Ator com a maior média de receita
average_index = header.index('Average per Movie')
actor_average = {}

for row in data:
    actor_name = row[0].strip()
    average = float(row[average_index].strip())
    actor_average[actor_name] = average

highest_average_actor = max(actor_average, key=actor_average.get)
highest_average_value = actor_average[highest_average_actor]

with open('etapa-3.txt', 'w', encoding='utf-8') as file:
    file.write(f"{highest_average_actor} - {highest_average_value}\n")

# Etapa 4: Contagem de filmes
movie_index = header.index('#1 Movie')
movie_count = {}

for row in data:
    movie_name = row[movie_index].strip()
    if movie_name in movie_count:
        movie_count[movie_name] += 1
    else:
        movie_count[movie_name] = 1

sorted_movies = sorted(movie_count.items(), key=lambda x: (-x[1], x[0]))

with open('etapa-4.txt', 'w', encoding='utf-8') as file:
    for movie, count in sorted_movies:
        file.write(f"{movie} aparece {count} vez(es) no dataset\n")

# Etapa 5: Listar atores ordenados pela receita bruta
total_gross_index = header.index('Total Gross')
actor_gross = {}

for row in data:
    actor_name = row[0].strip()
    total_gross = float(row[total_gross_index].strip())
    
    if actor_name in actor_gross:
        actor_gross[actor_name] += total_gross
    else:
        actor_gross[actor_name] = total_gross

sorted_actors = sorted(actor_gross.items(), key=lambda x: x[1], reverse=True)

with open('etapa-5.txt', 'w', encoding='utf-8') as file:
    for actor, gross in sorted_actors:
        file.write(f"{actor} - {gross}\n")

# Exibir os resultados
for actor, gross in sorted_actors:
    print(f"{actor} - {gross}")
