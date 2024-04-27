cinema = [[True for _ in range(8)] for _ in range(5)]


def mostrar_assentos(cinema):
    for i in range(len(cinema)):
        print(f'{i+1}', end='')
        for k in range(len(cinema[i])):
            if cinema[i][k] == True:
                print(f'|💺 {k+1} ✅|', end='')
            else:
                print(f'|💺 {k+1} ❌', end='')
            print('')


def escolher_assento(cinema):
    mostrar_assentos(cinema)
    while True:
        fila_livre = int(input('Escolha uma fila para se sentar: '))
        assento_livre = int(input('Escolha seu assento: '))
        if cinema[fila_livre-1][assento_livre-1] == False:
            print(f'o assento {
                  assento_livre} já foi reservado! Porfavor, escolha outro.')
        else:
            cinema[fila_livre-1][assento_livre-1] = False
            print(f'Você reservou o assento N°{
                  assento_livre} que se localiza na fila N°{fila_livre}!')
        mostrar_assentos(cinema)


escolher_assento(cinema)
