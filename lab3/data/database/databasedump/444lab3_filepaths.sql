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
-- Table structure for table `filepaths`
--

DROP TABLE IF EXISTS `filepaths`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `filepaths` (
  `id` int(11) NOT NULL,
  `filepath` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filepaths`
--

LOCK TABLES `filepaths` WRITE;
/*!40000 ALTER TABLE `filepaths` DISABLE KEYS */;
INSERT INTO `filepaths` VALUES (1,'data/440121518'),(2,'data/scope-440121518'),(3,'data/450121518'),(4,'data/scope-450121518'),(5,'data/455121518'),(6,'data/scope-455121518'),(7,'data/506121518'),(8,'data/scope-506121518'),(9,'data/511121518'),(10,'data/scope-511121518'),(11,'data/513121518'),(12,'data/scope-513121518'),(13,'data/515121518'),(14,'data/scope-515121518'),(15,'data/519121518'),(16,'data/scope-519121518'),(17,'data/525121518'),(18,'data/scope-525121518'),(19,'data/527121518'),(20,'data/scope-527121518'),(21,'data/556121518'),(22,'data/600121518'),(23,'data/50822218'),(24,'data/51122218'),(25,'data/51322218'),(26,'data/52622218'),(27,'data/53322218'),(28,'data/60722218'),(29,'data/61322218'),(30,'data/0352312078'),(31,'data/433030118'),(32,'data/437030118'),(33,'data/440030118'),(34,'data/442030118'),(35,'data/451030118'),(36,'data/0521030118'),(37,'data/556030118'),(38,'data/600030118'),(39,'data/11540306'),(40,'data/11560306'),(41,'data/12153618'),(42,'data/12163618');
/*!40000 ALTER TABLE `filepaths` ENABLE KEYS */;
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
