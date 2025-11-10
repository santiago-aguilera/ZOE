CREATE TABLE Usuario (
    ID_Usuario INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50),
    Email VARCHAR(100) NOT NULL,
    Contraseña VARCHAR(100),
    Rol VARCHAR(100)
    
);