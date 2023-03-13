create table whoop_logger.whoop_logger_app.event_type
(
	id INTEGER PRIMARY KEY,
	name VARCHAR(50),
	
);
insert into event_type (

)
create table whoop_logger.whoop_logger_app.event
(
	id INTEGER PRIMARY KEY,
	event_type INTEGER,
	event_dttm TIMESTAMP default now(),
)