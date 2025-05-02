# src/data_prep.py
"""
data_prep.py

Funciones de carga y limpieza de las tablas raw para PSet4_Showz_Marketing:

- visits   : Uid, Device, Start_Ts, End_Ts, Source_Id
- orders   : Uid, Buy_Ts, Revenue
- costs    : source_id, dt, costs

Cada función:
  1) Lee el CSV
  2) Parsea las fechas a datetime
  3) Ajusta dtypes (Uid y source IDs a str, montos a float)
  4) Elimina duplicados exactos
  5) Elimina filas con datos críticos faltantes
"""

import pandas as pd

def load_visits(path_csv: str, output_csv: str = None) -> pd.DataFrame:
    """
    Carga y limpia la tabla visits.
    - path_csv: ruta al CSV (ej. 'data/raw/visits.csv')
    - output_csv: ruta para guardar el CSV limpio (ej. 'data/clean/visits_clean.csv')
    
    Devuelve un DataFrame con:
      * Uid          → str
      * Device       → str
      * Start_Ts     → datetime64[ns]
      * End_Ts       → datetime64[ns]
      * Source_Id    → str
    """
    df = pd.read_csv(
        path_csv,
        parse_dates=['Start Ts', 'End Ts'],
        dtype={'Device': str, 'Uid': 'uint64', 'Source Id': 'Int64'}
    )
    
    # Eliminar duplicados exactos
    n_dup = df.duplicated().sum()
    if n_dup:
        print(f"[visits] Eliminando {n_dup} filas duplicadas")
        df = df.drop_duplicates()
    
    # Eliminar filas sin Uid o sin timestamps
    df = df.dropna(subset=['Uid', 'Start Ts', 'End Ts'])
    
    # Si se proporciona un archivo de salida, guarda el DataFrame limpio
    if output_csv:
        df.to_csv(output_csv, index=False)
        print(f"Archivo limpio guardado como: {output_csv}")
    
    return df.reset_index(drop=True)

def load_orders(path_csv: str, output_csv: str = None) -> pd.DataFrame:
    """
    Carga y limpia la tabla orders.
    - path_csv: ruta al CSV (ej. 'data/raw/orders.csv')
    - output_csv: ruta para guardar el CSV limpio (ej. 'data/clean/orders_clean.csv')
    
    Devuelve un DataFrame con:
      * Uid       → str
      * Buy_Ts    → datetime64[ns]
      * Revenue   → float64
    """
    df = pd.read_csv(
        path_csv,
        parse_dates=['Buy Ts'],
        dtype={'Uid': 'uint64'}
    )
    
    # Asegurar que Revenue sea numérico
    df['Revenue'] = pd.to_numeric(df['Revenue'], errors='raise')
    
    # Eliminar duplicados exactos
    n_dup = df.duplicated().sum()
    if n_dup:
        print(f"[orders] Eliminando {n_dup} filas duplicadas")
        df = df.drop_duplicates()
    
    # Eliminar filas sin Uid, Buy_Ts o Revenue inválido
    df = df.dropna(subset=['Uid', 'Buy Ts', 'Revenue'])
    
    # Si se proporciona un archivo de salida, guarda el DataFrame limpio
    if output_csv:
        df.to_csv(output_csv, index=False)
        print(f"Archivo limpio guardado como: {output_csv}")
    
    return df.reset_index(drop=True)

def load_costs(path_csv: str, output_csv: str = None) -> pd.DataFrame:
    """
    Carga y limpia la tabla costs.
    - path_csv: ruta al CSV (ej. 'data/raw/costs.csv')
    - output_csv: ruta para guardar el CSV limpio (ej. 'data/clean/costs_clean.csv')
    
    Devuelve un DataFrame con:
      * source_id → str
      * dt        → datetime64[ns]
      * costs     → float64
    """
    df = pd.read_csv(
        path_csv,
        parse_dates=['dt'],
        dtype={'source_id': 'Int64'}
    )
    # Asegurar que costs sea numérico
    df['costs'] = pd.to_numeric(df['costs'], errors='raise')
    # Eliminar duplicados exactos
    n_dup = df.duplicated().sum()
    if n_dup:
        print(f"[costs] Eliminando {n_dup} filas duplicadas")
        df = df.drop_duplicates()
    # Eliminar filas sin source_id, dt o costs inválido
    df = df.dropna(subset=['source_id', 'dt', 'costs'])
    # Renombrar columna a Source_Id para homogeneidad
    df = df.rename(columns={'source_id': 'Source_Id', 'dt': 'Dt', 'costs': 'Costs'})
    
    # Si se proporciona un archivo de salida, guarda el DataFrame limpio
    if output_csv:
        df.to_csv(output_csv, index=False)
        print(f"Archivo limpio guardado como: {output_csv}")
    
    return df.reset_index(drop=True)


def summarize_df(df: pd.DataFrame, name: str) -> None:
    """
    Imprime un pequeño resumen del DataFrame:
      - forma (filas × columnas)
      - dtypes
      - duplicados
      - valores nulos por columna
    """
    print(f"\n== Resumen: {name} ==")
    print("Shape:", df.shape)
    print("Dtypes:\n", df.dtypes)
    print("Duplicados:", df.duplicated().sum())
    print("Nulos por columna:\n", df.isna().sum())