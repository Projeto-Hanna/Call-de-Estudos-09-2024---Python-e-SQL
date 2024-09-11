import sqlite3

# Realiza a conexão com o banco de dados, criando um arquivo banco.db se necessário ou carregando o que já existe
connection = sqlite3.connect('banco.db')

# Cria um cursor, para poder manipular o banco de dados
cursor = connection.cursor()

# Criar a tabela de personagens no banco, se ela não existir
cursor.execute('CREATE TABLE IF NOT EXISTS personagens (nome TEXT PRIMARY KEY, idade INT, classe TEXT)')

# Cria um personagem com nome, idade e classe
def criarPersonagem(nome, idade, classe):
  cursor.execute('INSERT INTO personagens VALUES (?, ?, ?)', (nome, idade, classe))
  # Recomendação: pesquisar sobre SQL Injection

  # O commit serve para salvar as mudanças no arquivo
  connection.commit()

# Lista o nome de todos os personagens salvos no banco
def listarPersonagens():
  cursor.execute('SELECT nome FROM personagens')
  return cursor.fetchall()

# Busca um personagem pelo nome
def buscarPersonagem(nome):
  cursor.execute('SELECT * FROM personagens WHERE nome = ?', (nome,))
  return cursor.fetchone()

# Deleta um personagem pelo nome
def deletarPersonagem(nome):
  cursor.execute('DELETE FROM personagens WHERE nome = ?', (nome,))
  connection.commit()

# Mensagem de boas-vindas
print('Olá. Boas-vindas ao nosso game RPG!! Selecione o que deseja fazer com seus personagens para continuar.')

# Lista de opções possíveis
print('[1] - Criar novo personagem\n[2] - Listar todos os personagens\n[3] - Buscar personagem\n[4] - Deletar personagem')

opcao = input('Selecione sua opção: ')

# While loop para evitar que o programa feche após executar uma opção
# Digite "0" para encerrar a execução
while opcao != '0':
  match opcao:
    case '1':
      nome = input('Digite o nome (precisa ser único): ')

      personagem = buscarPersonagem(nome)

      if personagem:
        print('Já existe um personagem com esse nome!')
      else:
        idade = int(input('Digite a idade: '))
        classe = input('Digite a classe: ')
        criarPersonagem(nome, idade, classe)
    case '2':
      personagens = listarPersonagens()
      
      for personagem in personagens:
        print('- ' + personagem[0])

    case '3':
      nome = input('Digite o nome do personagem que você quer buscar: ')
      personagem = buscarPersonagem(nome)
      print('- Nome do personagem: ' + personagem[0])
      print('- Idade do personagem: ' + str(personagem[1]))
      print('- Classe do personagem: ' + personagem[2])
    case '4':
      nome = input('Digite o nome do personagem que você quer deletar: ')
      personagem = buscarPersonagem(nome)

      if not personagem:
        print('Não existe um personagem com esse nome!')
      else:
        deletarPersonagem(nome)

  opcao = input('Selecione sua opção: ')

# Fecha o cursor
cursor.close()

# Fecja a conexão
connection.close()

# Mensagem final
print('Obrigado por jogar!! Seus personagens estarão aqui salvos quando você voltar ;)')