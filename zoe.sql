-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 20, 2025 at 08:14 PM
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
(8, 'La Especialidad o Técnico', 'Área de enfoque práctico o técnico donde el estudiante desarrolla habilidades específicas relacionadas con su formación profesional o vocacional');

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `ID_Usuario` int(11) NOT NULL,
  `Nombre` varchar(50) DEFAULT NULL,
  `Email` varchar(100) NOT NULL,
  `Contraseña` varchar(100) DEFAULT NULL,
  `Rol` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`ID_Usuario`, `Nombre`, `Email`, `Contraseña`, `Rol`) VALUES
(1, 'Michael Pereira', 'mpfran0919@gmail.com', 'Adm3541', 'Estudiante'),
(2, 'Santiago Aguilera', 'santiago.aguilera681@hotmail.com', 'Adm3542', 'Estudiamte'),
(3, 'Sofia Hernandez', 'Shernd@gmail.com', 'Adm3543', 'Estudiante'),
(4, 'Maria Fernanda', 'marifer1@gmail.com', 'Adm3544', 'Estudiante'),
(5, 'Laura Gomez', 'Lauragomez@gmail.com', 'Adm3545', 'Profesor'),
(6, 'Maria Lopez', 'lauralopez@gmail.com', 'Adm3546', 'Profesor'),
(7, 'Allan Castro', 'allanc@gmail.com', 'Adm3547', 'Profesor'),
(8, 'Maria Alejandra', 'nfl@gmail.com', 'Adm3548', 'Profesor'),
(9, 'Miguel Angel', 'macort@gmail.com', 'Adm3549', 'Profesor');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `esquema`
--
ALTER TABLE `esquema`
  ADD PRIMARY KEY (`id_esquema`);

--
-- Indexes for table `materia`
--
ALTER TABLE `materia`
  ADD PRIMARY KEY (`id_materia`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`ID_Usuario`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `esquema`
--
ALTER TABLE `esquema`
  MODIFY `id_esquema` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `materia`
--
ALTER TABLE `materia`
  MODIFY `id_materia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `ID_Usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
