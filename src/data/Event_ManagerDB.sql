DROP TABLE IF EXISTS Users,Address,Events,Participants;
CREATE TABLE Users(
	user_id bigint PRIMARY KEY NOT NULL,
	user_name varchar(50) NOT NULL,
	passw varchar(20) NOT NULL,
	email varchar(50) UNIQUE NOT NULL
	
);

CREATE TABLE Address(
	address_id bigint PRIMARY KEY NOT NULL,
	street varchar(100) NOT NULL,
	house_number integer NOT NULL, 
	city varchar(50) NOT NULL,
	event_state varchar(30) NOT NULL, --geographical meaning of state, like Rio Grande do Sul
	zip_code integer NOT NULL,
	apartment integer,
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
	event_parent_id int DEFAULT NULL,
	FOREIGN KEY (event_parent_id) REFERENCES Events(event_id),
	FOREIGN KEY (host_id) REFERENCES Users(user_id), 
	FOREIGN KEY (address_id) REFERENCES Address(address_id)
);

CREATE TABLE Participants(
	user_id bigint NOT NULL,
	event_id bigint NOT NULL, 
	PRIMARY KEY(user_id,event_id),
	FOREIGN KEY(user_id) REFERENCES Users(user_id),
	FOREIGN KEY (event_id) REFERENCES Events(event_id)
);

insert into Address values(9069042560,'a',20,'b','c',123456);
insert into Users values(1660521522845,'algo','123','gmail.com');

