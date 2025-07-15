import pandas as pd

def get_ev_matches(gas_vehicle_query):
    # Dummy data for testing UI
    return pd.DataFrame({
        "Make": ["Tesla", "Ford"],
        "Model": ["Model 3", "F-150 Lightning"],
        "Price": ["$38,990", "$49,995"]
    })


