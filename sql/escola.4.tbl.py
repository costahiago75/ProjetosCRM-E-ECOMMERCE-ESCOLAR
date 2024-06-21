import mysql.connector

class Aluno:
    def __init__(self, nome_aluno, cpf_aluno):
        self.nome_aluno = nome_aluno
        self.cpf_aluno = cpf_aluno

class Curso:
    def __init__(self, nome_curso, carga_horaria):
        self.nome_curso = nome_curso
        self.carga_horaria = carga_horaria

class Professor:
    def __init__(self, nome_professor):
        self.nome_professor = nome_professor

class Matricula:
    def __init__(self, nome_aluno, cpf_aluno, nome_curso, carga_horaria, nome_professor):
        self.nome_aluno = nome_aluno
        self.cpf_aluno = cpf_aluno
        self.nome_curso = nome_curso
        self.carga_horaria = carga_horaria
        self.nome_professor = nome_professor

class SistemaEscola:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="he182555@",
            database="escola_db"
        )
        self.cursor = self.conexao.cursor()

    def adicionar(self, info_aluno):
        sql1 = "INSERT INTO aluno (nome_aluno, cpf_aluno) VALUES (%s, %s)"
        val1 = (info_aluno.nome_aluno, info_aluno.cpf_aluno)
        self.cursor.execute(sql1, val1)
        self.conexao.commit()
        print(f"Aluno adicionado: {info_aluno.nome_aluno}")

    def adicionar_curso(self, curso):
        sql2 = "INSERT INTO curso (nome_curso, carga_horaria) VALUES (%s, %s)"
        valores2 = (curso.nome_curso, curso.carga_horaria)
        self.cursor.execute(sql2, valores2)
        self.conexao.commit()
        print(f"Curso adicionado: {curso.nome_curso}")

    def adicionar_professor(self, professor):
        sql3 = "INSERT INTO professor (nome_professor) VALUES (%s)"
        valores3 = (professor.nome_professor,)
        self.cursor.execute(sql3, valores3)
        self.conexao.commit()
        print(f"Professor adicionado: {professor.nome_professor}")

    def listar_matricula(self):
        sql = """ SELECT 
    m.id_matricula,
    m.id_aluno,
    a.nome_aluno,
    a.cpf_aluno,
    m.id_curso,
    c.nome_curso,
    c.carga_horaria,
    m.id_professor,
    p.nome_professor
FROM 
    matricula m
    JOIN aluno a ON m.id_aluno = a.id_aluno
    JOIN curso c ON m.id_curso = c.id_curso
    JOIN professor p ON m.id_professor = p.id_professor; """
        
        self.cursor.execute(sql)
        matriculas = self.cursor.fetchall()
        print("Lista de matrículas:")
        for matricula in matriculas:
            print(f"Id da matricula: {matricula[0]}, ID do aluno: {matricula[1]}, nome do aluno: {matricula[2]}, CPF do aluno: {matricula[3]}, ID do curso: {matricula[4]}, Nome do curso: {matricula[5]}, Carga horaria :{matricula[6]}, ID do professor: {matricula[7]}, Nome do professor: {matricula[8]} ")

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()

# Instanciando o sistema de escola
sistema = SistemaEscola()

# Exemplo de adição de aluno, curso e professor
nome_al = input('Digite seu nome: ')
cpf = input('Digite seu CPF: ')
al = Aluno(nome_al, cpf)
sistema.adicionar(al)

nome_c = input('Digite o nome do curso desejado: ')
horario = input('Digite a carga horária do curso: ')
c1 = Curso(nome_c, horario)
sistema.adicionar_curso(c1)

nome_prof = input('Digite o nome do professor desejado: ')
professor = Professor(nome_prof)
sistema.adicionar_professor(professor)

# Listar matrículas existentes
sistema.listar_matricula()

# Fechar conexão com o banco de dados
sistema.fechar_conexao()
