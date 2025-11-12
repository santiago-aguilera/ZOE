CREATE TABLE Usuario (
    ID_Usuario INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50),
    Email VARCHAR(100) NOT NULL,
    Contraseña VARCHAR(100),
    Rol VARCHAR(100)
    
);

INSERT INTO Usuario(Nombre,Email,Contraseña,Rol)
VALUES("Michael Pereira", "mpfran0919@gmail.com", "Adm3541","Estudiante");

INSERT INTO Usuario(Nombre,Email,Contraseña,Rol)
VALUES("Santiago Aguilera", "santiago.aguilera681@hotmail.com", "Adm3542","Estudiamte");

INSERT INTO Usuario(Nombre,Email,Contraseña,Rol)
VALUES("Sofia Hernandez","Shernd@gmail.com","Adm3543","Estudiante");

INSERT INTO Usuario(Nombre,Email,Contraseña,Rol)
VALUES("Maria Fernanda","marifer1@gmail.com","Adm3544","Estudiante");


INSERT INTO Usuario(Nombre,Email,Contraseña,Rol)
VALUES("Carlos Gil","@gmail.com","Adm3545","Coordinador");

