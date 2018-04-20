## MySQL基本用法
```
数据库的CRUD表示create,drop,update,select分别表示：创建，删除，更新，查找
SQL: Structured Query Language 
-- DDL: Data Definition Languag (create / drop / alter)
-- DML: (insert / delete / update)
-- DQL: (select)
-- DCL: (grant / revoke)
```
##### 例：创建一个表格
```
drop database if exists company;  -- 删除数据库（慎用）
create database company default charset utf8;  -- （创建数据库）

-- 切换到company数据库
use company;

-- 创建部门表（一个部门，一个员工）
-- 能够唯一确定一条记录的列可以设置为主键
drop table if exists tb_dept;  -- 删除

create table tb_dept  -- 创建
(
deptno integer not null comment '部门编号',  -- 部门列表，数字，不能为空
dname varchar(10) not null comment '名称',  -- 部门名称，变长参数（1到20个字符），不能为空
dloc varchar (10) comment '所在地',  -- 没加not null 变长参数表示0到10个字符
primary key (deptno)  
);

alter table tb_dept add ddate date comment '成立日期';  -- 修改

-- 向部门添加数据
insert into tb_dept values (10, '财务部', '成都', now());
insert into tb_dept values (20, '研发部', null, null);
insert into tb_dept (deptno, dname) values (30, '销售1部'), (40, '销售2部'), (50, '销售3部');

-- 删除数据（注意：一定要带条件）
delete from tb_dept where deptno=50;

-- 修改数据（
update tb_dept set dloc='深圳', ddate='2018-4-1' where deptno=30;

-- 查询
select * from tb_dept;  -- 查询所有行和列
select deptno, dname from tb_dept;  -- 查询指定列（投影
select deptno as 部门编号, dname as 部门名称 from tb_dept; -- 别名
select deptno, dname from tb_dept where dloc='深圳'; -- 筛选
```


### 部分MySQL命令
(以下均用company表示创建的数据库名字，student表示表单名字。）

启动数据库（管理员身份运行cmd）
```
net start mysql57
```
进入数据库
```
mysql -u root -p; 
```
创建数据库命令
```
create database company default charset utf8;
```
删除数据库命令（慎用）
```
drop database if exists company;
```
切换到company数据库命令
```
use company;
```
查看数据库 / 表单目录
```
show database / tables;
```
查看表单说明
```
desc student; 
```
创建student表单
```
create table student(id int auto_increment, s_name varchar(30) not null,s_addr varchar(60) not null, s_sex varchar(6) not null, s_tel int(11), s_yuwen int(3), s_shuxue int(3), s_create_time varchar(10) not null,g_id int, primary key(id),foreign key(g_id) references grade(id));
```
#### 增加
```
insert into student( ) values( );

update student set s_grades=90 where id=2;

```
#### 删除
```
--drop是删除整个数据库 / 表格（慎用），
--删除表里的内容一般使用delete
drop table if exists student;  --删除表格
delete from student where name='xxx';  --删除表格内部内容
```

#### 更改
```
update student set name='xxx' where id=1;
```

#### 查询
```
select * from student where id in(1,2)   --查询第一个或者第二个

select * from student order by(-id);   --按id的倒叙排列

select * from student;   --查找表的所有内容

select * from student where id=1,name='';   --根据id或者那name查找

select * from student limit n;   --查找n行

select * from student limit n offset 1;   --查找2到第n行

select max(s_grades) from student;   --查询最大值

select min(s_grades) from student;   --查询最小值

select avg(s_grades) from student;   --查询平均值

select count(*) as '×××', g.g_name as '×××' from student s join grade g on s.g_id=g.id group by(g.id);  --外键调用：根据g.id查询班级学生个数
```




