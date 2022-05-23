DROP database IF EXISTS fasterbus_db;
CREATE database fasterbus_db;
use fasterbus_db;

DROP TABLE IF EXISTS passengers;
CREATE TABLE passengers (
    id INT(20) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    full_name VARCHAR(255) NOT NULL,
    document INT(20) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS buses;
CREATE table buses(
	id int(20) PRIMARY key not null auto_increment,
	plate varchar(50) not null,
	type varchar(50) not null,
	capacity int(10) not null,
    company varchar(255) not null
);

DROP TABLE IF EXISTS routes;
CREATE table routes(
	id int(20) PRIMARY key not null auto_increment,
	origin varchar(255) not null,
	destination varchar(255) not null
);

DROP TABLE IF EXISTS route_bus;
create table route_bus(
	id int(20) PRIMARY key not null auto_increment,
	bus_id int(20) not null,
	route_id int(20) not null,
	Foreign key(bus_id) references buses(id),
	Foreign key(route_id) references routes(id)
);

DROP TABLE IF EXISTS tickets;
create table tickets(
	id int(20) PRIMARY key not null auto_increment,
	route_bus_id int(20) not null,
	passenger_id int(20) not null,
	quantity int(5) not null,
	travel_date date not null,
	departure_time time not null,
	Foreign key(route_bus_id) references route_bus(id),	
	Foreign key(passenger_id) references passengers(id)
);
