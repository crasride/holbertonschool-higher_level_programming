--  create the table unique_id (id INT value default 1, unique name VARCHAR(256) )
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1,
	UNIQUE(id),
    name VARCHAR(256)
);
