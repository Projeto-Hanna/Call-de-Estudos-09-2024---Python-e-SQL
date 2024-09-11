-- Cria tabela personagens
CREATE TABLE IF NOT EXISTS personagens (nome TEXT PRIMARY KEY, idade INT, classe TEXT)

-- Exemplo de inserção de personagem
INSERT INTO personagens VALUES ('nome', 10, 'mago')

-- Busca por todos os personagens
SELECT * FROM personagens;

-- Busca pelo nome de todos os personagens
SELECT nome FROM personagens;

-- Busca todos os dados de um personagem a partir do nome
SELECT * FROM personagens WHERE nome = 'nome';

-- Deleta personagem a partir do nome
DELETE FROM personagens WHERE nome = 'nome';