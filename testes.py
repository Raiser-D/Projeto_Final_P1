# EXEMPLO FUNÇÕES DE CARRINHO_COMPRAS


import sqlite3

class Carrinho_compras:
    def __init__(self, cliente, valor_final, produtos, db_path='shopping_cart.db'):
        self._cliente = cliente
        self.produtos = produtos
        self.valor_final = valor_final
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Carrinho_compras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            valor_final REAL NOT NULL
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            carrinho_id INTEGER,
            FOREIGN KEY (carrinho_id) REFERENCES Carrinho_compras(id)
        )
        ''')
        self.conn.commit()

    def inserirProduto(self, produto): # AGREGAÇÃO
        self.cursor.execute('''
        INSERT INTO Produtos (nome, preco, carrinho_id) VALUES (?, ?, ?)
        ''', (produto.nome, produto.preco, self._get_carrinho_id()))
        self.conn.commit()

    def listarProduto(self):
        self.cursor.execute('''
        SELECT nome, preco FROM Produtos WHERE carrinho_id = ?
        ''', (self._get_carrinho_id(),))
        produtos = self.cursor.fetchall()
        for produto in produtos:
            print(f"Nome: {produto[0]}, Preço: {produto[1]}")

    def retirar_produto(self, produto):
        try:
            self.cursor.execute('''
            DELETE FROM Produtos WHERE id = ? AND carrinho_id = ?
            ''', (produto.id, self._get_carrinho_id()))
            self.conn.commit()
            produto_removido = self.cursor.rowcount > 0
            if produto_removido:
                print(f"Produto {produto.nome} removido com sucesso.")
            else:
                print(f"Produto {produto.nome} não encontrado no carrinho.")
        except Exception as e:
            print(f"Erro ao remover produto: {e}")

    def _get_carrinho_id(self):
        self.cursor.execute('''
        SELECT id FROM Carrinho_compras WHERE cliente = ? AND valor_final = ?
        ''', (self._cliente, self.valor_final))
        carrinho = self.cursor.fetchone()
        if carrinho:
            return carrinho[0]
        else:
            self.cursor.execute('''
            INSERT INTO Carrinho_compras (cliente, valor_final) VALUES (?, ?)
            ''', (self._cliente, self.valor_final))
            self.conn.commit()
            return self.cursor.lastrowid

    def __del__(self):
        self.conn.close()