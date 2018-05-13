DROP TABLE IF EXISTS todo_todo CASCADE;

CREATE TABLE todo_todo (
    id serial PRIMARY KEY,
    name character varying(50) NOT NULL,
    slug character varying(50) NOT NULL,
    content text default '',
    up_vote int not null default 0,
    down_vote int not null default 0,
    is_active boolean NOT NULL default false
);

CREATE UNIQUE INDEX todo_todo_slug on todo_todo(slug);
