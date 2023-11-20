from banco_de_dados import *
meucursor = banco.cursor()

# função para inserir:
def inserirAluno(nome, cpf, telefone, email, endereco):
    sqlAluno = "insert into alunos (nome, cpf, telefone, email, endereco) values (%s, %s, %s, %s, %s);"
    data = (nome, cpf, telefone, email, endereco)
    meucursor.execute(sqlAluno, data)
    banco.commit()

def inserirModalidades(nome):
    sqlModalidade = "insert into modalidades (nome) values (%s);"
    data = (nome)
    meucursor.execute(sqlModalidade, data)
    banco.commit()

def inserirFuncinarios(nome, cpf, departamento, salario, filhos):
    sqlFunc = "insert into func (nome, cpf, departamento, salario, filhos) values (%s, %s, %s, %s, %s);"
    data = (nome, cpf,departamento, salario, filhos)
    meucursor.execute(sqlFunc, data)
    banco.commit()

def inserirPersonal(cpf, cref, nome, telefone, email):
    sqlPersonal = "insert into personal (cpf, cref, nome, telefone, email) values (%s, %s, %s, %s, %s);"
    data = (nome, cref, nome, telefone, email)
    meucursor.execute(sqlPersonal, data)
    banco.commit()


# função para mostrar:
def mostrarAluno():
    pesquisa = "select * from alunos;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()
    for x in resultado:
        print(x)
def mostrarModalidades():
    pesquisa = "select * from modalidades;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()
    for x in resultado:
        print(x)
def MostrarFuncionarios():
    pesquisa = "select * from func;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()
    for x in resultado:
        print(x)
def mostrarPersonal():
    pesquisa = "select * from personal;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()
    for x in resultado:
        print(x)



# função para deletar:
def deletarAluno(matricula):
    sqlDeletar = f"delete from alunos where matricula = {matricula}"
    meucursor.execute(sqlDeletar)
    banco.commit()
def deletarModalidade(id_mod):
    sqlDeletar = f"delete from modalidades where id_mod = {id_mod}"
    meucursor.execute(sqlDeletar)
    banco.commit()
def deletarFuncionario(id_funcionario):
    sqlDeletar = f"delete from func where id_funcionario = {id_funcionario}"
    meucursor.execute(sqlDeletar)
    banco.commit()
def deletarPersonal(cref):
    sqlDeletar = f"delete from personal where cref = {cref}"
    meucursor.execute(sqlDeletar)
    banco.commit()
meucursor.close()
banco.close()