import mysql.connector
import re


class DB: # Criação de uma classe para armazenar todas as funções e fazer apenas um import no app.py
    
    def __init__(self):
        pass

    def Criar_conexao(self): # Função para criar a conexão com o Banco de Dados.
        
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="Listatelefonica" # Nome do Banco de dados.
        )

        if connection == False: # Tratamento de erro ao conectar no banco de dados.
            return print("Erro no Banco de dados")
        else:
            return connection

    def adicionar(self,nome,telefone,cidade): # Função para adicionar um novo contato na lista.

        telefone_formatado = self.formatar_para_numeros(telefone)
        
        connection = self.Criar_conexao()
        cursor = connection.cursor()

        cursor.execute(f"Insert Into contatos (nomeContato,telefoneContato,cidadeContato) Values ('{nome}',{telefone_formatado},'{cidade}')") # Código para adicionar o número no banco de dados
        connection.commit() # Código para confirmar as alterações posteriores.
        
        cursor.close()
        connection.close()
        
        return print("Adicionado")
    
    def pesquisartodos(self): # Função para pesquisar e listar todos os contatos.
        connection = self.Criar_conexao()
        cursor = connection.cursor()

        cursor.execute(f"select * from contatos") # Código SQL para procurar todos os contatos.
        result = cursor.fetchall()
        print(result)

        contatos = {}

        for i in range(len(result)): # For utilizado para armazenar todos os contatos em uma dicionário.
            contatos[result[i][0]] = {
                "id": result[i][0],
                "nome": result[i][1],
                "numero": result[i][2],
                "cidade": result[i][3]
            }
        cursor.close()
        connection.close()
        
        return contatos
    
    def remover(self,id): # Função para remover um contato da lista baseando-se no ID.
        connection = self.Criar_conexao()
        cursor = connection.cursor()

        cursor.execute(f"DELETE FROM contatos WHERE idContato = {id}") #Código SQL para remover o contato do banco de dados.
        connection.commit()

        cursor.close()
        connection.close()

        return print("Excluido")
    
    def formatar_para_numeros(self,telefone): #Função para formatar o valor requisitado do html para que seja colocado no banco de dados.
    # Remove todos os caracteres que não são dígitos (0-9)
        telefone_formatado = re.sub(r'\D', '', telefone)
        return telefone_formatado