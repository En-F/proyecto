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



--Devuelve los  investigadores que  trabajan donde trabaja el investigador 10
SELECT  
    i.*
FROM 
    plan.investigador i 
JOIN 
    plan.asignado_a aa 
ON 
    i.cod_investigador =aa.cod_investigador 
WHERE 
    cod_proyecto = (SELECT
                        cod_proyecto 
                    FROM 
                        plan.asignado_a
                    WHERE 
                        cod_investigador = 10);



SELECT 
    e.cod_entidad,
    e.entidad,
    count(*) 
FROM 
    plan p
    JOIN entidad e ON p.cod_ent_financiera= e.cod_entidad
    GROUP  BY (cod_entidad)
    HAVING count(*)>2 ;