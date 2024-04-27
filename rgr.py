def alunos_e_medias():
    dados_alunos = []
    while True:
        aluno = input(
            "Digite o nome do aluno (para sair, digite 'sair'): ").capitalize()

        if aluno == 'Sair':
            break

        nota_1 = float(input('Digite a primeira nota: '))
        nota_2 = float(input('Digite a segunda nota: '))
        nota_3 = float(input('Digite a terceita nota: '))

        resultado = (nota_1 + nota_2 + nota_3) / 3

        print(f"A média do aluno {aluno} é: {resultado:.2f}")
        dados_alunos.append((aluno, resultado))

    return dados_alunos


def gerar_e_escrever_arquivo(dados_alunos, nome_arquivo):
    with open(nome_arquivo, 'w') as arq:
        for i, (aluno, media) in enumerate(dados_alunos, start=1):
            linha = f'{i}. Aluno: {aluno}, Média: {media:.2f}\n'
            arq.write(linha)


# Chamada da função alunos_e_medias para obter os dados dos alunos
dados_alunos = alunos_e_medias()

# Chamada da função para gerar e escrever o arquivo com os dados dos alunos
gerar_e_escrever_arquivo(dados_alunos, nome_arquivo='Medias de alunos.txt')
