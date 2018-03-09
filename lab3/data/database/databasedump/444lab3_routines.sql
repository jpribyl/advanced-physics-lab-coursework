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
-- Temporary table structure for view `info`
--

DROP TABLE IF EXISTS `info`;
/*!50001 DROP VIEW IF EXISTS `info`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `info` AS SELECT 
 1 AS `id`,
 1 AS `filepath`,
 1 AS `source_name`,
 1 AS `form_name`,
 1 AS `channel_num`,
 1 AS `frequency`,
 1 AS `amplitude`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `measurement_info`
--

DROP TABLE IF EXISTS `measurement_info`;
/*!50001 DROP VIEW IF EXISTS `measurement_info`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `measurement_info` AS SELECT 
 1 AS `id`,
 1 AS `filepath`,
 1 AS `source_name`,
 1 AS `form_name`,
 1 AS `channel_num`,
 1 AS `frequency`,
 1 AS `amplitude`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `info`
--

/*!50001 DROP VIEW IF EXISTS `info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `info` AS select `a`.`id` AS `id`,`i`.`filepath` AS `filepath`,`h`.`source_name` AS `source_name`,`f`.`form_name` AS `form_name`,`c`.`channel_num` AS `channel_num`,`e`.`frequency` AS `frequency`,`d`.`amplitude` AS `amplitude` from ((((((((`measurements` `a` left join `measurement_frequencies_amplitudes_channels` `b` on((`a`.`id` = `b`.`measurements_id`))) left join `channels` `c` on((`b`.`channels_id` = `c`.`id`))) left join `amplitudes` `d` on((`b`.`amplitudes_id` = `d`.`id`))) left join `frequencies` `e` on((`b`.`frequencies_id` = `e`.`id`))) left join `forms` `f` on((`a`.`forms_id` = `f`.`id`))) left join `measurements_sources_filepaths` `g` on((`a`.`id` = `g`.`measurements_id`))) left join `sources` `h` on((`g`.`sources_id` = `h`.`id`))) left join `filepaths` `i` on((`g`.`filepaths_id` = `i`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `measurement_info`
--

/*!50001 DROP VIEW IF EXISTS `measurement_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `measurement_info` AS select `a`.`id` AS `id`,`i`.`filepath` AS `filepath`,`h`.`source_name` AS `source_name`,`f`.`form_name` AS `form_name`,`c`.`channel_num` AS `channel_num`,`e`.`frequency` AS `frequency`,`d`.`amplitude` AS `amplitude` from ((((((((`measurements` `a` left join `measurement_frequencies_amplitudes_channels` `b` on((`a`.`id` = `b`.`measurements_id`))) left join `channels` `c` on((`b`.`channels_id` = `c`.`id`))) left join `amplitudes` `d` on((`b`.`amplitudes_id` = `d`.`id`))) left join `frequencies` `e` on((`b`.`frequencies_id` = `e`.`id`))) left join `forms` `f` on((`a`.`forms_id` = `f`.`id`))) left join `measurements_sources_filepaths` `g` on((`a`.`id` = `g`.`measurements_id`))) left join `sources` `h` on((`g`.`sources_id` = `h`.`id`))) left join `filepaths` `i` on((`g`.`filepaths_id` = `i`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-08 11:12:30
