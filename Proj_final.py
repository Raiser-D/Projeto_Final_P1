import mysql.connector
from mysql.connector import Error

nome = ""
dt_nasc = ""
telefone = ""
email = ""
senha = ""
cpf = ""

class Pessoa:
    def __init__(self, nome, dt_nasc, telefone, email, senha, cpf):
        self.nome = nome
        self.dt_nasc = dt_nasc 
        self.telefone = telefone
        self.email = email
        self.__senha = senha
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha

    def cadastrar_usuario(self,conexao):
        try:
            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO pessoas (nome, dt_nasc, telefone, email, senha, cpf, tipo)
                VALUES (%s, %s, %s, %s, %s, %s, 'Cliente');
            """, (self.nome, self.dt_nasc, self.telefone, self.email, self.__senha, self.__cpf))

            conexao.commit()
            print("Cadastro realizado com sucesso!")
        except Error as e:
            print(f"Erro ao realizar cadastro: {e}")

class Cliente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Cliente [ID: {self.id}, Nome: {self.nome}, Email: {self.email}]"

class Produto:
    def __init__(self, id, descricao, valor):
        self.id = id
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f"Produto [ID: {self.id}, Descricao: {self.descricao}, Valor: R${self.valor:.2f}]"

class Carrinho:
    def __init__(self, cliente_id):
        self.cliente_id = cliente_id
        self.produtos = []

    def adicionar_produto(self, produto, quantidade):
        self.produtos.append((produto, quantidade))

    def remover_produto(self, produto_id):
        self.produtos = [(prod, qtd) for prod, qtd in self.produtos if prod.id != produto_id]

    def calcular_total(self):
        return sum(prod.valor * qtd for prod, qtd in self.produtos)

    def __str__(self):
        detalhes = "\n".join(
            [f"{prod.descricao} - Qtd: {qtd} - Valor: R${prod.valor:.2f}" for prod, qtd in self.produtos]
        )
        return f"Carrinho do Cliente {self.cliente_id}:\n{detalhes}\nTotal: R${self.calcular_total():.2f}"

def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='P1'
        )
        if conexao.is_connected():
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def inserir_dados_teste(conexao):
    try:
        cursor = conexao.cursor()
        
        produtos = [
            ('Tecnologia', 'Mouse', 50.00, 99999),
            ('Tecnologia', 'Teclado', 150.00, 99999),
            ('Tecnologia', 'Monitor', 800.00, 99999)
        ]
        cursor.executemany("""
            INSERT INTO produtos (categoria, descricao, valor, qtd_estoque)
            VALUES (%s, %s, %s, %s);
        """, produtos)

        conexao.commit()
        print("Dados de teste inseridos com sucesso!")
    except Error as e:
        print(f"Erro ao inserir dados de teste: {e}")

def login_usuario(conexao):
    try:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id, nome FROM pessoas WHERE email = %s AND senha = %s AND tipo = 'Cliente';
        """, (email, senha))
        resultado = cursor.fetchone()

        if resultado:
            print("Login realizado com sucesso!")
            return Cliente(id=resultado[0], nome=resultado[1], email=email)
        else:
            print("Email ou senha inválidos.")
            return None
    except Error as e:
        print(f"Erro ao realizar login: {e}")
        return None

def menu_principal(conexao):
    while True:
        print("\n--- Menu Principal ---")
        print("1. Login")
        print("2. Cadastre-se")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cliente = login_usuario(conexao)
            if cliente:
                menu_carrinho(conexao, cliente)
        elif opcao == '2':
            nome = input("Digite seu nome: ")
            dt_nasc = input("Digite sua data de nascimento (AAAA-MM-DD): ")
            telefone = input("Digite seu telefone: ")
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            cpf = input("Digite seu CPF (apenas números): ")
            cliente = Pessoa(nome, dt_nasc, telefone, email, senha, cpf)
            cliente.cadastrar_usuario(conexao)
        elif opcao == '0':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_carrinho(conexao, cliente):
    carrinho = Carrinho(cliente_id=cliente.id)

    while True:
        print("\n--- Menu Carrinho ---")
        print("1. Listar produtos no carrinho")
        print("2. Adicionar produto ao carrinho")
        print("3. Remover produto do carrinho")
        print("4. Finalizar compra")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print(carrinho)
        elif opcao == '2':
            adicionar_produto(conexao, carrinho)
        elif opcao == '3':
            remover_produto(carrinho)
        elif opcao == '4':
            finalizar_compra(conexao, carrinho)
            break
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def adicionar_produto(conexao, carrinho):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, descricao, valor FROM produtos;")
        produtos = cursor.fetchall()

        if produtos:
            print("\n--- Produtos Disponíveis ---")
            for produto_id, descricao, valor in produtos:
                print(f"{produto_id}. {descricao} - R${valor:.2f}")

            produto_id = int(input("Escolha o ID do produto para adicionar ao carrinho: "))
            quantidade = int(input("Digite a quantidade: "))

            produto = next((Produto(id=pid, descricao=desc, valor=val) for pid, desc, val in produtos if pid == produto_id), None)
            if produto:
                carrinho.adicionar_produto(produto, quantidade)
                print("Produto adicionado ao carrinho com sucesso!")
            else:
                print("Produto não encontrado.")
        else:
            print("Nenhum produto disponível.")
    except Error as e:
        print(f"Erro ao adicionar produto: {e}")

def remover_produto(carrinho):
    try:
        print(carrinho)
        produto_id = int(input("Escolha o ID do produto para remover do carrinho: "))
        carrinho.remover_produto(produto_id)
        print("Produto removido do carrinho com sucesso!")
    except Exception as e:
        print(f"Erro ao remover produto: {e}")

def finalizar_compra(conexao, carrinho):
    try:
        print("\n--- Nota Fiscal ---")
        print(carrinho)

        cursor = conexao.cursor()
        for produto, quantidade in carrinho.produtos:
            cursor.execute("""
                UPDATE produtos SET qtd_estoque = qtd_estoque - %s WHERE id = %s;
            """, (quantidade, produto.id))

        conexao.commit()
        print("Compra finalizada com sucesso!")
    except Error as e:
        print(f"Erro ao finalizar compra: {e}")

def main():
    conexao = conectar_banco()
    if conexao:
        '''
        Como o nosso programa possui o intuito de ser apenas um e-comerce client-side, não há a possibilidade de adicionar novos produtos, porém incluimos uma função
        que gera novos produtos para facilitar a utilização do codigo. Pedimos que caso utilize, retire a hashtag e depois adicione novamente caso rode novamente o programa,
        para evitar dados duplicados. 
        '''
        #inserir_dados_teste(conexao)
        menu_principal(conexao)
        conexao.close()

if __name__ == "__main__":
    main()
