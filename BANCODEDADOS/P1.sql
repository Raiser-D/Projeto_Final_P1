create  database P1;
use P1 ;

CREATE TABLE pessoas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    dt_nasc DATE NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    tipo ENUM('Cliente', 'Entregador') NOT NULL
);
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    endereco VARCHAR(255) NOT NULL,
    FOREIGN KEY (id) REFERENCES pessoas(id) ON DELETE CASCADE
);
CREATE TABLE entregadores (
    id INT PRIMARY KEY,
    veiculo VARCHAR(50), -- modelo do carrinho
    FOREIGN KEY (id) REFERENCES pessoas(id) ON DELETE CASCADE
);
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    categoria VARCHAR(50) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    qtd_estoque INT NOT NULL
);
CREATE TABLE carrinhos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    valor_total DECIMAL(10, 2) DEFAULT 0.00,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
);
CREATE TABLE carrinho_produtos (
    carrinho_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL,
    PRIMARY KEY (carrinho_id, produto_id),
    FOREIGN KEY (carrinho_id) REFERENCES carrinhos(id) ON DELETE CASCADE,
    FOREIGN KEY (produto_id) REFERENCES produtos(id) ON DELETE CASCADE
);
CREATE TABLE entregas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    carrinho_id INT NOT NULL,
    entregador_id INT NOT NULL,
    dt_entrega DATE NOT NULL,
    status VARCHAR(50) DEFAULT 'Pendente',
    FOREIGN KEY (carrinho_id) REFERENCES carrinhos(id) ON DELETE CASCADE,
    FOREIGN KEY (entregador_id) REFERENCES entregadores(id) ON DELETE CASCADE
);
