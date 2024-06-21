import mysql.connector  # importando a biblioteca

class Matricula: # criando uma classe 

    def __init__(self,nome,cpf): #definindo um método de inicialização e pode tá acessando os parâmentros, os paramêtros é como se fosse as colunas da tabela matricula
        self.nome = nome #criando uma variável dentro do propria classe que recebe os parâmetros (as colunas)
        self.cpf = cpf #criando uma variável dentro do propria classe que recebe os parâmetros (as colunas)

class SistemaDeMatricula: # criando uma classe

    def __init__(self): # criando um método de inicialização e está se referindo a ele mesmo
        self.conexao = mysql.connector.connect( # crindo uma variável dentro do proprio método e classe chamada de conexão que recebe a biblioteca e está sendo acompanhada pelo método connect e está passando parâmetros. E é uma tupla
            host ="localhost", # esse parâmetro são atributos(requisitos) para realiza a conexão corretamente com o banco de dados
            user = "root", # esse parâmetro são atributos(requisitos) para realiza a conexão corretamente com o banco de dados
            password = "he182555@", # esse parâmetro são atributos(requisitos) para realiza a conexão corretamente com o banco de dados
            database = "escola" # esse parâmetro são atributos(requisitos) para realiza a conexão corretamente com o banco de dados

        )
        self.cursor = self.conexao.cursor()  # criando outra variável dentro da propria classe e método que está recebendo a variável do proprio método e classe e está sendo acompanhada do método cursor, cursor é  que  se faz o acesso com mysql

    def adicionar_matricula(self, matricula):  # criando um método que se refere a ele mesmo que passa como parâmetro o indentificador deste método
        sql = "INSERT INTO matricula (nome,cpf) VALUES (%s,%s)" # criando uma variável que recebe comandos sql e que possui espaços a serem preenchidos
        valores = (matricula.nome, matricula.cpf) # temos outra variável que recebe como parâmetro o seu indentificador com as variáriaveis da classe matricula. Está concatenando a classe com o método e é uma tupla
        self.cursor.execute(sql,valores) #chamando a variável cursor dentro do método acompanhada do método execute (executar) e sendo passado como parâmetro as duas variáveis a serem executadas
        self.conexao.commit() # chamando a variável conexão neste método e sendo acompanhada pelo commit (salvar)
        print("Aluno adicionado com sucesso.")  

    def listar_matricula(self):  # criando um método que se refere a ele mesmo
        self.cursor.execute("SELECT nome,cpf FROM matricula") #chamando a variável cursor dentro do método acompanhada do método execute (executar) a string que no caso é um comando sql
        matriculas = self.cursor.fetchall() # criando a vriável matricula que recebe o cursor dentro do método acompanhada pelo método fetchall (fazer a busca)
        for matricula in matriculas: # para matricula em matriculas. Vai ficar percorrendo minha tabela registro por registro
            print(f"nome: {matricula[0]}  cpf: {matricula[1]}") # imprimir na tela o a coluna de indice 0 (primaeira coluna) e a segunda coluna

    def fechar_conexao(self):  # criando um método que se refere a ele mesmo
        self.cursor.close()  #chamando a variável cursor acompanhada do método close (fechar)
        self.conexao.close() # chamando a variável conexao acompanhada do método close (fechar)


sistema = SistemaDeMatricula () #instância da classe.É como se armazenasse todos os métodos criados para serem concatenados com a execussão mais a frente


matricula1 = input ("digite seu nome completo:")  # criando uma variável que e que está rebebendo a informação do usuário
matricula2 = input ("digite seu CPF:") # criando uma variável que vai receber do usuário o número de CPF
registrado = Matricula (matricula1,matricula2) # criando outra variável em forma de tupla que está se referindo  a classe matricula e que vai guardar as informações contidas nas variáveis que estão em parâmetro em ordem
sistema.adicionar_matricula(registrado)  # adicicionando (executando) as informações contidas na variável registro, ou seja, adicionando as info que estão na variável e em ordem


print('lista de alunos maticulados:') #imprimindo na tela a string
sistema.listar_matricula() # executando o método criado

sistema.fechar_conexao() #executando o método criado



