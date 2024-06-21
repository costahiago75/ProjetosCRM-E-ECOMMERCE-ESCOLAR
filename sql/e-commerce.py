import mysql.connector  # importando a biblioteca,ou seja, fazendo uma ponte de mysql com python


class Cliente: # criando uma classe Clientes
    
    def __init__(self,nome_cliente,cpf): # definindo método de inialização e referindo a se mesmo e está acessando os parâmetros (é como se fosse as clunas da tabela) em cor laraja
        self.nome_cliente = nome_cliente # criando uma variável dentro do proprio método e classe que vai receber nome_cliente
        self.cpf = cpf # criando uma variável que vai receber o parâmetro cpf (esse parâmetro é como se fosse uma coluna da tabela)



class Produtos:  # criando uma classe
    def __init__(self,nome_produto,preco): # definindo método de inialização e referindo a se mesmo e está acessando os parâmetros (é como se fosse as clunas da tabela) em cor laraja
        self.nome_produto = nome_produto # criando uma variável dentro da propria classe que vai receber o parâmetro nome_produto (esse parâmetro é como se fosse uma coluna da tabela)
        self.preco = preco #criando ouma variável dentro do proprio método  e clase que está recebendo o parâmetro


class SistemaDeProduto:  # criando uma classe

    def __init__(self):  # definindo método de inialização e referindo a se mesmo
        self.conexao = mysql.connector.connect(  # referindo a propria classe  e criando uma variável que ta recebendo a biblioteca acompanhada do método connect
            host="localhost",  # essa conexao está passando como parametro os atributos  host,user,password e database que são pré-requisitos pra fazer a conexão
            user="root",
            password="he182555@",
            database="e_commerce"
        )
        self.cursor = self.conexao.cursor()  # criando outra variável dentro da propria classe e método que está recebendo a variável do proprio método e classe e está sendo acompanhada do método cursor, cursor é  que  se faz o acesso com mysql

    def adicionar_cliente(self,tei):  # criando um método que se refere a ele mesmo que passa como parâmetro o indentificador deste método
        sql1 = "INSERT INTO cliente (nome_cliente,cpf) VALUES (%s,%s)"  # criando uma variável que recebe comandos sql e que possui espaços a serem preenchidos
        val = (tei.nome_cliente,tei.cpf)  # temos outra variável que recebe como parâmetro o seu indentificador com as variáriaveis da classe cliente. Está concatenando a classe com o método e é uma tupla
        self.cursor.execute(sql1,val) #chamando a variável cursor dentro do método acompanhada do método execute (executar) e sendo passado como parâmetro as duas variáveis a serem executadas
        self.conexao.commit()  # chamando a variável conexão neste método e sendo acompanhada pelo commit (salvar)
        print("cliente adicionado.")

    def adiconar_produto(self,produtos): 
        sql = "INSERT INTO produtos (nome_produto,preco) VALUES (%s,%s)"  #chamando a variável cursor dentro do método acompanhada do método execute (executar) a string que no caso é um comando sql
        valores = (produtos.nome_produto, produtos.preco) # temos outra variável que recebe como parâmetro o seu indentificador com as variáriaveis da classe produtos. Está concatenando a classe com o método e é uma tupla
        self.cursor.execute (sql,valores)  #chamando a variável cursor dentro do método acompanhada do método execute (executar) e sendo passado como parâmetro as duas variáveis a serem executadas
        self.conexao.commit() # chamando a variável conexão neste método e sendo acompanhada pelo commit (salvar)
        print('produto adicionado com sucesso no seu estoque')
    
    def listar_cliente(self): # criando um método que se refere a ele mesmo
        self.cursor.execute("SELECT id,nome_cliente,cpf FROM cliente ")  #chamando a variável cursor dentro do método acompanhada do método execute (executar) e sendo passado como parâmetro que é um comando sql em forma de string
        clientes = self.cursor.fetchall()  # criando a vriável clientes que recebe o cursor dentro do método acompanhada pelo método fetchall (fazer a busca)
        for cliente in clientes:  # para cliente em clientes. Vai ficar percorrendo minha tabela registro por registro
           print(f"id:{cliente[0]}, nome do client:{cliente[1]}, CPF: {cliente[2]}")  # imprimir na tela o a coluna de indice 0,1,2 (primaeira coluna,segunda e terceira)
 
    def listar_produto(self): # criando um método que se refere a ele mesmo
        self.cursor.execute("SELECT  id,nome_produto,preco FROM produtos") #chamando a variável cursor dentro do método acompanhada do método execute (executar) e sendo passado como parâmetro que é um comando sql em forma de string
        produtos = self.cursor.fetchall()  # criando a vriável produtos que recebe o cursor dentro do método acompanhada pelo método fetchall (fazer a busca)
        for produto in produtos :  # para produto em produtod. Vai ficar percorrendo minha tabela registro por registro
            print(f"id:  {produto[0]}, nome:{produto[1]}, preço:{produto[2]} ") # imprimir na tela o a coluna de indice 0,1,2 (primaeira coluna,segunda e terceira)

    def fechar_conexao(self): # criando um método que se refere a ele mesmo
        self.cursor.close() #chamando a variável cursor acompanhada do método close (fechar)
        self.conexao.close ()  # chamando a variável conexao acompanhada do método close (fechar)


sistema = SistemaDeProduto () #instância da classe.É como se armazenasse todos os métodos criados para serem concatenados com a execussão mais a frente

add_cliente = input ("qual é seu nome:") # criando uma variável que e que está rebebendo a informação do usuário
cpf_c= input ("qual é seu cpf:") # criando uma variável que e que está rebebendo a informação do usuário
recebe = Cliente (add_cliente,cpf_c) # criando outra variável em forma de tupla que está se referindo  a classe cliente e que vai guardar as informações contidas nas variáveis que estão em parâmetro em ordem
sistema.adicionar_cliente(recebe) # adicicionando (executando) as informações contidas na variável registro, ou seja, adicionando as info que estão na variável e em ordem


produto1 = input("digite nome do produto:") # criando uma variável que e que está rebebendo a informação do usuário
preco_p = input ("Preço:") # criando uma variável que e que está rebebendo a informação do usuário
variavel = Produtos (produto1,preco_p) # criando outra variável em forma de tupla que está se referindo  a classe Produtos e que vai guardar as informações contidas nas variáveis que estão em parâmetro em ordem
sistema.adiconar_produto(variavel) # adicicionando (executando) as informações contidas na variável VARIÁVEL, ou seja, adicionando as info que estão na variável e em ordem


print("lista de cliente:")
sistema.listar_cliente()  # adicicionando (executando)

print('lista de produtos no estoque:')
sistema.listar_produto()   # listando (executando)


sistema.fechar_conexao() #fechando a conexeção executando