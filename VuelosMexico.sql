create database VuelosMexico;

use VuelosMexico;

create table aerolineas(
id_aerolinea int primary key,
nombre_aerolinea varchar(20)
);

create table aeropuertos(
id_aeropuerto int primary key,
nombre_aeropuerto varchar(20)
);

create table movimientos(
id_movimiento int primary key,
descripcion varchar(20)
);


create table vuelos(
id_aerolinea int,
id_aeropuerto int,
id_movimiento int,
dia datetime,
foreign key (id_aerolinea) references aerolineas(id_aerolinea),
foreign key (id_aeropuerto) references aeropuertos(id_aeropuerto),
foreign key (id_movimiento) references movimientos(id_movimiento)

);

insert into aeropuertos values(1,'benito juarez')
insert into aeropuertos values(2,'guanajuato')
insert into aeropuertos values(3,'la paz')
insert into aeropuertos values(4,'oaxaca')


insert into aerolineas values(1,'volaris')
insert into aerolineas values(2,'aeromar')
insert into aerolineas values(3,'interjet')
insert into aerolineas values(4,'aeromexico')

insert into movimientos values(1,'salida')
insert into movimientos values(2,'llegada')


insert into vuelos values(1,1,1,'2021-05-02')
insert into vuelos values(2,1,1,'2021-05-02')
insert into vuelos values(3,2,2,'2021-05-02')
insert into vuelos values(4,3,2,'2021-05-02')
insert into vuelos values(1,3,2,'2021-05-02')
insert into vuelos values(2,1,1,'2021-05-02')
insert into vuelos values(2,3,1,'2021-05-04')
insert into vuelos values(3,4,1,'2021-05-04')
insert into vuelos values(2,3,1,'2021-05-04')


select * from aerolineas;
select * from aeropuertos;
select * from movimientos;
select * from vuelos;

--¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?--
select a.nombre_aeropuerto, count(v.id_movimiento)'MovimientoVuelos' from aeropuertos a
inner join vuelos v
on a.id_aeropuerto = v.id_aeropuerto
group by a.nombre_aeropuerto
order by MovimientoVuelos desc;
--¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año?--
select a.nombre_aerolinea, count(v.id_movimiento)'MovimientoAerolinea' from aerolineas a
inner join vuelos v
on a.id_aerolinea = v.id_aerolinea
group by a.nombre_aerolinea
order by MovimientoAerolinea desc;
--¿En qué día se han tenido mayor número de vuelos?--
select dia , count(id_movimiento) 'Vuelos' from vuelos 
group by dia
order by Vuelos desc;
--¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día?--
select a.nombre_aerolinea, count(v.id_movimiento)'MovimientoAerolinea'  from aerolineas a
inner join vuelos v
on a.id_aerolinea = v.id_aerolinea 
group by a.nombre_aerolinea 
having COUNT(v.id_movimiento) > 2;
