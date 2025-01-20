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


-------------------------------------------
