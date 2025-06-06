# data.py
turistic_sites = [
    {
        "id": 1,
        "nombre": "Salto Ángel",
        "ubicacion": "Bolívar",
        "clasificacion": "Selva",
        "atractivo": "La cascada más alta del mundo.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/salto_angel.webp",
        "caracteristicas": [
            "Altura de 979 metros.",
            "Ubicada en el Parque Nacional Canaima.",
            "Acceso principalmente por vía aérea."
        ]
    },
    {
        "id": 2,
        "nombre": "Archipiélago Los Roques",
        "ubicacion": "Dependencias Federales",
        "clasificacion": "Playa",
        "atractivo": "Parque Nacional con playas vírgenes y arrecifes de coral.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/los_roques.webp",
        "caracteristicas": [
            "Ideal para buceo y snorkel.",
            "Gran diversidad de fauna marina.",
            "Alojamiento en posadas locales."
        ]
    },
    {
        "id": 3,
        "nombre": "Teleférico de Mérida",
        "ubicacion": "Mérida",
        "clasificacion": "Montaña",
        "atractivo": "Sistema de teleférico más alto y largo del mundo.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/teleferico_merida.webp",
        "caracteristicas": [
            "Ascenso a 4.765 metros sobre el nivel del mar.",
            "Vistas panorámicas de la Sierra Nevada.",
            "Estaciones con servicios turísticos."
        ]
    },
    {
        "id": 4,
        "nombre": "Cueva del Guácharo",
        "ubicacion": "Monagas",
        "clasificacion": "Montaña",
        "atractivo": "Hogar del guácharo, ave nocturna única.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/cueva_guacharo.webp",
        "caracteristicas": [
            "Recorridos guiados por la cueva.",
            "Observación de aves y murciélagos.",
            "Senderos ecológicos."
        ]
    },
    {
        "id": 5,
        "nombre": "Parque Nacional Morrocoy",
        "ubicacion": "Falcón",
        "clasificacion": "Playa",
        "atractivo": "Playas de arena blanca y manglares.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/parque_morrocoy.webp",
        "caracteristicas": [
            "Ideal para deportes acuáticos.",
            "Diversidad de cayos y playas.",
            "Servicios de alojamiento y restaurantes."
        ]
    },
    {
        "id": 6,
        "nombre": "Parque Nacional Henri Pittier",
        "ubicacion": "Aragua y Carabobo",
        "clasificacion": "Montaña",
        "atractivo": "Primer parque nacional de Venezuela.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/parque_pittier.webp",
        "caracteristicas": [
            "Gran biodiversidad.",
            "Senderos para caminatas.",
            "Observación de aves."
        ]
    },
    {
        "id": 7,
        "nombre": "Medanos de Coro",
        "ubicacion": "Falcón",
        "clasificacion": "Desierto",
        "atractivo": "Dunas de arena en un entorno desértico.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/medanos_coro.webp",
        "caracteristicas": [
            "Actividades como sandboarding.",
            "Paisajes únicos en Venezuela.",
            "Cercanía a la ciudad colonial de Coro."
        ]
    },
    {
        "id": 8,
        "nombre": "Parque Nacional Mochima",
        "ubicacion": "Anzoátegui y Sucre",
        "clasificacion": "Playa",
        "atractivo": "Playas y bahías de gran belleza.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/parque_mochima.webp",
        "caracteristicas": [
            "Ideal para buceo y snorkel.",
            "Diversidad de fauna marina.",
            "Servicios turísticos en la zona."
        ]
    },
    {
        "id": 9,
        "nombre": "Roraima",
        "ubicacion": "Bolívar",
        "clasificacion": "Montaña",
        "atractivo": "Tepuy más famoso de Venezuela.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/parque_roraima.webp",
        "caracteristicas": [
            "Excursiones de varios días.",
            "Paisajes únicos y formaciones rocosas.",
            "Requiere guía para el ascenso."
        ]
    },
    {
        "id": 10,
        "nombre": "Delta del Orinoco",
        "ubicacion": "Delta Amacuro",
        "clasificacion": "Selva",
        "atractivo": "Uno de los deltas más grandes del mundo.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/delta_orinoco.webp",
        "caracteristicas": [
            "Recorridos en curiara (embarcación típica).",
            "Observación de flora y fauna.",
            "Contacto con comunidades indígenas."
        ]
    },
    {
        "id": 11,
        "nombre": "Parque Nacional Sierra Nevada",
        "ubicacion": "Mérida y Barinas",
        "clasificacion": "Montaña",
        "atractivo": "Picos nevados y lagunas de alta montaña.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/sierra_nevada.webp",
        "caracteristicas": [
            "Senderismo y escalada.",
            "Paisajes andinos.",
            "Observación de fauna de alta montaña."
        ]
    },
    {
        "id": 12,
        "nombre": "Isla de Margarita",
        "ubicacion": "Nueva Esparta",
        "clasificacion": "Playa",
        "atractivo": "Destino turístico con playas y centros comerciales.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/isla_margarita.webp",
        "caracteristicas": [
            "Variedad de playas.",
            "Actividades acuáticas.",
            "Vida nocturna y compras."
        ]
    },
    {
        "id": 13,
        "nombre": "Parque Nacional Guatopo",
        "ubicacion": "Miranda",
        "clasificacion": "Montaña",
        "atractivo": "Bosque nublado y ríos.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/refs/heads/main/static/images/parque_guatopo.webp",
        "caracteristicas": [
            "Senderos para caminatas.",
            "Observación de aves.",
            "Cascadas y ríos."
        ]
    },
    {
        "id": 14,
        "nombre": "Parque Nacional Sierra de La Culata",
        "ubicacion": "Mérida",
        "clasificacion": "Montaña",
        "atractivo": "Paisajes andinos y lagunas.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/sierra_culata.webp",
        "caracteristicas": [
            "Senderismo y escalada.",
            "Observación de fauna.",
            "Paisajes de alta montaña."
        ]
    },
    {
        "id": 15,
        "nombre": "Parque Nacional Sierra de Perijá",
        "ubicacion": "Zulia",
        "clasificacion": "Montaña",
        "atractivo": "Bosques nublados y ríos.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/refs/heads/main/static/images/sierra_perija.webp",
        "caracteristicas": [
            "Senderos para caminatas.",
            "Observación de aves.",
            "Diversidad de flora."
        ]
    },
    {
        "id": 16,
        "nombre": "Parque Nacional Yurubí",
        "ubicacion": "Bolívar",
        "clasificacion": "Selva",
        "atractivo": "Bosques tropicales y ríos.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/parque_yurubi.webp",
        "caracteristicas": [
            "Senderos ecológicos.",
            "Observación de fauna.",
            "Actividades de aventura."
        ]
    },
    {
        "id": 17,
        "nombre": "Parque Nacional El Guácharo",
        "ubicacion": "Monagas",
        "clasificacion": "Montaña",
        "atractivo": "Hogar del guácharo y otras aves.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/parque_guacharo.webp",
        "caracteristicas": [
            "Recorridos guiados por la cueva.",
            "Observación de aves y murciélagos.",
            "Senderos ecológicos."
        ]
    },
    {
        "id": 18,
        "nombre": "Parque Nacional Laguna de La Restinga",
        "ubicacion": "Nueva Esparta",
        "clasificacion": "Playa",
        "atractivo": "Laguna y manglares.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/laguna_larestinga.webp",
        "caracteristicas": [
            "Recorridos en bote.",
            "Observación de aves.",
            "Paisajes naturales."
        ]
    },
    {
        "id": 19,
        "nombre": "Parque Nacional Waraira Repano",
        "ubicacion": "Distrito Capital y Miranda",
        "clasificacion": "Montaña",
        "atractivo": "Montaña Ávila y teleférico.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/cerro_avila.webp",
        "caracteristicas": [
            "Senderos para caminatas.",
            "Vistas panorámicas de Caracas.",
            "Actividades de aventura."
        ]
    },
    {
        "id": 20,
        "nombre": "Parque Nacional Dinira",
        "ubicacion": "Lara",
        "clasificacion": "Montaña",
        "atractivo": "Bosques nublados y ríos.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/parque_dinira.webp",
        "caracteristicas": [
            "Senderos para caminatas.",
            "Observación de aves.",
            "Cascadas y ríos."
        ]
    },
    {
        "id": 21,
        "nombre": "Parque Nacional Terepaima",
        "ubicacion": "Lara",
        "clasificacion": "Montaña",
        "atractivo": "Bosques secos y ríos.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/refs/heads/main/static/images/parque_terepaima.webp",
        "caracteristicas": [
            "Senderos para caminatas.",
            "Observación de fauna.",
            "Paisajes naturales."
        ]
    },
    {
        "id": 22,
        "nombre": "Parque Nacional Cerro Saroche",
        "ubicacion": "Anzoátegui",
        "clasificacion": "Montaña",
        "atractivo": "Bosques secos y ríos.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/cerro_saroche.webp",
        "caracteristicas": [
            "Senderos para caminatas.",
            "Observación de aves.",
            "Paisajes naturales."
        ]
    },
    {
        "id": 23,
        "nombre": "Parque Nacional Macarao",
        "ubicacion": "Distrito Capital y Miranda",
        "clasificacion": "Montaña",
        "atractivo": "Bosques nublados y ríos.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/parque_macarao.webp",
        "caracteristicas": [
            "Senderos para caminatas.",
            "Observación de aves.",
            "Cascadas y ríos."
        ]
    },
    {
        "id": 24,
        "nombre": "Parque Nacional Turuépano",
        "ubicacion": "Delta Amacuro",
        "clasificacion": "Selva",
        "atractivo": "Bosques tropicales y ríos.",
        "imagen": "https://raw.githubusercontent.com/JoseLuisGalvis/api_venezuela_es_un_paraiso/main/static/images/parque_turuepano.webp",
        "caracteristicas": [
            "Senderos ecológicos.",
            "Observación de fauna.",
            "Actividades de aventura."
        ]
    }
]

