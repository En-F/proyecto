UD 4 - El lenguaje de consultas SQL. DQL


--1
SELECT
   codcliente AS "Código",
   nomcliente AS "Nombre",
   ap1cliente AS "Primer Apellido",
   ap2cliente AS "Segundo Apellido"
FROM cliente 
ORDER BY  ap1cliente ,ap2cliente ,nomcliente ;
--2
SELECT
   codcliente AS "Código",
   concat_ws(' ',nomcliente,ap1cliente,ap2cliente)
FROM cliente 
ORDER BY ap1cliente DESC ;
--3
SELECT
   codcliente AS "Código",
   nomcliente AS "Nombre",
   ap1cliente AS "Primer apellido",
   ap2cliente AS "Segundo apellido"
FROM cliente
WHERE credito > 1000::money
ORDER BY  ap1cliente ,ap2cliente ,nomcliente ;
--4
SELECT
   codoficina AS "Código",
   ciudad AS "Ciudad",
   objetivo AS "Objetivo"
FROM oficina a
WHERE
   (upper(ciudad) = 'SANLÚCAR')
or 
   (upper(ciudad) ='CHIPIONA')
OR
   (upper(ciudad) = 'ROTA');
--5
SELECT
   ciudad
FROM oficina
WHERE ciudad LIKE '%c%'
ORDER BY ciudad ;
--6
SELECT
   v.codvendedor AS "Codigo",
   v.ap1vendedor AS "Primer apeliido",
   v.ap2vendedor AS "Segundo apellido",
   v.nomvendedor AS "Nombre",
   a.ciudad AS "Ciudad"
FROM vendedor v JOIN oficina a ON v.codoficina = a.codoficina
ORDER BY ciudad ,v.ap1vendedor, v.ap2vendedor,v.nomvendedor ;
--7
SELECT
   v.codvendedor AS "Codigo",
   v.ap1vendedor AS "Primer apellido",
   v.ap2vendedor AS "Segundo apellido",
   v.nomvendedor AS "Nombre"
FROM vendedor v LEFT JOIN oficina o using(codoficina)
WHERE upper(ciudad) = 'SANLÚCAR'
ORDER BY v.ap1vendedor , v.ap2vendedor ,v.nomvendedor ;
--8
SELECT
   C.codcliente AS "Cósigo",
   c.nomcliente AS "NOmbre",
   c.ap1cliente AS "Primer apellido",
   c.ap2cliente AS "Segundo apellido",
   extract(YEAR FROM age(fnacimiento)) AS "Edad"
FROM cliente c
ORDER BY  ap1cliente ,ap2cliente ,nomcliente;
--9
SELECT
count(DISTINCT codarticulo)AS "Num Productos"
FROM articulo a ;
--10
SELECT
   DISTINCT ciudad AS "Ciudad"
FROM cliente 
ORDER BY ciudad DESC ;
--11
SELECT
    count(DISTINCT ciudad) AS "Num Ciudades"
FROM cliente  ;
--12
SELECT
   numfactura AS "Num Factura",
   fecha AS "Fecha",
   d.codarticulo AS "Cod Articulo",
   d.cantidad AS "Cantidad"
FROM factura  f JOIN detalle d using(numfactura)
WHERE numfactura  = 8;
--13
SELECT
   numfactura AS "Num Factura",
   fecha AS "Fecha",
   d.codarticulo AS "Cod Articulo",
   a.nomarticulo AS "Articulo",
   a.precio AS "Precio",
   d.cantidad AS "Cantidad"
FROM factura  f JOIN   detalle d using(numfactura)
JOIN articulo a using(codarticulo)
WHERE  d.numfactura = 8
ORDER BY nomarticulo ;
--14
SELECT
   numfactura AS "Num Factura",
   fecha AS "Fecha",
   d.codarticulo AS "Cod Articulo",
   a.nomarticulo AS "Articulo",
   a.precio AS "Precio",
   d.cantidad AS "Cantidad",
   (d.cantidad * a.precio)AS "Precio Total"
FROM factura  f JOIN   detalle d using(numfactura)
JOIN articulo a using(codarticulo)
WHERE  d.numfactura = 8
ORDER BY nomarticulo ;
--15
SELECT
   codarticulo AS "Codigo articulo",
   nomarticulo  AS "Nombre",
   precio AS "precio"
FROM articulo 
WHERE  precio = (SELECT max(precio)FROM articulo);
--16
SELECT
   codarticulo AS "Codigo articulo",
   nomarticulo  AS "Nombre",
   precio AS "precio"
FROM articulo 
WHERE  precio = (SELECT max(precio)FROM articulo)
or precio = (SELECT min(precio)FROM articulo)
ORDER BY nomarticulo ;
--17
select
   codarticulo as "Código",
   nomarticulo as "Articulo"
from articulo join detalle using (codarticulo)
join factura using (numfactura)
   where codcliente = 5
INTERSECT
select
   codarticulo as "Código",
   nomarticulo as "Articulo"
from articulo join detalle using (codarticulo)
   join factura using (numfactura)
   where codcliente = 8;
--18
SELECT
   c.codcliente AS "Codigo",
   c.ap1cliente AS "Primer apellido",
   c.ap2cliente AS "Segundo apellido",
   c.nomcliente AS "Nombre",
   count(numfactura)  AS "Num compras"
FROM cliente c LEFT JOIN factura f using(codcliente)
GROUP BY codcliente
ORDER BY "Num compras" DESC ,c.ap1cliente,c.ap2cliente,c.nomcliente;
--19
SELECT
   c.codcliente AS "Codigo",
   c.ap1cliente AS "Primer apellido",
   c.ap2cliente AS "Segundo apellido",
   c.nomcliente AS "Nombre",
   count(numfactura)  AS "Num compras"
FROM cliente c LEFT JOIN factura f using(codcliente)
GROUP BY codcliente
ORDER BY "Num compras" DESC ,c.ap1cliente,c.ap2cliente,c.nomcliente LIMIT 5 OFFSET 5;
--20
SELECT
   v.codvendedor AS "Codigo",
   v.ap1vendedor AS "Primer apellido",
   v.ap2vendedor AS "Segundo apellido",
   v.nomvendedor AS "Nombre",
   count(numfactura)  AS "Num compras"
FROM vendedor v  LEFT JOIN factura f using(codvendedor)
GROUP BY codvendedor
ORDER BY "Num compras"desc;
--21
select
   codvendedor AS "Código",
   ap1vendedor AS "Primer Apellido", ap2vendedor AS "Segundo Apellido" , nomvendedor AS "Nombre", count(numfactura) as "Num Ventas"
FROM vendedor join factura using (codvendedor)
group by codvendedor HAVING COUNT(numfactura) = (
   SELECT MIN(ventas) FROM (
       SELECT COUNT(numfactura) AS ventas
       FROM vendedor
       JOIN factura USING (codvendedor)
       GROUP BY codvendedor
   ) as "Subconsulta");


--22
select codvendedor AS "Código", ap1vendedor AS "Primer Apellido", ap2vendedor AS "Segundo Apellido" , nomvendedor AS "Nombre", count(numfactura) as "Num Ventas"
FROM vendedor left join factura using (codvendedor)
group by codvendedor HAVING COUNT(numfactura) = (
   SELECT MIN(ventas) FROM (
       SELECT COUNT(numfactura) AS ventas
       FROM vendedor
       left JOIN factura USING (codvendedor)
       GROUP BY codvendedor
   ) as "Subconsulta");
UD04-09 - El lenguaje de consultas - DQL - Restricciones en la salida - Operadores de unión
--1
SELECT
   i.cod_investigador AS "Codigo",
   i.nombre AS "Nombre"
FROM investigador i
JOIN asignado_a aa ON i.cod_investigador = aa.cod_investigador
JOIN proyecto p ON aa.cod_proyecto = p.cod_proyecto
WHERE p.nombre = 'Jedi'
INTERSECT
SELECT
   i.cod_investigador AS "Codigo",
   i.nombre AS "Nombre"
FROM investigador i
JOIN asignado_a aa using(cod_investigador)
JOIN proyecto p using(cod_proyecto)
WHERE p.nombre = 'Lion';


--2
SELECT
   i.cod_investigador AS "Codigo",
   i.nombre AS "Nombre"
FROM investigador i
JOIN asignado_a aa ON i.cod_investigador = aa.cod_investigador
JOIN proyecto p ON aa.cod_proyecto = p.cod_proyecto
WHERE p.nombre = 'Jedi'
AND i.cod_investigador IN (
   SELECT
   	i2.cod_investigador
   FROM investigador i2
   JOIN asignado_a aa2  using(cod_investigador)
   JOIN proyecto p2 using(cod_proyecto)   
   WHERE p2.nombre = 'Lion'
);


--3
SELECT
	i.cod_investigador AS "Id",
	i.nombre AS "Nombre"
FROM investigador i JOIN asignado_a aa using (cod_investigador)
JOIN proyecto p USING(cod_proyecto)
JOIN plan p2 using(cod_plan)
WHERE p2.nombre = 'Profundiza'
AND aa.cod_investigador NOT IN
(SELECT i2.cod_investigador AS "Id"
	FROM investigador i2 JOIN asignado_a aa2 using (cod_investigador)
	JOIN proyecto p2 USING(cod_proyecto)
	JOIN plan p3 using(cod_plan)
	WHERE p3.nombre = 'Avanza'
);


--4
SELECT
	i.cod_investigador AS "Id",
	i.nombre AS "Nombre"
FROM investigador i JOIN asignado_a aa using (cod_investigador)
JOIN proyecto p USING(cod_proyecto)
JOIN plan p2 using(cod_plan)
WHERE p2.nombre = 'Profundiza'
AND aa.cod_investigador NOT IN
(SELECT i2.cod_investigador AS "Id"
	FROM investigador i2 JOIN asignado_a aa2 using (cod_investigador)
	JOIN proyecto p2 USING(cod_proyecto)
	JOIN plan p3 using(cod_plan)
	WHERE p3.nombre = 'Avanza')
ORDER BY i.cod_investigador
LIMIT 3 OFFSET 3;

Cuaderno de Actividades Archivo (Actividad 2 (Factura))

--1
SELECT DISTINCT
   c.ciudad AS "Ciudad",
   COUNT(c.codcliente) AS "Numero Clientes"
FROM
   cliente c
GROUP BY
   c.ciudad
ORDER BY
   "Numero Clientes" DESC;
--2
SELECT
   c.ciudad AS "Ciudad",
   COUNT(c.codcliente) AS "Numero Clientes"
FROM
   cliente c
GROUP BY
   c.ciudad
HAVING
   COUNT(c.codcliente) > 2
ORDER BY
   "Numero Clientes" DESC;
--3
SELECT
	a.codarticulo  AS "Codigo",
	a.nomarticulo  AS "Articulo",
	a.precio AS "Precio"
FROM articulo a
WHERE precio = (SELECT min(precio) FROM articulo)
ORDER BY a.nomarticulo ASC  ;
--4
SELECT
   a.codarticulo  AS "Codigo",
   a.nomarticulo  AS "Articulo",
   a.precio AS "Precio"
FROM
   articulo a
WHERE
   precio::numeric < (SELECT AVG(a2.precio::numeric) FROM articulo a2) 
ORDER BY
   a.precio DESC, 
   a.nomarticulo ASC;
--5
SELECT
   FLOOR(a.precio::numeric) AS "Grupo Precio", 
   COUNT(*) AS "Núm Articulos"         
FROM
   articulo a
GROUP BY
   FLOOR(a.precio::numeric)                     
ORDER BY
   "Grupo Precio" DESC;                
--6
SELECT
   c.codcliente AS "Código",
   c.nomcliente AS "Cliente",
   COUNT(f.numfactura) AS "Num Compras"
FROM
   cliente c
LEFT JOIN
   factura f ON c.codcliente = f.codcliente
   AND EXTRACT(YEAR FROM f.fecha) = 2020 
GROUP BY
   c.codcliente
ORDER BY
    "Num Compras" DESC, c.nomcliente ASC;
--7
SELECT
   c.codcliente AS "Código",
   c.nomcliente AS "Cliente",
   COUNT(f.numfactura) AS "Num Compras"
FROM
   cliente c
LEFT JOIN
   factura f ON c.codcliente = f.codcliente
   AND EXTRACT(YEAR FROM f.fecha) = 2020 
GROUP BY
   c.codcliente
ORDER BY
    "Num Compras" DESC, c.nomcliente ASC
LIMIT 5;
--8
SELECT
   c.codcliente AS "Código",
   c.nomcliente AS "Cliente",
   COUNT(f.numfactura) AS "Num Compras"
FROM
   cliente c
LEFT JOIN
   factura f ON c.codcliente = f.codcliente
   AND EXTRACT(YEAR FROM f.fecha) = 2020 
GROUP BY
   c.codcliente
ORDER BY
    "Num Compras" DESC, c.nomcliente ASC
LIMIT 5 OFFSET 5;
--9
select
	cl.codcliente as "Código",
	nomcliente as "Cliente",
	count(numfactura) as "Num Compras"
from cliente cl  join factura f ON cl.codcliente = f.codcliente
group by cl.codcliente
having count(numfactura) = (select max(ventas) from (
		SELECT COUNT(numfactura) AS ventas
		        FROM cliente
		        left JOIN factura USING (codcliente)
		        GROUP BY codcliente
		) as "Subconsulta")
order by "Cliente" asc;


Cuaderno de Actividades Archivo(Actividad 3 (Planes y Proyectos))
--1
SELECT
   i.cod_investigador AS "Código",
   i.apellido1 AS "Primer Apellido",
   i.apellido2 AS "Segundo Apellido",
   i.nombre AS "Nombre",
   COUNT(p.cod_proyecto) AS "Num Proyectos"
FROM investigador i
JOIN asignado_a aa ON i.cod_investigador = aa.cod_investigador
JOIN proyecto p ON aa.cod_proyecto = p.cod_proyecto
GROUP BY
   i.cod_investigador
HAVING
   COUNT(p.cod_proyecto) = (
       SELECT MAX("Cantidad de Proyecto")
       FROM (
           SELECT COUNT(p2.cod_proyecto) AS "Cantidad de Proyecto"
           FROM investigador i2
           JOIN asignado_a aa2 ON i2.cod_investigador = aa2.cod_investigador
           JOIN proyecto p2 ON aa2.cod_proyecto = p2.cod_proyecto
           GROUP BY i2.cod_investigador
       ) AS "Maximos Proyectos"
   )
ORDER BY
   i.apellido1 ASC, i.apellido2 ASC, i.nombre ASC;
--2
SELECT
   i.cod_investigador AS "Código",
   i.apellido1 AS "Primer Apellido",
   i.apellido2 AS "Segundo Apellido",
   i.nombre AS "Nombre"
FROM investigador i
JOIN asignado_a aa ON i.cod_investigador = aa.cod_investigador
JOIN proyecto p ON aa.cod_proyecto = p.cod_proyecto
GROUP BY
   i.cod_investigador,p.fecha_inicio ,p.fecha_fin
HAVING AGE(p.fecha_fin, p.fecha_inicio) = (
   SELECT MAX(AGE(p.fecha_fin, p.fecha_inicio))
   FROM proyecto p
)
ORDER BY i.apellido1, i.apellido2, i.nombre;

--3
SELECT
   e.cod_entidad AS "Codigo",
   e.entidad AS "Nombre",
   to_char(sum(p2.presupuesto), 'LS9999999G999G999D00') AS "Presupuesto"
FROM entidad e
JOIN plan p ON p.cod_ent_financiera = e.cod_entidad
JOIN proyecto p2 ON p2.cod_plan = p.cod_plan
GROUP BY e.cod_entidad
ORDER BY "Presupuesto" DESC ;

--4
SELECT
   i.cod_investigador  AS "Código Investigador",
   i.apellido1 AS "Primer Apellido",
   i.apellido2  AS "Segundo Apellido",
   i.nombre AS "Nombre",
   p.cod_proyecto AS "Cod Proyecto",
   p.nombre AS "Nombre Proyecto"
FROM proyecto p JOIN asignado_a aa using(cod_proyecto)
JOIN investigador i using(cod_investigador)
group by i.cod_investigador, p.cod_proyecto, aa.fecha_fin, aa.fecha_inicio having p.fecha_fin < aa.fecha_fin or p.fecha_inicio > aa.fecha_inicio
ORDER BY i.apellido1 ASC, i.apellido2 ASC , i.nombre asc;


--5
SELECT
	p.cod_proyecto AS "Cod Proyecto",
	p.nombre AS "Proyecto",
	count(r.rol ) AS "Num Becarios"
FROM proyecto p JOIN asignado_a aa  ON p.cod_proyecto =aa.cod_proyecto
JOIN rol r ON aa.cod_rol = r.cod_rol
WHERE
   UPPER(r.rol) = 'BECARIO'
GROUP BY
   p.cod_proyecto
HAVING count(r.rol ) = (
	SELECT max("Cantidad Becarios")
	FROM (
		SELECT count(r2.rol ) AS "Cantidad Becarios"
		FROM proyecto p2 JOIN asignado_a aa2  ON p2.cod_proyecto =aa2.cod_proyecto
		JOIN rol r2 ON aa2.cod_rol = r2.cod_rol
		WHERE UPPER(r2.rol) = 'BECARIO'
		GROUP BY p2.cod_proyecto
		) AS "Maximo Becario"
)
ORDER BY p.nombre;

--6
SELECT
	p.cod_proyecto AS "Cod Proyecto",
	p.nombre AS "Proyecto",
	count(DISTINCT r.rol ) AS "Num roles"
FROM proyecto p JOIN asignado_a aa  ON p.cod_proyecto =aa.cod_proyecto
JOIN rol r ON aa.cod_rol = r.cod_rol
GROUP BY p.cod_proyecto
HAVING count(DISTINCT r.rol ) = (SELECT max("Cantidad Participantes")
FROM (SELECT  count(DISTINCT r2.rol ) AS "Cantidad Participantes"
	FROM proyecto p2 JOIN asignado_a aa2  ON p2.cod_proyecto =aa2.cod_proyecto
	JOIN rol r2 ON aa2.cod_rol = r2.cod_rol
	GROUP BY p2.cod_proyecto
	) AS "Maximo Participante"
);




--investigadores  que no trabajan en ningun proyecto, para trabajarlo bien 3 formas diferentes(left,sub,corr)
select *
from investigador i left join asignado_a aa using(cod_investigador)
where aa.cod_proyecto is null;
  
select *
from investigador
where cod_investigador not in
   (
   select  distinct aa.cod_investigador
   from asignado_a aa
   );
select *
from investigador i
where  not exists
(select aa.cod_investigador
from asignado_a aa
where cod_investigador = i.cod_investigador
);

select *
from investigador i left outer  join asignado_a aa using(cod_investigador);


--planaes que no tiene proyecto;
select *
from plan p LEFT  join proyecto p2 using(cod_plan)
where p2.cod_proyecto is null ;
select  *
from plan
where cod_plan not in
(
   select cod_plan
   from proyecto
);
select *
from plan p
where not exists
   (
   select cod_plan
   from proyecto
   where cod_plan = p.cod_plan
);
--empledos que ganan mas que la media de su departamento
SELECT *
FROM emple e 
WHERE e.salario::numeric >
   (
   SELECT avg(salario::NUMERIC)
   FROM emple em
   WHERE dept_no = e.dept_no
   GROUP BY e.salario
);
--proyectos con el presupuesto más alto  del plan al que pertenece
SELECT *
FROM proyecto p
WHERE p.presupuesto = (
  SELECT MAX(p2.presupuesto)
  FROM proyecto p2
  WHERE cod_plan = p.cod_plan
);













Cuaderno de Actividades Archivo(Actividad 4 (Departamento – Empleado))
--1
SELECT
	d.dept_no AS "ID",
	d.dnombre AS "Departamento",
	count(e.emp_no) AS "N Empleados"
FROM
depart d JOIN emple e USING(dept_no)
GROUP BY d.dept_no
HAVING count(e.emp_no) = (
	SELECT max("Empleados") FROM
	( SELECT count(e2.emp_no) AS "Empleados"
	FROM
	depart d2 JOIN emple e2 USING(dept_no)
	GROUP BY d2.dept_no
		) AS "Maximo Empleados"
)
ORDER BY d.dnombre ;

--2
SELECT
	d.dept_no AS "ID",
	d.dnombre AS "Departamento",
	count(e.emp_no) AS "N Empleados"
FROM
depart d LEFT JOIN emple e USING(dept_no)
GROUP BY d.dept_no
HAVING count(e.emp_no) = (
	SELECT min("Empleados") FROM
	( SELECT count(e2.emp_no) AS "Empleados"
	FROM
	depart d2 LEFT JOIN emple e2 USING(dept_no)
	GROUP BY d2.dept_no
		) AS "Minimo Empleados"
)
ORDER BY d.dnombre ;













--3
SELECT
  d.dept_no AS "ID",
  d.dnombre AS "Departamento",
  /*En la colocacion de los caracteres para  el formateo no me lo reconoce el € */
  COALESCE(TRIM(to_char(SUM(e.salario::NUMERIC), '9999G999G999D00L')) || '€','0,00€') AS "Tot Salarios"
FROM
  depart d
LEFT JOIN
  emple e USING(dept_no)
GROUP BY
  d.dept_no, d.dnombre
ORDER BY
  COALESCE(SUM(e.salario::NUMERIC), 0) DESC;




--4
SELECT
   e.emp_no AS "ID Emple",
   e.nombre AS "Empleado"
FROM emple e
GROUP BY e.emp_no
HAVING  EXTRACT(YEAR FROM age(CURRENT_DATE, e.fecha_alt)) =
(SELECT max("Años")
FROM (SELECT
   EXTRACT(YEAR FROM age(CURRENT_DATE, e2.fecha_alt)) AS "Años"
   FROM emple e2
   ) AS "Maximo Años"
)
ORDER BY e.nombre ;

--5
SELECT
   e.emp_no AS "ID Dir",
   e.nombre AS "Nombre"
from emple e
group by emp_no having emp_no in
(
select  e.dir from emple e
group by e.dir having count(e.emp_no) = (
   SELECT max("Cantidad empleados")
   FROM (
       SELECT COUNT(e2.emp_no) AS "Cantidad empleados"
       FROM emple e2
       GROUP BY e2.dir
   ) AS "Subconsulta"
));









Cuaderno de Actividades Archivo(Actividad 4 (Departamento – Empleado))


--1
SELECT
	f.numfactura AS "Num Factura",
	f.fecha AS "Fecha",
	sum(d.cantidad*precio) AS "total"
FROM factura f JOIN detalle d using(numfactura)
JOIN articulo USING(codarticulo)
GROUP BY f.numfactura
HAVING  f.numfactura = 8;
--2
SELECT
	c.codcliente AS "ID",
	c.ap1cliente AS "Primer Apellido",
	c.ap2cliente AS "Segundo Apellido",
	c.nomcliente AS "Nombre",
	count(f.numfactura) AS "Compras"
FROM cliente c JOIN factura f using(codcliente)
GROUP BY c.codcliente
HAVING count(f.numfactura) = (SELECT max("Compras") FROM
		(
		SELECT
			c2.codcliente  AS "Compras"
		FROM factura f2 JOIN cliente c2 using(codcliente)
		GROUP BY c2.codcliente,f2.fecha
		HAVING EXTRACT(YEAR FROM f2.fecha )= 2020
		) AS "Subconsulta"
)ORDER BY c.ap1cliente ,c.ap2cliente ,c.nomcliente ;
--2
SELECT
   c.codcliente AS "ID",
   c.ap1cliente AS "Primer Apellido",
   c.ap2cliente AS "Segundo Apellido",
   c.nomcliente AS "Nombre",
   COUNT(f.numfactura) AS "Compras"
FROM cliente c
JOIN factura f ON c.codcliente = f.codcliente
WHERE EXTRACT(YEAR FROM f.fecha) = 2020
GROUP BY c.codcliente
HAVING COUNT(f.numfactura) = (
   SELECT MAX("Num Compras")
   FROM (
       SELECT
           COUNT(f2.numfactura) AS "Num Compras"
       FROM cliente c2
       JOIN factura f2 ON c2.codcliente = f2.codcliente
       WHERE EXTRACT(YEAR FROM f2.fecha) = 2020
       GROUP BY c2.codcliente
   ) AS "Subconsulta"
)
ORDER BY c.ap1cliente, c.ap2cliente, c.nomcliente;
--3
SELECT
	a.codarticulo AS "ID",
	a.nomarticulo AS "Nombre"
FROM articulo a LEFT JOIN detalle d using(codarticulo)
LEFT JOIN factura f ON d.numfactura = f.numfactura
WHERE  f.codvendedor  IS NULL
ORDER BY a.nomarticulo ;
--4
SELECT
	a.codarticulo AS "ID",
	a.nomarticulo AS "Nombre",
	count(a.codarticulo) "Número de veces"
FROM articulo a  JOIN detalle d USING(codarticulo)
GROUP BY a.codarticulo
HAVING count(a.codarticulo) =
(SELECT max("Número de apariciones") FROM
		(SELECT
			count(a2.codarticulo) AS "Número de apariciones"
		FROM
			articulo a2  JOIN detalle d2 USING(codarticulo)
		GROUP BY
			a2.codarticulo) AS "Sub Consulta"
)ORDER BY a.nomarticulo;
--5
SELECT
   a.codarticulo AS "ID",
   a.nomarticulo AS "Nombre",
   sum(d.cantidad) "Número de veces"
FROM articulo a  JOIN detalle d USING(codarticulo)
GROUP BY a.codarticulo
HAVING count(a.codarticulo) =
(SELECT max("Número de apariciones") FROM
       (SELECT
           count(a2.codarticulo) AS "Número de apariciones"
       FROM
           articulo a2  JOIN detalle d2 USING(codarticulo)
       GROUP BY
           a2.codarticulo) AS "Sub Consulta"
)ORDER BY a.nomarticulo;


--6
SELECT
   a.codarticulo AS "ID",
   a.nomarticulo AS "Nombre",
   coalesce(sum(d.cantidad),'0') "Número de veces"
FROM articulo a  left JOIN detalle d USING(codarticulo)
GROUP BY a.codarticulo
order by  coalesce(sum(d.cantidad),'0') desc ;







--7
SELECT DISTINCT
   c.codcliente AS "ID",
   CONCAT_WS('', ap1cliente, c.ap2cliente, ',', c.nomcliente) AS "Cliente",
   c.ap1cliente
FROM cliente c
JOIN factura f USING(codcliente)
JOIN detalle d USING(numfactura)
JOIN articulo a USING(codarticulo)
GROUP BY a.precio, c.codcliente, c.ap1cliente
HAVING a.precio > 20::money
ORDER BY c.ap1cliente DESC;


--8
SELECT DISTINCT
   c.codcliente AS "ID",
   CONCAT_WS('', ap1cliente, c.ap2cliente, ',', c.nomcliente) AS "Cliente",
   c.ap1cliente
FROM cliente c
JOIN factura f on c.codcliente =f.codcliente
JOIN detalle d USING(numfactura)
JOIN articulo a USING(codarticulo)
where extract(year from f.fecha) = 2020
GROUP BY a.precio, c.codcliente, c.ap1cliente
HAVING a.precio > 20::money
ORDER BY c.ap1cliente DESC;

--9
SELECT
	a.codarticulo AS "ID Artículo",
	a.nomarticulo AS "Articulo",
	d.cantidad AS "cantidad",
	a.precio AS "precio",
	sum(d.cantidad * a.precio) AS "Cantidad"
FROM articulo a JOIN detalle d using(codarticulo)
GROUP BY a.codarticulo,d.cantidad,d.numfactura
HAVING d.numfactura = 14
ORDER BY a.nomarticulo ;
--10
SELECT
	d.numfactura AS "ID Factura",
	sum(d.cantidad * a.precio) AS "Total"
FROM articulo a JOIN detalle d using(codarticulo)
GROUP BY d.numfactura
having d.numfactura = 14;
--11
SELECT
	f.numfactura AS "ID Factura",
	f.fecha AS "Fecha",
	sum(d.cantidad *a.precio ) AS "Total"
FROM articulo a JOIN detalle d using(codarticulo)
JOIN factura f ON d.numfactura = f.numfactura
GROUP BY f.numfactura
having EXTRACT(YEAR FROM f.fecha ) = 2020
ORDER BY sum(d.cantidad *a.precio ) desc;
--12
SELECT
   c.codcliente AS "Id",
   c.ap1cliente AS "Primer Apellido",
   c.ap2cliente AS "Segundo Apellido",
   c.nomcliente AS "Cliente"
FROM cliente c
JOIN factura f ON c.codcliente = f.codcliente
JOIN detalle d ON f.numfactura = d.numfactura
JOIN articulo a ON d.codarticulo = a.codarticulo
GROUP BY c.codcliente
HAVING sum(d.cantidad * a.precio) =
   (SELECT max("Suma")
    FROM
       (SELECT sum(d2.cantidad * a2.precio) AS "Suma"
        FROM articulo a2
        JOIN detalle d2 ON a2.codarticulo = d2.codarticulo
        JOIN factura f2 ON d2.numfactura = f2.numfactura
        GROUP BY f2.codcliente
       ) AS subconsulta
   )
ORDER BY c.ap1cliente, c.ap2cliente, c.nomcliente;


UD 5 - El lenguaje de modificación de datos. DML
CUADERNO DE ACTIVIDADES Actividad 1 (Plan)
--1
BEGIN;
   INSERT INTO investigador
   VALUES (100,'12345678M','Enrique','Franco','Ulric','Barbate',NULL,20000);
   SELECT *
   FROM investigador i
   WHERE upper(i.nombre) = 'ENRIQUE';
COMMIT;
--2
BEGIN;
   INSERT  INTO investigador
   VALUES (101,'12345679M','Mario','Neta','Delgada','Rota',NULL,20000)
   RETURNING cod_investigador ;
   SELECT  *
   FROM investigador i
   WHERE cod_investigador = 101;
   COMMIT;
--3
BEGIN;
  INSERT  INTO plan
  VALUES (100,
  			'Plan Efranco',
  			(
  			SELECT cod_entidad
  			FROM entidad
  			WHERE upper(entidad) = 'ING DIRECT'
  			)
);




--4
BEGIN;
	INSERT INTO proyecto
	VALUES (100,
	(SELECT cod_plan FROM plan WHERE upper(nombre)= 'PLAN EFRANCO'),
	'Proyecto Eco Efranco',
	current_date,
	current_date + '1 year'::INTERVAL,
	100000
);
--5
BEGIN;
INSERT INTO asignado_a
VALUES (100,
		100,
		current_date,
		current_date + '105 days'::INTERVAL,
		(SELECT cod_rol FROM rol WHERE rol = 'Becario')
);
SELECT * FROM asignado_a WHERE cod_investigador = 100;
COMMIT;


