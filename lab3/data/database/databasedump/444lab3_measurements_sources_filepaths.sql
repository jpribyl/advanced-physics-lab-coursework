-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: 444lab3
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

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
-- Table structure for table `measurements_sources_filepaths`
--

DROP TABLE IF EXISTS `measurements_sources_filepaths`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `measurements_sources_filepaths` (
  `measurements_id` int(11) NOT NULL,
  `filepaths_id` int(11) NOT NULL,
  `sources_id` int(11) NOT NULL,
  PRIMARY KEY (`measurements_id`,`filepaths_id`),
  KEY `fk_filepaths_has_measurements_measurements1_idx` (`measurements_id`),
  KEY `fk_filepaths_has_measurements_filepaths1_idx` (`filepaths_id`),
  KEY `fk_filepaths_has_measurements_sources1_idx` (`sources_id`),
  CONSTRAINT `fk_filepaths_has_measurements_filepaths1` FOREIGN KEY (`filepaths_id`) REFERENCES `filepaths` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_filepaths_has_measurements_measurements1` FOREIGN KEY (`measurements_id`) REFERENCES `measurements` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_filepaths_has_measurements_sources1` FOREIGN KEY (`sources_id`) REFERENCES `sources` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `measurements_sources_filepaths`
--

LOCK TABLES `measurements_sources_filepaths` WRITE;
/*!40000 ALTER TABLE `measurements_sources_filepaths` DISABLE KEYS */;
INSERT INTO `measurements_sources_filepaths` VALUES (1,2,1),(2,4,1),(3,6,1),(4,8,1),(5,10,1),(6,12,1),(7,14,1),(8,16,1),(9,18,1),(10,20,1),(1,1,2),(2,3,2),(3,5,2),(4,7,2),(5,9,2),(6,11,2),(7,13,2),(8,15,2),(9,17,2),(10,19,2),(11,21,2),(12,22,2),(13,23,2),(14,24,2),(15,25,2),(16,26,2),(17,27,2),(18,28,2),(19,29,2),(20,30,2),(21,31,2),(22,32,2),(23,33,2),(24,34,2),(25,35,2),(26,36,2),(27,37,2),(28,38,2),(29,39,2),(30,40,2),(31,41,2),(32,42,2);
/*!40000 ALTER TABLE `measurements_sources_filepaths` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-08 11:12:29
