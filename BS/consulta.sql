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
