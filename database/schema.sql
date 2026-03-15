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

create table body_area (
	area_id INT primary key auto_increment ,
    area_name varchar(50) not null,
    region enum('upper', 'lower', 'full') not null
);

create table symptom_keyword (
	symptom_keyword_id int auto_increment primary key,
    keyword varchar(50) not null,
    weight int not null,
    rationale text not null, 
    massage_id int, foreign key (massage_id) references massage_type(massage_id),
	area_id int, foreign key (area_id) references body_area(area_id)
);

