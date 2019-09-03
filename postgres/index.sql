-- Create Table
CREATE TABLE table_name(
    id INT,
    username TEXT
);

-- Create column
CREATE TABLE table_name(
    id INT,
    username TEXT
);

-- Insert the value into column
INSERT INTO table_name(id,username) 
VALUES(1,"Rouen");

insert into table_name(1,'wgzhao') returning id,name;

-- The completed Create Table and Inserting the data
create table foo(id int,name text);
insert into foo values(1,'wgzhao') returning id,name;