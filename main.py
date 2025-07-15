import streamlit as st
from scraper import get_ev_matches

st.set_page_config(page_title="Gasoline to EV Replacement Tool", layout="centered")

# Styling (clean and bold section titles)
st.markdown("""
    <style>
        .main-title {
            font-size: 2.5em;
            font-weight: 700;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 6px;
            padding: 0.4em 1em;
            margin-top: 1em;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">Gasoline to EV Replacement Tool</div>', unsafe_allow_html=True)
st.write("Enter a gasoline vehicle below to find potential electric replacements based on public EV databases.")

# Input fields
make = st.text_input("Gasoline Vehicle Make")
model = st.text_input("Gasoline Vehicle Model")
year = st.text_input("Model Year (e.g. 2018)")

# Search button
if st.button("Find Electric Alternatives"):
    if not (make and model and year):
        st.warning("Please enter make, model, and year.")
    else:
        st.info("Searching for matches...")
        try:
            results = get_ev_matches(make, model, year)

            if results is not None and not results.empty:
                for source in results["Source"].unique():
                    st.subheader(f"Results from {source}")
                    source_data = results[results["Source"] == source].drop(columns=["Source"])
                    st.dataframe(source_data)
                    st.markdown("---")
            else:
                st.warning("No matches found from any source.")
        except Exception as e:
            st.error(f"An error occurred: {e}")






