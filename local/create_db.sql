CREATE DATABASE assets;
USE assets;
CREATE TABLE assets(
    entry_id INT NOT NULL AUTO_INCREMENT,
    path VARCHAR(100) NOT NULL,
    PRIMARY KEY ( entry_id )
);
