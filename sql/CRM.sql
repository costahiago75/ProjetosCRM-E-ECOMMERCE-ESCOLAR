create database crm;
use crm;

create table clientes (
id_cliente int not null auto_increment primary key,
nome_cliente varchar (30) not null,
telefone varchar (16) not null,
ultima_compra date not null);

insert into clientes(nome_cliente,telefone,ultima_compra) values ('Hiago','(99)991393037','2005-04-05');

select  * from clientes;