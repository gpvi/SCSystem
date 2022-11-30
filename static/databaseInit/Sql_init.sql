CREATE SCHEMA scdb1;

CREATE  TABLE scdb1.`Courses` (
	`Cno`                CHAR(10)  NOT NULL     PRIMARY KEY,
	`Cname`              VARCHAR(100)  NOT NULL     ,
	`Cmaxnum`            INT  NOT NULL     ,
	`Cleftnum`           INT  NOT NULL     ,
	`Credit`             INT  NOT NULL     ,
	`Chours`             INT  NOT NULL
 );

CREATE  TABLE scdb1.`Students` (
	`Sno`                CHAR(9)  NOT NULL     PRIMARY KEY,
	`Sname`              VARCHAR(100)  NOT NULL     ,
	`Ssex`               CHAR(4)   DEFAULT ('none')    ,
	`Sage`               INT  NOT NULL     ,
	email                VARCHAR(50)
 );

CREATE  TABLE scdb1.`Teachers` (
	`Tno`                CHAR(9)  NOT NULL     PRIMARY KEY,
	`Tname`              VARCHAR(100)  NOT NULL     ,
	`Tsex`               CHAR(4)       ,
	email                VARCHAR(50)       ,
	`Tage`               INT
 );

CREATE  TABLE scdb1.admins (
	id                   CHAR(9)  NOT NULL     PRIMARY KEY,
	password             CHAR(8)  NOT NULL
 );

CREATE  TABLE scdb1.entity (
 );

CREATE  TABLE scdb1.sc (
	sno                  CHAR(9)  NOT NULL     PRIMARY KEY,
	cno                  CHAR(10)  NOT NULL     ,
	grade                INT   DEFAULT ('none')
 );

CREATE  TABLE scdb1.tc (
	tno                  CHAR(9)  NOT NULL     ,
	cno                  CHAR(10)  NOT NULL     ,
	`time`               VARCHAR(50)  NOT NULL     ,
	textbook             VARCHAR(250)
 );

CREATE  TABLE scdb1.tlog (
 );

CREATE  TABLE scdb1.users (
	id                   CHAR(9)  NOT NULL     PRIMARY KEY,
	password             CHAR(8)  NOT NULL
 );

ALTER TABLE scdb1.sc ADD CONSTRAINT fk_sc_students FOREIGN KEY ( sno ) REFERENCES scdb1.`Students`( `Sno` ) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE scdb1.sc ADD CONSTRAINT fk_sc_courses FOREIGN KEY ( cno ) REFERENCES scdb1.`Courses`( `Cno` ) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE scdb1.tc ADD CONSTRAINT fk_tc_teachers FOREIGN KEY ( tno ) REFERENCES scdb1.`Teachers`( `Tno` ) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE scdb1.tc ADD CONSTRAINT fk_tc_courses FOREIGN KEY ( cno ) REFERENCES scdb1.`Courses`( `Cno` ) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE scdb1.users ADD CONSTRAINT fk_users_sc FOREIGN KEY ( id ) REFERENCES scdb1.`Students`( `Sno` ) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE VIEW scdb1.dbs_validate_view AS ...;

ALTER TABLE scdb1.`Courses` COMMENT '课程表';

ALTER TABLE scdb1.`Courses` MODIFY `Cno` CHAR(10)  NOT NULL   COMMENT '课程号';

ALTER TABLE scdb1.`Courses` MODIFY `Cname` VARCHAR(100)  NOT NULL   COMMENT '课程名';

ALTER TABLE scdb1.`Courses` MODIFY `Cmaxnum` INT  NOT NULL   COMMENT '最大选课人数';

ALTER TABLE scdb1.`Courses` MODIFY `Cleftnum` INT  NOT NULL   COMMENT '剩余人数';

ALTER TABLE scdb1.`Courses` MODIFY `Credit` INT  NOT NULL   COMMENT '学分';

ALTER TABLE scdb1.`Courses` MODIFY `Chours` INT  NOT NULL   COMMENT '课时';

ALTER TABLE scdb1.`Students` COMMENT '学生表';

ALTER TABLE scdb1.`Students` MODIFY `Sno` CHAR(9)  NOT NULL   COMMENT '学号';

ALTER TABLE scdb1.`Students` MODIFY `Sname` VARCHAR(100)  NOT NULL   COMMENT '姓名';

ALTER TABLE scdb1.`Students` MODIFY `Ssex` CHAR(4)   DEFAULT ('none')  COMMENT '性别';

ALTER TABLE scdb1.`Students` MODIFY `Sage` INT  NOT NULL   COMMENT '年龄';

ALTER TABLE scdb1.`Students` MODIFY email VARCHAR(50)     COMMENT '邮箱';

ALTER TABLE scdb1.`Teachers` COMMENT '教师表';

ALTER TABLE scdb1.`Teachers` MODIFY `Tno` CHAR(9)  NOT NULL   COMMENT '教师编号';

ALTER TABLE scdb1.`Teachers` MODIFY `Tname` VARCHAR(100)  NOT NULL   COMMENT '姓名';

ALTER TABLE scdb1.`Teachers` MODIFY `Tsex` CHAR(4)     COMMENT '性别';

ALTER TABLE scdb1.`Teachers` MODIFY email VARCHAR(50)     COMMENT '邮箱';

ALTER TABLE scdb1.`Teachers` MODIFY `Tage` INT     COMMENT '年龄';

ALTER TABLE scdb1.admins COMMENT '管理员';

ALTER TABLE scdb1.sc COMMENT '学生选课表';

ALTER TABLE scdb1.sc MODIFY sno CHAR(9)  NOT NULL   COMMENT '学生学号，参照学生表学号';

ALTER TABLE scdb1.sc MODIFY cno CHAR(10)  NOT NULL   COMMENT '课程号，参照课程表课程号';

ALTER TABLE scdb1.sc MODIFY grade INT   DEFAULT ('none')  COMMENT '学生对应课程成绩';

ALTER TABLE scdb1.tc COMMENT '教师授课表';

ALTER TABLE scdb1.tc MODIFY tno CHAR(9)  NOT NULL   COMMENT '教师号，参照教师表教师编号';

ALTER TABLE scdb1.tc MODIFY cno CHAR(10)  NOT NULL   COMMENT '课程号，参照课程表的课程号';

ALTER TABLE scdb1.tc MODIFY textbook VARCHAR(250)     COMMENT '教材';

ALTER TABLE scdb1.users COMMENT '普通用户';

ALTER TABLE scdb1.users MODIFY id CHAR(9)  NOT NULL   COMMENT '用户ID----学号';

ALTER TABLE scdb1.users MODIFY password CHAR(8)  NOT NULL   COMMENT '密码';