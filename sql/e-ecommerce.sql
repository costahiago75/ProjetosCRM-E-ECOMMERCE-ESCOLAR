create database contatos;
use contatos;

create table contatos (
id_contado int not null auto_increment primary key,
nome varchar (25) not null, 
contato varchar (16) not null);

insert into contatos (nome,contato) values ('Hiago','99991393037');
insert into contatos (nome,contato) values ('Gislane','99992230494');
insert into contatos (nome,contato) values ('Madson', '99991088620');

select * from contatos;


    
    
    
    
    
    
    



    
    
    
    
    