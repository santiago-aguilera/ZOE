-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2026 at 03:48 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `zoe`
--

-- --------------------------------------------------------

--
-- Table structure for table `cronograma`
--

CREATE TABLE `cronograma` (
  `Id_Cronograma` int(11) NOT NULL,
  `Id_Materia` int(11) NOT NULL,
  `Titulo` varchar(150) NOT NULL,
  `Descripcion` text NOT NULL,
  `Fecha` date NOT NULL,
  `Hora` time NOT NULL,
  `Tipo` varchar(50) NOT NULL,
  `Lugar` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `entrega`
--

CREATE TABLE `entrega` (
  `Id_Entrega` int(11) NOT NULL,
  `Id_Trabajo` int(11) NOT NULL,
  `Id_Usuario` int(11) NOT NULL,
  `Fecha_Entrega` timestamp NOT NULL DEFAULT current_timestamp(),
  `Archivo` varchar(255) DEFAULT NULL,
  `Estado` enum('entregado','calificado') DEFAULT 'entregado',
  `Calificacion` decimal(5,2) DEFAULT NULL,
  `Comentarios` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `esquema`
--

CREATE TABLE `esquema` (
  `id_esquema` int(11) NOT NULL,
  `titulo` varchar(100) DEFAULT NULL,
  `Archivo` varchar(100) DEFAULT NULL,
  `ID_Usuario` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `estudiante_materia`
--

CREATE TABLE `estudiante_materia` (
  `Id_Estudiante_Materia` int(11) NOT NULL,
  `Id_Usuario` int(11) NOT NULL,
  `Id_Materia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `foro`
--

CREATE TABLE `foro` (
  `Id_Foro` int(11) NOT NULL,
  `Titulo` varchar(200) NOT NULL,
  `Fecha_Creacion` timestamp NOT NULL DEFAULT current_timestamp(),
  `Id_Materia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `foro_post`
--

CREATE TABLE `foro_post` (
  `Id_Post` int(11) NOT NULL,
  `Contenido` text NOT NULL,
  `Fecha` timestamp NOT NULL DEFAULT current_timestamp(),
  `Id_Usuario` int(11) NOT NULL,
  `Id_Foro` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `grupo`
--

CREATE TABLE `grupo` (
  `Id_Grupo` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `grupo`
--

INSERT INTO `grupo` (`Id_Grupo`, `Nombre`) VALUES
(1, '1004'),
(2, '1003');

-- --------------------------------------------------------

--
-- Table structure for table `materia`
--

CREATE TABLE `materia` (
  `id_materia` int(11) NOT NULL,
  `nombre_materia` varchar(50) DEFAULT NULL,
  `Descripcion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `materia`
--

INSERT INTO `materia` (`id_materia`, `nombre_materia`, `Descripcion`) VALUES
(1, 'Lengua y Literatura', 'Materia donde se ve la literatura y se busca el reconocimiento y análisis de diferentes textos'),
(2, 'Matemáticas', 'Materia que cubre temas de álgebra, geometría, cálculo, probabilidad y estadística, entre otros'),
(3, 'Inglés', 'Estudio del idioma inglés, tanto en su aspecto gramatical como literario'),
(4, 'Aprendizaje y Servicio', 'Curso enfocado en la aplicación práctica de habilidades en la comunidad, combinando el aprendizaje académico con el servicio social'),
(5, 'Proyecto de Reflexión', 'Espacio de reflexión y evaluación personal sobre el aprendizaje y el desarrollo durante el Programa del IB'),
(6, 'Habilidades Personales y Profesionales (HPP)', 'Materia que desarrolla destrezas esenciales para la vida académica y laboral, como la gestión del tiempo, el trabajo en equipo y la resolución de problemas'),
(7, 'Desarrollo de Lenguas', 'Curso que promueve el aprendizaje de lenguas extranjeras y el desarrollo de competencias comunicativas en varios idiomas'),
(8, 'La Especialidad o Técnico', 'Área de enfoque práctico o técnico donde el estudiante desarrolla habilidades específicas relacionadas con su formación profesional o vocacional'),
(9, 'Inglés', 'Materia de inglés'),
(10, 'Matemáticas', 'Materia de matemáticas'),
(11, 'Lengua y Literatura', 'Materia de lengua y literatura'),
(12, 'HPP', 'Historia, Política y Participación'),
(13, 'Proyecto de Reflexión', 'Proyecto académico de reflexión'),
(14, 'Aprendizaje y Servicio', 'Asignatura de servicio comunitario'),
(15, 'Desarrollo de Lenguas', 'Desarrollo de habilidades lingüísticas');

-- --------------------------------------------------------

--
-- Table structure for table `profesor_materia`
--

CREATE TABLE `profesor_materia` (
  `Id_Profesor_Materia` int(11) NOT NULL,
  `Id_Usuario` int(11) NOT NULL,
  `Id_Materia` int(11) NOT NULL,
  `Ano_Academico` year(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `profesor_materia`
--

INSERT INTO `profesor_materia` (`Id_Profesor_Materia`, `Id_Usuario`, `Id_Materia`, `Ano_Academico`) VALUES
(1, 18, 2, '2025'),
(7, 19, 3, '2025'),
(8, 6, 13, '2025'),
(9, 7, 12, '2025'),
(11, 20, 7, '2025'),
(12, 8, 8, '2025'),
(13, 21, 8, '2025'),
(14, 22, 1, '2025');

-- --------------------------------------------------------

--
-- Table structure for table `trabajo`
--

CREATE TABLE `trabajo` (
  `Id_Trabajo` int(11) NOT NULL,
  `Titulo` varchar(200) NOT NULL,
  `Descripcion` text DEFAULT NULL,
  `Fecha_Entrega` date NOT NULL,
  `Id_Profesor_Materia` int(11) NOT NULL,
  `Fecha_Creacion` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `trabajo`
--

INSERT INTO `trabajo` (`Id_Trabajo`, `Titulo`, `Descripcion`, `Fecha_Entrega`, `Id_Profesor_Materia`, `Fecha_Creacion`) VALUES
(4, 'Subir portafolio', 'Subir portafolio', '2026-01-15', 7, '2026-01-03 23:37:41'),
(5, 'Subir portafolio', 'Subir portafolio', '2026-01-15', 7, '2026-01-03 23:40:27');

-- --------------------------------------------------------

--
-- Table structure for table `trabajo_grupo`
--

CREATE TABLE `trabajo_grupo` (
  `Id_Trabajo` int(11) NOT NULL,
  `Id_Grupo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `trabajo_grupo`
--

INSERT INTO `trabajo_grupo` (`Id_Trabajo`, `Id_Grupo`) VALUES
(5, 2);

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `ID_Usuario` int(11) NOT NULL,
  `Nombre` varchar(50) DEFAULT NULL,
  `Email` varchar(100) NOT NULL,
  `Contraseña` varchar(100) DEFAULT NULL,
  `Rol` varchar(100) DEFAULT NULL,
  `Telefono` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`ID_Usuario`, `Nombre`, `Email`, `Contraseña`, `Rol`, `Telefono`) VALUES
(1, 'Michael Pereira', 'mpfran0919@gmail.com', 'Adm3541', 'Estudiante', 'None'),
(2, 'Santiago Aguilera', 'santiago.aguilera681@hotmail.com', 'Adm3542', 'Estudiante', NULL),
(3, 'Sofia Hernandez', 'Shernd@gmail.com', 'Adm3543', 'Estudiante', NULL),
(4, 'Maria Fernanda', 'marifer1@gmail.com', 'Adm3544', 'Estudiante', NULL),
(6, 'Maria Lopez Martinez', 'lauralopez@gmail.com', 'Adm3546', 'Profesor', 'None'),
(7, 'Allan Castro', 'allanc@gmail.com', 'Adm3547', 'Profesor', 'None'),
(8, 'Maria Alejandra', 'nfl@gmail.com', 'Adm3548', 'Profesor', 'None'),
(13, 'Nicolas Penagos', 'nic.penagos14@gmail.com', '123456', 'Profesor', 'None'),
(17, 'Carmen', 'carmen17@gmail.com', '123456', 'Profesor', '3114434459'),
(18, 'Maria Paula', 'lauralopezi@gmail.com', '123456', 'Profesor', '3114434459'),
(19, 'Valeria Aguilera', 'vale.aguilera@gmail.com', '123456', 'Profesor', ''),
(20, 'Angee Viviana ', 'angeevms@gmail.com', '123456', 'Profesor', '3134106473'),
(21, 'Wilber Aguilera', 'Wilberaab@gmail.com', '$2b$12$XXO5mkNx83SHuTbHCgMO7OXwMuyAvjaDs2zFqTt/MlOIFjjmU.nq6', 'Profesor', ''),
(22, 'Ludy Aguilera', 'ludymab@gmail.com', '$2b$12$IrgPqLETetwRip84jYZmJevANqXjt3gJ4LI9Qjfuw97B.85tdP8EO', 'Profesor', '');

-- --------------------------------------------------------

--
-- Table structure for table `usuario_grupo`
--

CREATE TABLE `usuario_grupo` (
  `Id_Usuario` int(11) NOT NULL,
  `Id_Grupo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuario_grupo`
--

INSERT INTO `usuario_grupo` (`Id_Usuario`, `Id_Grupo`) VALUES
(1, 2),
(2, 2),
(3, 1),
(4, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cronograma`
--
ALTER TABLE `cronograma`
  ADD PRIMARY KEY (`Id_Cronograma`),
  ADD KEY `Id_Materia` (`Id_Materia`);

--
-- Indexes for table `entrega`
--
ALTER TABLE `entrega`
  ADD PRIMARY KEY (`Id_Entrega`),
  ADD KEY `Id_Trabajo` (`Id_Trabajo`),
  ADD KEY `Id_Usuario` (`Id_Usuario`);

--
-- Indexes for table `esquema`
--
ALTER TABLE `esquema`
  ADD PRIMARY KEY (`id_esquema`);

--
-- Indexes for table `estudiante_materia`
--
ALTER TABLE `estudiante_materia`
  ADD PRIMARY KEY (`Id_Estudiante_Materia`),
  ADD KEY `Id_Usuario` (`Id_Usuario`),
  ADD KEY `Id_Materia` (`Id_Materia`);

--
-- Indexes for table `foro`
--
ALTER TABLE `foro`
  ADD PRIMARY KEY (`Id_Foro`),
  ADD KEY `Id_Materia` (`Id_Materia`);

--
-- Indexes for table `foro_post`
--
ALTER TABLE `foro_post`
  ADD PRIMARY KEY (`Id_Post`),
  ADD KEY `Id_Usuario` (`Id_Usuario`),
  ADD KEY `Id_Foro` (`Id_Foro`);

--
-- Indexes for table `grupo`
--
ALTER TABLE `grupo`
  ADD PRIMARY KEY (`Id_Grupo`);

--
-- Indexes for table `materia`
--
ALTER TABLE `materia`
  ADD PRIMARY KEY (`id_materia`);

--
-- Indexes for table `profesor_materia`
--
ALTER TABLE `profesor_materia`
  ADD PRIMARY KEY (`Id_Profesor_Materia`),
  ADD KEY `Id_Usuario` (`Id_Usuario`),
  ADD KEY `Id_Materia` (`Id_Materia`);

--
-- Indexes for table `trabajo`
--
ALTER TABLE `trabajo`
  ADD PRIMARY KEY (`Id_Trabajo`),
  ADD KEY `Id_Profesor_Materia` (`Id_Profesor_Materia`);

--
-- Indexes for table `trabajo_grupo`
--
ALTER TABLE `trabajo_grupo`
  ADD PRIMARY KEY (`Id_Trabajo`,`Id_Grupo`),
  ADD KEY `Id_Grupo` (`Id_Grupo`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`ID_Usuario`);

--
-- Indexes for table `usuario_grupo`
--
ALTER TABLE `usuario_grupo`
  ADD PRIMARY KEY (`Id_Usuario`,`Id_Grupo`),
  ADD UNIQUE KEY `Id_Usuario` (`Id_Usuario`,`Id_Grupo`),
  ADD KEY `Id_Grupo` (`Id_Grupo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cronograma`
--
ALTER TABLE `cronograma`
  MODIFY `Id_Cronograma` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `entrega`
--
ALTER TABLE `entrega`
  MODIFY `Id_Entrega` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `esquema`
--
ALTER TABLE `esquema`
  MODIFY `id_esquema` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `estudiante_materia`
--
ALTER TABLE `estudiante_materia`
  MODIFY `Id_Estudiante_Materia` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `foro`
--
ALTER TABLE `foro`
  MODIFY `Id_Foro` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `foro_post`
--
ALTER TABLE `foro_post`
  MODIFY `Id_Post` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `grupo`
--
ALTER TABLE `grupo`
  MODIFY `Id_Grupo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `materia`
--
ALTER TABLE `materia`
  MODIFY `id_materia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `profesor_materia`
--
ALTER TABLE `profesor_materia`
  MODIFY `Id_Profesor_Materia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `trabajo`
--
ALTER TABLE `trabajo`
  MODIFY `Id_Trabajo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `ID_Usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cronograma`
--
ALTER TABLE `cronograma`
  ADD CONSTRAINT `cronograma_ibfk_1` FOREIGN KEY (`Id_Materia`) REFERENCES `materia` (`id_materia`);

--
-- Constraints for table `entrega`
--
ALTER TABLE `entrega`
  ADD CONSTRAINT `entrega_ibfk_1` FOREIGN KEY (`Id_Trabajo`) REFERENCES `trabajo` (`Id_Trabajo`),
  ADD CONSTRAINT `entrega_ibfk_2` FOREIGN KEY (`Id_Usuario`) REFERENCES `usuario` (`ID_Usuario`);

--
-- Constraints for table `estudiante_materia`
--
ALTER TABLE `estudiante_materia`
  ADD CONSTRAINT `estudiante_materia_ibfk_1` FOREIGN KEY (`Id_Usuario`) REFERENCES `usuario` (`ID_Usuario`),
  ADD CONSTRAINT `estudiante_materia_ibfk_2` FOREIGN KEY (`Id_Materia`) REFERENCES `materia` (`id_materia`);

--
-- Constraints for table `foro`
--
ALTER TABLE `foro`
  ADD CONSTRAINT `foro_ibfk_1` FOREIGN KEY (`Id_Materia`) REFERENCES `materia` (`id_materia`);

--
-- Constraints for table `foro_post`
--
ALTER TABLE `foro_post`
  ADD CONSTRAINT `foro_post_ibfk_1` FOREIGN KEY (`Id_Usuario`) REFERENCES `usuario` (`ID_Usuario`),
  ADD CONSTRAINT `foro_post_ibfk_2` FOREIGN KEY (`Id_Foro`) REFERENCES `foro` (`Id_Foro`);

--
-- Constraints for table `profesor_materia`
--
ALTER TABLE `profesor_materia`
  ADD CONSTRAINT `profesor_materia_ibfk_1` FOREIGN KEY (`Id_Usuario`) REFERENCES `usuario` (`ID_Usuario`),
  ADD CONSTRAINT `profesor_materia_ibfk_2` FOREIGN KEY (`Id_Materia`) REFERENCES `materia` (`id_materia`);

--
-- Constraints for table `trabajo`
--
ALTER TABLE `trabajo`
  ADD CONSTRAINT `trabajo_ibfk_1` FOREIGN KEY (`Id_Profesor_Materia`) REFERENCES `profesor_materia` (`Id_Profesor_Materia`);

--
-- Constraints for table `trabajo_grupo`
--
ALTER TABLE `trabajo_grupo`
  ADD CONSTRAINT `trabajo_grupo_ibfk_1` FOREIGN KEY (`Id_Trabajo`) REFERENCES `trabajo` (`Id_Trabajo`),
  ADD CONSTRAINT `trabajo_grupo_ibfk_2` FOREIGN KEY (`Id_Grupo`) REFERENCES `grupo` (`Id_Grupo`);

--
-- Constraints for table `usuario_grupo`
--
ALTER TABLE `usuario_grupo`
  ADD CONSTRAINT `usuario_grupo_ibfk_1` FOREIGN KEY (`Id_Usuario`) REFERENCES `usuario` (`ID_Usuario`),
  ADD CONSTRAINT `usuario_grupo_ibfk_2` FOREIGN KEY (`Id_Grupo`) REFERENCES `grupo` (`Id_Grupo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
