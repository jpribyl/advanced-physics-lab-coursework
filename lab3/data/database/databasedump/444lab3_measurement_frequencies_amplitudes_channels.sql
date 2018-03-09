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
-- Table structure for table `measurement_frequencies_amplitudes_channels`
--

DROP TABLE IF EXISTS `measurement_frequencies_amplitudes_channels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `measurement_frequencies_amplitudes_channels` (
  `measurements_id` int(11) NOT NULL,
  `frequencies_id` int(11) DEFAULT NULL,
  `amplitudes_id` int(11) DEFAULT NULL,
  `channels_id` int(11) NOT NULL,
  KEY `fk_measurements_has_channels_measurements_idx` (`measurements_id`),
  KEY `fk_measurements_has_channels_frequencies1_idx` (`frequencies_id`),
  KEY `fk_measurements_has_channels_amplitudes1_idx` (`amplitudes_id`),
  KEY `fk_measurements_has_channels_channels1_idx` (`channels_id`),
  CONSTRAINT `fk_measurements_has_channels_amplitudes1` FOREIGN KEY (`amplitudes_id`) REFERENCES `amplitudes` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_measurements_has_channels_channels1` FOREIGN KEY (`channels_id`) REFERENCES `channels` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_measurements_has_channels_frequencies1` FOREIGN KEY (`frequencies_id`) REFERENCES `frequencies` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_measurements_has_channels_measurements` FOREIGN KEY (`measurements_id`) REFERENCES `measurements` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `measurement_frequencies_amplitudes_channels`
--

LOCK TABLES `measurement_frequencies_amplitudes_channels` WRITE;
/*!40000 ALTER TABLE `measurement_frequencies_amplitudes_channels` DISABLE KEYS */;
INSERT INTO `measurement_frequencies_amplitudes_channels` VALUES (1,1,5,1),(2,1,5,1),(3,2,5,1),(4,2,5,1),(4,2,1,2),(5,2,5,1),(5,16,1,2),(6,2,5,1),(6,3,1,2),(7,2,5,1),(7,4,1,2),(8,2,5,1),(8,6,1,2),(9,5,5,1),(9,5,1,2),(10,5,5,1),(10,7,1,2),(13,11,5,1),(14,12,5,1),(15,13,5,1),(20,8,5,1),(21,15,5,1),(22,11,5,1),(23,14,5,1),(24,12,5,1),(27,9,5,1),(28,10,5,1);
/*!40000 ALTER TABLE `measurement_frequencies_amplitudes_channels` ENABLE KEYS */;
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
