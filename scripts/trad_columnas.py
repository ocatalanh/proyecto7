import pandas as pd

# Definir la función con anotaciones de tipo
def trad_columnas(data: pd.DataFrame) -> pd.DataFrame:
    """
    Renombra las columnas de un DataFrame de pandas de inglés a español.

    Parameters:
    data (pd.DataFrame): El DataFrame original con nombres de columnas en inglés.

    Returns:
    pd.DataFrame: El DataFrame con los nombres de columnas renombrados a español.
    """
    # Diccionario que mapea los nombres de las columnas de inglés a español
    new_column_names = {
        'Your Current Country.': 'PaisActual',
        'Your Current Zip Code / Pin Code': 'CodigoPostalActual',
        'Your Gender': 'Genero',
        'Which of the below factors influence the most about your career aspirations ?': 'FactoresInfluenciaCarrera',
        'Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it.': 'EducacionSuperiorExtranjero',
        'How likely is that you will work for one employer for 3 years or more ?': 'ProbabilidadLealtadLaboral',
        'Would you work for a company whose mission is not clearly defined and publicly posted.': 'TrabajariaEmpresaMisionNoDefinida',
        'How likely would you work for a company whose mission is misaligned with their public actions or even their product ?': 'ProbabilidadTrabajarMisionDesalineada',
        'How likely would you work for a company whose mission is not bringing social impact ?': 'ProbabilidadTrabajarSinImpactoSocial',
        'What is the most preferred working environment for you.': 'EntornoTrabajoPreferido',
        'Which of the below Employers would you work with.': 'EmpleadoresPreferidos',
        'Which type of learning environment that you are most likely to work in ?': 'EntornoAprendizajePreferido',
        'Which of the below careers looks close to your Aspirational job ?': 'CarreraAspiracional',
        'What type of Manager would you work without looking into your watch ?': 'TipoGerentePreferido',
        'Which of the following setup you would like to work ?': 'ConfiguracionPreferida'
    }

    # Renombrar las columnas del DataFrame usando el diccionario
    data = data.rename(columns=new_column_names)
    return data
