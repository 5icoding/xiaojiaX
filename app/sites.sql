create table blogs (
    id int(11)  PRIMARY KEY AUTO_INCREMENT,
    author varchar(30) not null,
    title varchar(50),    
    content text not null,
    createTime datetime not null default now()
);

