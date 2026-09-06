import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Water Leak Digital Twin",
    page_icon="💧",
    layout="wide"
)

st.title("💧 AI-Based Digital Twin for Water Leak Impact & Response Optimisation")

st.write(
    "Digital Twin dashboard for water network simulation, "
    "leak analysis and AI prediction."
)

# Load dataset
try:
    df = pd.read_csv("dataset.csv")
    st.success("Dataset loaded successfully")
except Exception as e:
    st.error(e)
    st.stop()

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Dashboard",
        "Dataset",
        "Leak Statistics"
    ]
)

# Dashboard
if page == "Dashboard":

    st.header("Project Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Scenarios",
        len(df)
    )

    c2.metric(
        "Features",
        len(df.columns)
    )

    c3.metric(
        "Leak Locations",
        df["Leak_Junction"].nunique()
    )

    c4.metric(
        "Leak Sizes",
        df["Leak_Size"].nunique()
    )


# Dataset
elif page == "Dataset":

    st.header("Generated Simulation Dataset")

    st.dataframe(
        df.head(100),
        use_container_width=True
    )


# Statistics
elif page == "Leak Statistics":

    st.header("Leak Analysis")

    st.subheader("Leak Junction Distribution")

    st.bar_chart(
        df["Leak_Junction"].value_counts()
    )


    st.subheader("Leak Size Distribution")

    st.bar_chart(
        df["Leak_Size"].value_counts()
    )


    st.subheader("Demand Distribution")

    st.bar_chart(
        df["Demand"].value_counts()
    )

	