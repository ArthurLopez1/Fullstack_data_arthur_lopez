import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px


def read_data():
    data_path = Path(__file__).parent / "data"
    df = pd.read_csv(data_path / "clean_yh_region.csv", index_col=0, parse_dates=[0])
    df.index = df.index.year
    return df


def layout():
    df = read_data()
    df_reset = df.reset_index(names=["year"]).style.format({"year": lambda x: f"{x}"})

    st.write("# YH Dashboard")

    st.header("This table shows educations started per region per year")

    st.markdown("## Raw data")
    st.dataframe(df_reset)

    st.header("## Trends per region")
    region = st.selectbox("Choose a region", df.columns)

    region_stats = df[region].describe()

    cols = st.columns(4)

    stats = ("min", "50%", "max")
    labels = ("min", "median", "max")

    for col, stat, label in zip(cols, stats, labels):
        with col:
            st.metric(label=label, value=region_stats[stat])

    fig = px.line(
        data_frame=df,
        x=df.index,
        y=df[region],
        title=f"started educations in {region} 2007-2023",
        labels={"index": "year", region: "started educations"},
    )

    fig.update_traces(line=dict(width=3))
    fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))

    st.plotly_chart(fig)

    read_css()


def read_css():
    css_path = Path(__file__).parent / "style.css"

    with open(css_path) as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)


if __name__ == "__main__":
    layout()
