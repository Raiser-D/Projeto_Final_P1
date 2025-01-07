'''Diagrama de classes de um sistema para o gerenciamento de uma loja virtual (E-Commerce), 
em que a pessoa poderá se cadastrar no site da loja, virando um cliente. 
Também terá a possibilidade de comprar quantos produtos quiser, que serão adicionados ao carrinho de compras, 
o qual cada cliente terá um único seu. Após a compra ser efetuada, 
o entregador utilizará as informações do cadastro do cliente e do carrinho de compras para sair para entrega.'''
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

class Cliente(Pessoa):
    def __init__(self, nome, dt_nasc, telefone, email, senha, cpf, id, endereco):
        super().__init__(nome, dt_nasc, telefone, email, senha, cpf)
        self.__id = id
        self.endereco = endereco

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    def fazer_cadastro(self):
        pass

    def fazer_login(self):
        pass

    def editar_dados(self):
        pass

    def get_id(self):
        return self.__id    # ???

    def __str__(self):
        return f'''
            {super().__str__()}
            Endereço: {self.endereco_ent}'''
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
        if self.qtd_estoque >= qtd:
            self.qtd_estoque -= qtd # Se tiver produto em estoque, será retirado a qtd comprada pelo cliente
        else:
            raise ValueError("Quantidade em estoque insuficiente")

    def get_id(self):
        return self.__id    # ???

    def __str__(self):
        return f'''
        Descrição: {self.descricao} 
        Preço: R${self.valor:.2f}'''

    
class Carrinho_compras:
    def __init__(self, cliente, valor_final):
        self._cliente = cliente
        self.produtos = []
        self.valor_final = valor_final

    def inserirProduto(self, produto): # AGREGAÇÃO
        self.produtos.append(produto)

    def listarProduto(self):
        for produto in self.produtos:
            print(produto)

    def retirar_produto(self, produto):
        for produto in self.produtos:
            if produto.id == produto_id: # produto_id criado no fim do código
                self.produtos.remove(produto)
                break

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

class Entregador(Pessoa):
    def __init__(self, nome, dt_nasc, telefone, email, senha, cpf):
        super().__init__(nome, dt_nasc, telefone, email, senha, cpf)

    def atribuir_entrega(entrega): # FAZER COMPOSIÇÃO
        pass

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
novo_status = "Entregue"
