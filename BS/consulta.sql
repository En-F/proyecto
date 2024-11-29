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