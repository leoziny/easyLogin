# Sistema de Cadastro e Login de Usuários

Este é um sistema simples de cadastro e login de usuários, desenvolvido em Python, utilizando MySQL como banco de dados. O sistema permite criar uma conta de usuário, fazer login e visualizar os usuários cadastrados.

## Funcionalidades

- **Cadastro de usuários**: Permite que o usuário insira nome, idade e e-mail para criar uma conta.
- **Login**: Valida as credenciais (nome e e-mail) para permitir o acesso ao sistema.
- **Visualizar usuários cadastrados**: Exibe todos os usuários que foram registrados no banco de dados.

## Requisitos

- Python 3.x
- MySQL
- Biblioteca `MySQLdb` para interação com o banco de dados

## Instalação

1. **Instalar o Python 3.x** (caso ainda não tenha instalado):
   - [Baixe o Python](https://www.python.org/downloads/)

2. **Instalar o MySQL**:
   - [Baixe o MySQL](https://dev.mysql.com/downloads/)

3. **Instalar a biblioteca `MySQLdb`**:
   Para instalar a biblioteca necessária para interagir com o MySQL, execute o seguinte comando:

   ```bash
   pip install mysqlclient
   ```
  ## Banco de Dados
Crie um banco de dados chamado usuarios no MySQL e crie a tabela usuario com a seguinte estrutura:

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    email VARCHAR(100),
    admin BOOLEAN default false
);

(caso queira um usuario administrador, altere diretamente no banco de dados e coloque True)

## Estrutura do Código
### Função criar_usuario()
Esta função permite criar um novo usuário no sistema. Ela solicita as informações de nome, idade e e-mail, valida os dados e os insere na tabela usuario do banco de dados.

### Função mostrarUsuarios()
Esta função exibe todos os usuários registrados no banco de dados, mostrando nome, idade e e-mail.
### Função login()
A função login() permite que o usuário entre no sistema fornecendo um e-mail e nome (que é usado como senha). A validação é feita consultando os dados no banco de dados.
## Como Executar
Configure o banco de dados: Crie a tabela usuario no seu banco de dados MySQL com o script fornecido.
### Execute o código:
Após configurar o banco de dados e a biblioteca MySQLdb, basta rodar o código Python para interagir com o sistema de cadastro e login.




