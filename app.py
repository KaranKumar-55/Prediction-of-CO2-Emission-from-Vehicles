import streamlit as st
import joblib
st.title("""
          Prediction of CO2 Emission from vehicles
         
         "**Predict the **C02 Emssions** based on the features.**"
         """)
# Load the linear regression model
lr_model = joblib.load('LR_model.pkl')

# # Title of the app
st.title("Feature Selection")
# Dropdown for selecting Model Year
selected_year = st.selectbox("Select Model Year", list(range(1995, 2024)), index=0)

# Mapping for Vehicle Class
vehicle_class_mapping = {
    # "Select": None,  # You can set a default value like None for "Select"
    "subcompact": 7, #d
    "compact": 0, #d
    "two-seater": 9, #d
    "station wagon": 6, #d
    "minicompact": 3, #d
    "mid-size": 2, #d
    "full-size": 1,
    "pickup truck": 5, #d
    "van": 10, # d
    "suv": 8, # d
    "other": 4 # d
}
selected_vehicle_class = st.selectbox("Select Vehicle Class", list(vehicle_class_mapping.keys()))
# Get the encoded value based on user selection
encoded_vehicle_class = vehicle_class_mapping[selected_vehicle_class]
# Mapping for Fuel Type
fuel_type_mapping = {
    # "Select": None,  # You can set a default value like None for "Select"
    "Regular gasoline": 4,
    "Premium gasoline": 3,
    "Diesel": 0,
    "Natural gas": 2,
    "Ethanol": 1
}
selected_fuel_type = st.selectbox("Select Fuel Type", list(fuel_type_mapping.keys()))
# Get the encoded value based on user selection
encoded_fuel_type = fuel_type_mapping[selected_fuel_type]
# Mapping for Transmission
transmission_mapping = {
    # "Select": None,  # You can set a default value like None for "Select"
    "Automatic": 1,
    "Manual": 4,
    "Automatic of Selective type": 2,
    "CVT": 3,
    "Automated Manual": 0
}
selected_transmission = st.selectbox("Select Transmission", list(transmission_mapping.keys()))
# Get the encoded value based on user selection
encoded_transmission = transmission_mapping[selected_transmission]
# Dropdown for selecting Cylinders
cylinders_options = [4, 6, 5, 8, 12, 10, 3, 2, 16]
cylinders_options.sort()
selected_cylinders = st.selectbox("Select Cylinders", cylinders_options)
# Dropdown for selecting Engine Size (L)
engine_size_options = [1.8, 3.2, 3.0, 2.8, 2.2, 6.7, 2.0, 2.5, 4.0, 5.4, 3.1, 3.8, 5.7, 2.3, 4.6,
                        4.9, 3.4, 4.3, 3.3, 3.5, 1.5, 8.0, 2.4, 5.5, 1.3, 1.9, 5.0, 1.0, 2.7,
                          1.6, 4.5, 6.0, 4.2, 3.6, 2.9, 6.5, 3.9, 5.2, 5.9, 5.8,
                            2.6, 1.2, 4.4, 4.1, 4.8, 5.3, 4.7, 1.7, 3.7, 8.3, 5.6,
                              6.1, 0.8, 7.0, 6.2, 6.8, 8.4, 6.6, 1.4, 6.4, 6.3, 2.1, 0.9]
engine_size_options.sort()
selected_engine_size = st.selectbox("Select Engine Size (L)", engine_size_options)
# Button to submit the selected features
if st.button("Submit"):
    # Display the selected features
    st.write(f"Selected Model Year: {selected_year}")
    st.write(f"Selected Vehicle Class: {selected_vehicle_class}")
    st.write(f"Selected Fuel Type: {selected_fuel_type}")
    st.write(f"Selected Transmission: {selected_transmission}")
    st.write(f"Selected Cylinders: {selected_cylinders}")
    st.write(f"Selected Engine Size (L): {selected_engine_size}")
# Reset button to clear selections
if st.button("Reset"):
    st.experimental_rerun()

lr2 = joblib.load('fuel_C.pkl')
# Previous code for prediction
Fuel_c = lr2.predict([[selected_year, encoded_vehicle_class,selected_engine_size, selected_cylinders,
              encoded_transmission , encoded_fuel_type]])
Fuel_c_value = Fuel_c[0]

# Example: Collect user input
user_input = [selected_year, encoded_vehicle_class,selected_engine_size, selected_cylinders,
              encoded_transmission , encoded_fuel_type, Fuel_c_value]
# Use the loaded model to make predictions
predictions = lr_model.predict([user_input])
# Display the predictions
st.write(f"CO2 Emissions : {predictions[0]:.2f} g/km")


















































# # Dropdown for selecting Vehicle Class
# vehicle_class_options = ['subcompact', 'compact', 'two-seater', 'station wagon', 'minicompact', 'mid-size', 'full-size', 'pickup truck', 'van', 'suv', 'other']
# selected_vehicle_class = st.selectbox("Select Vehicle Class", vehicle_class_options)




# # Dropdown for selecting Fuel Type
# fuel_type_options = ['Regular gasoline', 'Premium gasoline', 'Diesel', 'Natural gas', 'Ethanol']
# selected_fuel_type = st.selectbox("Select Fuel Type", fuel_type_options)


# # Dropdown for selecting Transmission
# transmission_options = ['Automatic', 'Manual', 'Automatic of Selective type', 'CVT', 'Automated Manual']
# selected_transmission = st.selectbox("Select Transmission", transmission_options)


# import streamlit as st

# # Title of the app
# st.title("Feature Selection")

# # Dropdown for selecting Model Year with "Select" as the initial value
# selected_year = st.selectbox("Select Model Year", ["Select"] + list(map(str, range(1995, 2024))))


# # Mapping for Fuel Type
# fuel_type_mapping = {
#     "Select": None,  # You can set a default value like None for "Select"
#     "Regular gasoline": 0,
#     "Premium gasoline": 1,
#     "Diesel": 2,
#     "Natural gas": 3,
#     "Ethanol": 4
# }
# selected_fuel_type = st.selectbox("Select Fuel Type", list(fuel_type_mapping.keys()))

# # Get the encoded value based on user selection
# encoded_fuel_type = fuel_type_mapping[selected_fuel_type]

# # Mapping for Transmission
# transmission_mapping = {
#     "Select": None,  # You can set a default value like None for "Select"
#     "Automatic": 0,
#     "Manual": 1,
#     "Automatic of Selective type": 2,
#     "CVT": 3,
#     "Automated Manual": 4
# }
# selected_transmission = st.selectbox("Select Transmission", list(transmission_mapping.keys()))

# # Get the encoded value based on user selection
# encoded_transmission = transmission_mapping[selected_transmission]

# # Button to submit the selected features
# if st.button("Submit"):
#     # Display the selected features
#     st.write(f"Selected Model Year: {selected_year}")
#     st.write(f"Selected Vehicle Class: {encoded_vehicle_class}")
#     st.write(f"Selected Fuel Type: {encoded_fuel_type}")
#     st.write(f"Selected Transmission: {encoded_transmission}")
   
# # Reset button to clear selections
# if st.button("Reset"):
#     st.experimental_rerun()
