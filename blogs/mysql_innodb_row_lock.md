1. at any transaction level. this is storage engine, innodb has row lock.
2. create table in mysql.
create table row_lock (id integer primary key,text varchar(200));

3. insert a new data in row_lock;
insert into row_lock values(1,'first');

| session 1 | session 2 |
| --- | --- |
| insert into row_lock values(1,'first');           |                                                        |
|                                                          | select * from row_lock; result:(1,'first')      |
| start transaction;                                       |                                                        |
|                                                          | start transaction;                                     |
| update row_lock set text = 'second' where id = 1; |                                                        |
| Rows matched: 1  Changed: 0  Warnings: 0                 |                                                        |
|                                                          | update row_lock set text = 'third' where id = 1;|
|                                                          | result: waiting...                                     |
| commit;                                                  |                                                        |
| Query OK, 0 rows affected (0.00 sec)                     |                                                        |
|                                                          | Query OK, 0 rows affected (4.94 sec[waiting time])     |
|                                                          | commit;                                                |
|                                                          | Query OK, 0 rows affected (0.00 sec)                   |