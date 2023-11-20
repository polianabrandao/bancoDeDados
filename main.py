from biblioteca_python import *

while True:
    menu = input("[1] Alunos \n"
                 "[2] Modalidades \n"
                 "[3] Funcionários \n"
                 "[4] Personal \n"
                 "[S] Sair \n"
                 "Digite uma opção: ")
    while menu not in "1234sS":
        menu = input("[1] Alunos \n"
                     "[2] Modalidades \n"
                     "[3] Funcionários \n"
                     "[4] Personal \n"
                     "Digite uma opção válida:")
    while menu == "1":
        opcao = input("[1] Inserir \n"
                      "[2] Deletar \n"
                      "[3] Mostrar \n"
                      "[4] Sair \n"
                      "Digite uma opção: ")
        if opcao == "1":
            nome = input("Digite um nome: ")
            cpf = input("Digite um cpf: ")
            telefone = input("Digite um telefone: ")
            email = input("Digite um email: ")
            endereco = input("Digite um endereço: ")
            inserirAluno(nome, cpf, telefone, email, endereco)
            print("Aluno inserido com sucesso.")
        elif opcao == "2":
            matricula = int(input("Digite o número da matrícula: "))
            deletarAluno(matricula)
            print("Aluno deletado com sucesso.")
        elif opcao == "3":
            mostrarAluno()
        else:
            break

    while menu == "2":
        opcao = input("[1] Inserir \n"
                      "[2] Deletar \n"
                      "[3] Mostrar \n"
                      "[4] Sair \n"
                      "Digite uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome da modalidade:")
            inserirModalidades(nome)
            print("Modalidade inserida com sucesso.")
        elif opcao == "2":
            id_mod = int(input("Digite o ID da modalidade: "))
            deletarModalidade(id_mod)
            print("Modalidade excluída com sucesso.")
        elif opcao == "3":
            mostrarModalidades()
        else:
            break

    while menu == "3":
        opcao = input("[1] Inserir \n"
                      "[2] Deletar \n"
                      "[3] Mostrar \n"
                      "[4] Sair \n"
                      "Digite uma opção: ")
        if opcao == "1":
            nome = input("Digite um nome: ")
            cpf = input("Digite o CPF: ")
            departamento = input("Digite o número do departamento: ")
            salario = float(input("Digite o salário: "))
            filhos = int(input("Digite a quantidade de filhos: "))
            inserirFuncinarios(nome, cpf,departamento, salario, filhos)
            print("Funcionário inserido com sucesso.")
        elif opcao == "2":
            id_funcionario = int(input("Digite o ID do funcionário: "))
            deletarFuncionario(id_funcionario)
            print("Funcionário excluído com sucesso.")
        elif opcao == "3":
            inserirFuncinarios()
        else:
            break

    while menu == "4":
        opcao = input("[1] Inserir \n"
                      "[2] Deletar \n"
                      "[3] Mostrar \n"
                      "[4] Sair \n"
                      "Digite uma opção: ")
        if opcao == "1":
            cpf = input("Digite o CPF: ")
            cref = input("Digite o CREF: ")
            nome = input("Digite o nome do funcionário: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o e-mail: ")
            inserirPersonal(cpf, cref, nome, telefone, email)
            print("Personal inserido com sucesso.")
        elif opcao == "2":
            cref = int(input("Digite o CREF do personal: "))
            deletarPersonal(cref)
            print("Personal excluído com sucesso.")
        elif opcao == "3":
            mostrarPersonal()
        else:
            break
