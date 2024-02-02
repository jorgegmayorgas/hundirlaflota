import pandas as pd
from scipy.stats import pearsonr
def describe_df(df):
    """
    Función que devuelve un dataframe con 
    * El tipo de datos por columna
    * El porcentaje de nulos
    * La cantidad de valores únicos
    * La cardinalidad de la columna en porcentaje

    Argumentos:
    df (pandas dataframe): Variable dataframe de Pandas a describir.
    

    Retorna:
    tipo: Dataframe
    """
    tipo_de_dato = df.dtypes
    valores_nulos = (df.isna().mean() * 100).round(2)
    valores_unicos = df.nunique()
    cardinalidad = ((df.nunique()/df.shape[0])*100).round(2)

    descripcion = pd.DataFrame({
        'Tipo de dato': tipo_de_dato,
        'Valores nulos (%)': valores_nulos,
        'Valores unicos': valores_unicos,
        'Cardinalidad (%)': cardinalidad
    })

    return descripcion.T

def get_features_num_regression(df, target_col, umbral_corr, pvalue=None):
    """
    Función que devuelve una lista con las columnas numéricas 
    del dataframe cuya correlación con la columna designada 
    por "target_col" sea superior en valor absoluto al valor dado 
    por "umbral_corr". 
    
    Además si la variable "pvalue" es distinta de None, sólo devolvera 
    las columnas numéricas cuya correlación supere el valor indicado y 
    además supere el test de hipótesis con significación 
    mayor o igual a 1-pvalue

    Argumentos:
    df (pandas.DataFrame): Variable que contiene dataframe de Pandas.
    target_col (string): Nombre de la columna target de un modelo de regresión
    umbral_corr (float): Umbral de correlación, entre 0 y 1.
    pvalue (int): Descripción de param1.

    Retorna:
    list: Lista de Python
    """
    # Verificamos si existe algún error al llamar a la columna 'target_col'
    if target_col not in df.columns:
        print(f"Error: La columna '{target_col}' no está bien indicada, no se puede asignar como 'target_col'.")
        return None

    # Verificamos si 'target_col' es una variable numérica continua
    if not np.issubdtype(df[target_col].dtype, np.number):
        print(f"Error: La columna '{target_col}' no es una variable numérica continua.")
        return None

    # Verificamos si 'umbral_corr' está en el rango [0, 1]
    if not (0 <= umbral_corr <= 1):
        print("Error: Se ha indicado un 'umbral_corr' incorrecto, debe estar entre el rango [0, 1].")
        return None
    
    # Verificamos si 'pvalue' es un valor válido
    if pvalue is not None and (not isinstance(pvalue, (float, int)) or pvalue <= 0 or pvalue >= 1):
        print("Error: Si 'pvalue' no es 'None', debe tener un valor entre (0, 1).")
        return None

    # Obtenemos las columnas numéricas del dataframe
    cols_numericas = df.select_dtypes(include=[np.number]).columns

    # Calculamos la correlación y p-value para cada columna numérica con 'target_col'
    correlaciones = []
    for col in cols_numericas:
        corr, p_value = pearsonr(df[col], df[target_col])
        correlaciones.append((col, corr, p_value))

    # Filtramos las columnas basadas en 'umbral_corr' y 'pvalue'
    features_seleccionadas = []
    for col, corr, p_value in correlaciones:
        if abs(corr) > umbral_corr and (pvalue is None or p_value < 1 - pvalue):
            features_seleccionadas.append((col, corr, p_value))

    # Devolvemos la lista de características seleccionadas junto con sus correlaciones y valores p
    return features_seleccionadas
