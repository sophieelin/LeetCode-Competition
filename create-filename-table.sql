-- create table to keep track of uploaded profile pictures
-- (image bytes are stored in the database so the app can run on hosts
-- without a writable filesystem, like Vercel)
drop table if exists picfile;
create table picfile (
    pid int primary key,
    filename varchar(50),
    mimetype varchar(50),
    data mediumblob,
    foreign key (pid) references person(pid) 
        on delete cascade on update cascade
);
