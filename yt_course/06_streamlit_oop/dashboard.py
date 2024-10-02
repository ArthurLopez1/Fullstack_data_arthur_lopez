import streamlit as st
from components.data import MedalsSummer

medals_df = MedalsSummer()

def layout():
    st.markdown("# Summer olympics dashboard")
    st.markdown(
        """
        This dashboard shows 124 years of olympic data. In this demo, only summer olympics will be shown.
        The source of the dataset comes from here https://www.kaggle.com/datasets/nitishsharma01/olympics-124-years-datasettill-2020
        
        """
    )
    
    st.dataframe(medals_df.data)
    
    
if __name__ == "__main__":
    layout()
    
    