import mysql.connector # importando a biblioteca,ou seja, fazendo uma ponte de mysql com python

class Clientes: # criando uma classe Clientes
    
    def __init__(self,nome_cliente,telefone,ultima_compra):  # definindo método de inialização e referindo a se mesmo e está acessando os atributos em cor laraja
        self.nome_cliente = nome_cliente  # criando uma variável que vai receber nome_cliente
        self.telefone = telefone          
        self.ultima_compra = ultima_compra



class SistemaCRM: # criando outra classe 
    def __init__(self):  # definindo método de inicialização da estrutura e está usando ele mesmo
        self.conexao = mysql.connector.connect(  # referindo a propria classe  e criando uma variável que ta recebendo a biblioteca acompanhada do método connect
            host = "localhost", # essa conexao está passando como parametro os atributos  host,user,password e database que são pré-requisitos pra fazer a conexão
            user = "root",
            password = "he182555@",
            database = "crm"

        ) 
        self.cursor = self.conexao.cursor() # referido a propria classe e está criando uma variável que está recebendo a outra variávej e adicionando método cursor

    def adicionar_registro(self,cliente): # definindo um métoto de adicionar e referindo a ele mesmo e passando um parâmetro de identificação logo para fazer a interação com as variáveis da classe de cima
        sql = "INSERT INTO clientes( nome_cliente,telefone,ultima_compra) VALUES (%s,%s,%s)" # criando uma variável recebendo o comando sql
        val = (cliente.nome_cliente,cliente.telefone,cliente.ultima_compra) # criando uma variável que está sendo passado como parâmetro a relaçãp da classe atual com as variáveis da classe de cima
        self.cursor.execute(sql,val) # está chamando o comando cursor e sendo acompanhado pelo comando de executar, e está executando  as duas variáveis que estão em parâmetros
        self.conexao.commit()  # chamando a variável dentro do proprio método sendo acompanhado do método para salvar
        print("novo registro adicionado.")  

    def listar_registros(self):
        self.cursor.execute("SELECT  id_cliente,nome_cliente,telefone,ultima_compra FROM clientes") #está chamando  a variável cursor e está sendo acompanhada do comando pra executar o comando sql que está em forma de string
        registros = self.cursor.fetchall() #criando uma variável que tá recebendo o cursor do proprio método e sendo acompanhado do método de fazer a busca
        for registro in registros : # fazer abusca de registro através da variável registros
            print(f" ID:{registro[0]}, Nome do cliente: {registro[1]}, telefone: {registro[2]}, ultima compra: {registro[3]}") # aqui é como se o registro estivesse recebendo os indicies de cada coluna da tabela matricula

    def fechar_conexao(self): # definido um método de fechar a conexao e cursor e está usando ele mesmo
        self.cursor.close()
        self.conexao.close()


sistema = SistemaCRM ()  # criando a intância de SistemaCRM
nome_cliente =input("digite seu nome:") # Criando uma variável pra receber essa informação do proprio usuario
telefone = input ("digite seu telefone pra contato:") # Criando uma variável pra receber essa informação do proprio usuario
ultima_compra = input ("qual foi sua ultima compra?") # Criando uma variável pra receber essa informação do proprio usuario
registro1 = Clientes (nome_cliente, telefone,ultima_compra) # e aqui criei outra variável que chamando a classe clientes e passando como parâmetro as informações de cada vriável
sistema.adicionar_registro(registro1) # aqui está executando o método e passando todas as informaões contidas em registro1


print("registros já salvos:")
sistema.listar_registros() # executando o método de listas

sistema.fechar_conexao # executando o método de fechar a conexão

#  Neste sistema, temos a criação de um banco de dados de CRM para guardar registros, e no código em Python, criamos um sistema de interação com o banco.