CREATE TABLE Livre (
    isbn int PRIMARY KEY,
    titre varchar(255),
    auteur int,
    FOREIGN KEY (auteur) REFERENCES Auteur(id)
);

CREATE TABLE Auteur (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom varchar(255),
    prenom varchar(255)
);
