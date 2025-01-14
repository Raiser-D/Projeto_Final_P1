from db_conexao import conectar_banco
import mysql.connector

def main():
    """Função principal do sistema."""
    conexao = conectar_banco()
    if conexao:
        try:
            cursor = conexao.cursor()

            # Exemplo de comando SQL
            cursor.execute("SELECT * FROM tabela_exemplo;")  # Substitua pelo nome da sua tabela
            resultados = cursor.fetchall()
            print("Resultados da consulta:")
            for linha in resultados:
                print(linha)

            # TESTE DE INSERÇÃO DE DADOS
            cursor.execute(f"INSERT INTO carrinhos (cliente_id, valor_total) VALUES (1, 0.00);")
            conexao.commit()

        except mysql.connector.Error as err:
            print(f"Erro ao executar comando no banco: {err}")
        finally:
            # Fechar cursor e conexão
            cursor.close()
            conexao.close()

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
    @cpf.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha

    def get_cpf(self):
        return self.__cpf # ???

    def __str__(self):
        return f'''
Nome de Usuário: {self.nome}
Data de Nascimento: {self.dt_nasc}
Telefone: {self.telefone}
E-mail: {self.email}
'''
# PRECISA COLOCAR CPF E SENHA?


class Cadastro:
    def __init__(self):
        self.nome = ""
        self.dt_nasc = ""
        self.telefone = ""
        self.email = ""
        self.__senha = ""
        self.__cpf = ""

    def fazer_cadastro(self):
        try:
            # Solicita os dados do cliente
            self.nome = input("Digite seu nome: ")
            self.dt_nasc = input("Digite sua data de nascimento (DD-MM-AAAA): ")
            self.telefone = input("Digite seu telefone: ")
            self.email = input("Digite seu email: ")
            self.__senha = input("Digite sua senha: ")
            self.__cpf = input("Digite seu CPF: ")

            if not self.nome or not self.dt_nasc or not self.email or not self.__cpf or not self.__senha:
                print("Todos os campos são obrigatórios.")
                raise ValueError("Todos os campos são obrigatórios.")

            if len(self.__cpf) != 11 or not self.__cpf.isdigit():
                print("O CPF deve conter exatamente 11 dígitos numéricos.")
            if len(self.__cpf) != 11 or not self.__cpf.isdigit():           #raise ValueError, serve para salvar a informação do erro que será posteriormente exibid
                raise ValueError("O CPF deve ter exatos 11 dígitos numéricos.")

            print("Cadastro realizado com sucesso!")
            self.cliente = Cliente(self.nome, self.dt_nasc, self.telefone, self.email, self.__senha, self.__cpf, "001", "Endereço Padrão")
        except ValueError as e:
            print(f"Erro ao realizar cadastro: {e}")


class Cliente(Pessoa):
    def __init__(self, nome, dt_nasc, telefone, email, senha, cpf, id, endereco):
        super().__init__(nome, dt_nasc, telefone, email, senha, cpf)
        self.__id = id
        self._endereco = endereco

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id


    def fazer_login(self):
        pass

    def editar_dados(self):
        pass

    def get_id(self):
        return self.__id    # ???

    def __str__(self):
        return f'''
            {super().__str__()}
            Endereço: {self._endereco}'''
            # PRECISA COLOCAR ID?

class Produto:
    def __init__(self, id, categoria, descricao, valor, qtd_estoque):
        self.__id = id
        self.categoria = categoria
        self.descricao = descricao
        self.valor = valor
        self.qtd_estoque = qtd_estoque

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    def diminuir_estoque(self, qtd):
        self.cursor.execute(f'SELECT qtd_estoque FROM Produtos WHERE id = {self.__id}')
        result = self.cursor.fetchone() # Apenas um registro, uma linha por vez/chamada
        if result and result[0] >= qtd:
            nova_qtd = result[0] - qtd
            self.cursor.execute(f'UPDATE produtos SET qtd_estoque = {nova_qtd} WHERE id = {self.__id}')
            # Salva o valor do qtd_estoque com a nova_qtd e pega o próprio ID do produto
            self.conexao.commit()
            self.qtd_estoque = nova_qtd # Atualiza o valor do atributo
            print(f"Estoque atualizado. Nova quantidade: {nova_qtd}")
        else:
            raise ValueError("Quantidade em estoque insuficiente")

    def get_id(self):
        return self.__id    # ???

    def __str__(self):
        return f'''
        Descrição: {self.descricao} 
        Preço: R${self.valor:.2f}'''
    

class Entrega:
    def __init__(self, id, carrinho, entregador, dt_entrega, status):
        self.__id = id
        self._carrinho = carrinho
        self.entregador = entregador
        self.dt_entrega = dt_entrega
        self.status = status

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    def calcular_prazo_entrega(self):
        # Tratar erro para caso insira um estado diferente de SC, não faz entrega
        '''A pessoa insere a cidade, comparamos com o banco, 
        aí o cara coloca Indaial. Vemos a distância entre eles e 
        calculamos o tempo usando uma velocidade média de sla 40 km/h'''
        # Pegar distância do Banco de Dados?
        pass

    def pegar_dados_carrinho(self):
        return self._carrinho.produtos
        # COMPOSIÇÃO
        '''
        self._carrinho = Carrinho_compras(cliente, valor_final)
        PRECISA ADICIONAR OS ATRIBUTOS COMO PARAMENTROS
        '''

    def atualizar_status(self):
        self.status = novo_status

    def imprimir_dados(self):
        print(f"ID: {self.__id}")
        print(f"Entregador: {self.entregador}")
        print(f"Data de Entrega: {self.dt_entrega}")
        print(f"Status: {self.status}")
        print("Produtos no Carrinho:")
        for produto in self._carrinho.produtos:
            print(f"- {produto.nome} (ID: {produto.id}, Preço: {produto.preco})")

    def get_id(self):
        return self.__id   # ???


class Carrinho_compras:
    def __init__(self, cliente, valor_final, produtos):
        self._cliente = cliente
        self.produtos = produtos
        self.valor_final = valor_final

    def inserirProduto(self, produto): # AGREGAÇÃO
        self.cursor.execute(f"INSERT INTO produtos (categoria, descricao, valor, qtd_estoque) VALUES ('Tecnologia', 'Mouse', 30.00, 15);")
        self.cursor.execute(f"INSERT INTO produtos (categoria, descricao, valor, qtd_estoque) VALUES ('Tecnologia', 'Teclado Redragon', 120.00, 10);")
        self.conexao.commit()

    def listarProduto(self):
        self.cursor.execute("SELECT descricao, valor FROM produtos WHERE carrinho_id = ?;")

    def retirar_produto(self, produto):
        try:
            self.cursor.execute(f"DELETE FROM carrinho_produtos WHERE produto_id = {produto.id} AND carrinho_id = ?);")
            '? - Função para pegar o ID do carrinho'
            # VERIFICAR SE ESTÁ DELETANDO DO LUGAR CERTO
            self.conexao.commit()
            produto_removido = self.cursor.rowcount > 0

            if produto_removido:
                print(f"Produto {produto.descricao} removido com sucesso.")
            else:
                print(f"Produto {produto.descricao} não encontrado no carrinho.")
        except Exception as e:
            print(f"Erro ao remover produto: {e}")
            

    def calcularTotal(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total
    
    def pegar_dados_cliente(self): # AGREGAÇÃO
        pass

    def finalizar_compra(self):
        for produto in self.produtos:
            produto.diminuir_estoque(1)  # Exemplo de 1 item sendo reduzido do estoque
        self.produtos.clear()  # Limpa o carrinho após finalizar a compra
    

class Entregador(Pessoa):
    def __init__(self, nome, dt_nasc, telefone, email, senha, cpf):
        super().__init__(nome, dt_nasc, telefone, email, senha, cpf)

    def atribuir_entrega(self, entrega):
        self.cursor.execute(f"INSERT INTO Entrega (descricao, carrinho_id, entregador_id, dt_entrega, status) VALUES ({entrega.descricao}, {entrega._carrinho}, {self.id}, {entrega.data_entrega}, {entrega.status})")
        self.conexao.commit()
        print(f"Entrega {entrega.descricao} atribuída ao entregador {self.nome}.")

cadastro = Cadastro()
cadastro.fazer_cadastro()


def main():
    print("Bem-vindo ao sistema de cadastro da loja virtual!")
    
    # Solicita informações básicas para instanciar o cliente
    # cliente = Cliente(None, None, None, None, None, None, "001", "Endereço Padrão")
    
    # Chama o método para realizar o cadastro
    
    # Exibe os dados cadastrados
    print("\nCadastro finalizado! Dados do cliente:")
    print(cadastro.cliente)

# Inicia o programa
if __name__ == "__main__":
    main()
'''
c1 = Cliente("João", "10-04-2003", "912563470", "jojo.p@gmail.com", "11254", "12345678901", "001", "Blumenau, SC")
carrinho = Carrinho_compras()

# solicitação de produtos
descricao = "."
while descricao != "":
    descricao = input("Insira a descrição do produto (Aperte 'enter' para parar a inserção): ")
    if descricao:
        valor = float(input("Insira o preço do produto: ")) 
        obj_produto = Produto(descricao, valor)
        carrinho.inserirProduto(obj_produto)

print(f"Cliente: {c1}")
carrinho.listarProduto()
print(f"\nValor total da compra: {carrinho.calcularTotal()}")

# ID do produto para remover
produto_id = 1
'''
novo_status = "Entregue"


