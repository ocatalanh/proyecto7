#Funciones que se contruyeron el proceso de analasis y se traen para facilitar el codigo
import pandas as pd

def reemplazar(data: pd.DataFrame):
     # Verificar los tipos de los argumentos
    if not isinstance(data, pd.DataFrame):
        raise TypeError("El primer argumento debe ser un DataFrame")


    #Diccionario de reemplazos
    reemplazos = {
        'Germany': 'Alemania',
        'United Arab Emirates': 'Emiratos Árabes Unidos',
        'United States of America': 'Estados Unidos',
        'Male': 'Masculino',
        'Female': 'Femenino',
        'My Parents': 'Mis Padres',
        'People who have changed the world for better': 'Personas que cambiaron el mundo para mejor',
        'People from my circle, but not family members': 'Personas de mi circulo, pero no de mi familia',
        'Influencers who had successful careers': 'Influencer con carreras exitosas',
        'Social Media like LinkedIn': 'Redes sociales como LinkedIn',
        'Yes, I will earn and do that': 'Si, ganaría lo suficiente y lo haría',
        'No I would not be pursuing Higher Education outside of India': 'No, no buscaría Educación Superior fuera de la India',
        'No, But if someone could bare the cost I will': 'No, pero si alguien pudiera cubrir el costo lo haría',
        'This will be hard to do, but if it is the right company I would try': 'Eso sería dificil, pero si es la compañía correcta lo intentaría',
        'Will work for 3 years or more': 'Trabajaría por 3 años o más',
        'No way, 3 years with one employer is crazy': 'De ninguna forma, 3 años con un empleador es para volverse loco',
        'Yes': 1,
        'No': 0,
        'Will NOT work for them': 0,
        'Will work for them':  1,
        'Fully Remote with Options to travel as and when needed': 'Completamente remoto con opciones de viajar cuando sea necesario',
        'Hybrid Working Environment with less than 15 days a month at office': 'Entorno de trabajo híbrido con menos de 15 días al mes en la oficina',
        'Every Day Office Environment': 'Entorno de oficina todos los días',
        'Hybrid Working Environment with less than 10 days a month at office': 'Entorno de trabajo híbrido con menos de 10 días al mes en la oficina',
        'Hybrid Working Environment with less than 3 days a month at office': 'Entorno de trabajo híbrido con menos de 3 días al mes en la oficina',
        'Fully Remote with No option to visit offices': 'Completamente remoto sin opción de visitar oficinas',
        'Employer who pushes your limits by enabling an learning environment, and rewards you at the end': 'Empleador que te lleva al límite proporcionando un entorno de aprendizaje y te recompensa al final',
        'Employer who appreciates learning and enables that environment': 'Empleador que aprecia el aprendizaje y facilita ese entorno',
        'Employer who rewards learning and enables that environment': 'Empleador que recompensa el aprendizaje y facilita ese entorno',
        "Employer who pushes your limits and doesn't enables learning environment and never rewards you": 'Empleador que te lleva al límite pero no proporciona un entorno de aprendizaje y nunca te recompensa',
        "Employers who appreciates learning but doesn't enables an learning environment": 'Empleador que aprecia el aprendizaje pero no proporciona un entorno de aprendizaje',
        'Self Paced Learning Portals, Instructor or Expert Learning Programs': 'Portales de aprendizaje autodirigido, Programas de aprendizaje con instructor o experto',
        'Instructor or Expert Learning Programs, Trial and error by doing side projects within the company': 'Programas de aprendizaje con instructor o experto, Prueba y error haciendo proyectos paralelos dentro de la empresa',
        'Instructor or Expert Learning Programs, Learning by observing others': 'Programas de aprendizaje con instructor o experto, Aprendizaje observando a otros',
        'Self Paced Learning Portals, Learning by observing others' : 'Portales de aprendizaje autodirigido, Aprendizaje observando a otros',
        'Learning by observing others, Trial and error by doing side projects within the company': 'Aprendizaje observando a otros, Prueba y error haciendo proyectos paralelos dentro de la empresa',
        'Self Paced Learning Portals, Trial and error by doing side projects within the company': 'Portales de aprendizaje autodirigido, Prueba y error haciendo proyectos paralelos dentro de la empresa',
        'Design and Creative strategy in any company': 'Estrategia de diseño y creatividad en cualquier empresa',
        'Look deeply into Data and generate insights': 'Analizar datos profundamente y generar insights',
        'Business Operations in any organization': 'Operaciones comerciales en cualquier organización',
        'Manage and drive End-to-End Projects or Products' : 'Gestionar y dirigir proyectos o productos de principio a fin',
        'Build and develop a Team': 'Construir y desarrollar un equipo',
        'Teaching in any of the institutes/online or Offline': 'Enseñar en cualquier institución (en línea o presencial)',
        'Work as a freelancer and do my thing my way': 'Trabajar como freelancer y hacer las cosas a mi manera',
        'Design and Develop amazing software': 'Diseñar y desarrollar software increíble',
        'Become a content Creator in some platform': 'Convertirse en un creador de contenido en alguna plataforma',
        'Work in a BPO setup for some well known client': 'Trabajar en un centro de atención al cliente para algún cliente conocido',
        'Manager who explains what is expected, sets a goal and helps achieve it': 'Gerente que explica lo que se espera, establece un objetivo y ayuda a alcanzarlo',
        'Manager who clearly describes what she/he needs': 'Gerente que describe claramente lo que necesita',
        'Manager who sets goal and helps me achieve it': 'Gerente que establece un objetivo y me ayuda a alcanzarlo',
        'Manager who sets targets and expects me to achieve it' : 'Gerente que establece objetivos y espera que los logre',
        'Manager who sets unrealistic targets': 'Gerente que establece objetivos inalcanzables',
        'Work with 5 to 6 people in my team': 'Trabajar con 5 a 6 personas en mi equipo',
        'Work with 2 to 3 people in my team': 'Trabajar con 2 a 3 personas en mi equipo',
        'Work alone': 'Trabajar solo',
        'Work with more than 10 people in my team' : 'Trabajar con más de 10 personas en mi equipo',
        'Work with 7 to 10 or more people in my team': 'Trabajar con 7 a 10 o más personas en mi equipo'
    }

    
    # Reemplazar valores 
    df_replace = data.replace(reemplazos)
    return df_replace
    