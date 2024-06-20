DROP DATABASE IF EXISTS typeshit;
CREATE DATABASE typeshit;

USE typeshit;
CREATE TABLE `client_accounts` (
    `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(64) NOT NULL,
    `password` VARCHAR(64) NOT NULL
);
CREATE TABLE `clients` (
    `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_account` SMALLINT UNSIGNED NOT NULL,
    `firstname` VARCHAR(64) NOT NULL,
    `lastname` VARCHAR(64) NOT NULL,
    `mail` VARCHAR(64) NOT NULL,
    `phone` VARCHAR(16) NOT NULL,
    FOREIGN KEY (`id_account`) REFERENCES `client_accounts`(`id`)
);
CREATE TABLE `employee_accounts` (
    `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(64) NOT NULL,
    `password` VARCHAR(64) NOT NULL
);
CREATE TABLE `employees` (
    `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_account` SMALLINT UNSIGNED NOT NULL,
    `firstname` VARCHAR(64) NOT NULL,
    `lastname` VARCHAR(64) NOT NULL,
    `mail` VARCHAR(64) NOT NULL,
    `phone` VARCHAR(16) NOT NULL,
    FOREIGN KEY (`id_account`) REFERENCES `employee_accounts`(`id`)
);
CREATE TABLE `devis` (
    `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_client` SMALLINT UNSIGNED NOT NULL,
    `id_employee` SMALLINT UNSIGNED NOT NULL,
    FOREIGN KEY (`id_client`) REFERENCES `clients`(`id`),
    FOREIGN KEY (`id_employee`) REFERENCES `employees`(`id`)
);
CREATE TABLE `devis_details` (
    `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_devis` SMALLINT UNSIGNED NOT NULL,
    `id_service` SMALLINT UNSIGNED NOT NULL,
    FOREIGN KEY (`id_devis`) REFERENCES `devis`(`id`),
    FOREIGN KEY (`id_service`) REFERENCES `services`(`id`)
);
CREATE TABLE `services` (
    `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(64) NOT NULL,
    `description` VARCHAR(256)
);
