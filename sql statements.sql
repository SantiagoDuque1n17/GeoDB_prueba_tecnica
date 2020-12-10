create table Ticket (
	id_ticket varchar(20) not null, 
	id_evento varchar(10) not null, 
	numero_de_entrada int not null, 
	estado varchar(1) not null, 
	primary key (id_ticket)
);

create table Evento (
	id_evento varchar(10) not null,
	id_recinto varchar(5) not null,
	descripcion varchar(255) not null,
	fecha date not null,
	primary key (id_evento)
);
	
create table Recinto (
	id_recinto varchar(5) not null,
	latitud float(20) not null,
	longitud float(20) not null,
	primary key (id_recinto)
);

alter table Ticket
add foreign key (id_evento) references Evento(id_evento);

alter table Evento
add foreign key (id_recinto) references Recinto(id_recinto);

INSERT INTO Recinto (id_recinto, latitud, longitud) 
	VALUES ("MADRD", 40.416729, -3.703339);
INSERT INTO Recinto (id_recinto, latitud, longitud) 
	VALUES ("BERLN", 52.520008, 13.404954);
	
INSERT INTO Evento (id_evento, id_recinto, descripcion, fecha) 
	VALUES (1111111111, 'MADRD', 'Concierto', '2020-12-29');
INSERT INTO Evento (id_evento, id_recinto, descripcion, fecha) 
	VALUES (1111111112, 'BERLN', 'Obra de teatro', '2021-1-2');
INSERT INTO Evento (id_evento, id_recinto, descripcion, fecha) 
	VALUES (1111111113, 'MADRD', 'Monólogo', '2021-2-28');
I
	

INSERT INTO Ticket (id_ticket, id_evento, numero_de_entrada, estado) 
	VALUES ("ewuiehwmuwhenjLsdkj", 1111111111, 1, 'v');
INSERT INTO Ticket (id_ticket, id_evento, numero_de_entrada, estado) 
	VALUES ("qsADNLAkahdk291nsdd", 1111111111, 2, 'u');
INSERT INTO Ticket (id_ticket, id_evento, numero_de_entrada, estado) 
	VALUES ("9hX98i4TVDLpc3tkTzs", 1111111111, 3, 'v');
INSERT INTO Ticket (id_ticket, id_evento, numero_de_entrada, estado) 
	VALUES ("2smpubHaV46Hj49inss", 1111111112, 1, 'u');
INSERT INTO Ticket (id_ticket, id_evento, numero_de_entrada, estado) 
	VALUES ("2uxog2FH2N2E1ZboNLL", 1111111112, 2, 'v');
INSERT INTO Ticket (id_ticket, id_evento, numero_de_entrada, estado) 
	VALUES ("9NGjuknaAuvD2qq5Nxs", 1111111112, 3, 'u');
INSERT INTO Ticket (id_ticket, id_evento, numero_de_entrada, estado) 
	VALUES ("b'jpYA5K9FMcN7366kT", 1111111113, 1, 'v');
INSERT INTO Ticket (id_ticket, id_evento, numero_de_entrada, estado) 
	VALUES ("2yJiRg62HEVhmSwtLQQ", 1111111113, 2, 'u');