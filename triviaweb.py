import streamlit as st
import random
import time

# =====================================================================
# CONFIGURACIÓN VISUAL Y COLORES (Diseño llamativo y responsive)
# =====================================================================
st.set_page_config(page_title="Trivia Escolar Interactiva", layout="centered")

# Inyectamos estilos personalizados para cambiar el fondo aburrido por un degradado alegre
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    h1 {
        color: #2E4053 !important;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .stButton>button {
        background-color: #3498DB !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 10px 20px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background-color: #2980B9 !important;
        transform: scale(1.02);
    }
    .css-11vccas {
        background-color: white !important;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }
    </style>
""",  unsafe_allow_html=True)

# =====================================================================
# BASE DE DATOS DE PREGUNTAS ORGANIZADA POR GRADOS (1° a 5°)
# =====================================================================
# Puedes seguir aumentando decenas de preguntas dentro de cada grado siguiendo la misma estructura.
BANCO_POR_GRADOS = {
    "1° Grado de Secundaria": [
        {
            "pregunta": "¿Cuál es la capital del departamento de Loreto en el Perú?",
            "imagen": None,
            "opciones": ["Pucallpa", "Tarapoto", "Iquitos", "Moyobamba"],
            "correcta": "Iquitos"
        },
        {
            "pregunta": "¿Cuál es el órgano del cuerpo humano encargado de bombear la sangre a todo el organismo?",
            "imagen": None,
            "opciones": ["Los pulmones", "El cerebro", "El corazón", "El hígado"],
            "correcta": "El corazón"
        },
        {
            "pregunta": "¿Cuál es el río más largo y caudaloso del mundo?",
            "imagen": None,
            "opciones": ["Río Nilo", "Río Misisipi", "Río Amazonas", "Río Rin"],
            "correcta": "Río Amazonas"
        }, 
        {
            "pregunta": "Cuál es la unidad básica y estructural de todos los seres vivos",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["El átomo", "La célula", "El tejido", "El órgano"],
            "correcta": "La célula"
        },
        {
            "pregunta": "Cuál es el único planeta del sistema solar conocido que alberga vida",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Marte", "Venus", "Tierra", "Júpiter"],
            "correcta": "Tierra"
        },
        {
            "pregunta": "Qué gas absorben las plantas de la atmósfera para realizar la fotosíntesis",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Oxígeno", "Nitrógeno", "Dióxido de carbono", "Hidrógeno"],
            "correcta": "Dióxido de carbono"
        },
        {
            "pregunta": "Qué estado de la materia tiene volumen fijo pero una forma que se adapta al recipiente que lo contiene",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Sólido", "Líquido", "Gaseoso", "Plasmático"],
            "correcta": "Líquido"
        },
        {
            "pregunta": "Qué civilización antigua construyó las famosas pirámides de Giza y momificaba a sus faraones",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["La egipcia", "La griega", "La romana", "La mesopotámica"],
            "correcta": "La egipcia"
        },
        {
            "pregunta": "En qué continente se originó la especie humana",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Europa", " Asia", "África", "América"],
            "correcta": "África"
        },
        {
            "pregunta": "Cómo se llamaba el sistema social y económico de la Edad Media basado en feudos, señores y siervos",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Capitalismo", "Feudalismo", "Esclavismo", "Socialismo"],
            "correcta": "Feudalismo"
        },
        {
            "pregunta": "Cuál era la capital del vasto Imperio Inca en Sudamérica",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Lima", "Cusco", "Machu Picchu", "Quito"],
            "correcta": "Cusco"
        },
        {
            "pregunta": "Qué invento de Johannes Gutenberg en el siglo XV facilitó la producción masiva de libros en el mundo",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["El papel", " El pergamino", "La imprenta de tipos móviles", "La máquina de escribir"],
            "correcta": "La imprenta de tipos móviles"
        },
        {
            "pregunta": "Cuál es la línea imaginaria que divide a la Tierra en Hemisferio Norte y Hemisferio Sur",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["El meridiano de Greenwich", "El trópico de Cáncer", " La línea del Ecuador", "El trópico de Capricornio"],
            "correcta": "La línea del Ecuador"
        },
        {
            "pregunta": "Cuál es el río más caudaloso y largo del planeta ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["El río Nilo", "El río Misisipi", "El río Amazonas", "El río Yangtsé"],
            "correcta": "El río Amazonas "
        },
        {
            "pregunta": "Cuál es el país más grande del mundo en cuanto a extensión territorial ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Canadá", "China", "Estados Unidos", "Rusia"],
            "correcta": "Rusia "
        },
        {
            "pregunta": "En qué océano se encuentra la fosa de las Marianas, el punto más profundo de la Tierra ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Océano Atlántico", "Océano Índico", "Océano Pacífico", "Océano Ártico"],
            "correcta": " Océano Pacífico "
        },
        {
            "pregunta": "Cómo se les llama a las palabras que se escriben diferente pero tienen el mismo significado, como 'feliz' y contento",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Sinónimos", "Antónimos", "Antónimos", "Parónimas"],
            "correcta": "Sinónimos "
        },
        {
            "pregunta": "Qué tipo de palabra funciona como el núcleo del sujeto en una oración ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["El verbo", "El adjetivo", "El sustantivo", "El adverbio"],
            "correcta": " El sustantivo "
        },
        {
            "pregunta": "Cuáles son las palabras que llevan la mayor fuerza de voz en la última sílaba y se tildan cuando terminan en N, S o vocal ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Graves o llanas", "Esdrújulas", "Sobreesdrújulas", "Agudas"],
            "correcta": "Agudas "
        },
        {
            "pregunta": "Quién es el legendario personaje literario que luchaba contra molinos de viento creyendo que eran gigantes ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Sancho Panza", "OpcDon Quijote de la Manchaión", " El Cid Campeador", "Robin Hood"],
            "correcta": "Don Quijote de la Mancha "
        },
        {
            "pregunta": "Qué recurso literario consiste en exagerar la realidad para darle más énfasis, como decir 'te lo he dicho un millón de veces'",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Metáfora", "Hipérbole", "Personificación", "Símil"],
            "correcta": "Hipérbole "
        },
        {
            "pregunta": "Cómo se llama el triángulo que tiene sus tres lados con longitudes totalmente diferentes ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Triángulo equilátero", "Triángulo isósceles", "Triángulo escaleno", "Triángulo rectángulo"],
            "correcta": "Triángulo escaleno "
        },
        {
            "pregunta": "Cuál es el resultado de multiplicar cualquier número por cero ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["El mismo número", "Cero", "Uno", "Infinito"],
            "correcta": "Cero "
        },
        {
            "pregunta": "Si un ángulo mide exactamente 90 grados, ¿cómo se le clasifica ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Ángulo agudo", " Ángulo obtuso", "Ángulo llano", "Ángulo recto"],
            "correcta": "Ángulo recto "
        },
        {
            "pregunta": "Qué número sigue en la secuencia lógica: 2, 4, 8, 16, ... ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": [" 20", "24", "32", "64"],
            "correcta": "32 "
        },
        {
            "pregunta": "Qué nombre recibe la línea recta que une el centro de un círculo con cualquier punto de su borde ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Diámetro", "Cuerda", "Secante", "Radio"],
            "correcta": "Radio "
        },
        {
            "pregunta": "Qué instrumento de viento es conocido por tener teclas blancas y negras y usar un teclado, aunque produce sonido mediante cuerdas percutidas ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["El piano", " El acordeón", "El órgano", "La flauta"],
            "correcta": "El piano "
        },
        {
            "pregunta": "Cuántos colores componen de forma natural el arcoíris ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Cinco", "Seis", "Siete", "Ocho"],
            "correcta": "Siete "
        },
        {
            "pregunta": "En qué continente se celebraron los primeros Juegos Olímpicos de la antigüedadcribe ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["Asia", "Europa", "África", "Oceanía"],
            "correcta": "Europa (en Grecia) "
        },
        {
            "pregunta": "Cuál es el metal que se encuentra en estado líquido a temperatura ambiente y se usaba antes en los termómetros ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": ["El hierro", "El mercurio", "El plomo", "El aluminio"],
            "correcta": "El mercurio "
        },
        {

            "pregunta": "Qué científico es famoso por formular la teoría de la relatividad y la ecuación E=mc² ",
            "imagen": None, # Cambia por "imagenes/foto.png" si usas imagen
            "opciones": [" Isaac Newton", " Galileo Galilei", "Albert Einstein", " Nikola Tesla"],
            "correcta": "Albert Einstein "
        }

    ],
    
    "2° Grado de Secundaria": [
        {
            "pregunta": "¿Qué cultura preínca es famosa por sus impresionantes trepanaciones craneanas?",
            "imagen": None,
            "opciones": ["Cultura Nazca", "Cultura Paracas", "Cultura Chavín", "Cultura Mochica"],
            "correcta": "Cultura Paracas"
        },
        {
            "pregunta": "En biología, ¿cuál es el estado de la materia donde las partículas están sumamente juntas y apenas vibran?",
            "imagen": None,
            "opciones": ["Líquido", "Gaseoso", "Sólido", "Plasmático"],
            "correcta": "Sólido"
        },
        {
                "pregunta": "¿Qué tipo de energía se encuentra almacenada en los alimentos y se libera durante la digestión?",
                "imagen": None,
                "opciones": ["Energía cinética", "Energía química", "Energía térmica", "Energía nuclear"],
                "correcta": "Energía química"
            },
            {
                "pregunta": "¿Qué drástico cambio histórico del siglo XVIII sustituyó el trabajo manual por las máquinas y el uso del vapor?",
                "imagen": None,
                "opciones": ["La Revolución Francesa", "La Revolución Industrial", "La Ilustración", "El Renacimiento"],
                "correcta": "La Revolución Industrial"
            },
            {
                "pregunta": "¿Cómo se llaman los bloques gigantes en los que está dividida la corteza terrestre y cuyos movimientos causan sismos?",
                "imagen": None,
                "opciones": ["Capas de la atmósfera", "Placas tectónicas", "Fallas marinas", "Relieves continentales"],
                "correcta": "Placas tectónicas"
            },
            {
                "pregunta": "¿Qué función cumplen los adjetivos calificativos dentro de una oración?",
                "imagen": None,
                "opciones": ["Indicar la acción que realiza el sujeto", "Reemplazar al sustantivo", "Modificar al sustantivo expresando una cualidad o característica", "Unir dos palabras o ideas distintas"],
                "correcta": "Modificar al sustantivo expresando una cualidad o característica"
            },
            {
                "pregunta": "¿Cómo se llama el polígono regular que tiene exactamente ocho lados iguales?",
                "imagen": None,
                "opciones": ["Hexágono", "Heptágono", "Octágono", "Decágono"],
                "correcta": "Octágono"
            },
            {
                "pregunta": "¿Qué célebre dramaturgo inglés escribió la trágica historia de amor de 'Romeo y Julieta'?",
                "imagen": None,
                "opciones": ["Charles Dickens", "William Shakespeare", "Miguel de Cervantes", "Oscar Wilde"],
                "correcta": "William Shakespeare"
            },
            {
                "pregunta": "¿Cuál es el orgánulo celular encargado de producir la energía de la célula mediante la respiración celular?",
                "imagen": "imagenes/mitocondria.png",
                "opciones": ["El cloroplasto", "El ribosoma", "La mitocondria", "El aparato de Golgi"],
                "correcta": "La mitocondria"
            },
            {
                "pregunta": "¿Qué movimiento intelectual y cultural del siglo XVIII defendía el uso de la razón y la ciencia frente a la superstición?",
                "imagen": None,
                "opciones": ["El Barroco", "La Ilustración", "El Feudalismo", "El Absolutismo"],
                "correcta": "La Ilustración"
            },
            {
                "pregunta": "¿Cuál es el desierto más extenso y caluroso del planeta, ubicado en el norte de África?",
                "imagen": None,
                "opciones": ["Desierto de Atacama", "Desierto de Gobi", "Desierto del Sahara", "Desierto de Kalahari"],
                "correcta": "Desierto del Sahara"
            },
            {
                "pregunta": "¿Cómo se les llama a las palabras que se pronuncian igual pero tienen significados y escrituras diferentes, como 'tubo' y 'tuvo'?",
                "imagen": None,
                "opciones": ["Sinónimas", "Homófonas", "Antónimas", "Parónimas"],
                "correcta": "Homófonas"
            },
            {
                "pregunta": "¿Cómo se llama el teorema matemático que establece que en todo triángulo rectángulo la suma de los cuadrados de los catetos es igual al cuadrado de la hipotenusa?",
                "imagen": None,
                "opciones": ["Teorema de Tales", "Teorema de Pitágoras", "Teorema de Euclides", "Ley de senos"],
                "correcta": "Teorema de Pitágoras"
            },
            {
                "pregunta": "¿Qué sustancia de color verde presente en las hojas de las plantas es la encargada de absorber la luz del sol?",
                "imagen": None,
                "opciones": ["Hemoglobina", "Melanina", "Clorofila", "Caroteno"],
                "correcta": "Clorofila"
            },
            {
                "pregunta": "¿Qué fuerza universal descubierta por Isaac Newton atrae a los cuerpos según su masa?",
                "imagen": None,
                "opciones": ["Fuerza magnética", "Fuerza de fricción", "Fuerza de gravedad", "Fuerza eléctrica"],
                "correcta": "Fuerza de gravedad"
            },
            {
                "pregunta": "¿Qué imperio conquistó la ciudad de Constantinopla en 1453, marcando el fin de la Edad Media?",
                "imagen": None,
                "opciones": ["El Imperio Romano", "El Imperio Otomano", "El Imperio Mongol", "El Imperio Carolingio"],
                "correcta": "El Imperio Otomano"
            },
            {
                "pregunta": "¿Qué capa de la atmósfera concentra la mayor cantidad de gases y es donde ocurren los fenómenos climáticos como la lluvia?",
                "imagen": None,
                "opciones": ["Troposfera", "Estratosfera", "Mesosfera", "Termosfera"],
                "correcta": "Troposfera"
            },
            {
                "pregunta": "¿Qué género literario agrupa a las obras escritas en verso donde el autor expresa sus sentimientos y emociones?",
                "imagen": None,
                "opciones": ["Género lírico", "Género narrativo", "Género dramático", "Género didáctico"],
                "correcta": "Género lírico"
            },
            {
                "pregunta": "¿Cuál es el resultado de resolver la operación matemática con potencia: 5 al cubo (5³)?",
                "imagen": None,
                "opciones": ["15", "25", "75", "125"],
                "correcta": "125"
            },
            {
                "pregunta": "¿En qué país europeo se originó el movimiento artístico e intelectual conocido como el Renacimiento?",
                "imagen": None,
                "opciones": ["Francia", "España", "Italia", "Alemania"],
                "correcta": "Italia"
            },
            {
                "pregunta": "¿Cómo se llama el proceso biológico por el cual las células se dividen para formar dos células hijas idénticas?",
                "imagen": None,
                "opciones": ["Meiosis", "Mitosis", "Mutación", "Fecundación"],
                "correcta": "Mitosis"
            },
            {
                "pregunta": "¿Qué navegante comandó la expedición española que completó la primera vuelta al mundo en la historia?",
                "imagen": None,
                "opciones": ["Cristóbal Colón", "Juan Sebastián Elcano", "Hernán Cortés", "Francisco Pizarro"],
                "correcta": "Juan Sebastián Elcano"
            },
            {
                "pregunta": "En álgebra, ¿cómo se le llama a una igualdad matemática que contiene una o más cantidades desconocidas llamadas incógnitas?",
                "imagen": None,
                "opciones": ["Expresión", "Ecuación", "Variable", "Fracción"],
                "correcta": "Ecuación"
            },
            {
                "pregunta": "¿Cuál es la capital oficial de Italia, famosa por albergar el Coliseo?",
                "imagen": None,
                "opciones": ["Milán", "Venecia", "Florencia", "Roma"],
                "correcta": "Roma"
            },
            {
                "pregunta": "¿Cuál es la sílaba que recibe la mayor fuerza de voz en una palabra, lleve o no tilde escrita?",
                "imagen": None,
                "opciones": ["Sílaba átona", "Sílaba tónica", "Prefijo", "Sufijo"],
                "correcta": "Sílaba tónica"
            },
            {
                "pregunta": "¿Qué tipo de animal es la ballena azul, considerado el ser vivo más grande que habita nuestro planeta?",
                "imagen": None,
                "opciones": ["Pez", "Mamífero", "Anfibio", "Reptil"],
                "correcta": "Mamífero"
            }
        
    ],
    "3° Grado de Secundaria": [
        {
            "pregunta": "¿Qué estructura celular se encarga de fabricar las proteínas a partir del ARN?",
            "imagen": "imagenes/ribosoma.png",
            "opciones": ["Mitocondria", "Ribosoma", "Núcleo", "Aparato de Golgi"],
            "correcta": "Ribosoma"
        },
        {
            "pregunta": "¿En qué año se proclamó la Independencia del Perú de forma oficial por José de San Martín?",
            "imagen": None,
            "opciones": ["1810", "1821", "1824", "1879"],
            "correcta": "1821"
        },
        {
            "pregunta": "Cómo se les llama a los átomos de un mismo elemento químico que tienen el mismo número de protones pero diferente número de neutrones ?",
            "imagen": None,
            "opciones": ["Isótopos", "Isóbaros", "Iones", "Moléculas"],
            "correcta": "1821"
        },
        {
            "pregunta": "Cuál es el compuesto químico universal, formado por dos átomos de hidrógeno y uno de oxígeno, indispensable para la vida ?",
            "imagen": None,
            "opciones": ["Dióxido de carbono", "Agua", "Metano", "Ácido clorhídrico"],
            "correcta": "Agua"
        },
        {
            "pregunta": "Qué biomolécula contiene la información genética hereditaria que determina las características de un ser vivo ?",
            "imagen": None,
            "opciones": ["Las proteínas", "Los lípidos", "El ADN", " Los carbohidratos"],
            "correcta": "El ADN"
        },
        {
            "pregunta": "Cómo se denominan las filas horizontales en las que se organiza la tabla periódica de los elementos ?",
            "imagen": None,
            "opciones": ["Grupos", "Familias", "Periodos", "Bloques"],
            "correcta": "Periodos"
        },
        {
            "pregunta": "Qué tipo de enlace químico se produce cuando dos átomos comparten electrones para alcanzar la estabilidad ?",
            "imagen": None,
            "opciones": ["Enlace iónico", "Enlace covalente", "Enlace metálico", "Enlace de hidrógeno"],
            "correcta": "Enlace covalente"
        },
        {
            "pregunta": "¿Qué conflicto armado de escala global se desarrolló entre los años 1914 y 1918?",
            "imagen": None,
            "opciones": ["La Segunda Guerra Mundial", "La Guerra Fría", "La Primera Guerra Mundial", "La Guerra de los Cien Años"],
            "correcta": "La Primera Guerra Mundial"
        },
        {
            "pregunta": "¿Qué drástico proceso del siglo XIX consistió en la expansión y dominio de las potencias europeas sobre territorios de África y Asia?",
            "imagen": None,
            "opciones": ["El Imperialismo", " El Renacimiento", " El Renacimiento", "La Globalización"],
            "correcta": "El Imperialismo"
        },
        {
            "pregunta": "¿Qué documento histórico fue proclamado en 1789 durante la Revolución Francesa, defendiendo los derechos de igualdad y libertad?",
            "imagen": None,
            "opciones": ["La Carta Magna", "La Declaración de los Derechos del Hombre y del Ciudadano", "El Tratado de Versalles", "El Código de Hammurabi"],
            "correcta": "La Declaración de los Derechos del Hombre y del Ciudadano"
        },
        {
            "pregunta": "¿Qué periodo de tensión política e ideológica dividió al mundo en dos bloques (capitalista y comunista) tras la Segunda Guerra Mundial?",
            "imagen": None,
            "opciones": ["La Gran Depresión", " El Imperio Napoleónico", "La Guerra Fría", " La Paz Armada"],
            "correcta": "La Guerra Fría"
        },
        {
            "pregunta": "¿Qué país de América logró su independencia formal en el año 1776, convirtiéndose en una república federal?",
            "imagen": None,
            "opciones": ["México", "Brasil", "Canadá", "Estados Unidos"],
            "correcta": " Estados Unidos"
        },
        {
            "pregunta": "Cuál es la capa de gas ozono que protege a la Tierra absorbiendo la mayor parte de la radiación ultravioleta dañina del sol",
            "imagen": None,
            "opciones": ["Ionosfera", "Ozonosfera (Capa de ozono)", "Exosfera", "Termosfera"],
            "correcta": "Ozonosfera (Capa de ozono)"
        },
        {
            "pregunta": "Cuál es el océano que separa el continente americano de los continentes europeo y africano",
            "imagen": None,
            "opciones": [" Océano Índico", "Océano Pacífico", " Océano Atlántico", "Océano Ártico"],
            "correcta": "Océano Atlántico"
        },
        {
            "pregunta": "Qué nombre recibe el fenómeno climático global caracterizado por el aumento a largo plazo de la temperatura media del sistema climático de la Tierra",
            "imagen": None,
            "opciones": ["Efecto invernadero natural", "Calentamiento global", "Presión atmosférica", "Deforestación"],
            "correcta": "Calentamiento globa"
        },
        {
            "pregunta": "Qué país de Europa se encuentra geográficamente ubicado en la península Ibérica junto a Portugal",
            "imagen": None,
            "opciones": ["Francia", "Italia", "España", "Grecia"],
            "correcta": "España"
        },
        {
            "pregunta": "Qué estrecho canal artificial conecta el océano Atlántico con el océano Pacífico en América Central, facilitando el comercio marítimo mundial",
            "imagen": None,
            "opciones": ["El canal de Suez", " El canal de Panamá", " El estrecho de Gibraltar", "El estrecho de Magallanes"],
            "correcta": "El canal de Panam"
        },
        {
            "pregunta": "Qué movimiento literario y artístico del siglo XIX se caracterizó por la exaltación de los sentimientos, la libertad creadora y el idealismo",
            "imagen": None,
            "opciones": ["El Clasicismo", "El Romanticismo", "El Realismo", "El Barroco"],
            "correcta": "El Romanticismo"
        },
        {
            "pregunta": "Cómo se le llama a la forma de composición literaria que simula un diálogo real y está escrita para ser representada en un teatro",
            "imagen": None,
            "opciones": ["Género dramático", "Género lírico", "Género ensayístico", "Género epistolar"],
            "correcta": "Género dramático"
        },
        {
            "pregunta": "Cómo se clasifican las palabras que llevan el acento o la mayor fuerza de voz en la penúltima sílaba",
            "imagen": None,
            "opciones": ["Agudas", "Graves o llanas", "Esdrújulas", "Sobreesdrújulas"],
            "correcta": "Graves o llanas"
        },
        {
            "pregunta": "Qué elemento de la oración expresa la acción, estado o proceso que realiza o experimenta el sujeto",
            "imagen": None,
            "opciones": ["El sustantivo", "El adjetivo", "El verbo", "El artículo"],
            "correcta": "El verbo"
        },
        {
            "pregunta": "Qué figura retórica consiste en establecer una relación de identidad o sustitución entre dos ideas sin usar nexos como la palabra 'como', por ejemplo: 'Tus cabellos son de oro'",
            "imagen": None,
            "opciones": ["Símil", "Hipérbole", "Metáfora", "Anáfora"],
            "correcta": "Metáfora"
        },
        {
            "pregunta": "En álgebra, ¿cómo se denomina a la expresión matemática que consta de la suma o resta de dos términos o monomios",
            "imagen": None,
            "opciones": ["Monomio", "Binomio", "Trinomio", "Polinomio de cuatro términos"],
            "correcta": "Binomio"
        },
        {
            "pregunta": "Cuál es el valor aproximado de la constante matemática Pi (\(\pi \)), utilizada para calcular el área y perímetro de un círculo",
            "imagen": None,
            "opciones": ["2.7182", "1.4142", "3.1416", "0.5772"],
            "correcta": "3.1416"
        },
        {
            "pregunta": "Cómo se le conoce en estadística al valor que aparece con mayor frecuencia en un conjunto de datos numéricos?",
            "imagen": None,
            "opciones": ["Media aritmética", "Mediana", "Moda", "Rango"],
            "correcta": "Moda"
        },
        {
            "pregunta": "Qué tipo de ecuación matemática tiene la forma general \(ax^2 + bx + c = 0\), donde la incógnita está elevada al cuadrado",
            "imagen": None,
            "opciones": ["Ecuación lineal", "Ecuación de primer grado", "Ecuación cuadrática o de segundo grado", "Ecuación cúbica"],
            "correcta": "Ecuación cuadrática o de segundo grado"
        },
        {
            "pregunta": "Si en una bolsa hay 3 bolas rojas y 7 bolas azules, ¿cuál es la probabilidad matemática de sacar una bola roja al azar",
            "imagen": None,
            "opciones": ["3%", "30% (o 3/10)", "70% (o 7/10)", "50%"],
            "correcta": "30% (o 3/10)"
        },
        {
            "pregunta": "Qué famoso científico polaco propuso la teoría heliocéntrica, demostrando que la Tierra y los planetas giran alrededor del Sol",
            "imagen": None,
            "opciones": ["Nicolás Copérnico", "Nicolás Copérnico", "Isaac Newton", "René Descartes"],
            "correcta": "Nicolás Copérnico"
        },
        {
            "pregunta": "Qué país asiático es conocido popularmente en el mundo como 'La tierra del sol naciente'",
            "imagen": None,
            "opciones": ["China", "Corea del Sur", "Japón", "Tailandia"],
            "correcta": "Japón"
        },
        {
            "pregunta": "Qué célebre pintor neerlandés, exponente del postimpresionismo, es el autor del famoso cuadro 'La noche estrellada'",
            "imagen": None,
            "opciones": ["Pablo Picasso", "Vincent van Gogh", "Claude Monet", " Salvador Dalí"],
            "correcta": "Vincent van Gogh"
        },
        {
            "pregunta": "Qué importante órgano del sistema nervioso central coordina las funciones cognitivas, la memoria y las emociones en el ser humano",
            "imagen": None,
            "opciones": ["La médula espinal", "El cerebelo", " El cerebro", "El bulbo raquídeo"],
            "correcta": "El cerebro"
        },
        {
            "pregunta": "En qué año del siglo XX comenzó formalmente la Segunda Guerra Mundial con la invasión a Polonia",
            "imagen": None,
            "opciones": [" 1914", "1939", "1945", "v"],
            "correcta": "1939"
        }
    ],
    "4° Grado de Secundaria": [
        {
            "pregunta": "¿Qué evento histórico de 1789 dio inicio a la Revolución Francesa y la Edad Contemporánea?",
            "imagen": "imagenes/revolucion.png",
            "opciones": ["La Toma de la Bastilla", "La Declaración de Independencia de EE.UU.", "La Coronación de Napoleón", "El Descubrimiento de América"],
            "correcta": "La Toma de la Bastilla"
        },
        {
            "pregunta": "Si un elemento químico pertenece al grupo de los Gases Nobles, ¿cuál de los siguientes podría ser?",
            "imagen": None,
            "opciones": ["Oxígeno", "Hidrógeno", "Helio", "Hierro"],
            "correcta": "Helio"
        }
    ],
    "5° Grado de Secundaria": [
        {
            "pregunta": "De acuerdo al modelo atómico moderno, ¿qué partículas subatómicas se encuentran en el núcleo?",
            "imagen": "imagenes/atomo.png",
            "opciones": ["Solo electrones", "Electrones y protones", "Protones y neutrones", "Fotones y electrones"],
            "correcta": "Protones y neutrones"
        },
        {
            "pregunta": "¿Quién escribió la célebre obra literaria peruana 'Tradiciones Peruanas'?",
            "imagen": None,
            "opciones": ["César Vallejo", "Mario Vargas Llosa", "Ricardo Palma", "Abraham Valdelomar"],
            "correcta": "Ricardo Palma"
        }
    ]
}

# =====================================================================
# CONTROL DEL ESTADO DEL JUEGO
# =====================================================================
if "iniciado" not in st.session_state:
    st.session_state.iniciado = False
    st.session_state.preguntas_ronda = []
    st.session_state.indice_actual = 0
    st.session_state.respuestas_usuario = []
    st.session_state.tiempo_inicio = 0
    st.session_state.grado_seleccionado = ""

# =====================================================================
# PANTALLA VISUAL
# =====================================================================
st.markdown("<h1>🎓 Trivia Escolar de Secundaria 🚀</h1>", unsafe_allow_html=True)

# 1. PANTALLA DE INICIO: Selección de Grado
if not st.session_state.iniciado:
    st.write("### ¡Hola, estudiante! Elige tu año escolar para comenzar el desafío:")
    
    # Menú desplegable para los grados
    grado = st.selectbox(
        "Selecciona tu grado actual:",
        ["1° Grado de Secundaria", "2° Grado de Secundaria", "3° Grado de Secundaria", "4° Grado de Secundaria", "5° Grado de Secundaria"]
    )
    
    st.info("⏱️ Tendrás un máximo de 20 preguntas seleccionadas al azar y un tiempo límite global de 5 minutos.")
    
    if st.button("🏁 INICIAR DESAFÍO", width="stretch"):
        preguntas_disponibles = BANCO_POR_GRADOS[grado]
        # Tomar máximo 20 preguntas de ese grado específico al azar
        cantidad = min(20, len(preguntas_disponibles))
        
        st.session_state.preguntas_ronda = random.sample(preguntas_disponibles, cantidad)
        st.session_state.indice_actual = 0
        st.session_state.respuestas_usuario = []
        st.session_state.tiempo_inicio = time.time()
        st.session_state.grado_seleccionado = grado
        st.session_state.iniciado = True
        st.rerun()

# 2. PANTALLA DE JUEGO ACTIVO
else:
    st.caption(f"📍 Jugando en: **{st.session_state.grado_seleccionado}**")
    
    # Cronómetro (300 segundos = 5 minutos)
    tiempo_transcurrido = time.time() - st.session_state.tiempo_inicio
    tiempo_restante = 300 - tiempo_transcurrido
    
    if tiempo_restante <= 0:
        st.error("🛑 ¡Tiempo agotado! El examen ha finalizado automáticamente.")
        st.session_state.indice_actual = len(st.session_state.preguntas_ronda)
    else:
        mins, segs = divmod(int(tiempo_restante), 60)
        st.metric(label="⏱️ Tiempo Restante", value=f"{mins:02d}:{segs:02d}")

    # Mostrar preguntas una a una
    if st.session_state.indice_actual < len(st.session_state.preguntas_ronda):
        pregunta_actual = st.session_state.preguntas_ronda[st.session_state.indice_actual]
        
        st.write(f"### Pregunta {st.session_state.indice_actual + 1}:")
        st.markdown(f"#### {pregunta_actual['pregunta']}")
        
        if pregunta_actual["imagen"]:
            try:
                st.image(pregunta_actual["imagen"], width="stretch")
            except:
                st.caption("(Imagen de apoyo no encontrada)")
                
        st.write("Selecciona la respuesta correcta:")
        for opcion in pregunta_actual["opciones"]:
            if st.button(opcion, key=f"{opcion}_{st.session_state.indice_actual}", width="stretch"):
                st.session_state.respuestas_usuario.append({
                    "pregunta": pregunta_actual["pregunta"],
                    "tu_respuesta": opcion,
                    "correcta": pregunta_actual["correcta"]
                })
                st.session_state.indice_actual += 1
                st.rerun()
                
    # =====================================================================
    # 3. PANTALLA DE REPORTES FINALES CON REACCIONES ANIMADAS
    # =====================================================================
    else:
        st.success("🏁 ¡Cuestionario finalizado con éxito!")
        
        correctas = sum(1 for r in st.session_state.respuestas_usuario if r["tu_respuesta"] == r["correcta"])
        total = len(st.session_state.preguntas_ronda)
        
        # Calculamos la nota en base 20 (puedes ajustar si la ronda tiene menos preguntas)
        nota_base_20 = int((correctas / total) * 20) if total > 0 else 0
        
        st.markdown(f"<h2>📊 Tu Nota Final: <span style='color:#2E4053;'>{nota_base_20} de 20</span></h2>", unsafe_allow_html=True)
        st.write(f"Acertaste **{correctas}** preguntas de un total de **{total}**.")
        
        # -----------------------------------------------------------------
        # SISTEMA DE EMOCIONES Y CELEBRACIÓN SEGÚN LA NOTA
        # -----------------------------------------------------------------
        st.write("---")
        
        # CASO 1: Menos de 10 (Renegando / Molesto)
        if nota_base_20 < 10:
            st.markdown("<h1 style='font-size: 80px; margin: 0;'>😡💢</h1>", unsafe_allow_html=True)
            st.error("### ¡No te rindas! Te sacaste una nota baja. ¡A estudiar más para la próxima!")
            
        # CASO 2: Menos de 15 (Más o menos alegre / Conforme)
        elif nota_base_20 < 15:
            st.markdown("<h1 style='font-size: 80px; margin: 0;'>😐👍</h1>", unsafe_allow_html=True)
            st.warning("### ¡Pasaste! Tienes una nota regular. ¡Estuviste cerca, puedes mejorar mucho más!")
            
        # CASO 3: De 15 a 20 (Súper Feliz + Fuegos Artificiales de celebración)
        else:
            st.markdown("<h1 style='font-size: 80px; margin: 0;'>🤩🥳👑</h1>", unsafe_allow_html=True)
            st.success(f"### ¡Felicidades! Excelente desempeño. ¡Te sacaste un notón de {nota_base_20}!")
            # Efecto especial en pantalla que simula la ráfaga de fuegos artificiales/globos
            st.balloons()
            
        st.write("---")
        
        # Desglose de respuestas para retroalimentación
        st.subheader("📋 Revisión de tus respuestas:")
        for idx, r in enumerate(st.session_state.respuestas_usuario, 1):
            if r["tu_respuesta"] == r["correcta"]:
                st.markdown(f"**{idx}. {r['pregunta']}**")
                st.markdown(f"🟢 *Tu respuesta es correcta:* {r['tu_respuesta']}")
            else:
                st.markdown(f"**{idx}. {r['pregunta']}**")
                st.markdown(f"🔴 *Tu respuesta:* {r['tu_respuesta']}")
                st.markdown(f"💡 *La respuesta correcta era:* {r['correcta']}")
            st.write("")
            
        if st.button("🔄 Cambiar de Grado / Reiniciar", width="stretch"):
            st.session_state.iniciado = False
            st.rerun()
