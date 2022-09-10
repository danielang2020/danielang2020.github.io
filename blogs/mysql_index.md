create table cast_info
(
    id             bigint not null
        primary key,
    movie_id       bigint,
    role_id        bigint,
    nr_order       bigint,
    person_id      bigint,
    person_role_id bigint
);

explain select person_id, person_role_id from cast_info where movie_id = 91280 and role_id = 1 order by nr_order asc;

+--+-----------+---------+----------+----+-------------+----+-------+----+----+--------+---------------------------+
|id|select_type|table    |partitions|type|possible_keys|key |key_len|ref |rows|filtered|Extra                      |
+--+-----------+---------+----------+----+-------------+----+-------+----+----+--------+---------------------------+
|1 |SIMPLE     |cast_info|null      |ALL |null         |null|null   |null|1   |100     |Using where; Using filesort|
+--+-----------+---------+----------+----+-------------+----+-------+----+----+--------+---------------------------+

create index two_column on cast_info(movie_id,role_id);
+--+-----------+---------+----------+----+-------------+----------+-------+-----------+----+--------+--------------+
|id|select_type|table    |partitions|type|possible_keys|key       |key_len|ref        |rows|filtered|Extra         |
+--+-----------+---------+----------+----+-------------+----------+-------+-----------+----+--------+--------------+
|1 |SIMPLE     |cast_info|null      |ref |two_column   |two_column|18     |const,const|1   |100     |Using filesort|
+--+-----------+---------+----------+----+-------------+----------+-------+-----------+----+--------+--------------+

drop index two_column on cast_info;
create index three_column on cast_info(movie_id,role_id,nr_order);
+--+-----------+---------+----------+----+-------------+------------+-------+-----------+----+--------+-----+
|id|select_type|table    |partitions|type|possible_keys|key         |key_len|ref        |rows|filtered|Extra|
+--+-----------+---------+----------+----+-------------+------------+-------+-----------+----+--------+-----+
|1 |SIMPLE     |cast_info|null      |ref |three_column |three_column|18     |const,const|1   |100     |null |
+--+-----------+---------+----------+----+-------------+------------+-------+-----------+----+--------+-----+

drop index three_column on cast_info;
create index four_column on cast_info(movie_id,role_id,nr_order,person_id,person_role_id);
+--+-----------+---------+----------+----+-------------+-----------+-------+-----------+----+--------+-----------+
|id|select_type|table    |partitions|type|possible_keys|key        |key_len|ref        |rows|filtered|Extra      |
+--+-----------+---------+----------+----+-------------+-----------+-------+-----------+----+--------+-----------+
|1 |SIMPLE     |cast_info|null      |ref |four_column  |four_column|18     |const,const|1   |100     |Using index|
+--+-----------+---------+----------+----+-------------+-----------+-------+-----------+----+--------+-----------+


[How to Design Indexes, Really](https://www.slideshare.net/billkarwin/how-to-design-indexes-really)
