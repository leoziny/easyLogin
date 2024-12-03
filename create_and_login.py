import random
import time

import MySQLdb

def conectar_banco():
    return MySQLdb.connect(host="localhost", user="seu_usuario", passwd="sua_senha", db="usuarios")

def criar_usuario():
    try:
        # Conectar ao banco de dados
        conexao = conectar_banco()
        cursor = conexao.cursor()

        while True:
            nome = input("Digite seu nome: ").strip()
            if not nome:
                print("O nome não pode ser vazio. Tente novamente.")
                continue

            try:
                idade = int(input("Digite sua idade: "))
                if idade <= 0:
                    print("A idade deve ser um número positivo. Tente novamente.")
                    continue
            except ValueError:
                print("Digite uma idade válida.")
                continue

            email = input("Digite seu email: ").strip()
            if "@" not in email or "." not in email:
                print("Digite um email válido. Tente novamente.")
                continue

            # Dados válidos; sair do loop
            break

        # Inserir os dados na tabela
        comando_insert = "INSERT INTO usuario (nome, idade, email) VALUES (%s, %s, %s)"
        valores = (nome, idade, email)
        cursor.execute(comando_insert, valores)
        conexao.commit()
        cursor.close()
        conexao.close()

        print("Conta criada com sucesso!")

    except MySQLdb.Error as erro:
        print(f"Erro ao inserir os dados no banco: {erro}")
def admin():
    while True:
        print("\n===== Bem-vindo ao Sistema ADM =====")
        print("1. Mostrar Usuarios")
        print("2. Apagar um usuario")
        print ("3. Criar Usuario")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrarUsuarios()
        elif opcao == "2":
            exclusao_usuario()
        elif opcao == "3":
            criar_usuario()
        elif opcao == "0":
            print("\nEncerrando o programa. Até logo!")
            break
        else:
            print("\nOpção inválida. Escolha novamente.")


def usuario_comum():
    while True:
        try:
            print("[1] Fazer somas de numeros")
            print("[2] jogar advinhação de numero")
            print("[0] Sair")
            escolha = int(input("Digite sua escolha: "))

            if escolha == 1:
                n1 = int(input("Digite um numero: "))
                n2 = int(input("Digite o outro numero: "))
                print(f"A soma é {n1 + n2}")
            elif escolha == 2:
                numero = random.randint(1, 100)
                print("Advinhe numero de 1 a 100")
                while True:
                    num = int(input("Digite o numero: "))
                    if num > numero:
                        print("Um pouco menossss")
                    elif num < numero:
                        print("Um pouco maisssss")
                    elif num == numero:
                        print(f"Advinhou, o numero era {numero}")
                        break
                    else:
                        print("Digite um numero valido")
            elif escolha == 0:
                print("Saindoooo....")
                break
        except ValueError:
            print("Digite um numero.")

def mostrarUsuarios():
    conexao = conectar_banco()

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuario")
    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"Nome: {linha[0]}, Idade: {linha[1]}, Email: {linha[2]}")
        time.sleep(.4)
    print(f"Tem {len(resultados)} pessoas cadastradas")


def exclusao_usuario():
    conexao = MySQLdb.connect(host="localhost", user="leogo", passwd="luaneleo", db="usuarios")
    cursor = conexao.cursor()

    # Mostrar usuários disponíveis antes da exclusão
    mostrarUsuarios()
    while True:

        try:
            emailTemporario = input("Digite o email da conta que deseja excluir: ").strip()

            # Verificar se o usuário existe
            comando = "SELECT * FROM usuario WHERE email = %s"
            cursor.execute(comando, (emailTemporario,))
            resultado = cursor.fetchone()

            if resultado:
                print("[1] Excluir")
                print("[2] Desistir")
                escolha = int(input("Digite sua escolha: "))
                if escolha == 1:
                    comando_delete = "DELETE FROM usuario WHERE email = %s"
                    cursor.execute(comando_delete, (emailTemporario,))
                    conexao.commit()
                    print("Usuário excluído com sucesso.")
                    break
                elif escolha == 2:
                    print("Exclusão cancelada.")
                    cursor.close()
                    conexao.close()
                    break
                else:
                    print("Digite um numero válido")
            else:
                print("Usuário não encontrado.")
                break

        except MySQLdb.Error as erro:
            print(f"Erro ao excluir usuário: {erro}")
            break


def login():
    while True:
        try:
            # Conectar ao banco de dados
            conexao = conectar_banco()
            cursor = conexao.cursor()

            # Solicitar credenciais
            email = input("Digite seu email: ").strip()
            nome = input("Digite sua senha (nome): ").strip()

            # Query para validar login e obter status de admin
            comando = "SELECT nome, admin FROM usuario WHERE email = %s AND nome = %s"
            cursor.execute(comando, (email, nome))
            resultado = cursor.fetchone()

            if resultado:
                nome_usuario, is_admin = resultado  # Resultado retorna (nome, admin)
                print("\nLogin realizado com sucesso!")
                print(f"Bem-vindo, {nome_usuario}!")

                # Verifica se o usuário é admin
                if is_admin:
                    print("Você está logado como administrador.")
                    cursor.close()
                    conexao.close()
                    admin()
                    break
                else:
                    print("Você está logado como usuário comum.")
                    cursor.close()
                    conexao.close()
                    usuario_comum()
                    break

            else:
                print("\nEmail ou senha incorretos. Tente novamente.")

        except MySQLdb.Error as erro:
            print(f"\nErro ao acessar os dados: {erro}")

# Chamar a função de login
login()


