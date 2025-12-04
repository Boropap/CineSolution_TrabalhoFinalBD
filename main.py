import psycopg2
import psycopg2.extras

hostname = 'pg-20b26842-caio-d9b3.d.aivencloud.com' 
database = 'CineSolution'
username = 'avnadmin'
pwd = 'AVNS_HOEIdywgc3g7QxM8FTA'
port_id = '11136'
conn = None
cur = None

def makeConnnection():#Função para conectar ao banco de dados
    try:
        conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)
        return conn
    except Exception as error:
        print(error)
        print("Failed to make connection to CineSolution data base.")
        return None

def addUser(conn):#Função para adicionar um novo usuário
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:#Vai primeiro selecionar tudo de pessoa e imprimir os dados já na tabela
        cur.execute('''select * from pessoa''')
        for row in cur.fetchall():
            print(numLinhas, row['pessoanome'], "-", row['emailpessoa'])
            numLinhas += 1

        nomePessoa = input("Digite o nome da pessoa que quer adicionar: ").strip()#Em seguida irá armazenar o que o usuário quer adicionar
        dataNasc = input("Digite a data de nascimento (Ex.2003-12-31): ").strip()
        emailPessoa = input("Digite o email da pessoa: ").strip()
        senhaPessoa = input("Digite a senha da pessoa: ").strip()

        adicionarUsuario = '''insert into pessoa(pessoaNome, dataNasc, emailPessoa, senhaPessoa) values (%s, %s, %s, %s);'''#Esse é o comando para adicionar os dados novos na tabela
        valorUsuarios = (nomePessoa, dataNasc, emailPessoa, senhaPessoa)
        cur.execute(adicionarUsuario, valorUsuarios)#E aqui o comando é executado

        conn.commit()#E por fim mandado ao banco de dados conectado
        print("Usuário adicionado!")

    except Exception as error:#Caso dê alguma coisa errada, irá desfazer tudo que já tinha feita, imprimir o erro na tela e avisar o usuário através de uma mensagemm
        conn.rollback()
        print(error)
        print("Não foi possível adicionar usuário")
        return None

def addMovie(conn):#Função para adicionar um novo filme
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from filme''')#Imprime todos os filmes já na tabela
        for row in cur.fetchall():
            print(numLinhas, row['filmenome'], "-", row['duracaominutos'], "-", row['datafilme'])
            numLinhas += 1

        filmeNome = input("Digite o nome do filme: ").strip()#Armazena informações do novo filme que o usuário deseja cadastrar
        dataFilme = input("Digite a data de lançamento do filme (Ex. 1999-6-12): ").strip()
        generoFilme = input("Digite os dois principais gêneros do filme (Ex. Thriller/Drama): ").strip()
        duracaoFilme = input("Digite em minutos a duração do filme (Ex. 198): ").strip()

        adicionarFilme = '''insert into filme(filmenome, datafilme, generofilme, duracaominutos) values (%s, %s, %s, %s)'''#Realiza comando para acrescentar os novos valores
        valorFilme = (filmeNome, dataFilme, generoFilme, duracaoFilme)
        cur.execute(adicionarFilme, valorFilme)#Executa o comando

        conn.commit()#Envia resultado para o banco de dados
        print("Filme Adicionado!")

    except Exception as error:#Caso há falha em algo, desfaz o que tinha feito, imprime o erro na tela, e avisa o usuário a falha
        conn.rollback()
        print(error)
        print("Não foi possível adicionar filme")
        return None

def addAtor(conn):#Função para adicionar um novo ator
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from ator''')#Lista todos atores na tabela
        for row in cur.fetchall():
            print(numLinhas, row['atornome'])
            numLinhas += 1

        atorNome = input("Digite o nome do ator: ").strip()#Armazena novo ator que usuário quer adicionar

        adicionarAtor = '''insert into ator(atornome) values (%s)'''#Realiza comando de adicionar ator na tabela de atores
        valorAtor = (atorNome,)
        cur.execute(adicionarAtor, valorAtor)#Executa o comando

        conn.commit()#Envia resultado para tabela no banco de dados
        print("Ator Adicionado!")

    except Exception as error:#Caso falhe, desfaz o que tinha sido feito, imprime o erro e avisa o usuário na tela
        conn.rollback()
        print(error)
        print("Não foi possível adicionar ator")
        return None
    
def addDiretor(conn):#Função para adicionar um novo diretor
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from diretor''')#Lista todos diretores da tabela
        for row in cur.fetchall():
            print(numLinhas, row['diretornome'])
            numLinhas += 1

        diretorNome = input("Digite o nome do diretor: ").strip()#Armazena novo diretor que usuário quer adicionar

        adicionarDiretor = '''insert into diretor(diretornome) values (%s)'''#Realiza comando de adicionar diretor na tabela de diretores
        valorDiretor = (diretorNome,)
        cur.execute(adicionarDiretor, valorDiretor)#Executa o comando

        conn.commit()#Envia resultado para tabela no banco de dados
        print("Diretor Adicionado!")

    except Exception as error:#Caso falhe, desfaz o que tinha sido feito, imprime o erro e avisa o usuário na tela
        conn.rollback()
        print(error)
        print("Não foi possível adicionar diretor")
        return None
 
def addReview(conn):#Função para adicionar uma nova review
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from pessoa''')#Imprime todas pessoas disponíveis na tela
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['pessoanome']:<20} - ID:{row['idpessoa']}")
            numLinhas += 1

        pessoaDesejada = int(input("Digite o id da pessoa que quer fazer a review: ").strip())#Pede para o usuário escolher uma pessoa baseado nos IDs e salva a escolha
        print("______________________________________")

        numLinhas = 1
        cur.execute('''select * from filme''')#Imprime todos filmes na tela
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['filmenome']:<20} - ID:{row['idfilme']}")
            numLinhas += 1

        filmeDesejado = int(input("Digite o id do filme que quer fazer a review: ").strip())#Pede para o usuário escolher um filme baseado nos IDs e salva a escolha

        numAvali = input("Digite um valor de 1 a 10 que você daria para o filme: ").strip()#Pede o usuário a nota e o comentário
        comentarioAvali = input("Digite um comentário que deseja fazer ao filme: ").strip()

        adicionarReview = '''insert into avaliacaopessoafilme(idfilmeavali, idpessoaavali, numaval, comentarioaval) values (%s, %s, %s, %s)'''#Realiza o script para adicionar uma review
        valorReview = (filmeDesejado, pessoaDesejada, numAvali, comentarioAvali)
        cur.execute(adicionarReview, valorReview)#Executa esse script com os valores dado pelo usuário

        conn.commit()#Envia resultado para tabela no banco de dados
        print("Review Adicionada!")

    except Exception as error:#Caso haja falha, desfaz o que tinha sido feito, imprime o erro e avisa o usuário
        conn.rollback()
        print(error)
        print("Não foi possível adicionar uma review")
        return None

def addGrupo(conn):#Função para adicionar um novo grupo
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from grupo''')#Mostra todos grupos disponíveis
        for row in cur.fetchall():
            print(numLinhas, row['gruponome'])
            numLinhas += 1

        grupoNome = input("Digite o nome do grupo: ").strip()#Pede o nome do grupo

        adicionarGrupo = '''insert into grupo(gruponome) values (%s)'''#Cria script para adicionar um novo grupo
        valorGrupo = (grupoNome,)
        cur.execute(adicionarGrupo, valorGrupo)#Executa esse script

        conn.commit()#Envia resultado para tabela no banco de dados
        print("Grupo criado!")

    except Exception as error:#Caso falhe, desfaz o que tinha sido feito, imprime o erro e avisa o usuário
        conn.rollback()
        print(error)
        print("Não foi possível criar grupo")
        return None
    
def filmeAtor(conn):#Função para atrelar um ator a um filme
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from ator''')#imprime todos atores
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['atornome']:<20} - ID:{row['idator']}")
            numLinhas += 1

        atorDesejado = int(input("Digite o id do ator que deseja: ").strip())#Armazena o ID do ator desejado
        print("______________________________________")

        numLinhas = 1
        cur.execute('''select * from filme''')#Imprime todos os filmes
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['filmenome']:<20} - ID:{row['idfilme']}")
            numLinhas += 1

        filmeDesejado = int(input(f"Digite o id do filme cujo o ator escolhido participa: ").strip())#Armazena o ID do filme desejado

        adicionarFilmeAtor = '''insert into filmeator(idfilmeatrib, idatoratrib) values (%s, %s)'''#Cria script para atribuir ator a um filme
        valorFilmeAtor = (filmeDesejado, atorDesejado,)
        cur.execute(adicionarFilmeAtor, valorFilmeAtor)#Executa o script

        conn.commit()#Envia resultado para tabela
        print("Ator atribuido ao filme!")

    except Exception as error:#Caso falhe, desfaz o que tinha sido feito, imprime o erro e avisa o usuário da falha
        conn.rollback()
        print(error)
        print("Não foi possível atribuir ator ao filme.")
        return None

def filmeDiretor(conn):#Função para atrelar um diretor a um filme
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from diretor''')#imprime todos diretores
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['diretornome']:<20} - ID:{row['iddiretor']}")
            numLinhas += 1

        diretorDesejado = int(input("Digite o id do diretor que deseja: ").strip())#Armazena o ID do diretor desejado
        print("______________________________________")

        numLinhas = 1
        cur.execute('''select * from filme''')
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['filmenome']:<20} - ID:{row['idfilme']}")
            numLinhas += 1

        filmeDesejado = int(input(f"Digite o id do filme cujo o diretor escolhido participa: ").strip())#Armazena o ID do filme desejado

        adicionarFilmeDiretor = '''insert into filmediretor(idfilmeatrib, iddiretoratrib) values (%s, %s)'''#Cria script para atribuir diretor a um filme
        valorFilmeDiretor = (filmeDesejado, diretorDesejado,)
        cur.execute(adicionarFilmeDiretor, valorFilmeDiretor)#Executa o script

        conn.commit()#Envia resultado para tabela
        print("Diretor atribuido ao filme!")

    except Exception as error:#Caso falhe, desfaz o que tinha sido feito, imprime o erro e avisa o usuário da falha
        conn.rollback()
        print(error)
        print("Não foi possível atribuir diretor ao filme.")
        return None
    
def grupoPessoa(conn):#Função para atrelar uma pessoa a um grupo
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from pessoa''')#Lista todas pessoas na tabela
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['pessoanome']:<20} - ID:{row['idpessoa']}")
            numLinhas += 1

        pessoaDesejada = int(input("Digite o id da pessoa que quer adicionar em um grupo: ").strip())#Armazena o ID da pessoa que deseja
        print("______________________________________")

        numLinhas = 1
        cur.execute('''select * from grupo''')#Lista todos os grupos na tela
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['gruponome']:<20} - ID:{row['idgrupo']}")
            numLinhas += 1

        grupoDesejado = int(input("Digite o id do grupo no qual vai adicionar pessoa: ").strip())#Armazena o ID do grupo que deseja

        adicionarGrupoPessoa = '''insert into grupopessoa(idpessoaatrib, idgrupoatrib) values (%s, %s)'''#Cria script para adicionar pessoa em um grupo
        valorGrupoPessoa = (pessoaDesejada, grupoDesejado, )
        cur.execute(adicionarGrupoPessoa, valorGrupoPessoa)#Executa esse script

        conn.commit()#Envia resultado para tabela
        print("Pessoa Adicionada no grupo!")

    except Exception as error:#Caso falhe, desfaz o que tinha sido feito, imprime erro e retorna falha ao usuário
        conn.rollback()
        print(error)
        print("Não foi possível adicionar a pessoa no grupo")
        return None
    
def updateUser(conn):#Função para atualizar alguma informação do usuário
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from pessoa''')#Imprime todas as pessoas da tabela
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['pessoanome']:<20} - ID:{row['idpessoa']}")
            numLinhas += 1

        pessoaDesejada = int(input("Digite o id da pessoa que deseja alterar: ").strip())#Armazena ID da pessoa desejada
        print("______________________________________")
        print("1 - Nome\n2 - Data Nascimento\n3 - Senha")
        opcaoDesejada = input("Digite o número do que deseja alterar: ").strip()#Armazena a opção que o usuário deseja

        if(opcaoDesejada == "1"):
                
                novoNome = input("Digite o novo nome da pessoa: ").strip()#Armazena novo nome para pessoa
                updateUsuario = '''Update pessoa set pessoanome = %s where idpessoa = %s'''#Cria script para alterar pessoa com o ID armazenado e o novo nome armazenado
                valoresAlteracao = (novoNome, pessoaDesejada)#Atrela essas informações, ID e valor alterado na variável

        elif(opcaoDesejada == "2"):
                
                novaDataNasc = input("Digite a nova data de nascimento (Ex.2003-6-14): ").strip()#Armazena data de nascimento para pessoa
                updateUsuario = '''Update pessoa set datanasc = %s where idpessoa = %s'''#Cria script para alterar pessoa com o ID armazenado e nova data armazenada
                valoresAlteracao = (novaDataNasc, pessoaDesejada)#Atrela essas informações, ID e valor alterado na variável

        elif(opcaoDesejada == "3"):
                
                novaSenha = input("Digite a nova senha: ").strip()#Armazena nova senha para pessoa
                updateUsuario = '''Update pessoa set senhapessoa = %s where idpessoa = %s'''#Cria script para alterar pessoa com o ID armazenado e a nova senha armazenada
                valoresAlteracao = (novaSenha, pessoaDesejada)#Atrela essas informações, ID e valor alterado na variável

        else:
            print("Pessoa inválida.")#Caso usuário selecione uma pessoa inexistente, retorna nada
            return None

        cur.execute(updateUsuario, valoresAlteracao)#Executa o script com os dados armazenados
        conn.commit()#Envia resultado para tabela
        print("Valores de pessoa atualizado!")

    except Exception as error:#Caso falhe, desfaz o que tinha sido feito, imprime erro e avisa ao usuário
        conn.rollback()
        print(error)
        print("Não foi possível alterar valor de Pessoa.")
        return None
    
def updateMovie(conn):#Função para atualizar alguma informação do filme
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from filme''')#Imprime todos filmes na tela
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['filmenome']:<20} - ID:{row['idfilme']}")
            numLinhas += 1

        filmeDesejado = int(input("Digite o id do filme que deseja alterar: ").strip())#Salva ID do filme desejado
        print("______________________________________")
        print("1 - Nome\n2 - Data lançamento\n3 - Duração\n4 - Gênero")
        opcaoDesejada = input("Digite o número do que deseja alterar: ").strip()#Salva opção que o usuário quer alterar

        if(opcaoDesejada == "1"):
                
                novoNome = input("Digite o novo nome do filme: ").strip()#Armazena novo nome do filme
                updateFilme = '''Update filme set filmenome = %s where idfilme = %s'''#Cria script para realizar alteração
                valoresAlteracao = (novoNome, filmeDesejado)#Atrelas dados armazenados juntos

        elif(opcaoDesejada == "2"):
                
                novaDataLanc = input("Digite a nova data de lançamento (Ex. 2003-6-14): ").strip()#Armazena nova data de lançamento do filme
                updateFilme = '''Update filme set datafilme = %s where idfilme = %s'''#Cria script para realizar alteração
                valoresAlteracao = (novaDataLanc, filmeDesejado)#Atrel dados armazenados juntos

        elif(opcaoDesejada == "3"):
                
                novoDuracao = int(input("Digite a nova duração do filme: ").strip())#Armazena nova duração do filme
                updateFilme = '''Update filme set duracaominutos = %s where idfilme = %s'''#Cria script para realizar alteração
                valoresAlteracao = (novoDuracao, filmeDesejado)#Atrela dados armazenados juntos

        elif(opcaoDesejada == "4"):
                
                novoGenero = input("Digite os novos dois gêneros (Ex. Comedy/Drama): ").strip()#Armazena novo gênero do filme
                updateFilme = '''Update filme set generofilme = %s where idfilme = %s'''#Cria script para realizar alteração
                valoresAlteracao = (novoGenero, filmeDesejado)#Atrela dados armazenados juntos

        else:
            print("Filme inválido.")#Se ID filme desejado não existe, retorna nada
            return None

        cur.execute(updateFilme, valoresAlteracao)#Executa script com os dados armazenados 
        conn.commit()
        print("Valores de filme atualizados!")

    except Exception as error:#Caso falhe, desfaz o que tinha sido feito, retorna erro e avisa o usuário da falha
        conn.rollback()
        print(error)
        print("Não foi possível alterar valor de filme.")
        return None
    
def updateAtor(conn):#Função para atualizar alguma informação de um ator
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from ator''')#Imprime todos os atores
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['atornome']:<20} - ID:{row['idator']}")
            numLinhas += 1

        atorDesejado = int(input("Digite o id do ator que deseja alterar: ").strip())#Armazena ID do ator que deseja alterar
        print("______________________________________")

        novoNome = input("Digite o novo nome do Ator: ").strip()#Armazena novo nome do ator
        updateAtor = '''Update ator set atornome = %s where idator = %s'''#Cria script para alterar nome do ator
        valoresAlteracao = (novoNome, atorDesejado)#Armazena dados dados juntos

        cur.execute(updateAtor, valoresAlteracao)#Executa script usando os dados armazenados
        conn.commit()#Envia resultado para tabela do banco de dados
        print("Valores de ator atualizados!")

    except Exception as error:#Em caso de falha, desfaz o que tinha sido feito, retorna erro e avisa ao usuário
        conn.rollback()
        print(error)
        print("Não foi possível alterar valor de ator.")
        return None
    
def updateDiretor(conn):#Função para atualizar alguma informação de um diretor
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from diretor''')#Imprime todos os diretores 
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['diretornome']:<20} - ID:{row['iddiretor']}")
            numLinhas += 1

        diretorDesejado = int(input("Digite o id do diretor que deseja alterar: ").strip())#Armazena o ID do diretor desjado
        print("______________________________________")

        novoNome = input("Digite o novo nome do diretor: ").strip()#Armazena o nome do novo diretor
        updateDiretor = '''Update diretor set diretornome = %s where iddiretor = %s'''#Cria script para alterar valor de diretor
        valoresAlteracao = (novoNome, diretorDesejado)#Armazena ID e novo dado do diretor

        cur.execute(updateDiretor, valoresAlteracao)#Executa script com os dados armazenados
        conn.commit()#Envia resultado para tabela
        print("Valores de diretor atualizados!")

    except Exception as error:#Se der erro, desfaz o que tinha sido feito, imprime erro e avisa ao usuário a falha
        conn.rollback()
        print(error)
        print("Não foi possível alterar valor de diretor.")
        return None

def updateGrupo(conn):#Função para atualizar alguma informação de um grupo
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from grupo''')#Imprime todos os grupos
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['gruponome']:<20} - ID:{row['idgrupo']}")
            numLinhas += 1

        grupoDesejado = int(input("Digite o id do grupo que deseja alterar: ").strip())#Armazena ID do grupo desejado
        print("______________________________________")

        novoNome = input("Digite o novo nome do grupo: ").strip()#Armazena novo nome do grupo
        updateGrupo = '''Update grupo set gruponome = %s where idgrupo = %s'''#Cria script para atualizar o grupo
        valoresAlteracao = (novoNome, grupoDesejado)#Armazena ID do grupo desejado e o novo nome

        cur.execute(updateGrupo, valoresAlteracao)#Executa script com os dados armazenados
        conn.commit()#Envia resultado para tabela
        print("Valores de grupo atualizados!")

    except Exception as error:#Caso dê erro, desfaz oque tinha sido feito, imprime o erro e retorna falha ao usuário
        conn.rollback()
        print(error)
        print("Não foi possível alterar valor de grupo.")
        return None

def deleteUser(conn):#Função para deletar um usuário
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from pessoa''')#Imprime todas pessoas
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['pessoanome']:<20} - ID:{row['idpessoa']}")
            numLinhas += 1

        pessoaDesejado = int(input("Digite o id da pessoa que deseja apagar: ").strip())#Armazena o ID da pessoa que deseja
        print("______________________________________")

        print("Tem certeza que deseja apagar? Apagar pessoa irá apagar as suas reviews e participações em grupos também.\n")#Cria uma pergunta de confirmação
        confimarEscolha = input("Digite a letra da sua escolha (S/N): ").strip().capitalize()#Armazena escolha do usuário
        if(confimarEscolha == "S"):#Continua com processo de apagar pessoa
            print("Apagando pessoa...")
            deletePessoa = '''delete from pessoa where idpessoa = %s'''#Cria script para apagar pessoa

            cur.execute(deletePessoa, (pessoaDesejado,))#Executa o script
            conn.commit()#Manda resultado para o banco de dados
            print("Pessoa apagada do banco de dados.")
        else:#Cancela procsso de apagar

            print("Processo de deletar pessoa cancelado.")
            return None

    except Exception as error:#Caso dê erro, desfaz o que tinha sido feito, imprime erro e avisa ao usuário
        conn.rollback()
        print(error)
        print("Não foi possível apagar pessoa.")
        return None
    
def deleteFilme(conn):#Função para deletar um filme
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from filme''')#Imprime todos os filmes
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['filmenome']:<20} - ID:{row['idfilme']}")
            numLinhas += 1

        filmeDesejado = int(input("Digite o id do filme que deseja apagar: ").strip())#Armazena ID do filme desejado
        print("______________________________________")

        print("Tem certeza que deseja apagar? Apagar filme irá apagar as suas reviews\n")#Cria pergunta de confirmação
        confimarEscolha = input("Digite a letra da sua escolha (S/N): ").strip().capitalize()
        if(confimarEscolha == "S"):#Continua com processo de apagar
            print("Apagando filme...")
            deleteFilme = '''delete from filme where idfilme = %s'''#Cria script para apagar filme

            cur.execute(deleteFilme, (filmeDesejado,))#Executa o script
            conn.commit()#Envia resultado para o banco de dados
            print("Filme apagado do banco de dados.")
        else:#Cancela processo de apagar

            print("Processo de deletar filme cancelado.")
            return None

    except Exception as error:#Em caso de falha, desfaz o que tinha sido feito, imprime erro e avisa o usuário
        conn.rollback()
        print(error)
        print("Não foi possível apagar filme.")
        return None

def deleteAtor(conn):#função para deletar um ator
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from ator''')#Imprime todos os atores
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['atornome']:<20} - ID:{row['idator']}")
            numLinhas += 1

        atorDesejado = int(input("Digite o id do ator que deseja apagar: ").strip())#Armazena ID do ator desejado
        print("______________________________________")

        print("Tem certeza que deseja apagar? Apagar ator irá apagar também sua ligação em filmes\n")#Cria pergunta de confirmação
        confimarEscolha = input("Digite a letra da sua escolha (S/N): ").strip().capitalize()
        if(confimarEscolha == "S"):#Continua com processo de apagar
            print("Apagando ator...")
            deleteAtor = '''delete from ator where idator = %s'''#Cria script para apagar ator

            cur.execute(deleteAtor, (atorDesejado,))#Executa o script
            conn.commit()#Envia resultado para o banco de dados
            print("Ator apagado do banco de dados.")
        else:#Cancela processo de apagar

            print("Processo de deletar ator cancelado.")
            return None

    except Exception as error:#Em caso de falha, desfaz o que tinha sido feito, imprime erro e avisa o usuário
        conn.rollback()
        print(error)
        print("Não foi possível apagar ator.")
        return None
    
def deleteDiretor(conn):#função para deletar um diretor
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from diretor''')#Imprime todos os diretores
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['diretornome']:<20} - ID:{row['iddiretor']}")
            numLinhas += 1

        diretorDesejado = int(input("Digite o id do diretor que deseja apagar: ").strip())#Armazena ID do diretor desejado
        print("______________________________________")

        print("Tem certeza que deseja apagar? Apagar diretor irá apagar também sua ligação em filmes\n")#Cria pergunta de confirmação
        confimarEscolha = input("Digite a letra da sua escolha (S/N): ").strip().capitalize()
        if(confimarEscolha == "S"):#Continua com processo de apagar
            print("Apagando diretor...")
            deleteDiretor = '''delete from diretor where iddiretor = %s'''#Cria script para apagar diretor

            cur.execute(deleteDiretor, (diretorDesejado,))#Executa o script
            conn.commit()#Envia resultado para o banco de dados
            print("Diretor apagado do banco de dados.")
        else:#Cancela processo de apagar

            print("Processo de deletar diretor cancelado.")
            return None

    except Exception as error:#Em caso de falha, desfaz o que tinha sido feito, imprime erro e avisa o usuário
        conn.rollback()
        print(error)
        print("Não foi possível apagar diretor.")
        return None
    
def deleteGrupo(conn):#Função para deletar um grupo
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:
        cur.execute('''select * from grupo''')#Imprime todos os grupos
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['gruponome']:<20} - ID:{row['idgrupo']}")
            numLinhas += 1

        grupoDesejado = int(input("Digite o id do grupo que deseja apagar: ").strip())#Armazena ID do grupo desejado
        print("______________________________________")

        print("Tem certeza que deseja apagar? Apagar grupo irá apagar também sua ligação com pessoas\n")#Cria pergunta de confirmação
        confimarEscolha = input("Digite a letra da sua escolha (S/N): ").strip().capitalize()
        if(confimarEscolha == "S"):#Continua com processo de apagar
            print("Apagando grupo...")
            deleteGrupo = '''delete from grupo where idgrupo = %s'''#Cria script para apagar grupo

            cur.execute(deleteGrupo, (grupoDesejado,))#Executa o script
            conn.commit()#Envia resultado para o banco de dados
            print("Grupo apagado do banco de dados.")
        else:#Cancela processo de apagar

            print("Processo de deletar grupo cancelado.")
            return None

    except Exception as error:#Em caso de falha, desfaz o que tinha sido feito, imprime erro e avisa o usuário
        conn.rollback()
        print(error)
        print("Não foi possível apagar grupo.")
        return None
    
def averageReviewMovies(conn):#Função para mostrar média de todos filmes
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1

    try:

        cur.execute('''select * from filmesmedias''')#Imprime todos os dados da tabela Review já criada
        for row in cur.fetchall():
            print(f"{numLinhas:<2}- {row['filmenome']:<20} - Média das reviews:{row['mediafilme']}")#Imprime o nome do filme e em seguida sua média de reviews
            numLinhas += 1


    except Exception as error:#Em caso de erro, imprime o erro e avisa o usuário
        print(error)
        print("Não foi possível mostrar as médias dos filmes")
        return None
    
def filmeAtorDiretor(conn):#Função para mostrar um filme e seus respectivos atores e diretores
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    numLinhas = 1
    count = 0

    try:

        cur.execute('''select * from filmediretorator''')#Imprime todos os dados da tabela review filmediretorator
        for row in cur.fetchall():
            count = 0
            print(f"{numLinhas:<2}- {row['filmenome']:<20}")#primeiro imprime o nome do filme

            print(" - Ator(es): ", end = " ")#Em seguida um texto para indicar atores
            while(count < len(row['atores'])):#Vai imprimir ator do filme enquanto tiver ator naquela lista
                print( f"{row['atores'][count]}", end = "/")
                count += 1
            count = 0
            
            print("")
            print(" - Diretor(es): ", end=" ")#Em seguida um texto para indicar diretores
            while(count < len(row['diretores'])):#Vai imprimir diretor do filme enquanto tiver diretor naquela lista
                print( f"{row['diretores'][count]}", end = "/ ")
                count += 1

            numLinhas += 1
            print("\n")



    except Exception as error:#Caso falhe, imprime o erro na tela e avisa ao usuário
        print(error)
        print("Não foi possível mostrar as filmes e seus atores e diretores")
        return None
    
def integrantesGrupos(conn):#Função para mostrar grupo e seus integrantes
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

    try:

        cur.execute('''select * from pessoasgrupos''')#Pega todos os dados da tabela review pessoasgrupos

        totalLinhas = cur.fetchall()#Armazena o total de linhas daquela tabela

        if totalLinhas == 0:#Se não existir linhas, não existem grupos. Avisa o usuário e retorna nada
            print("Não existem grupos")
        
        linhagrupoAtual = None

        for row in totalLinhas:#Para cada linha no total de linhas
            count = 0
            linhaGrupo = row['gruponome']#Armazena o nome do grupo atual
            linhaPessoa = row['pessoanome']#Armazena o nome da pessoa atual
            
            if(linhaGrupo != linhagrupoAtual):#Se nome do grupo atual for diferente do grupo seguinte
                print(f"\n{linhaGrupo}")#Imprime nome do grupo atual
                linhagrupoAtual = linhaGrupo#Muda o nome do grupo atual para usar nas próximas comparações
            
            print(f" - {linhaPessoa}")#Imprime pessoa atual da linha

    except Exception as error:#Em caso de erro, imprime o erro e avisa ao usuário
        print(error)
        print("Não foi possível mostrar os grupos e seus integrantes")
        return None

def menu(conn):#Função menu
    choice = 50

    while choice != "0":#Enquanto choice for zero
        #imprima o menu
        print("______________________________________\n" \
        "1 - Adicionar usuário\n" \
        "2 - Adicionar filme\n" \
        "3 - Adicionar ator\n" \
        "4 - Adicionar diretor\n" \
        "5 - Adicionar review\n" \
        "6 - Criar grupo\n" \
        "___\n" \
        "7 - Atribuir filme a um ator\n" \
        "8 - Atribuir filme a um diretor\n" \
        "9 - Adicionar pessoa em um grupo\n" \
        "___\n" \
        "10 - Alterar valor de um usuário\n" \
        "11 - Alterar valor de um filme\n" \
        "12 - Alterar valor de um ator\n" \
        "13 - Alterar valor de um diretor\n" \
        "14 - Alterar valor de um grupo\n" \
        "___\n" \
        "15 - Apagar um usuário\n" \
        "16 - Apagar um filme\n" \
        "17 - Apagar um ator\n" \
        "18 - Apagar um diretor\n" \
        "19 - Apagar um grupo\n" \
        "___\n" \
        "20 - Média todos filmes\n" \
        "21 - Filme + Ator + Diretor\n" \
        "22 - Grupo e seus integrantes\n" \
        "0 - Sair")

        #Armazena escolha do menu do usuário
        choice = input("\nDigite o número:")
        print("______________________________________")
        match choice:
            case "1":
                addUser(conn)
            case "2":
                addMovie(conn)
            case "3":
                addAtor(conn)
            case "4":
                addDiretor(conn)
            case "5":
                addReview(conn)
            case "6":
                addGrupo(conn)
            case "7":
                filmeAtor(conn)
            case "8":
                filmeDiretor(conn)
            case "9":
                grupoPessoa(conn)       
            case "10":
                updateUser(conn)
            case "11":       
                updateMovie(conn)
            case "12":                
                updateAtor(conn)
            case "13":                
                updateDiretor(conn)
            case "14":               
                updateGrupo(conn)
            case "15":               
                deleteUser(conn)
            case "16":               
                deleteFilme(conn)
            case "17":               
                deleteAtor(conn)
            case "18":               
                deleteDiretor(conn)
            case "19":
                deleteGrupo(conn)
            case "20":
                averageReviewMovies(conn)
            case "21":
                filmeAtorDiretor(conn)
            case "22":
                integrantesGrupos(conn)
            case "0":#0 é sair do programa
                print("Saindo...\n")
            case _:#Default é avisar ao usuário para tentar de novo
                print("Número inválido, tente novamente\n")


def main():#Função main
    conn = makeConnnection()#Faz conecção com banco de dados
    try:#Caso falhe retorne nada
        if conn is None:
            return

        #Chama menu e dá como parâmetro valor entregue pela conecção feita da função makeConnection() criada
        menu(conn)
        print("Tchau!\n")
    
    #Depois de tudo ser feito, fecha conecção e fecha variável para rodar script
    finally:
        if conn != None:
            conn.close()
        if cur != None:
            cur.close()

#Chamar a função main()
if __name__  == "__main__":
    main()