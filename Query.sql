USE magazin ;

-- Crează tabela "clienti"
CREATE TABLE IF NOT EXISTS clienti (
    client_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nume VARCHAR(45) NOT NULL,
    prenume VARCHAR(45) NOT NULL,
    adresa VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS achizitii (
    achizite_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    client_id INT NOT NULL,
    produs_id INT NOT NULL,
    data_achzitie DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS produsalimentar (
    produs_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    denumire VARCHAR(60) NOT NULL,
    data_producere DATETIME NOT NULL,
    data_expirare DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS comanda (
    comanda_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    produs_id INT NOT NULL,
    producator_id INT NOT NULL,
    data_comanda DATETIME NOT NULL
);


CREATE TABLE IF NOT EXISTS producatori (
    producator_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    denumire VARCHAR(45) NOT NULL,
    tara_origine VARCHAR(60) NOT NULL,
    adresa VARCHAR(60) NOT NULL
);


ALTER TABLE achizitii
ADD FOREIGN KEY (client_id) REFERENCES clienti(client_id);

ALTER TABLE achizitii
ADD FOREIGN KEY (produs_id) REFERENCES produsalimentar(produs_id);

ALTER TABLE comanda
ADD FOREIGN KEY (produs_id) REFERENCES produsalimentar(produs_id);

ALTER TABLE comanda
ADD FOREIGN KEY (producator_id) REFERENCES producatori(producator_id);