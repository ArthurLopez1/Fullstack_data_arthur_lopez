import streamlit as st
import pandas as pd
from pathlib import Path

def read_data():
    data_path = Path(__file__).parent / "data"
    df = pd.read_csv(data_path / "clean_yh_region.csv", index_col=0, parse_dates=[0])
    df.index = df.index.year
    return df

def layout():
    df = read_data()
    df_reset = df.reset_index(names=["year"]).style.format({"year": lambda x: f"{x}"})
    
    st.markdown("# YH Dashboard")
    
    st.dataframe(df_reset)
    
if __name__ == "__main__":
    layout()
    