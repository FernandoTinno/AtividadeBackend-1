
#como não pode usar Banco de dados para essa tarega, escolhi o dicionario para conseguir simular o banco de dados.
tasks_db = {}

# colocando essa variavel, eu consigo simular o auto incremento, que geralmente é aplicado aos bancos de dados, porque se não usar essa variavel, toda vez que uma tarefa for criada, ela ira apagar uma que já foi criada.
current_id = 1