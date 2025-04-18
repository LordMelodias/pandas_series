-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	5.5.62

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `department` varchar(50) DEFAULT NULL,
  `salary` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'Alice Johnson',28,'HR',50000.00),(2,'Bob Smith',35,'Engineering',75000.00),(3,'Charlie Lee',30,'Marketing',60000.00),(4,'Diana Brown',40,'Finance',80000.00),(5,'Ethan Wilson',25,'Support',40000.00),(6,'Sophia Martinez',32,'Engineering',78000.00),(7,'Liam Anderson',29,'Marketing',58000.00),(8,'Olivia Taylor',45,'Finance',85000.00),(9,'Noah Thomas',27,'HR',52000.00),(10,'Emma Hernandez',33,'Support',42000.00),(11,'William Moore',38,'Engineering',82000.00),(12,'Ava Jackson',31,'Marketing',62000.00),(13,'James White',42,'Finance',88000.00),(14,'Isabella Harris',26,'HR',51000.00),(15,'Benjamin Clark',34,'Support',43000.00),(16,'Mia Lewis',36,'Engineering',79000.00),(17,'Lucas Robinson',28,'Marketing',59000.00),(18,'Charlotte Walker',39,'Finance',87000.00),(19,'Henry Allen',30,'HR',53000.00),(20,'Amelia Young',35,'Support',44000.00),(21,'Alexander King',41,'Engineering',84000.00),(22,'Harper Scott',29,'Marketing',61000.00),(23,'Michael Green',37,'Finance',89000.00),(24,'Evelyn Adams',27,'HR',54000.00),(25,'Daniel Nelson',33,'Support',45000.00),(26,'Grace Mitchell',31,'HR',55000.00),(27,'Samuel Carter',36,'Engineering',81000.00),(28,'Abigail Perez',29,'Marketing',63000.00),(29,'Jackson Roberts',43,'Finance',91000.00),(30,'Emily Turner',26,'Support',46000.00),(31,'Sebastian Phillips',34,'Engineering',83000.00),(32,'Madison Campbell',30,'Marketing',64000.00),(33,'David Parker',38,'Finance',92000.00),(34,'Scarlett Evans',28,'HR',56000.00),(35,'Joseph Edwards',35,'Support',47000.00),(36,'Victoria Collins',37,'Engineering',85000.00),(37,'Caleb Stewart',32,'Marketing',65000.00),(38,'Chloe Sanchez',40,'Finance',94000.00),(39,'Andrew Morris',27,'HR',57000.00),(40,'Zoey Rogers',33,'Support',48000.00),(41,'Ryan Reed',39,'Engineering',86000.00),(42,'Penelope Cook',31,'Marketing',66000.00),(43,'Nathan Bell',44,'Finance',95000.00),(44,'Hannah Murphy',29,'HR',58000.00),(45,'Luke Bailey',36,'Support',49000.00);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-18 20:57:17
