import sqlite3

conexion = sqlite3.connect('mi_base_de_datos.db')

cursor = conexion.cursor()

desayunos_data = [
    ('Tostadas de aguacate con huevo pochado', 380, 'Pan integral, aguacate, huevo, sal, pimienta'),
    ('Omelette de champiñones y espinacas', 350, 'Huevo, champiñones, espinacas, queso, sal, pimienta'),
    ('Batido de plátano y espinacas', 250, 'Plátano, espinacas, leche de almendras, miel'),
    ('Avena con frutos rojos y nueces', 300, 'Avena, leche, frutos rojos, nueces, miel'),
    ('Yogur griego con granola y frutas', 280, 'Yogur griego, granola, fresas, plátano, miel'),
    ('Panqueques de avena y plátano', 320, 'Harina de avena, plátano, huevo, leche, canela'),
    ('Smoothie de mango y coco', 280, 'Mango, leche de coco, yogur, miel'),
    ('Tortilla de pimientos y cebolla', 300, 'Huevo, pimientos, cebolla, sal, pimienta'),
    ('Tostadas de salmón ahumado y queso crema', 350, 'Pan integral, salmón ahumado, queso crema, pepino, eneldo'),
    ('Huevos revueltos con aguacate y tomate', 350, 'Huevo, aguacate, tomate, sal, pimienta'),
    ('Muffins de huevo y espinacas', 320, 'Huevo, espinacas, tomate, cebolla, sal, pimienta'),
    ('Gachas de trigo sarraceno con frutos secos', 320, 'Trigo sarraceno, leche, almendras, nueces, miel'),
    ('Bagel integral con salmón y pepino', 380, 'Bagel integral, salmón ahumado, pepino, queso crema'),
    ('Tostadas francesas con frutas frescas', 350, 'Pan, huevo, leche, canela, frutas frescas, miel'),
    ('Tortitas de queso cottage y arándanos', 300, 'Queso cottage, huevo, arándanos, harina de avena'),
    ('Smoothie bowl de bayas y granola', 320, 'Bayas, plátano, leche, granola, semillas de chía'),
    ('Yogur con granola y plátano', 280, 'Yogur natural, granola, plátano, miel'),
    ('Huevos Benedictinos', 380, 'Huevo pochado, jamón, pan inglés, salsa holandesa'),
    ('Pan de plátano con nueces', 320, 'Plátano, harina, huevo, nueces, azúcar'),
    ('Desayuno inglés completo', 500, 'Huevo frito, salchicha, tocino, tomate, champiñones, frijoles, pan frito')
]

cursor.executemany('INSERT INTO desayunos (nombre, calorias, ingredientes) VALUES (?, ?, ?)', desayunos_data)

almuerzos_data = [
    ('Ensalada César con pollo a la parrilla', 450, 'Lechuga romana, pollo a la parrilla, pan tostado, aderezo César'),
    ('Wrap de pollo y aguacate', 380, 'Pechuga de pollo, aguacate, lechuga, tomate, mayonesa, tortilla de trigo integral'),
    ('Ensalada de quinoa y aguacate', 400, 'Quinoa, aguacate, tomate, pepino, cebolla, aderezo de limón'),
    ('Sándwich de pavo y queso', 350, 'Pavo, queso, lechuga, tomate, mostaza, pan integral'),
    ('Tacos de pescado con coleslaw', 380, 'Filete de pescado, tortillas de maíz, repollo, zanahoria, cebolla, mayonesa'),
    ('Poke bowl de salmón', 420, 'Salmón crudo, arroz, aguacate, pepino, zanahoria, edamame, aderezo de soja'),
    ('Hamburguesa vegetariana con batatas fritas', 450, 'Hamburguesa de lentejas, pan integral, batatas, aceite de oliva, sal, pimienta'),
    ('Tostadas de aguacate con huevo pochado', 380, 'Pan integral, aguacate, huevo pochado, sal, pimienta'),
    ('Ensalada griega con queso feta', 380, 'Lechuga, tomate, pepino, cebolla roja, aceitunas, queso feta, aderezo de limón'),
    ('Rollitos de sushi vegetarianos', 400, 'Arroz de sushi, pepino, zanahoria, aguacate, nori'),
    ('Buddha bowl de garbanzos y verduras asadas', 420, 'Garbanzos, calabaza, brócoli, zanahoria, cebolla, tahini'),
    ('Wrap de salmón ahumado y queso crema', 380, 'Salmón ahumado, queso crema, espinacas, tortilla de trigo integral'),
    ('Pasta integral con pesto y tomates cherry', 380, 'Pasta integral, pesto, tomates cherry, piñones, queso parmesano'),
    ('Bowl de arroz con curry de vegetales', 420, 'Arroz integral, curry, calabacín, zanahoria, pimiento, cebolla, leche de coco'),
    ('Tacos de pollo a la parrilla', 380, 'Pechuga de pollo, tortillas de maíz, lechuga, tomate, aguacate, salsa'),
    ('Bowl de quinoa con espinacas y garbanzos', 400, 'Quinoa, espinacas, garbanzos, tomate, pepino, aderezo balsámico'),
    ('Pasta al pesto con tomates secos', 400, 'Pasta, pesto, tomates secos, aceitunas, albahaca'),
    ('Ensalada de salmón y aguacate', 420, 'Salmón ahumado, aguacate, espinacas, tomate, pepino, aderezo de limón'),
    ('Arroz frito con verduras y tofu', 400, 'Arroz, tofu, brócoli, zanahoria, cebolla, salsa de soja'),
    ('Ensalada de pasta con tomate y mozzarella', 380, 'Pasta, tomate, mozzarella, albahaca, aceite de oliva'),
    ('Pollo al curry con arroz integral', 420, 'Pechuga de pollo, curry, leche de coco, arroz integral, zanahoria, guisantes'),
    ('Wrap de pollo teriyaki', 380, 'Pechuga de pollo, salsa teriyaki, lechuga, zanahoria, tortilla de trigo integral')
]

cursor.executemany('INSERT INTO almuerzos (nombre, calorias, ingredientes) VALUES (?, ?, ?)', almuerzos_data)

meriendas_data = [
    ('Batido de proteínas de vainilla', 300, 'Proteína en polvo de vainilla, leche de almendra, plátano, mantequilla de cacahuete'),
    ('Palitos de apio con mantequilla de maní', 250, 'Apio, mantequilla de maní'),
    ('Rollitos de jamón y queso', 200, 'Jamón, queso, pepino'),
    ('Tazón de frutas tropicales', 250, 'Papaya, piña, mango, kiwi'),
    ('Yogur griego con miel y nueces', 280, 'Yogur griego, miel, nueces'),
    ('Quesadilla de espinacas y queso', 300, 'Tortilla de trigo, espinacas, queso cheddar'),
    ('Galletas de avena y pasas', 280, 'Harina de avena, pasas, huevo, miel'),
    ('Plátano con mantequilla de almendra', 200, 'Plátano, mantequilla de almendra'),
    ('Tazón de fresas con crema batida', 220, 'Fresas, crema batida'),
    ('Batido de frutas con espinacas', 250, 'Plátano, fresas, espinacas, leche de coco'),
    ('Yogur con granola y frutos rojos', 280, 'Yogur natural, granola, frutos rojos'),
    ('Batido de bayas con leche de almendra', 250, 'Bayas, leche de almendra, miel'),
    ('Barrita de granola casera', 200, 'Avena, miel, frutos secos, pasas, mantequilla de cacahuete'),
    ('Huevo cocido con zanahorias baby', 180, 'Huevo, zanahorias baby'),
    ('Rollitos de pepino con queso cottage', 150, 'Pepino, queso cottage'),
    ('Batido de proteínas de chocolate', 300, 'Proteína en polvo de chocolate, leche de almendra, plátano'),
    ('Yogur con almendras y miel', 280, 'Yogur natural, almendras, miel'),
    ('Galletas integrales con queso crema', 250, 'Galletas integrales, queso crema'),
    ('Tostadas de pan integral con aguacate', 220, 'Pan integral, aguacate'),
    ('Batido de plátano y leche de coco', 280, 'Plátano, leche de coco')
]

cursor.executemany('INSERT INTO refrigerios (nombre, calorias, ingredientes) VALUES (?, ?, ?)', meriendas_data)

cenas_data = [
    ('Salmón al horno con espárragos', 400, 'Filete de salmón, espárragos, limón, aceite de oliva, sal, pimienta'),
    ('Tortilla española con ensalada', 350, 'Huevos, patatas, cebolla, aceite de oliva, lechuga, tomate, vinagreta'),
    ('Pechuga de pollo a la parrilla con ensalada', 380, 'Pechuga de pollo, lechuga, tomate, pepino, aderezo'),
    ('Sopa de verduras con garbanzos', 320, 'Caldo de verduras, zanahoria, puerro, garbanzos, apio, cebolla'),
    ('Ensalada de pasta con tomate cherry y albahaca', 350, 'Pasta, tomates cherry, albahaca, aceite de oliva, queso parmesano'),
    ('Hamburguesa vegetariana con patatas asadas', 420, 'Hamburguesa de lentejas, pan integral, patatas, aceite de oliva, sal, pimienta'),
    ('Tofu al curry con arroz basmati', 380, 'Tofu, cebolla, pimiento, salsa de curry, arroz basmati'),
    ('Espaguetis integrales con brócoli y ajo', 350, 'Espaguetis integrales, brócoli, ajo, aceite de oliva, sal, pimienta'),
    ('Wrap de pollo y aguacate', 380, 'Pechuga de pollo, aguacate, lechuga, tomate, mayonesa, tortilla de trigo integral'),
    ('Pescado al horno con verduras', 400, 'Filete de pescado blanco, calabacín, zanahoria, cebolla, limón, aceite de oliva'),
    ('Pasta integral con pesto de espinacas y nueces', 380, 'Pasta integral, espinacas, nueces, ajo, aceite de oliva, queso parmesano'),
    ('Arroz frito con tofu y vegetales', 400, 'Arroz, tofu, brócoli, zanahoria, cebolla, salsa de soja'),
    ('Sopa de lentejas con verduras', 320, 'Lentejas, zanahoria, cebolla, apio, caldo de verduras'),
    ('Tacos de coliflor con guacamole', 350, 'Coliflor, aguacate, tomate, cilantro, cebolla, tortillas de maíz'),
    ('Quiche de espinacas y champiñones', 350, 'Masa quebrada, espinacas, champiñones, huevo, nata, queso'),
    ('Ensalada de quinoa con vegetales asados', 380, 'Quinoa, calabaza, pimiento, berenjena, cebolla, aderezo balsámico'),
    ('Pasta con salsa de tomate y albóndigas de pavo', 400, 'Pasta, tomate, cebolla, ajo, pavo, pan rallado, huevo'),
    ('Tofu a la plancha con verduras al vapor', 350, 'Tofu, brócoli, zanahoria, calabacín, aceite de oliva, limón'),
    ('Pasta con pesto de albahaca y tomate cherry', 380, 'Pasta, albahaca, tomate cherry, piñones, aceite de oliva, queso parmesano'),
    ('Hamburguesa de pavo con guarnición de ensalada', 420, 'Carne de pavo, pan integral, lechuga, tomate, cebolla, pepinillos'),
    ('Salmón al horno con verduras asadas', 400, 'Filete de salmón, calabacín, berenjena, tomate, cebolla, aceite de oliva'),
    ('Ensalada de pollo con aguacate y mango', 380, 'Pechuga de pollo, aguacate, mango, espinacas, nueces, aderezo de limón'),
    ('Wrap vegetariano con hummus y verduras', 350, 'Tortilla de trigo, hummus, espinacas, pepino, pimiento, zanahoria'),
    ('Cuscús con verduras y garbanzos', 380, 'Cuscús, calabacín, zanahoria, garbanzos, pasas, cilantro'),
    ('Tortilla de espinacas y queso feta', 350, 'Huevo, espinacas, queso feta, cebolla, aceite de oliva'),
    ('Ensalada de salmón ahumado con aguacate', 400, 'Salmón ahumado, aguacate, lechuga, tomate, pepino, aderezo de limón'),
    ('Tacos de champiñones portobello', 350, 'Champiñones portobello, repollo morado, salsa de yogur, cilantro'),
    ('Pasta integral con salsa de tomate y albahaca', 380, 'Pasta integral, tomate, ajo, albahaca, aceite de oliva')
]

cursor.executemany('INSERT INTO cenas (nombre, calorias, ingredientes) VALUES (?, ?, ?)', cenas_data)

# Datos de los aperitivos

aperitivos = [
    ('Papas fritas', 150, 'Alto contenido de grasas saturadas, Alto contenido de sodio', '', None),
    ('Palitos de zanahoria', 50, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', '', None),
    ('Galletas saladas', 100, 'Moderado contenido de grasas saturadas, Moderado contenido de sodio', '', None),
    ('Nueces', 200, 'Alto contenido calórico, Contenido alto en grasas saludables', '', None),
    ('Chips de maíz', 180, 'Moderado contenido de grasas saturadas, Alto en sodio', '', None),
    ('Barritas de granola', 120, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en fibra', None),
    ('Aceitunas', 60, 'Bajo contenido de grasas saturadas, Moderado en sodio', 'Alto contenido de grasas saludables', None),
    ('Almendras tostadas', 160, 'Moderado contenido de grasas saturadas, Bajo contenido de sodio', 'Alto contenido de grasas saludables', None),
    ('Hummus con palitos de apio', 100, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en proteínas', None),
    ('Tortillas de maíz con salsa', 120, 'Bajo contenido de grasas saturadas, Moderado en sodio', '', None),
    ('Cubos de queso', 90, 'Moderado contenido de grasas saturadas, Moderado en sodio', 'Rico en calcio', None),
    ('Tostadas integrales con aguacate', 110, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en grasas saludables', None),
    ('Bolitas de melón', 50, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en vitamina C', None),
    ('Zanahorias baby con hummus', 70, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en proteínas', None),
    ('Pepinos con aderezo griego', 80, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', '', None),
    ('Rodajas de manzana con mantequilla de almendras', 120, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en grasas saludables', None),
    ('Rodajas de pepino con queso cottage', 60, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en proteínas', None),
    ('Tiras de pimiento rojo con guacamole', 90, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en grasas saludables', None),
    ('Tostadas de trigo integral con salsa de tomate', 100, 'Bajo contenido de grasas saturadas, Moderado en sodio', '', None),
    ('Rollitos de jamón con queso', 110, 'Moderado contenido de grasas saturadas, Moderado en sodio', 'Rico en proteínas', None),
    ('Huevos duros', 70, 'Moderado contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en proteínas', None),
    ('Tiras de jícama con limón y chile', 40, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en vitamina C', None),
    ('Tomates cherry con mozzarella', 100, 'Moderado contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en calcio', None),
    ('Rollitos de salmón ahumado con queso crema', 120, 'Moderado contenido de grasas saturadas, Moderado en sodio', 'Rico en proteínas', None),
    ('Gelatina sin azúcar', 20, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', 'Bajo en calorías', None),
    ('Bolitas de sandía', 30, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en vitamina C', None),
    ('Pepinillos en vinagre', 10, 'Bajo contenido de grasas saturadas, Moderado en sodio', 'Bajo en calorías', None),
    ('Tiras de zanahoria con salsa de yogur', 60, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en proteínas', None),
    ('Huevos rellenos', 80, 'Moderado contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en proteínas', None),
    ('Tostadas de pan integral con queso crema y salmón', 150, 'Moderado contenido de grasas saturadas, Moderado en sodio', 'Rico en proteínas', None),
    ('Brochetas de frutas', 70, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en vitaminas', None),
    ('Higos secos envueltos en jamón serrano', 90, 'Moderado contenido de grasas saturadas, Moderado en sodio', 'Rico en proteínas', None),
    ('Rollitos de tortilla de trigo integral con pollo', 130, 'Moderado contenido de grasas saturadas, Moderado en sodio', 'Rico en proteínas', None),
    ('Rollitos de pepino con salmón ahumado y queso crema', 110, 'Moderado contenido de grasas saturadas, Moderado en sodio', 'Rico en proteínas', None),
    ('Rodajas de piña con jamón', 70, 'Bajo contenido de grasas saturadas, Moderado en sodio', 'Rico en proteínas', None),
    ('Dátiles rellenos de queso de cabra', 100, 'Moderado contenido de grasas saturadas, Moderado en sodio', 'Rico en proteínas', None),
    ('Almendras tostadas con especias', 150, 'Moderado contenido de grasas saturadas, Bajo contenido de sodio', 'Alto contenido en grasas saludables', None),
    ('Tostadas de pan integral con aguacate y tomate', 120, 'Bajo contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en grasas saludables', None),
    ('Bocaditos de mozzarella con tomate cherry', 90, 'Moderado contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en calcio', None),
    ('Rollitos de calabacín con queso feta', 110, 'Moderado contenido de grasas saturadas, Bajo contenido de sodio', 'Rico en calcio', None)
]


cursor.executemany("INSERT INTO aperitivos (nombre, calorias, grasas_saturadas, sodio, otros) VALUES (?, ?, ?, ?, ?)", aperitivos)


conexion.commit()

conexion.close()

print("Datos insertados correctamente.")
