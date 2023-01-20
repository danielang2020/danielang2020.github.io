1. at any transaction level. this is storage engine, innodb has row lock.
2. create table in mysql.
create table ex (id integer primary key,text varchar(200));


| session 1 | session 2 |
| --- | --- |
| start transaction;                                       |                                                        |
|                                                          | start transaction;                                     |
| INSERT INTO ex (id, text) SELECT * FROM (SELECT 2, 'first') AS tmp WHERE NOT EXISTS ( SELECT id FROM repexeatable_read WHERE text = 'first' ) LIMIT 1; |                                                        |
| Query OK, 1 row affected (0.00 sec)                 |                                                        |
| Records: 1  Duplicates: 0  Warnings: 0                   |  |
|                                                          | INSERT INTO ex (id, text) SELECT * FROM (SELECT 3, 'first') AS tmp WHERE NOT EXISTS (     SELECT id FROM ex WHERE text = 'first' ) LIMIT 1;                                     |
|                                                          | result: waiting...                                                       |
| commit;                                                  |                                                        |
|                                                          | Query OK, 0 rows affected (4.94 sec[waiting time])     |
|                                                          | commit;                                                |
|                                                          | Query OK, 0 rows affected (0.00 sec)                   |