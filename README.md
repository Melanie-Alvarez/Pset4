# Análisis de Cohortes de Marketing para Showz

Este proyecto realiza un análisis de cohortes para evaluar el comportamiento de los usuarios en una plataforma de comercio en línea, considerando métricas de fidelidad como DAU (Usuarios Activos Diarios), WAU (Usuarios Activos Semanales) y MAU (Usuarios Activos Mensuales), así como el cálculo del Lifetime Value (LTV) y el costo de adquisición de clientes (CAC) para optimizar la asignación de presupuesto en marketing.

## Estructura del Proyecto

El código está dividido en varias secciones clave:

### 1. **Carga y limpieza de datos**

Se cargan y limpian tres datasets principales:
- **Visitas**: Información sobre las visitas a la plataforma.
- **Órdenes**: Información sobre las compras realizadas por los usuarios.
- **Costos**: Gastos asociados con las campañas de marketing.

La limpieza de los datos se realiza utilizando funciones personalizadas que preparan los datos para el análisis posterior.

### 2. **Métricas de fidelidad**

Se calculan tres métricas fundamentales de fidelidad:
- **DAU (Usuarios Activos Diarios)**: Mide cuántos usuarios únicos visitan la plataforma cada día.
- **WAU (Usuarios Activos Semanales)**: Mide la cantidad de usuarios únicos que visitan la plataforma cada semana.
- **MAU (Usuarios Activos Mensuales)**: Mide la cantidad de usuarios únicos que visitan la plataforma cada mes.

Estas métricas son esenciales para entender el comportamiento de los usuarios a lo largo del tiempo.

### 3. **Análisis de sesiones**

Se analiza la cantidad de sesiones por día, la frecuencia de regreso de los usuarios y la duración de las sesiones. Estos análisis proporcionan información sobre la retención y el nivel de interacción de los usuarios con la plataforma.

### 4. **Análisis de cohortes**

El análisis de cohortes se centra en la retención de usuarios a lo largo del tiempo. Los usuarios son agrupados según la fecha de su primera visita y su comportamiento posterior es analizado para identificar patrones de deserción y fidelización.

### 5. **Análisis de compras y ventas**

Se estudia el comportamiento de compra de los usuarios, incluyendo el tiempo que tardan en realizar su primera compra después de su primera visita, cuántos pedidos realizan y el ticket promedio de sus compras.

### 6. **Métricas de marketing**

Se calculan dos métricas clave para evaluar la efectividad de las campañas de marketing:
- **CAC (Costo de Adquisición de Clientes)**: Se calcula el costo por cliente adquirido a través de cada fuente de marketing.
- **ROMI (Retorno sobre la Inversión en Marketing)**: Se evalúa el retorno generado por cada dólar invertido en marketing.

### 7. **Visualización de datos**

Se generan varias visualizaciones para analizar las métricas y resultados de manera más clara. Los gráficos incluyen:
- **Gráficos de DAU, WAU y MAU**.
- **Gráfico de sesiones por usuario**.
- **Mapa de calor de la retención de cohortes**.

### 8. **Conclusiones**

El análisis concluye con recomendaciones para optimizar el presupuesto de marketing, basadas en los datos obtenidos sobre la retención de usuarios y la efectividad de las campañas. Se sugiere redirigir el presupuesto hacia las fuentes más rentables y mejorar la fidelización de los usuarios en las cohortes más jóvenes.

## Requisitos

Este proyecto requiere las siguientes librerías:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `plotly`

Para instalar las dependencias, usa el siguiente comando:

```bash
pip install -r requirements.txt
