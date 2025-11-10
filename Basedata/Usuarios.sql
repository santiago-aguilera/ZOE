CREATE TABLE Usuario (
    ID_Usuario INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50),
    Email VARCHAR(100) NOT NULL,
    Contraseña VARCHAR(100),
    Rol VARCHAR(100)
    
);

INSERT INTO Usuario(Nombre,Email,Contraseña,Rol)
VALUES("Michael Pereira", "mpfran0919@gmail.com", "Adm3541","Administrador");

INSERT INTO Usuario(Nombre,Email,Contraseña,Rol)
VALUES("Santiago Aguilera", "santiago.aguilera681@hotmail.com", "Adm3542","Administador");

INSERT INTO Usuario(Nombre,Email,Contraseña,Rol)
VALUES("Sofia Hernandez","Shernd@gmail.com","Adm3543","Administrador");

INSERT INTO Usuario(Nombre,Email,Contraseña,Rol)
VALUES("Maria Fernanda","marifer1@gmail.com","Adm3544","Administrador");
