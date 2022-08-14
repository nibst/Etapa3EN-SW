
CREATE TABLE Users(
	user_id int PRIMARY KEY NOT NULL,
	user_name varchar(50) NOT NULL,
	passw varchar(20) NOT NULL,
	email varchar(50) NOT NULL
	
);

CREATE TABLE Events(
	event_id int PRIMARY KEY NOT NULL,
	host_id int NOT NULL,
	event_name varchar(50) NOT NULL,
	address_id int NOT NULL,
	start_date date NOT NULL,
	end_date date NOT NULL,
	visibility BOOLEAN NOT NULL,
	check_in time,
	check_out time,
	event_parent_id int DEFAULT NULL,
	FOREIGN KEY (event_parent_id) REFERENCES Evento(event_id),
	FOREIGN KEY (host_id) REFERENCES Usuario(user_id) 
	FOREIGN KEY (address_id) REFERENCES Address(address_id)
);
CREATE TABLE Address(
	address_id int PRIMARY KEY NOT NULL,
	street varchar(100) NOT NULL,
	house_number int NOT NULL, 
	city varchar(50) NOT NULL,
	event_state varchar(30) NOT NULL, --geographical meaning of state, like Rio Grande do Sul
	zip_code int NOT NULL,
	apartment int,
	complement varchar(150)
);
CREATE TABLE Participants(
	user_id int NOT NULL,
	event_id int NOT NULL, 
	PRIMARY KEY(user_id,event_id),
	FOREIGN KEY(user_id) REFERENCES Usuario(user_id),
	FOREIGN KEY (event_id) REFERENCES Evento(event_id)
);