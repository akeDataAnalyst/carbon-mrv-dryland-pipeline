import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Carbon MRV Dashboard", layout="wide")
st.title("🌳 Dryland Carbon MRV Dashboard")
st.subheader("Verra VM0047 ARR | Tree Aid Portfolio Project")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/tree_level_clean.csv")
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
selected_plots = st.sidebar.multiselect("Select Plots", options=sorted(df['plot_id'].unique()), default=sorted(df['plot_id'].unique()))
selected_species = st.sidebar.multiselect("Select Species", options=sorted(df['species'].unique()), default=sorted(df['species'].unique()))

# Filter data
df_filtered = df[(df['plot_id'].isin(selected_plots)) & (df['species'].isin(selected_species))]

# Key Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Trees", len(df_filtered))
col2.metric("Total Plots", df_filtered['plot_id'].nunique())
col3.metric("Total Carbon (t)", f"{df_filtered['carbon_ton'].sum():.3f}")
col4.metric("Total CO₂e (t)", f"{df_filtered['co2e_ton'].sum():.3f}")

# Visualizations
st.subheader("Carbon Stock per Plot")
fig1 = px.bar(df_filtered.groupby('plot_id')['carbon_ton'].sum().reset_index(),
              x='plot_id', y='carbon_ton', color='carbon_ton',
              title="Carbon Stock by Plot")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Biomass Distribution by Species")
fig2 = px.box(df_filtered, x='species', y='agb_ton', color='species')
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Carbon vs DBH Relationship")
fig3 = px.scatter(df_filtered, x='dbh_cm', y='carbon_ton', 
                  color='species', size='height_m', hover_data=['plot_id'])
st.plotly_chart(fig3, use_container_width=True)

# Data Table
if st.checkbox("Show Detailed Data"):
    st.dataframe(df_filtered, use_container_width=True)

st.caption("Developed by **Aklilu Abera** | **Carbon & Geospatial Analyst**")
