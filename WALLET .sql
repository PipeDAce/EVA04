--Creacion de las tablas Segundarias

CREATE TABLE SEXO (
    id_sexo NUMBER(5) PRIMARY KEY,
    nombre_sexo VARCHAR2(30)
);

INSERT INTO SEXO (id_sexo,nombre_sexo)
VALUES (1, 'Hombre');

INSERT INTO SEXO (id_sexo,nombre_sexo)
VALUES (2, 'Mujer');

CREATE TABLE CARGO (
    id_cargo NUMBER(5) PRIMARY KEY,
    nombre_cargo VARCHAR2(30),
    descripcion_cargo VARCHAR2(100)
);

INSERT INTO CARGO (id_cargo,nombre_cargo,descripcion_cargo)
VALUES (1, 'RRHH','Encargado de realizar las gestiones de la empresa');

INSERT INTO CARGO (id_cargo,nombre_cargo,descripcion_cargo)
VALUES (2, 'Gerente','Encargado de dirigir y supervisar los procesos de la empresa');

INSERT INTO CARGO (id_cargo,nombre_cargo,descripcion_cargo)
VALUES (3, 'Empleado','Encargado de realizar las acciones de la empresa');

CREATE TABLE PARENTESCO(
    id_parentesco NUMBER(5) PRIMARY KEY,
    nombre_parentesco VARCHAR2(30),
    descripcion_parentesco VARCHAR2(100)
);

INSERT INTO PARENTESCO (id_parentesco, nombre_parentesco, descripcion_parentesco)
VALUES (1, 'Hijo', 'Cesar Carga de Felipe por ser su Hijo');

INSERT INTO PARENTESCO (id_parentesco, nombre_parentesco, descripcion_parentesco)
VALUES (2, 'Hija','Martina es Carga de Felipe por ser su Hija');

INSERT INTO PARENTESCO (id_parentesco, nombre_parentesco, descripcion_parentesco)
VALUES (3, 'Esposa','Maria es Carga de Felipe por ser su Esposa');

CREATE TABLE RELACION(
    id_relacion NUMBER(5) PRIMARY KEY,
    nombre_relacion VARCHAR2(30)
);

INSERT INTO RELACION (id_relacion, nombre_relacion)
VALUES (1, 'hermanos');

INSERT INTO RELACION (id_relacion, nombre_relacion)
VALUES (2, 'padres');

INSERT INTO RELACION (id_relacion, nombre_relacion)
VALUES (3, 'amigos');

CREATE TABLE AREA(
    id_area NUMBER(5) PRIMARY KEY,
    nombre_area VARCHAR2(30),
    descripcion_area VARCHAR2(100)
);

INSERT INTO AREA (id_area, nombre_area, descripcion_area)
VALUES (1, 'Recursos Humanos', 'Pertenece al area de Recursos Humanos');

INSERT INTO AREA (id_area, nombre_area, descripcion_area)
VALUES (2, 'Gerencia', 'Pertenece al rea de la Gerencia');

INSERT INTO AREA (id_area, nombre_area, descripcion_area)
VALUES (3, 'Empleados', 'Pertenece al area de Trabajadores');


CREATE TABLE DEPARTAMENTO(
    id_departamento NUMBER(5) PRIMARY KEY,
    nombre_departamento VARCHAR2(30),
    descripcion_departamento VARCHAR2(100)
);

INSERT INTO DEPARTAMENTO (id_departamento, nombre_departamento, descripcion_departamento)
VALUES (1, 'Compra/Venta', 'Encargados en realizar las compras y las ventas de la empresa');

INSERT INTO DEPARTAMENTO (id_departamento, nombre_departamento, descripcion_departamento)
VALUES (2, 'Marketing', 'Encargados a realizar todas las funcionalidades de marketing para ddar a conocer la empresa');

INSERT INTO DEPARTAMENTO (id_departamento, nombre_departamento, descripcion_departamento)
VALUES (3, 'Programacion', 'Encargados en realizar todos los procesos en la creacion de aplicaciones');

--Creacion de las tablas primarias
CREATE TABLE TRABAJADOR (
  id_trabajador NUMBER(5) PRIMARY KEY,
  rut_trabajador VARCHAR2(15),
  id_sexo_fk NUMBER(5),
  nombre_trabajador VARCHAR2(50),
  id_cargo_fk NUMBER(5),
  FOREIGN KEY (id_sexo_fk) REFERENCES SEXO(id_sexo),
  FOREIGN KEY (id_cargo_fk) REFERENCES CARGO(id_cargo)
);

INSERT INTO TRABAJADOR (id_trabajador, rut_trabajador,id_sexo_fk, nombre_trabajador,id_cargo_fk)
VALUES (001, '25.098.785-4',1,'Felipe',2);

CREATE TABLE DATOSLABORALES (
  id_datoslaborales NUMBER(5) PRIMARY KEY,
  id_cargo_fk NUMBER(5),
  id_departamento_fk NUMBER(5),
  fechaingreso DATE, 
  id_area_fk NUMBER(5),
  FOREIGN KEY (id_cargo_fk) REFERENCES CARGO(id_cargo),
  FOREIGN KEY (id_departamento_fk) REFERENCES DEPARTAMENTO(id_departamento),
  FOREIGN KEY (id_area_fk) REFERENCES AREA(id_area)
);

INSERT INTO DATOSLABORALES (id_datoslaborales, id_cargo_fk,id_departamento_fk,fechaingreso,id_area_fk)
VALUES (1,2,1,TO_DATE('2023-01-01','YYYY-MM-DD'),2);

CREATE TABLE CONTACTODEEMERGENCIA(
    id_contactodeemergencia NUMBER(5) PRIMARY KEY,
    id_relacion_fk NUMBER(5),
    telefono NUMBER(20),
    nombre VARCHAR2(50),
    FOREIGN KEY (id_relacion_fk) REFERENCES RELACION(id_relacion)
);

INSERT INTO CONTACTODEEMERGENCIA (id_contactodeemergencia, id_relacion_fk,telefono, nombre)
VALUES (1,1,965452367,'Marcelo');

CREATE TABLE CARGASFAMILIARES(
    id_cargasfamiliares NUMBER(5) PRIMARY KEY,
    id_sexo_fk NUMBER(5),
    nombre VARCHAR2(50),
    rut_carga VARCHAR2(15),
    id_parentesco_fk NUMBER(5),
    FOREIGN KEY (id_sexo_fk) REFERENCES SEXO(id_sexo),
    FOREIGN KEY (id_parentesco_fk) REFERENCES PARENTESCO(id_parentesco)  
);

INSERT INTO CARGASFAMILIARES (id_cargasfamiliares, id_sexo_fk,nombre, rut_carga, id_parentesco_fk)
VALUES (1,2,'Martina',25065485-4, 2);

 --la tabla ficha tiene todas las fk de las demas tablas
CREATE TABLE FICHA(
    id_ficha NUMBER(5) PRIMARY KEY,
    id_trabajador_fk NUMBER(5),
    id_datoslaborales_fk NUMBER(5),
    id_contactodeemergencia_fk NUMBER(5),
    id_cargasfamiliares_fk NUMBER(5),
    FOREIGN KEY (id_trabajador_fk) REFERENCES TRABAJADOR(id_trabajador),
    FOREIGN KEY (id_datoslaborales_fk) REFERENCES DATOSLABORALES(id_datoslaborales),
    FOREIGN KEY (id_contactodeemergencia_fk) REFERENCES CONTACTODEEMERGENCIA(id_contactodeemergencia),
    FOREIGN KEY (id_cargasfamiliares_fk) REFERENCES CARGASFAMILIARES(id_cargasfamiliares) 
);

INSERT INTO FICHA (id_ficha, id_trabajador_fk,id_datoslaborales_fk, id_contactodeemergencia_fk, id_cargasfamiliares_fk)
VALUES (1,1,1,1,1);

--Consutar datos usando el inner join
--Tabla principal TRABAJADOR Tablas Segundarias - SEXO - CARGO
SELECT t.*, s.nombre_sexo, c.nombre_cargo, c.descripcion_cargo
FROM TRABAJADOR t
INNER JOIN SEXO s ON t.id_sexo_fk = s.id_sexo
INNER JOIN CARGO c ON t.id_cargo_fk = c.id_cargo;

--Tabla principal DATOSLABORALES Tablas segundarias - CARGO - DEPARTAMENTO - AREA
SELECT bd.*, c.nombre_cargo, c.descripcion_cargo, d.nombre_departamento, d.descripcion_departamento, a.nombre_area, a.descripcion_area
FROM DATOSLABORALES bd
INNER JOIN CARGO c ON bd.id_cargo_fk = c.id_cargo
INNER JOIN DEPARTAMENTO d ON bd.id_departamento_fk = d.id_departamento
INNER JOIN AREA a ON bd.id_area_fk = a.id_area;

--Tabla principal CONTACTODEEMERGENCIA Tablas segundarias - RELACION
SELECT c.*, nombre_relacion
FROM CONTACTODEEMERGENCIA c
INNER JOIN RELACION r ON c.id_relacion_fk = r.id_relacion;

--Tabla principal CARGASFAMILIARES Tablas Segundarias SEXO - CARGO - PARENTESCO
SELECT cf.*, nombre_sexo, nombre_parentesco, descripcion_parentesco
FROM CARGASFAMILIARES cf
INNER JOIN SEXO s ON cf.id_sexo_fk = s.id_sexo
INNER JOIN PARENTESCO p ON cf.id_parentesco_fk = p.id_parentesco;

--Tabla principal FICHA Tablas Segundarias TRABAJADOR - DATOSLABORALES - CONTACTOSDEEMERGENCIA - CARGASFAMILIARES
SELECT f.*, t.rut_trabajador, t.nombre_trabajador, d.fechaingreso, c.telefono, c.nombre, cf.nombre, cf.rut_carga
FROM FICHA f
INNER JOIN TRABAJADOR t ON f.id_trabajador_fk = t.id_trabajador
INNER JOIN DATOSLABORALES d ON f.id_datoslaborales_fk = d.id_datoslaborales
INNER JOIN CONTACTODEEMERGENCIA c ON f.id_contactodeemergencia_fk = c.id_contactodeemergencia
INNER JOIN CARGASFAMILIARES cf ON f.id_cargasfamiliares_fk = cf.id_cargasfamiliares;


--Consultar las tablas
SELECT *FROM SEXO;
SELECT *FROM CARGO;
SELECT *FROM PARENTESCO;
SELECT *FROM RELACION;
SELECT *FROM AREA;
SELECT *FROM DEPARTAMENTO;

SELECT *FROM TRABAJADOR;
SELECT *FROM DATOSLABORALES;
SELECT *FROM CONTACTODEEMERGENCIA;
SELECT *FROM CARGASFAMILIARES;
SELECT *FROM FICHA;

--drops tablets de las tablas
DROP TABLE SEXO;
DROP TABLE CARGO;
DROP TABLE PARENTESCO;
DROP TABLE RELACION;
DROP TABLE AREA;
DROP TABLE DEPARTAMENTO;

DROP TABLE TRABAJADOR;
DROP TABLE DATOSLABORALES;
DROP TABLE CONTACTODEEMERGENCIA;
SELECT *FROM CARGASFAMILIARES;
DROP TABLE FICHA;