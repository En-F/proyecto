--EJERCICIO DE CLASE DE ASIGNAR DOS TABLAS
-- Seleccionamos los siguientes campos de las tablas  
SELECT  
    plan.cod_plan AS "ID Plan",  -- Obtenemos el código del plan y lo renombramos como "ID Plan"  
    plan.nombre AS "Plan",        -- Obtenemos el nombre del plan y lo renombramos como "Plan"  
    ent.cod_entidad AS "ID Entidad", -- Obtenemos el código de la entidad y lo renombramos como "ID Entid
    ent.entidad AS "Entidad",     -- Obtenemos el nombre de la entidad y lo renombramos como "Entidad"  
    pro.cod_proyecto AS "ID Proyecto", -- Obtenemos el código del proyecto y lo renombramos como "ID Proy
    pro.nombre AS "Proyecto"      -- Obtenemos el nombre del proyecto y lo renombramos como "Proyecto"  
FROM   plan  -- Especificamos que la tabla principal es 'plan'  
    
    -- Realizamos un JOIN con la tabla 'proyecto' utilizando la columna cod_plan  
    JOIN proyecto pro USING (cod_plan)  
    
    -- Realizamos un JOIN con la tabla 'ENTIDAD' para obtener información sobre la entidad que financia c
    JOIN ENTITDAD ent ON (plan.cod_ent_financiera = ent.cod_entidad)  

-- Ordenamos los resultados primero por el nombre del Plan y después por el nombre del Proyecto  
ORDER BY "Plan", "Proyecto";


-------------------------------------------------------------------------------------------------
--Nombre de los investigadores y nombre de los proyectos en los que trabaja.

-- Seleccionamos el nombre del investigador y el nombre del proyecto
SELECT
    inve.nombre AS "Investigador",  -- Obtenemos el nombre del investigador desde la tabla 'investigador'
    pr.nombre AS "Nombre del Proyecto"  -- Obtenemos el nombre del proyecto desde la tabla 'proyecto'
  
-- Especificamos las tablas que vamos a utilizar en la consulta
FROM investigador inve
-- Realizamos un JOIN entre la tabla 'investigador' y la tabla 'asignado_a'
    JOIN asignado_a a USING (cod_investigador)  -- Utilizamos 'USING' para hacer JOIN en 'cod_investigador', que es la clave común
    -- Luego, realizamos otro JOIN entre la tabla 'asignado_a' y la tabla 'proyecto'
    JOIN proyecto pr ON a.cod_proyecto = pr.cod_proyecto;  -- Unimos la tabla 'proyecto' con 'asignado_a' usando 'cod_proyecto'
where 

--------------------------------------------------------------------------------------
--Nombre de los investigadores de Cádiz y el nombre de los proyectos en los que trabajan
SELECT
    inve.nombre AS "Investigador", 
    pr.nombre AS "Nombre del Proyecto" 

FROM investigador inve

    JOIN asignado_a a USING (cod_investigador)  
    JOIN proyecto pr ON a.cod_proyecto = pr.cod_proyecto
Where lower(inves.ciudad)= 'cádiz';

--------------------------------------------------------------------------------------
--Nombre del investigador responsable y fecha de inicio del proyecto llamado “Phoenix”.
SELECT
    inve.nombre AS "Investigador",
    pr.fecha_inicio AS "Fecha inicial"
FROM investigador inve
    JOIN asignado_a a USING (cod_investigador)  
    JOIN proyecto pr ON a.cod_proyecto = pr.cod_proyecto
Where lower(pr.nombre)= 'phoenix';


--Realiza las siguientes consultas sobre la base de datos alias_db (esquema depart)
--1Realiza la consulta que nos diga el número de analistas que hay. Alias: Núm Analistas
SELECT count(*) AS "Núm Analistas"
FROM emple
WHERE upper(oficio)= 'ANALISTA';
--2. Realiza la consulta que nos diga el número de empleados con comisión tenemos.Alias: Núm Empleados El lenguaje de consultas - DQL Desarrollo Aplicaciones Web Desarrollo de Aplicaciones Web IES Doñana Página 17 de 19
SELECT count(*) AS "Núm Empleados"
FROM emple
WHERE comision NOT NULL; 

--3. Realiza la consulta que nos diga cuántos empleados hay en el departamento de Contabilidad. Alias: Núm Empleados
ELECT 
    count(*) AS "Núm Empleados"
FROM 
    emple 
WHERE
    dept_no  = (
                SELECT 
                    dept_no 
                FROM 
                    depart  
                WHERE 
                    upper(dnombre)='CONTABILIDAD'
                );
--4. Lista de empleados con el departamento en el que trabaja (cod dpto., nombre departamento,  código de empleado, nombre empleado) Ordenado el resultado por nombre de departamento (Z-A), y nombre de empleado (A-Z) Alias: Cod Dpto, Departamento, Cod Empleado, Empleado.
SELECT 
    d.dept_no AS "Cod Dpto",
    d.dnombre AS  "Departamento",
    e.emp_no AS " Cod Empleado",
    e.nombre AS "Empleado"
FROM 
    emple e JOIN depart d ON e.dept_no=d.dept_no 
ORDER BY 
    d.dnombre DESC , 
    ltrim(e.nombre,' ') ASC ;
--5. Mostrar la lista de empleados (código y nombre) y su antigüedad en la empresa.
--Ordenado el resultado por nombre de nombre (A-Z)
--Alias: Cod Emple, Empleado, Antigüedad
SELECT
    e.emp_no AS "Cod Emple",
    e.nombre AS "Empleado",
    age(e.fecha_alt) AS "Antigüedad"
FROM 
    emple e 
ORDER BY 
    trim(e.nombre) ASC ;

--6. Repite la actividad anterior, pero sólo mostrando los años de antigüedad (sin meses ni días). Ordena el resultado por antigüedad apareciendo primero lo que más tiempo llevan en la empresa Hazlo de dos formas disitntas l lenguaje de consultas - DQL Desarrollo Aplicaciones Web Desarrollo de Aplicaciones Web IES Doñana Página 18 de 19
SELECT
    e.emp_no AS "Cod Emple",
    e.nombre AS "Empleado",
    EXTRACT(YEAR FROM age(e.fecha_alt)) AS "Antigüedad"
FROM 
    emple e
ORDER BY 
    e.fecha_alt ASC ;

SELECT 
    e.emp_no AS "Cod Emple",
    e.nombre AS " Empleado",
    trunc( EXTRACT(YEAR FROM age(e.fecha_alt))/6) AS "Sexenios" 
FROM
    emple e ;


--7. Muestra el listado de empleados (código y nombre), junto con el número de sexenios que tiene Un sexenio son 6 años en la empresa Deben de aparecer primero los que más sexenios tienen. Alias: Cod Emple, Empleado, Sexenios
SELECT 
    e.emp_no AS "Cod Emple",
    e.nombre AS " Empleado",
    trunc( EXTRACT(YEAR FROM age(e.fecha_alt))/6) AS "Sexenios" 
FROM
    emple e ;
--8. ¿Cuál es el salario medio de los vendedores? Debe de mostrase con el formato: XX.XXX,XX€
SELECT
    round(avg(salario),2)::money AS "Salario"
FROM 
    emple  
WHERE  lower(oficio) = 'vendedor';


-- EJERCICIO DE CLASE
--Devuelve los  investigadores que  trabaja en  algunos dde los  proyecto  donde trabaja el investigador 10 
SELECT  
    i.*
FROM 
    plan.investigador i 
JOIN 
    plan.asignado_a aa 
ON 
    i.cod_investigador =aa.cod_investigador 
WHERE 
    cod_proyecto = ALL/*(tambien se puede colocar ANY)*/ (SELECT
                        cod_proyecto 
                    FROM 
                        plan.asignado_a
                    WHERE 
                        cod_investigador = 10);

-------------------------------------------------------------------
SELECT 
    (
    SELECT  count(*)
    FROM investigador i 
    ) AS "Num Investigadores",
    (
    SELECT  count(*)
    FROM entidad 
    ) AS "Num Entidades"
    ;

-------------------------------------------------------------------

-- Seleccionamos el nombre de la ciudad convertido a mayúsculas
SELECT         
    upper(ciudad),          -- 'upper(ciudad)' convierte el nombre de la ciudad a mayúsculas
    count(*)                -- 'count(*)' cuenta cuántos registros existen para cada ciudad
FROM investigador          -- La consulta es sobre la tabla 'investigador'
GROUP BY upper(ciudad);   -- Agrupamos por el nombre de la ciudad en mayúsculas


-------------------------------------------------------------------
-- Seleccionamos el código del investigador, su nombre y apellidos, y el número de proyectos en los que trabaja
SELECT 
    i.cod_investigador,       -- Código del investigador
    i.nombre,                 -- Nombre del investigador
    i.apellido1,              -- Primer apellido del investigador
    i.apellido2,              -- Segundo apellido del investigador
    count(cod_proyecto)       -- Contamos el número de proyectos en los que el investigador está asignado
FROM 
    investigador i            -- Desde la tabla 'investigador'
    JOIN asignado_a aa        -- Hacemos un JOIN con la tabla 'asignado_a' para obtener los proyectos
    USING (cod_investigador)  -- Usamos la columna 'cod_investigador' para hacer el JOIN entre ambas tablas
GROUP BY 
    cod_investigador         -- Agrupamos por el 'cod_investigador' para contar los proyectos por cada investigador
ORDER BY 
    cod_investigador ASC;    -- Ordenamos el resultado por el código del investigador en orden ascendente


-------------------------------------------------------------------

SELECT 
    e.cod_entidad,             -- Seleccionamos el código de la entidad
    e.entidad,                 -- Seleccionamos el nombre de la entidad
    count(*)                   -- Contamos cuántos registros (proyectos) están asociados a cada entidad
FROM 
    plan p                     -- Desde la tabla 'plan' que tiene la información de los proyectos
    JOIN entidad e ON p.cod_ent_financiera = e.cod_entidad  -- Hacemos un JOIN con la tabla 'entidad' usando el código de entidad
GROUP BY 
    e.cod_entidad,             -- Agrupamos por el código de entidad para obtener el número de proyectos por entidad
    e.entidad                  -- También agrupamos por el nombre de la entidad para que esté disponible en el resultado
ORDER BY 
    e.cod_entidad ASC;         -- Ordenamos los resultados por el código de la entidad en orden ascendente




    
--Proyecto (código y nombre) que tienen el menor presupuesto            
SELECT p.cod_proyecto AS "código",
       p.nombre AS "Nombre"
FROM proyecto p
WHERE p.presupuesto = (SELECT MIN(p.presupuesto) FROM proyecto p);

--2. Investigadores que viven en la misma ciudad 
--que el investigador con código 8

SELECT *
FROM investigador i 
WHERE  ciudad = (SELECT i.ciudad 
FROM investigador i 
WHERE cod_investigador  = 8);

--3. Investigadores que en algunos de los 
--proyectos en los que trabaja el investigador 12

SELECT i.*
FROM asignado_a aa 
JOIN investigador i  ON aa.cod_investigador = i.cod_investigador 
WHERE aa.cod_proyecto = ANY (SELECT cod_proyecto 
                        FROM asignado_a 
                        WHERE  cod_investigador = 12
                                );

--4. Listado de planes (Código y nombre), que no tienen proyectos
                            
SELECT
    pl.cod_plan, 
    pl.nombre
FROM plan pl
WHERE pl.cod_plan NOT IN 
    (SELECT  DISTINCT p.cod_plan 
    FROM proyecto p);



--5. Listado de investigadores (Código y nombre) 
--que no participan en ningún proyecto

SELECT
    i.cod_investigador,
    i.nombre 
FROM investigador i
WHERE i.cod_investigador NOT IN (
                            SELECT aa.cod_investigador 
                             FROM asignado_a aa 
                            )
ORDER BY cod_investigador  ASC ;



--Obtener un listado con el id de empleado que es jefe y con el número de empleados que dirige

SELECT e.nombre,e.dir , COUNT(e2.emp_no) AS "num_empleados"
FROM emple e
JOIN emple e2 ON e.emp_no = e2.dir 
GROUP BY e.emp_no;

d
SELECT  * FROM emple ;



--4. Dame todos los planes  con el numeor de proyecto que tiene cada plan.

SELECT  
    cod_plan,
    plan.nombre,
    count(pr.cod_proyecto) 
FROM plan
LEFT JOIN proyecto pr USING (cod_plan)
GROUP BY cod_plan
ORDER BY cod_plan;

            

SELECT  
    cod_plan,
    plan.nombre,
    count(pr.cod_proyecto) 
FROM plan
LEFT JOIN proyecto pr USING (cod_plan)
GROUP BY cod_plan
ORDER BY cod_plan DESC ;




--2 Ordena el istado de todos los investigadres que tenemos registrados junto con el ombre deproyectos en los que participa
--Codigo,Nombre,Proyecto
--Ordena los inestigaroes por el numero de proyectos
--en los que participa (de menor a mayor)
SELECT 
    cod_investigador AS "Código",
    concat_ws(' ',nombre,apellido1,apellido2) AS "Nombre",
    count(cod_proyecto) AS "Proyectos"
FROM investigador LEFT JOIN asignado_a  USING(cod_investigador) 
GROUP BY cod_investigador
ORDER BY count(cod_proyecto) ;



--Ordena los nombres de los proyectos que no tiene investiadores
SELECT
    p.cod_proyecto AS "Código" ,
    p.nombre AS "Nombre"
FROM proyecto p LEFT JOIN asignado_a aa  USING(cod_proyecto)
GROUP BY p.cod_proyecto 
ORDER BY cod_proyecto ;


--4. Dame todos los planes  con el numeor de proyecto que tiene cada plan.

SELECT 
    cod_investigador AS "Código",
    concat(nombre,' ',apellido1,' ', apellido2) AS "Nombre",
    count(cod_proyecto) AS "Proyectos"
FROM investigador LEFT JOIN asignado_a  USING(cod_investigador) 
GROUP BY investigador.cod_investigador
ORDER BY count(cod_investigador) ;



--Ordena los nombres de los proyectos que no tiene investiadores
SELECT
    p.cod_proyecto AS "Código" ,
    p.nombre AS "Nombre"
FROM proyecto p LEFT JOIN asignado_a aa  USING(cod_proyecto)
GROUP BY p.cod_proyecto ;

SELECT 
    cod_proyecto ,
    nombre
FROM  asignado_a aa  RIGHT JOIN proyecto p  using(cod_proyecto)
GROUP BY cod_proyecto 
HAVING count(cod_investigador) = 0 
ORDER BY cod_proyecto ;

SELECT 
    cod_proyecto ,
    nombre
FROM proyecto p 
WHERE cod_proyecto NOT IN (SELECT DISTINCT cod_proyecto FROM asignado_a aa);

--5 Obtener todos los proyectos existentes junto con el numeor de investigador de C... Leer más

SELECT 
    p.cod_proyecto AS "Codigo",
    p.nombre AS "Nombre",
    COUNT(aa.cod_investigador) AS "Investigadores"
FROM 
    proyecto p
LEFT JOIN 
    asignado_a aa USING(cod_proyecto)
LEFT JOIN 
--Lo que esta dentro del on se ejecuta antes del join, el where se ejecuta despues del join.
    investigador i ON (aa.cod_investigador = i.cod_investigador
    AND UPPER(i.ciudad) = 'CÁDIZ')  
GROUP BY 
    p.cod_proyecto
ORDER BY
    p.cod_proyecto ;

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


