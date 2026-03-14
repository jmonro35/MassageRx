CREATE DATABASE IF NOT EXISTS massagerx;
USE massagerx;

CREATE TABLE massage_type (
    massage_id INT AUTO_INCREMENT PRIMARY KEY,
    massage_name VARCHAR(50) NOT NULL,
    massage_description TEXT,
    massage_intensity_level VARCHAR(20),
    massage_base_price DECIMAL (6,2)
);

CREATE TABLE add_on (
    addon_id INT AUTO_INCREMENT PRIMARY KEY,
    addon_name VARCHAR(50) NOT NULL,
    addon_description TEXT,
    addon_price DECIMAL (6,2) NOT NULL
);