-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema 444lab3
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema 444lab3
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `444lab3` DEFAULT CHARACTER SET utf8 ;
USE `444lab3` ;

-- -----------------------------------------------------
-- Table `444lab3`.`frequencies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `444lab3`.`frequencies` (
  `id` INT NOT NULL COMMENT '\n',
  `frequency` DOUBLE NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `frequency_UNIQUE` (`frequency` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `444lab3`.`amplitudes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `444lab3`.`amplitudes` (
  `id` INT NOT NULL,
  `amplitude` DOUBLE NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `444lab3`.`forms`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `444lab3`.`forms` (
  `id` INT NOT NULL,
  `form_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `444lab3`.`measurements`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `444lab3`.`measurements` (
  `id` INT NOT NULL COMMENT '\n',
  `forms_id` INT NOT NULL,
  PRIMARY KEY (`id`, `forms_id`),
  INDEX `fk_measurements_forms1_idx` (`forms_id` ASC),
  CONSTRAINT `fk_measurements_forms1`
    FOREIGN KEY (`forms_id`)
    REFERENCES `444lab3`.`forms` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `444lab3`.`channels`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `444lab3`.`channels` (
  `id` INT NOT NULL,
  `channel_num` SMALLINT(6) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `444lab3`.`sources`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `444lab3`.`sources` (
  `id` INT NOT NULL,
  `source_name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `444lab3`.`measurement_frequencies_amplitudes_channels`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `444lab3`.`measurement_frequencies_amplitudes_channels` (
  `measurements_id` INT NOT NULL,
  `frequencies_id` INT NULL,
  `amplitudes_id` INT NULL,
  `channels_id` INT NOT NULL,
  INDEX `fk_measurements_has_channels_measurements_idx` (`measurements_id` ASC),
  INDEX `fk_measurements_has_channels_frequencies1_idx` (`frequencies_id` ASC),
  INDEX `fk_measurements_has_channels_amplitudes1_idx` (`amplitudes_id` ASC),
  INDEX `fk_measurements_has_channels_channels1_idx` (`channels_id` ASC),
  CONSTRAINT `fk_measurements_has_channels_measurements`
    FOREIGN KEY (`measurements_id`)
    REFERENCES `444lab3`.`measurements` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_measurements_has_channels_frequencies1`
    FOREIGN KEY (`frequencies_id`)
    REFERENCES `444lab3`.`frequencies` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_measurements_has_channels_amplitudes1`
    FOREIGN KEY (`amplitudes_id`)
    REFERENCES `444lab3`.`amplitudes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_measurements_has_channels_channels1`
    FOREIGN KEY (`channels_id`)
    REFERENCES `444lab3`.`channels` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `444lab3`.`filepaths`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `444lab3`.`filepaths` (
  `id` INT NOT NULL,
  `filepath` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `444lab3`.`measurements_sources_filepaths`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `444lab3`.`measurements_sources_filepaths` (
  `measurements_id` INT NOT NULL,
  `filepaths_id` INT NOT NULL,
  `sources_id` INT NOT NULL,
  PRIMARY KEY (`measurements_id`, `filepaths_id`),
  INDEX `fk_filepaths_has_measurements_measurements1_idx` (`measurements_id` ASC),
  INDEX `fk_filepaths_has_measurements_filepaths1_idx` (`filepaths_id` ASC),
  INDEX `fk_filepaths_has_measurements_sources1_idx` (`sources_id` ASC),
  CONSTRAINT `fk_filepaths_has_measurements_filepaths1`
    FOREIGN KEY (`filepaths_id`)
    REFERENCES `444lab3`.`filepaths` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_filepaths_has_measurements_measurements1`
    FOREIGN KEY (`measurements_id`)
    REFERENCES `444lab3`.`measurements` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_filepaths_has_measurements_sources1`
    FOREIGN KEY (`sources_id`)
    REFERENCES `444lab3`.`sources` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `444lab3`.`frequencies`
-- -----------------------------------------------------
START TRANSACTION;
USE `444lab3`;
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (1, 5097.0);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (2, 11097.0);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (3, 11697.0);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (4, 22697.0);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (5, 25097.0);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (6, 31697.0);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (7, 207.0);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (8, 333.333);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (9, 5533.0);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (10, 33.33);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (11, 6000.0);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (12, 12000.0);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (13, 18000.0);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (14, 9000.0);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (15, 3000.0);
INSERT INTO `444lab3`.`frequencies` (`id`, `frequency`) VALUES (16, 11597.0);

COMMIT;


-- -----------------------------------------------------
-- Data for table `444lab3`.`amplitudes`
-- -----------------------------------------------------
START TRANSACTION;
USE `444lab3`;
INSERT INTO `444lab3`.`amplitudes` (`id`, `amplitude`) VALUES (1, 1.000);
INSERT INTO `444lab3`.`amplitudes` (`id`, `amplitude`) VALUES (2, 2.000);
INSERT INTO `444lab3`.`amplitudes` (`id`, `amplitude`) VALUES (3, 3.000);
INSERT INTO `444lab3`.`amplitudes` (`id`, `amplitude`) VALUES (4, 4.000);
INSERT INTO `444lab3`.`amplitudes` (`id`, `amplitude`) VALUES (5, 5.000);

COMMIT;


-- -----------------------------------------------------
-- Data for table `444lab3`.`forms`
-- -----------------------------------------------------
START TRANSACTION;
USE `444lab3`;
INSERT INTO `444lab3`.`forms` (`id`, `form_name`) VALUES (1, 'sine');
INSERT INTO `444lab3`.`forms` (`id`, `form_name`) VALUES (2, 'triangle');
INSERT INTO `444lab3`.`forms` (`id`, `form_name`) VALUES (3, 'square');
INSERT INTO `444lab3`.`forms` (`id`, `form_name`) VALUES (4, 'noise');
INSERT INTO `444lab3`.`forms` (`id`, `form_name`) VALUES (5, 'chirp');
INSERT INTO `444lab3`.`forms` (`id`, `form_name`) VALUES (6, 'buried-treasure');

COMMIT;


-- -----------------------------------------------------
-- Data for table `444lab3`.`measurements`
-- -----------------------------------------------------
START TRANSACTION;
USE `444lab3`;
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (1, 3);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (2, 2);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (3, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (4, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (5, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (6, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (7, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (8, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (9, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (10, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (11, 6);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (12, 6);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (13, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (14, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (15, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (16, 4);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (17, 4);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (18, 5);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (19, 5);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (20, 3);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (21, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (22, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (23, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (24, 1);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (25, 4);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (26, 5);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (27, 3);
INSERT INTO `444lab3`.`measurements` (`id`, `forms_id`) VALUES (28, 3);

COMMIT;


-- -----------------------------------------------------
-- Data for table `444lab3`.`channels`
-- -----------------------------------------------------
START TRANSACTION;
USE `444lab3`;
INSERT INTO `444lab3`.`channels` (`id`, `channel_num`) VALUES (1, 1);
INSERT INTO `444lab3`.`channels` (`id`, `channel_num`) VALUES (2, 2);

COMMIT;


-- -----------------------------------------------------
-- Data for table `444lab3`.`sources`
-- -----------------------------------------------------
START TRANSACTION;
USE `444lab3`;
INSERT INTO `444lab3`.`sources` (`id`, `source_name`) VALUES (1, 'scope');
INSERT INTO `444lab3`.`sources` (`id`, `source_name`) VALUES (2, 'analyzer');

COMMIT;


-- -----------------------------------------------------
-- Data for table `444lab3`.`measurement_frequencies_amplitudes_channels`
-- -----------------------------------------------------
START TRANSACTION;
USE `444lab3`;
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (1, 1, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (2, 1, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (3, 2, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (4, 2, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (4, 2, 1, 2);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (5, 2, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (5, 16, 1, 2);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (6, 2, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (6, 3, 1, 2);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (7, 2, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (7, 4, 1, 2);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (8, 2, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (8, 6, 1, 2);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (9, 5, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (9, 5, 1, 2);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (10, 5, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (10, 7, 1, 2);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (13, 11, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (14, 12, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (15, 13, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (20, 8, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (21, 15, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (22, 11, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (23, 14, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (24, 12, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (27, 9, 5, 1);
INSERT INTO `444lab3`.`measurement_frequencies_amplitudes_channels` (`measurements_id`, `frequencies_id`, `amplitudes_id`, `channels_id`) VALUES (28, 10, 5, 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `444lab3`.`filepaths`
-- -----------------------------------------------------
START TRANSACTION;
USE `444lab3`;
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (1, 'data/440121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (2, 'data/scope-440121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (3, 'data/450121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (4, 'data/scope-450121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (5, 'data/455121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (6, 'data/scope-455121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (7, 'data/506121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (8, 'data/scope-506121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (9, 'data/511121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (10, 'data/scope-511121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (11, 'data/513121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (12, 'data/scope-513121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (13, 'data/515121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (14, 'data/scope-515121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (15, 'data/519121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (16, 'data/scope-519121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (17, 'data/525121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (18, 'data/scope-525121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (19, 'data/527121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (20, 'data/scope-527121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (21, 'data/556121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (22, 'data/600121518');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (23, 'data/50822218');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (24, 'data/51122218');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (25, 'data/51322218');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (26, 'data/52622218');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (27, 'data/53322218');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (28, 'data/60722218');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (29, 'data/61322218');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (30, 'data/0352312078');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (31, 'data/433030118');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (32, 'data/437030118');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (33, 'data/440030118');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (34, 'data/442030118');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (35, 'data/451030118');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (36, 'data/0521030118');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (37, 'data/556030118');
INSERT INTO `444lab3`.`filepaths` (`id`, `filepath`) VALUES (38, 'data/600030118');

COMMIT;


-- -----------------------------------------------------
-- Data for table `444lab3`.`measurements_sources_filepaths`
-- -----------------------------------------------------
START TRANSACTION;
USE `444lab3`;
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (1, 1, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (1, 2, 1);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (2, 3, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (2, 4, 1);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (3, 5, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (3, 6, 1);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (4, 7, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (4, 8, 1);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (5, 9, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (5, 10, 1);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (6, 11, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (6, 12, 1);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (7, 13, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (7, 14, 1);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (8, 15, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (8, 16, 1);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (9, 17, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (9, 18, 1);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (10, 19, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (10, 20, 1);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (11, 21, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (12, 22, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (13, 23, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (14, 24, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (15, 25, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (16, 26, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (17, 27, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (18, 28, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (19, 29, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (20, 30, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (21, 31, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (22, 32, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (23, 33, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (24, 34, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (25, 35, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (26, 36, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (27, 37, 2);
INSERT INTO `444lab3`.`measurements_sources_filepaths` (`measurements_id`, `filepaths_id`, `sources_id`) VALUES (28, 38, 2);

COMMIT;

