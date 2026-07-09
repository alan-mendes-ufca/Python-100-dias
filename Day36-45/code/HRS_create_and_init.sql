-- Crie um banco de dados chamado `hrs`
drop database if exists `hrs`;
create database `hrs` default charset utf8mb4;

-- Mude para o banco de dados `hrs`
use `hrs`;

-- Crie a tabela de departamento
create table `tb_dept`
(
`dno` int not null comment 'id',
`dname` varchar(10) not null comment 'name',
`dloc` varchar(20) not null comment 'location',
primary key (dno)
);

-- Insira quatro departamentos
insert into `tb_dept` values 
    (10, 'Accounting', 'Beijing'),
    (20, 'R&D', 'Chengdu'),
    (30, 'Sales', 'Chongqing'),
    (40, 'Operations', 'Shenzhen');

-- Crie a tabela de funcionários
create table `tb_emp`
(
`eno` int not null comment 'employee id',
`ename` varchar(20) not null comment 'employee name',
`job` varchar(20) not null comment 'job title',
`mgr` int comment 'manager id',
`sal` int not null comment 'monthly salary',
`comm` int comment 'monthly allowance',
`dno` int comment 'department id',
primary key (eno),
constraint `fk_emp_mgr` foreign key (`mgr`) references tb_emp (`eno`),
constraint `fk_emp_dno` foreign key (`dno`) references tb_dept (`dno`)
);

-- Inserir quatorze funcionários
insert into `tb_emp` values 
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


-- Consultar o nome e salário do funcionário com maior salário mensal

-- Consultar nomes de funcionários e salário anual (salário anual = (sal + comm) * 13)

-- Consultar IDs de departamento e número de funcionários para departamentos que possuem funcionários

-- Consulte todos os nomes de departamentos e número de funcionários

-- Consultar funcionários cujo salário mensal excede o salário médio

-- Consultar funcionários cujo salário mensal excede a média do departamento

-- Consulte o funcionário mais bem pago em cada departamento

-- Consultar nomes de gerentes e cargos

-- Consulte a posição, o nome e o salário dos funcionários classificados de 4 a 6 por salário

-- Consulte os dois principais salários de cada departamento
