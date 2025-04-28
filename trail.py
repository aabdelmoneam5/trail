import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import scipy.stats as linrgress
from scipy.interpolate import interp1d

st.title("MD & MDT interpolation Tool")
survey_file = st.file_uploader("Upload your directional survey data (CSV/Excel)", type=['csv', 'xlsx'])
st.write(survey_file)
if survey_file:
    survey_data = pd.read_excel(survey_file)
    st.dataframe(survey_data)
    well_names = survey_data["Well_Name"].unique()
    st.write(well_names)
    selected_well = st.sidebar.selectbox("Select Well Name", well_names)
    st.write(selected_well)
    selected_well = st.sidebar.selectbox("Select Well Name", well_names)
    st.write(selected_well)
    survey_columns = survey_data.columns.to_list()
    st.write(survey_columns)
    well_names = survey_data["Well_Name"].unique()
    st.write(well_names)
    selected_well = st.sidebar.selectbox("Select Well Name", well_names)
    st.write(selected_well)
