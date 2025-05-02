import pandas as pd

def create_cohorts(df, date_column='Buy_Ts'):
    # Asegurarse de que la columna de fecha esté en formato datetime
    df[date_column] = pd.to_datetime(df[date_column])

    # Crear la columna Cohort con el primer mes de compra
    df['Cohort'] = df.groupby('Uid')[date_column].transform('min').dt.to_period('M')
    
    return df

def cohort_retention(df, date_column='Buy_Ts', cohort_column='Cohort'):
    # Asegurarse de que la columna de fecha esté en formato datetime
    df[date_column] = pd.to_datetime(df[date_column])

    # Añadir una columna que muestra el mes de cada compra en términos relativos a la cohorte
    df['CohortMonth'] = (df[date_column].dt.to_period('M') - df[cohort_column]).apply(lambda x: x.n)
    
    # Contar el número de usuarios en cada cohorte por mes
    cohort_counts = df.groupby([cohort_column, 'CohortMonth'])['Uid'].nunique().unstack(fill_value=0)

    # Calcular la tasa de retención (usuarios activos en cada mes dividido por los usuarios originales en la cohorte)
    cohort_sizes = cohort_counts.iloc[:, 0]  # Tamaño de la cohorte original
    retention = cohort_counts.divide(cohort_sizes, axis=0)
    
    return retention

def cohort_ltv(df, date_column='Buy_Ts', cohort_column='Cohort', revenue_column='Revenue'):
    # Asegurarse de que la columna de fecha esté en formato datetime
    df[date_column] = pd.to_datetime(df[date_column])

    # Calcular el LTV por cohorte sumando los ingresos generados por cada cohorte
    cohort_ltv = df.groupby([cohort_column])[revenue_column].sum()
    
    return cohort_ltv

def cohort_cac(df_orders, df_costs, cohort_column='Cohort'):
    # Calcular el número de compradores únicos por cohorte
    cohort_customers = df_orders.groupby(cohort_column)['Uid'].nunique()
    
    # Sumar los costos de marketing por cohorte
    cohort_costs = df_costs.groupby(cohort_column)['Costs'].sum()
    
    # Calcular el CAC
    cohort_cac = cohort_costs / cohort_customers
    
    return cohort_cac
