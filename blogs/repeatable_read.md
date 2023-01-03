1. set transaction level to repeatable read.
2. create table in mysql and postgresql.
create table repeatable_read (id integer primary key,text varchar(200));

3. insert a new data in repeatable_read;
insert into repeatable_read values(1,'first');

4. mysql 
    | session 1 | session 2 |
    | --- | --- |
    | insert into repeatable_read values(1,'first');           |                                                        |
    |                                                          | select * from repeatable_read; result:(1,'first')      |
    | start transaction;                                       |                                                        |
    |                                                          | start transaction;                                     |
    | update repeatable_read set text = 'second' where id = 1; |                                                        |
    | select * from repeatable_read; result:(1,'second')       | select * from repeatable_read; result:(1,'first')      |
    | commit;                                                  |                                                        |
    |                                                          | update repeatable_read set text = 'third' where id = 1;|
    | select * from repeatable_read; result:(1,'second')       | select * from repeatable_read; result:(1,'third')      |
    |                                                          | commit;                                                |
    | select * from repeatable_read; result:(1,'third')        | select * from repeatable_read; result:(1,'third')      |

5. postgresql
    | session 1 | session 2 |
    | --- | --- |
    | insert into repeatable_read values(1,'first');           |                                                        |
    |                                                          | select * from repeatable_read; result:(1,'first')      |
    | begin;                                                   |                                                        |
    |                                                          | begin;                                                 |
    | update repeatable_read set text = 'second' where id = 1; |                                                        |
    | select * from repeatable_read; result:(1,'second')       | select * from repeatable_read; result:(1,'first')      |
    | commit;                                                  |                                                        |
    |                                                          | update repeatable_read set text = 'third' where id = 1; result: (ERROR:  could not serialize access due to concurrent update)|
    |                                                          | update repeatable_read set text = 'third' where id = 1; result: (ERROR:  current transaction is aborted, commands ignored until end of transaction block)|
    | select * from repeatable_read; result:(1,'second')       | select * from repeatable_read; result:(ERROR:  current transaction is aborted, commands ignored until end of transaction block)      |
    |                                                          | commit; result: (ROLLBACK)                             |
    | select * from repeatable_read; result:(1,'second')       | select * from repeatable_read; result:(1,'second')     |


- [UNDERSTANDING MYSQL ISOLATION LEVELS: REPEATABLE-READ](https://blog.pythian.com/understanding-mysql-isolation-levels-repeatable-read/)