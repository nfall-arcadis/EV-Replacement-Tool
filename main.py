import streamlit as st
from scraper import get_ev_matches

st.title("Gasoline to EV Replacement Tool")
st.write("👋 Enter a vehicle and click the button to begin.")

try:
    vehicle_input = st.text_input("Enter a gasoline vehicle:")

    if st.button("Find Electric Alternatives"):
        st.write("Searching...")
        results = get_ev_matches(vehicle_input)

        if results is not None and not results.empty:
            st.success("Results found!")
            st.table(results)
        else:
            st.warning("No matches found or scraping returned nothing.")
except Exception as e:
    st.error(f"An error occurred: {e}")



