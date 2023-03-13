insert into whoop_logger.event_type (
	event_class_id,
	event_type_name_en,
	event_type_name
)
SELECT ec.id, t.column2, t.column3
FROM (
	VALUES 
		('lifestyle', 'Airplane', 'Самолет'),
		('lifestyle', 'Alcohol', 'Алкоголь'),
		('lifestyle', 'Caffeine', 'Кофеин'),
		('lifestyle', 'Marijuana', 'Марихуанна'),
		('lifestyle', 'Masturbation', 'Мастурбация'),
		('lifestyle', 'Sex', 'Секс'),
		('lifestyle', 'Tobacco', 'Табак'),
		('recovery', 'Massage', 'Массаж'),
		('recovery', 'Meditation', 'Медитация'),
		('recovery', 'Sauna', 'Сауна'),
		('recovery', 'Melatonin', 'Мелатонин')
	) AS t
	LEFT JOIN whoop_logger.event_class ec ON t.column1 = ec.event_class_name;


select event_type
     , min(event_dttm)
     , max(event_dttm)
	 , sum(event_cnt)
from whoop_logger.event
where event_dttm >
(
	select greatest(max(event_dttm), '1970-01-01'::timestamp) 
	 from whoop_logger.event 
	where event_type_id = (
		select id 
		from whoop_logger.event_type 
		where event_type_name_ = 'sleep'
	)
)
group by event_type