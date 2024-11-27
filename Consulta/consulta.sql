-- Seleccionamos los siguientes campos de las tablas  
SELECT  
    plan.cod_plan AS "ID Plan",  -- Obtenemos el código del plan y lo renombramos como "ID Plan"  
    plan.nombre AS "Plan",        -- Obtenemos el nombre del plan y lo renombramos como "Plan"  
    ent.cod_entidad AS "ID Entidad", -- Obtenemos el código de la entidad y lo renombramos como "ID Entidad"  
    ent.entidad AS "Entidad",     -- Obtenemos el nombre de la entidad y lo renombramos como "Entidad"  
    pro.cod_proyecto AS "ID Proyecto", -- Obtenemos el código del proyecto y lo renombramos como "ID Proyecto"  
    pro.nombre AS "Proyecto"      -- Obtenemos el nombre del proyecto y lo renombramos como "Proyecto"  
FROM   plan  -- Especificamos que la tabla principal es 'plan'  
    
    -- Realizamos un JOIN con la tabla 'proyecto' utilizando la columna cod_plan  
    JOIN proyecto pro USING (cod_plan)  
    
    -- Realizamos un JOIN con la tabla 'ENTIDAD' para obtener información sobre la entidad que financia cada plan  
    JOIN ENTITY ent ON (plan.cod_ent_financiera = ent.cod_entidad)  

-- Ordenamos los resultados primero por el nombre del Plan y después por el nombre del Proyecto  
ORDER BY "Plan", "Proyecto";

 ID Plan |           Plan            | ID Entidad |      Entidad      | ID Proyecto |           Proyecto            
---------+---------------------------+------------+-------------------+-------------+-------------------------------
      15 | Avance Tecnológico        |         10 | La Caixa          |          34 | Ciudades Inteligentes
      15 | Avance Tecnológico        |         10 | La Caixa          |          35 | Transformación 360
       8 | Conectividad Inteligente  |          4 | Bankia            |          19 | Conexión 5G
       8 | Conectividad Inteligente  |          4 | Bankia            |          51 | Conexión Global
       8 | Conectividad Inteligente  |          4 | Bankia            |          18 | Redes del Futuro
       8 | Conectividad Inteligente  |          4 | Bankia            |          20 | Tecnología Verde
      11 | Crecimiento Verde         |          5 | Banco Sabadell    |          27 | Movilidad Sostenible
      11 | Crecimiento Verde         |          5 | Banco Sabadell    |          26 | Reciclaje Urbano
      19 | Cultura Digital           |         14 | Abanca            |          43 | Economía Circular
      19 | Cultura Digital           |         14 | Abanca            |          44 | Plan de Descarbonización
      19 | Cultura Digital           |         14 | Abanca            |          42 | Sistemas de Energía Limpia
      12 | Economía Circular         |          7 | Banco Popular     |          29 | Eficiencia Energética
      12 | Economía Circular         |          7 | Banco Popular     |          28 | Energía Solar
      16 | Educación Digital         |         11 | Kutxabank         |          37 | Alianza por la Innovación
      16 | Educación Digital         |         11 | Kutxabank         |          36 | Smart Education
      17 | Energía Renovable         |         12 | Banco de Valencia |          38 | Revolución Energética
      17 | Energía Renovable         |         12 | Banco de Valencia |          39 | Smart Cities
       9 | Futuro Sostenible         |          6 | Unicaja           |          22 | Desarrollo Sostenible
       9 | Futuro Sostenible         |          6 | Unicaja           |          52 | Desarrollo Sostenible 2.0
       9 | Futuro Sostenible         |          6 | Unicaja           |          21 | Transformación Digital
       5 | Generación 3.0            |          9 | ING Direct        |          11 | Ciberacoso
       5 | Generación 3.0            |          9 | ING Direct        |          10 | Levanta la cabeza
       5 | Generación 3.0            |          9 | ING Direct        |          12 | Tecnología Con-ciencia
       1 | I+D                       |          1 | Santander         |           2 | Jedi
       1 | I+D                       |          1 | Santander         |           1 | Skyfall
       1 | I+D                       |          1 | Santander         |           3 | Yoda
       7 | Innovación Global         |          2 | CaixaBank         |          17 | Ciudades Conectadas
       7 | Innovación Global         |          2 | CaixaBank         |          16 | Cultura Digital
       7 | Innovación Global         |          2 | CaixaBank         |          50 | Innovación 4.0
       2 | IoT                       |          3 | BBVA              |           4 | Mapdwell
       2 | IoT                       |          3 | BBVA              |           5 | Phoenix
      18 | Plan de Desarrollo Urbano |         13 | Cajasol           |          41 | Biosostenibilidad
      18 | Plan de Desarrollo Urbano |         13 | Cajasol           |          40 | Digitalización Agrícola
       6 | Planeta Verde             |          5 | Banco Sabadell    |          15 | Bioenergía 4.0
       6 | Planeta Verde             |          5 | Banco Sabadell    |          13 | Crecimiento Urbano
       6 | Planeta Verde             |          5 | Banco Sabadell    |          49 | Energía Verde
       6 | Planeta Verde             |          5 | Banco Sabadell    |          14 | Redes Inteligentes
      21 | Planificación Eficiente   |         16 | Liberbank         |          48 | Ciudades Sostenibles
      21 | Planificación Eficiente   |         16 | Liberbank         |          47 | Desarrollo Urbano Inteligente
       3 | Profundiza                |          5 | Banco Sabadell    |           8 | Eagle
       3 | Profundiza                |          5 | Banco Sabadell    |           9 | Lion
       3 | Profundiza                |          5 | Banco Sabadell    |           6 | Panther
       3 | Profundiza                |          5 | Banco Sabadell    |           7 | Sapphire

