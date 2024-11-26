import MySQLdb

def criar_usuario():
    try:
        # Conectar ao banco de dados
        conexao = MySQLdb.connect(host="localhost", user="seu_usuario", passwd="sua_senha", db="usuarios")
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

# Chamar a função para criar o usuário
criar_usuario()

def mostrarUsuarios():
    conexao = MySQLdb.connect(host="localhost", user="seu_usuario", passwd="sua_senha", db="usuarios")

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuario")
    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"Nome: {linha[0]}, Idade: {linha[1]}, Email: {linha[2]}")
def login():
    while True:
        print("\n===== Bem-vindo ao Sistema =====")
        print("1. Fazer Login")
        print("2. Sair")
        print("3 Mostrar Usuarios")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                # Conectar ao banco de dados
                conexao = MySQLdb.connect(host="localhost", user="seu_usuario", passwd="sua_senha", db="usuarios")

                cursor = conexao.cursor()

                # Solicitar credenciais
                email = input("Digite seu email: ").strip()
                nome = input("Digite sua senha (nome): ").strip()

                # Query para validar login
                comando = "SELECT * FROM usuario WHERE email = %s AND nome = %s"
                cursor.execute(comando, (email, nome))
                resultado = cursor.fetchone()

                if resultado:
                    print("\nLogin realizado com sucesso!")
                    print(f"Bem-vindo, {resultado[0]}!")  # Mostra o nome do usuário
                    break  # Sai do loop após login bem-sucedido
                    cursor.close()
                    conexao.close()
                else:
                    print("\nEmail ou senha incorretos. Tente novamente.")


            except MySQLdb.Error as erro:
                print(f"\nErro ao acessar os dados: {erro}")

        elif opcao == "2":
            print("\nEncerrando o programa. Até logo!")
            break  # Sai do loop se o usuário escolher sair
        elif opcao == "3":
            mostrarUsuarios()
        else:
            print("\nOpção inválida. Escolha novamente.")

# Chamar a função de login
login()


