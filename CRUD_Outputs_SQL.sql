use phonebook_records;
create table phone_records(Name varchar(50),Email varchar(50),Phone1 varchar(20),Phone2 varchar(20));
insert into phone_records(Name,Email,Phone1,Phone2)values('Test','test@test.xtyz','1234456','1233233');
select* from phone_records;
UPDATE phone_records SET Phone1 = '9568738833'WHERE Name = 'Test';
delete from phone_records where Name = "Test"
drop table phone_records;

