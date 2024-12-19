'''Diagrama de classes de um sistema para o gerenciamento de uma loja virtual (E-Commerce), 
em que a pessoa poderá se cadastrar no site da loja, virando um cliente. 
Também terá a possibilidade de comprar quantos produtos quiser, que serão adicionados ao carrinho de compras, 
o qual cada cliente terá um único seu. Após a compra ser efetuada, 
o entregador utilizará as informações do cadastro do cliente e do carrinho de compras para sair para entrega.'''

class Carrinho_compras:
    def __init__(self, cliente, valor_final):
        self._cliente = cliente
        self.produtos = []
        self.valor_final = valor_final

    def inserirProduto(self, produto):
        self.produtos.append(produto)

    def listarProduto(self):
        for produto in self.produtos:
            print(produto)

    def retirar_produto(self, produto):
        self.produtos.remove(produto) # ??????

    def calcularTotal(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total
    
    def pegar_dados_cliente(self):
        pass

    def finalizar_compra(self):
        pass

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

    def diminuir_estoque(self):
        pass

    def get_id(self):
        pass

    def __str__(self):
        return f'''
        Descrição: {self.descricao} 
        Preço: R${self.valor:.2f}'''

class Pessoa:
    def __init__(self, nome, dt_nasc, telefone, email, senha, cpf):
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def get_cpf(self):
        pass

    def __str__(self):
        return f'Nome de Usuário: {self.nome}'

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
        pass    

    def __str__(self):
        return f'''
            {super().__str__()}
            Nome do cliente: {self.nome}
            Contato: {self.contato}
            Endereço: {self.endereco_ent}'''
    
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
        pass

    def pegar_dados_carrinho(self):
        pass

    def atualizar_status(self):
        pass

    def imprimir_dados(self):
        pass

    def get_id(self):
        pass

class Entregador(Pessoa):
    def __init__(self, nome, dt_nasc, telefone, email, senha, cpf):
        super().__init__(nome, dt_nasc, telefone, email, senha, cpf)

    def atribuir_entrega(entrega):
        pass

c1 = Cliente("Pedro", "99872-1107", "Rolândia, Paraná", "Pedrinho", 12345)
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