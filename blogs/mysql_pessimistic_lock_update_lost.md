1. at any transaction level. this is storage engine, innodb has row lock.
2. create table in mysql.
create table lc (id integer primary key,text varchar(200));

3. insert a new data in lc;
insert into lc values(1,'first');

| session 1 | session 2 |
| --- | --- |
| insert into lc values(1,'first');                              |                                                                            |
|                                                                             | select * from lc; result:(1,'first')                          |
| start transaction;                                                          |                                                                            |
|                                                                             | start transaction;                                                         |
| update lc set text = 'second' where id = 1 and text = 'first'; |                                                                            |
| Query OK, 1 row affected (0.00 sec)                                         |                                                                            |
| Rows matched: 1  Changed: 0  Warnings: 0                                    |                                                                            |
|                                                                             | update lc set text = 'thrid' where id = 1 and text = 'first'; |
|                                                                             | result: waiting...                                                         |
| commit;                                                                     |                                                                            |
|                                                                             | Query OK, 0 rows affected (4.94 sec[waiting time])                         |
|                                                                             | Rows matched: 0  Changed: 0  Warnings: 0                                   |
|                                                                             | commit;                                                                    |