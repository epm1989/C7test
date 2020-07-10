
GRANT ALL PRIVILEGES ON CsieteTest.* TO 'vcvcvcvc'@'localhost' IDENTIFIED BY  'xxxxxxxxxx';
CREATE DATABASE IF NOT EXISTS CsieteTest;
USE CsieteTest;

CREATE TABLE IF NOT EXISTS dominios (
    dominio_id INTEGER UNSIGNED  PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(255) NOT NULL UNIQUE,
    active TINYINT(1) DEFAULT 1
    );

CREATE TABLE IF NOT EXISTS ips (
    ip_id INTEGER UNSIGNED  PRIMARY KEY AUTO_INCREMENT, 
    dominio_id INTEGER UNSIGNED,
    ip VARCHAR(100) NOT NULL
    );

CREATE TABLE IF NOT EXISTS logs (
    log_id INTEGER UNSIGNED  PRIMARY KEY AUTO_INCREMENT, 
    dominio_id INTEGER UNSIGNED,
    ip_id INTEGER UNSIGNED,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    description TEXT
    );


ALTER TABLE ips
ADD FOREIGN KEY (dominio_id) REFERENCES dominios(dominio_id);

ALTER TABLE logs
ADD    FOREIGN KEY (dominio_id) REFERENCES dominios(dominio_id);
ALTER TABLE logs
ADD    FOREIGN KEY (ip_id) REFERENCES ips(ip_id);


--pruebas para las tablas
SET @domi='www.purebaejemplo.locasl';
SET @laip='10.2.5.46';
INSERT INTO dominios(name,active) VALUES (@domi,0);
SET @varmydominio = (SELECT dominio_id FROM dominios WHERE name = @domi LIMIT 1)  ;
INSERT INTO ips(ip,dominio_id) VALUES (@laip,@varmydominio);
SET @varmyip = (SELECT ip_id FROM ips WHERE ip = @laip LIMIT 1)  ;

--INSERT INTO logs(dominio_id,description) VALUES ('10.2.5.6');

INSERT INTo logs(dominio_id,ip_id,description) VALUES (@varmydominio,@varmyip,CONCAT('Se detecto un cambio en el dominio ',@domi,' con IP nueva ',@laip));



--ALTER TABLE dominios
--DROP COLUMN ip_id;

--ALTER TABLE dominios 
--DROP FOREIGN KEY ips(ip_id);