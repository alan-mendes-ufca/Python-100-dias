drop database if exists hrs;
create database hrs default charset utf8mb4;

use hrs;

create table tb_dept
(
dno int not null comment 'id',
dname varchar(10) not null comment 'name',
dloc varchar(20) not null comment 'location',
primary key (dno)
);

insert into tb_dept values 
    (10, 'Accounting', 'Beijing'),
    (20, 'R&D', 'Chengdu'),
    (30, 'Sales', 'Chongqing'),
    (40, 'Operations', 'Shenzhen');

create table tb_emp
(
eno int not null comment 'employee id',
ename varchar(20) not null comment 'employee name',
job varchar(20) not null comment 'job title',
mgr int comment 'manager id',
sal int not null comment 'monthly salary',
comm int comment 'monthly allowance',
dno int comment 'department id',
primary key (eno),
foreign key (dno) references tb_dept (dno)
);

-- alterar tabela tb_emp adicionar restrição pk_emp_eno chave primária (eno);
-- alterar tabela tb_emp adicionar restrição uk_emp_ename exclusivo (ename);
-- alterar tabela tb_emp adicionar restrição fk_emp_mgr referências de chave estrangeira (mgr) tb_emp (eno);
-- alterar tabela tb_emp adicionar restrição fk_emp_dno referências de chave estrangeira (dno) tb_dept (dno);

insert into tb_emp values 
    (7800, 'Zhang Sanfeng', 'President', null, 9000, 1200, 20),
    (2056, 'Qiao Feng', 'Analyst', 7800, 5000, 1500, 20),
    (3088, 'Li Mochou', 'Designer', 2056, 3500, 800, 20),
    (3211, 'Zhang Wuji', 'Programmer', 2056, 3200, null, 20),
    (3233, 'Qiu Chuji', 'Programmer', 2056, 3400, null, 20),
    (3251, 'Zhang Cuishan', 'Programmer', 2056, 4000, null, 20),
    (5566, 'Song Yuanqiao', 'Accountant', 7800, 4000, 1000, 10),
    (5234, 'Guo Jing', 'Cashier', 5566, 2000, null, 10),
    (3344, 'Huang Rong', 'Sales Manager', 7800, 3000, 800, 30),
    (1359, 'Hu Yidao', 'Sales Representative', 3344, 1800, 200, 30),
    (4466, 'Miao Renfeng', 'Sales Representative', 3344, 2500, null, 30),
    (3244, 'Ouyang Feng', 'Programmer', 3088, 3200, null, 20),
    (3577, 'Yang Guo', 'Accountant', 5566, 2200, null, 10),
    (3588, 'Zhu Jiuzhen', 'Accountant', 5566, 2500, null, 10);


-- Consulte o nome e o salário mensal do funcionário mais bem pago
select ename, sal from tb_emp where sal=(select max(sal) from tb_emp);

select ename, sal from tb_emp where sal>=all(select sal from tb_emp);

-- Consultar nomes de funcionários e remuneração anual ((salário mensal + abono) * 13)
select ename, (sal+ifnull(comm,0))*13 as ann_sal from tb_emp order by ann_sal desc;

-- Consultar IDs de departamento e número de funcionários para departamentos que possuem funcionários
select dno, count(*) as total from tb_emp group by dno;

-- Consulte os nomes e números de funcionários de todos os departamentos
select dname, ifnull(total,0) as total from tb_dept left join 
(select dno, count(*) as total from tb_emp group by dno) tb_temp 
on tb_dept.dno=tb_temp.dno;

-- Consultar o nome e o salário mensal do funcionário mais bem pago, excluindo o chefe
select ename, sal from tb_emp where sal=(
	select max(sal) from tb_emp where mgr is not null
);

-- Consultar o nome e o salário mensal do funcionário com o segundo maior salário
select ename, sal from tb_emp where sal=(
	select distinct sal from tb_emp order by sal desc limit 1,1
);

select ename, sal from tb_emp where sal=(
	select max(sal) from tb_emp where sal<(select max(sal) from tb_emp)
);

-- Consultar nomes e salários mensais de funcionários que ganham acima da média salarial
select ename, sal from tb_emp where sal>(select avg(sal) from tb_emp);

-- Consulte funcionários cujo salário está acima da média do departamento, com nome, ID do departamento e salário
select ename, t1.dno, sal from tb_emp t1 inner join 
(select dno, avg(sal) as avg_sal from tb_emp group by dno) t2
on t1.dno=t2.dno and sal>avg_sal;

-- Consulte a pessoa mais bem paga em cada departamento com nome, salário e nome do departamento
select ename, sal, dname 
from tb_emp t1, tb_dept t2, (
	select dno, max(sal) as max_sal from tb_emp group by dno
) t3 where t1.dno=t2.dno and t1.dno=t3.dno and sal=max_sal;

-- Consulte os nomes e cargos dos gerentes
-- Dica: evite o uso excessivo de in/not in e distinto
-- Você pode usar verificações de existência (existe/não existe) em vez de definir operações e desduplicação
select ename, job from tb_emp where eno in (
	select distinct mgr from tb_emp where mgr is not null
);

select ename, job from tb_emp where eno=any(
	select distinct mgr from tb_emp where mgr is not null
);

select ename, job from tb_emp t1 where exists (
	select 'x' from tb_emp t2 where t1.eno=t2.mgr
);

-- MySQL 8 fornece funções de janela: row_number()/rank()/dense_rank()
-- Consulte a classificação, nome e salário mensal dos funcionários classificados de 4º a 6º por salário
select ename, sal from tb_emp order by sal desc limit 3,3;

select row_num, ename, sal from 
(select @a:=@a+1 as row_num, ename, sal 
from tb_emp, (select @a:=0) t1 order by sal desc) t2 
where row_num between 4 and 6;

-- As funções de janela são mais adequadas para análises offline do que bancos de dados de negócios transacionais
select 
	ename, sal, 
	row_number() over (order by sal desc) as row_num,
    rank() over (order by sal desc) as ranking,
    dense_rank() over (order by sal desc) as dense_ranking
from tb_emp limit 3 offset 3;

select ename, sal, ranking from (
	select ename, sal, dense_rank() over (order by sal desc) as ranking from tb_emp
) tb_temp where ranking between 4 and 6;

-- As funções de janela são usadas principalmente para resolver problemas de consulta Top-N
-- Consulte os dois maiores ganhadores em cada departamento com nome, salário e ID do departamento
select ename, sal, dno from (
	select ename, sal, dno, rank() over (partition by dno order by sal desc) as ranking
	from tb_emp
) tb_temp where ranking<=2;

select ename, sal, dno from tb_emp t1 
where (select count(*) from tb_emp t2 where t1.dno=t2.dno and t2.sal>t1.sal)<2 
order by dno asc, sal desc;
