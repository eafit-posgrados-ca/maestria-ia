# Guion · Charla informativa Maestría en Inteligencia Artificial

Este archivo alimenta las notas del presentador (tecla `S` durante la presentación).
Cada bloque `## CLAVE` corresponde a un paso de la presentación, en orden.
`[clic]` indica que hay que avanzar para que aparezca el siguiente elemento.
Duración estimada: 22 a 25 minutos, más preguntas.

Para editar: cambia el texto bajo cada clave y ejecuta `python build_deck.py && python build_onefile.py`.
No hace falta volver a renderizar las animaciones.

## Portada.0
*(Mientras se arma la red y aparece el título.)*

Buenas tardes y bienvenidos. Gracias por acompañarnos en esta charla sobre la Maestría en Inteligencia Artificial de EAFIT.

## Portada.1
*(La red queda con señales en bucle. Puedes hablar todo lo necesario aquí.)*

En los próximos minutos les voy a contar tres cosas: por qué creemos que hoy hace falta una maestría como esta, qué van a aprender y cómo está organizado el programa. Al final tendremos tiempo para sus preguntas.

## CONTACTO
Soy Juan David Martínez, profesor del Área de Computación y Analítica de la Escuela de Ciencias Aplicadas e Ingeniería, y soy el jefe de la Maestría en Inteligencia Artificial.

*(Si hay más personas del equipo, preséntalas aquí.)*

## DosEpocas.0
*(Aparece la columna "Antes".)*

Quiero empezar con un problema concreto, de los que llegan a cualquier organización: una empresa recibe cientos de solicitudes al día y necesita clasificarlas y responderlas.

Hace unos años, la forma de resolverlo con IA era clara: etiquetar miles de ejemplos a mano, entrenar un modelo propio con esos datos y desplegarlo.

## DosEpocas.1
*(Aparece la columna "Hoy".)*

Hoy ese mismo problema se resuelve de otra manera. Muchas veces no empezamos entrenando: empezamos eligiendo un modelo fundacional ya existente. Lo adaptamos al contexto de la empresa, con buenas instrucciones, conectándolo a sus documentos con RAG o, si hace falta, con fine-tuning. Construimos un agente que consulta los sistemas de la empresa y actúa. Lo evaluamos en los casos reales de esa organización y lo observamos en producción paso a paso.

El flujo de trabajo cambió muchísimo en muy poco tiempo.

## DosEpocas.2
*(Sube la base común.)*

Pero fíjense en esto: los dos flujos se apoyan en lo mismo. Matemáticas, estadística, aprendizaje automático, aprendizaje profundo, y la teoría de agentes, de búsqueda y de planificación.

Cambió el enfoque, no la necesidad de entender. Y yo diría que hoy esa base hace más falta que antes: elegir bien un modelo, adaptarlo y saber si de verdad funciona exige entender lo que hay por dentro.

## DosEpocas.3
Por eso esta maestría tiene las dos cosas: lo más actual de la IA y una fundamentación sólida que no se vuelve obsoleta con la próxima herramienta.

## PREGUNTAS
Veámoslo desde las preguntas que hoy surgen cuando se trabaja con IA en serio, ya sea en una empresa, en una entidad pública o en un proyecto propio.

[clic] ¿Qué modelo uso? [clic] Responder eso bien es aprendizaje automático: entender generalización, métricas, sesgo y varianza.

[clic] ¿Cómo sé que funciona en mi caso? [clic] Eso es estadística: diseñar evaluaciones, medir la incertidumbre y comparar con rigor.

[clic] ¿Por qué falla y cómo lo mejoro? [clic] Eso exige aprendizaje profundo y optimización: entender el modelo para poder adaptarlo.

[clic] ¿Cómo decide un agente qué hacer? [clic] Eso es Fundamentos de IA: búsqueda, planificación y razonamiento.

[clic] Y, una vez en producción: ¿qué pasó en cada etapa y cuánto costó? [clic] Eso es operación de la IA: trazas, evaluaciones continuas, LLMOps.

[clic] Usar IA hoy es fácil. Hacerla confiable exige fundamentos. Esa es la idea que atraviesa todo el programa.

*(Si preguntan por el contexto: Colombia tiene una Política Nacional de Inteligencia Artificial, el CONPES 4144, que pone la formación de talento como uno de sus ejes. Esta sería la primera maestría en IA de una universidad antioqueña.)*

## CicloIA.0
Si ponemos todo esto junto, el ciclo de vida de una solución de IA hoy se ve así. Y lo primero que quiero que noten es el subtítulo: muchas veces no se entrena. Se elige, se adapta, se evalúa y se observa.

## CicloIA.1
*(Aparecen las etapas del ciclo, una a una.)*

Todo empieza por entender bien el problema y los datos o el contexto con que contamos. Luego viene una decisión que antes casi no existía: seleccionar el modelo. Después lo adaptamos, o lo entrenamos si de verdad hace falta. Lo evaluamos, lo desplegamos y lo observamos con trazas, y lo que aprendemos en producción vuelve al comienzo del ciclo.

Las etapas en azul oscuro son las que más han cambiado: selección, evaluaciones y observabilidad. A la operación de todo esto la llamamos MLOps, LLMOps o AgentOps, según lo que estemos operando.

## CicloIA.2
*(El punto recorre el ciclo en bucle.)*

Es un ciclo, no una línea: una solución de IA no se termina el día que se despliega. Detengámonos en dos de estas etapas.

## CicloIA.3
*(El ciclo se reduce y se resalta "Selección del modelo".)*

Primero, la selección del modelo. La pregunta ya no es solo cómo entrenar, sino qué modelo usar. Y no hay un mejor modelo en abstracto: hay un mejor modelo para una tarea, un presupuesto y unas restricciones.

Se decide con criterios: la calidad medida en la tarea propia, no en los rankings públicos; el costo por consulta y la latencia; la privacidad, la soberanía de los datos y la licencia, es decir, si conviene un modelo abierto que se pueda alojar o uno comercial; y el soporte para contexto, herramientas y agentes.

¿Y entrenar? Solo cuando los datos o la tarea lo exigen.

## CicloIA.4
*(Se resalta "Evaluaciones".)*

Y antes de desplegar, el modelo elegido se evalúa: exactitud en casos de prueba propios, fidelidad al contexto que recupera, un LLM que actúa como juez de la utilidad de las respuestas, pruebas de seguridad y sesgos, y pruebas de regresión frente a la versión anterior.

Las evaluaciones son, de alguna forma, las pruebas unitarias de la IA moderna. Y diseñarlas bien es, otra vez, estadística. Solo entonces el sistema está listo para desplegarse y observarse con trazas.

*(Las cifras de la diapositiva son ilustrativas.)*

## EVOLUCION
Todo esto cambia el perfil que se necesita.

La formación base sigue siendo indispensable: programación en Python, matemáticas y estadística, análisis de datos y entrenamiento de modelos clásicos.

Pero hoy se espera más. [clic] Aprendizaje profundo, visión y lenguaje. [clic] IA generativa y agentes. [clic] Selección y adaptación de modelos fundacionales. [clic] Evaluación rigurosa de modelos. [clic] Operación con trazas, control de costos y observabilidad. [clic] Y ética, gobernanza y liderazgo de proyectos de IA.

El valor ya no está solo en entrenar modelos, sino en elegir, adaptar, evaluar y operar el adecuado.

## PROFUNDIZACION
Antes de los datos del programa, una aclaración importante: esta es una maestría de profundización.

[clic] En Colombia, una maestría de profundización busca el desarrollo avanzado de competencias para resolver problemas y analizar situaciones de carácter disciplinar, interdisciplinario o profesional. El énfasis está en saber hacer, con rigor. Por eso el trabajo de grado es aplicado: un prototipo, una solución, un modelo implementado.

[clic] La otra modalidad es la maestría de investigación, que forma competencias científicas para generar conocimiento nuevo, con una tesis que hace un aporte original.

[clic] Nuestro propósito es que ustedes apliquen con rigor el estado del arte para resolver problemas reales.

*(Si preguntan por el doctorado: el programa se articula con el Sistema Metro de la Escuela, del pregrado al doctorado. Para detalles de homologación, remitir a la oficina de admisiones.)*

## GENERALIDADES
Vamos a los datos del programa.

[clic] Es la Maestría en Inteligencia Artificial, otorga el título de Magíster en Inteligencia Artificial y se ofrece en modalidad presencial, en Medellín.

[clic] Dura tres semestres, tiene 36 créditos y la admisión es semestral. La primera cohorte empieza en marzo de 2027.

## PORQUE
¿Por qué esta maestría?

Porque queremos formar líderes capaces de diseñar, integrar y escalar sistemas de IA responsables, desde el modelo hasta el despliegue.

[clic] Primero, trabajamos los agentes de principio a fin: desde los agentes clásicos en Fundamentos de IA hasta agentes con modelos de lenguaje en producción.

[clic] Segundo, enseñamos el ciclo actual de la IA: seleccionar, adaptar, evaluar y observar modelos.

[clic] Tercero, rigor matemático aplicado y aprender haciendo, con proyectos integradores y retos reales.

[clic] Y cuarto, IA responsable: la ética, la integridad y la gobernanza son transversales.

[clic] No se trata solo de usar IA, sino de diseñar, evaluar y liderar soluciones completas.

## Recorrido.0
Ahora, ¿cómo se recorre todo esto en tres semestres? Lo pensamos como un camino con tres etapas: fundamentos, aplicaciones avanzadas, e IA generativa y operación.

## Recorrido.1
*(Se activa el primer semestre: agente y entorno.)*

El primer semestre es el de los fundamentos. Y empezamos con algo que muchas veces se olvida: la IA, antes que modelos, es la teoría de agentes. Un agente percibe su entorno, razona, busca, planifica y actúa. Eso lo vemos en Fundamentos de IA, y es exactamente la base conceptual de los agentes con modelos de lenguaje que veremos al final.

En paralelo están Matemáticas aplicadas, Estadística aplicada, Aprendizaje automático, Aprendizaje profundo y la primera electiva.

## Recorrido.2
*(El ciclo percepción–acción en bucle.)*

Percepción, decisión, acción. Ese ciclo lo vamos a volver a encontrar más adelante.

## Recorrido.3
*(La ecuación y la frontera de clasificación.)*

Las matemáticas y la estadística son el lenguaje de todo lo demás. Esta ecuación, el descenso de gradiente, está detrás de cómo aprende casi cualquier modelo moderno. Y aquí ven la idea más básica del aprendizaje automático: un modelo que ajusta una frontera para separar dos clases a partir de los datos.

## Recorrido.4
*(La frontera se convierte en red neuronal.)*

Cuando la frontera necesita ser más compleja, pasamos al aprendizaje profundo: redes neuronales con muchas capas. Es la base de la visión, del lenguaje y de los modelos generativos.

## Recorrido.5
*(Segundo semestre: visión y lenguaje.)*

El segundo semestre es el de las aplicaciones avanzadas. En Visión por computador trabajamos detección y segmentación: que el modelo encuentre y entienda lo que hay en una imagen. En Procesamiento de lenguaje natural llegamos a los transformers y al mecanismo de atención, que es lo que está detrás de los grandes modelos de lenguaje.

En este semestre también empieza el Seminario de proyecto de grado, está Formación en integridad, con ética en datos e IA, y la segunda electiva.

## Recorrido.6
*(Tercer semestre: el agente con LLM.)*

Y en el tercer semestre todo converge. En IA generativa trabajamos los grandes modelos de lenguaje, la recuperación aumentada, el RAG, y los agentes.

Fíjense en que es el mismo ciclo del primer semestre: percibir, razonar, actuar, observar. Pero ahora el razonamiento lo hace un modelo de lenguaje que usa herramientas: busca, ejecuta código, consulta bases de datos y llama a APIs.

## Recorrido.7
*(El agente consulta sus herramientas en bucle.)*

Un agente es un modelo más herramientas, más memoria, más planificación. Y para construirlo bien necesitas todo lo anterior.

## Recorrido.8
*(La traza y las evaluaciones.)*

En Operaciones en datos e IA aprendemos a llevarlo a producción y a operarlo. Esto es una traza: el registro de cada paso de una ejecución del agente, con su duración, los tokens que gastó, lo que costó y las herramientas que usó. Con las trazas se encuentran los errores, se controlan los costos y se explica lo que hizo el sistema. Y cada versión pasa por evaluaciones continuas antes de salir.

En este semestre también están el trabajo de grado y la tercera electiva.

## Recorrido.9
En resumen: del modelo al impacto. De los fundamentos matemáticos y los agentes clásicos a agentes con modelos de lenguaje, evaluados y observados en producción.

## PlanEstudios.0
*(Semestre 1 y el contador de créditos.)*

Este es el plan de estudios completo. En el primer semestre, 12 créditos: Matemáticas aplicadas, Estadística aplicada, Fundamentos de IA, Aprendizaje automático, Aprendizaje profundo y una electiva. Al final del semestre hay un primer proyecto integrador que reúne lo aprendido.

Un dato importante: este primer semestre también funciona como línea de énfasis para nuestros estudiantes de pregrado, que pueden continuar luego en la maestría.

## PlanEstudios.1
*(Semestre 2.)*

En el segundo semestre, otros 12 créditos: Visión por computador, Procesamiento de lenguaje natural, el Seminario de proyecto de grado, Formación en integridad y la segunda electiva. Y un segundo proyecto integrador.

## PlanEstudios.2
*(Semestre 3.)*

Y en el tercero, Operaciones en datos e IA, IA generativa, la tercera electiva y el trabajo de grado, que vale 6 créditos. En total, 36 créditos.

## PlanEstudios.3
Cada asignatura de 2 créditos tiene 24 horas con el profesor y 72 horas de trabajo independiente.

## ELECTIVAS
Las electivas permiten que cada estudiante oriente su formación según sus intereses.

[clic] Si quieren más matemáticas: Estadística avanzada, Optimización o Métodos numéricos.

[clic] Si su interés es el software: Computación en la nube o Desarrollo de software para IA.

[clic] Si es el trabajo con datos: Visualización, Almacenamiento y procesamiento de grandes datos.

[clic] Y también pueden tomar asignaturas de la Maestría en Ciencias de los Datos y Analítica y de otros posgrados de la Escuela.

## DIFERENCIALES
¿Qué nos diferencia?

[clic] Una trayectoria académica completa: el programa se articula desde el pregrado, con la línea de énfasis, hasta el doctorado.

[clic] Un currículo flexible, con 9 créditos electivos.

[clic] Aprendizaje práctico, con proyectos integradores en el primer y en el segundo semestre.

[clic] Profesores de planta con doctorado, que investigan en grupos clasificados en A1 por Minciencias.

[clic] Una formación en la IA actual: agentes, evaluaciones y LLMOps integrados al plan de estudios, y conexión con el entorno a través de retos con empresas y créditos en las principales nubes.

[clic] Y microcredenciales: Fundamentos de IA, Aprendizaje profundo, Procesamiento de lenguaje natural e IA generativa conforman la Credencial en Inteligencia Artificial.

[clic] Y algo que nos importa: sería la primera maestría en IA de una universidad antioqueña, presencial en Medellín y virtual en todo el país.

## PERFILES
¿Para quién es?

[clic] Para profesionales de ciencias, ingenierías, finanzas, administración, economía o áreas afines, con bases en matemáticas, estadística y computación, que quieran liderar el desarrollo de productos y servicios basados en IA. No es necesario venir de sistemas.

[clic] Al terminar, el egresado diseña soluciones a problemas complejos construyendo, optimizando y evaluando críticamente modelos de IA, y lidera proyectos con rigor científico y responsabilidad ética.

[clic] Y puede desempeñarse como gestor de proyectos de IA, arquitecto o ingeniero de soluciones de IA, o consultor estratégico.

## TRABAJO
El trabajo de grado vale 6 créditos y tiene cuatro modalidades. [clic] Un proyecto aplicado, un artículo en revista indexada en coautoría con el director, un caso de estudio aplicado o una pasantía en un grupo de investigación.

Lo que esperamos es "saber hacer": un prototipo funcional, una solución o un modelo implementado.

[clic] Y a lo largo del programa hay charlas con expertos de la industria, retos y competencias, proyectos con empresas, ONG y entidades públicas, y seminarios sobre tendencias en IA.

## HORARIOS
En cuanto a horarios, el programa está pensado para profesionales que trabajan.

Las clases empiezan el primer fin de semana de marzo de 2027. Las asignaturas obligatorias son los viernes y los sábados; las electivas, entre semana.

[clic] Cada asignatura obligatoria se desarrolla durante tres fines de semana, [clic] [clic] y luego [clic] empieza la siguiente. No hay clases en Semana Santa ni en los fines de semana festivos.

## GRACIAS
Muchas gracias por su atención. Con gusto respondo sus preguntas.

*(Preguntas frecuentes: requisitos de admisión, costos y financiación, diferencias entre la modalidad presencial y la virtual, homologación desde la especialización y la línea de énfasis, y continuidad hacia el doctorado.)*
