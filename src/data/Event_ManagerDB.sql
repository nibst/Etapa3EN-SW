DROP TABLE IF EXISTS Users,Address,Events,Participants;
CREATE TABLE Users(
	user_id bigint PRIMARY KEY NOT NULL,
	user_name varchar(50) NOT NULL,
	email varchar(50) UNIQUE NOT NULL,
	passw varchar(20) NOT NULL

	
);

CREATE TABLE Address(
	address_id bigint PRIMARY KEY NOT NULL,
	street varchar(100) NOT NULL,
	house_number integer NOT NULL, 
	city varchar(50) NOT NULL,
	event_state varchar(30) NOT NULL, --geographical meaning of state, like Rio Grande do Sul
	zip_code integer NOT NULL,
	complement varchar(150)
);

CREATE TABLE Events(
	event_id bigint PRIMARY KEY NOT NULL,
	host_id bigint NOT NULL,
	event_name varchar(50) NOT NULL,
	address_id bigint NOT NULL,
	start_date date NOT NULL,
	end_date date NOT NULL,
	visibility BOOLEAN NOT NULL,
	check_in time,
	check_out time,
	description varchar(200) DEFAULT NULL,
	category varchar(20) DEFAULT NULL,
	event_parent_id bigint DEFAULT NULL,
	FOREIGN KEY (event_parent_id) REFERENCES Events(event_id),
	FOREIGN KEY (host_id) REFERENCES Users(user_id), 
	FOREIGN KEY (address_id) REFERENCES Address(address_id)
);

CREATE TABLE Participants(
	user_id bigint NOT NULL,
	event_id bigint NOT NULL,
	has_checked_in BOOLEAN DEFAULT false,
	has_checked_out BOOLEAN DEFAULT false,
	PRIMARY KEY(user_id,event_id),
	FOREIGN KEY(user_id) REFERENCES Users(user_id),
	FOREIGN KEY (event_id) REFERENCES Events(event_id)
);


insert into Address values(9069042560,'a',20,'b','c',123456);
insert into Users values(166,'nibs', 'nikolasps7@gmail.com', 'senha123');
insert into Users values(1234, 'nikolas', 'emaildetesteparaevento@teste.eu', 'senha123');
insert into Users values(1235, 'nikolas', 'emaildetest36eparaevento@teste.eu', 'senha123');

Insert INTO Events VALUES(01,1234,'event name',9069042560, '2023-06-03','2023-06-03',TRUE,'20:06:03','23:06:03','Evento sobre bla bla bla','Festa');
INSERT INTO Participants VALUES(1234,01,true,false);


