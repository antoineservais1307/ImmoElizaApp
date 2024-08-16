import streamlit as st
import pandas as pd
import joblib
from category_encoders import TargetEncoder

# Load the trained model and encoder
model = joblib.load(open("trained_model.joblib", "rb"))
encoder = joblib.load(open("encoder.joblib", "rb"))

# List of categorical columns
categoricals_columns = ['TypeOfProperty', 'Kitchen', 'PEB', 'StateOfBuilding', 'SubtypeOfProperty', 'TypeOfSale', 'District', 'ConstructionYear']

# Streamlit application
st.title("🏠 ImmoEliza 🏠")
st.header("💶 Price Predictor 💶")
st.write("Select the features of the property you want to predict the price of from the box down below")
st.write("For TypeOfProperty : 1 = House, 2 = Appartment")

TypeOfProperty = st.selectbox("TypeOfProperty", ("House", "Appartment"))
SubtypeOfProperty = st.selectbox("SubtypeOfProperty", ("house", "appartment", "villa", "ground_floor", "duplex", "penthouse", "apartment_block", "mixed_use_building", "flat_studio", "service_flat", "mansion", "kot", "town_house", "bungalow", "loft", "coubntry_cottage", "exeptional_property", "farmhouse", "triplex", "chalet", "castle", "manor_house", "pavillon", "other_property"))
TypeOfSale = st.selectbox("TypeOfSale", ("residential_sale", "residential_monthly_rent"))
LivingArea = st.number_input("Living Area", format="%0f")
PostalCode = st.number_input("Postal Code", format="%0f")
BathroomCount = st.number_input("BathroomCount", format="%0f")
BedroomCount = st.number_input("BedroomCount", format="%0f")
Furnished = st.selectbox("Furnished", ("Yes", "No"))
Fireplace = st.selectbox("Fireplace", ("Yes", "No"))
Kitchen = st.selectbox("Kitchen", ("NOT_INSTALLED", "INSTALLED", "USA_INSTALLED", "SEMI_EQUIPPED", "USA_SEMI_EQUIPPED", "HYPER_EQUIPPED", "USA_HYPER_EQUIPPED"))
PEB = st.selectbox("PEB", ("A++", "A+", "A", "B", "C", "D", "E", "F", "G"))
StateOfBuilding = st.selectbox("State Of Building", ("AS_NEW", "GOOD", "TO_BE_DONE_UP", "TO_RENOVATE", "JUST_RENOVATED", "TO_RESTORE"))
NumberOfFacades = st.number_input("Number of Facades", format="%0f")
Garden = st.selectbox("Garden", ("Yes", "No"))
GardenArea = st.number_input("Garden Area", format="%0f")
SwimmingPool = st.selectbox("Swimming Pool", ("Yes", "No"))
Terrace = st.selectbox("Terrace", ("Yes", "No"))
ConstructionYear = st.number_input("Construction Year", format="%0f")
District = st.selectbox("District", ("Brussels", "Antwerp", "Liège", "Brugge", "Gent", "Halle-Vilvoorde", "Turnhout", "Nivelles", "Leuven", "Oostend", "Kortrijk", "Aalst", "Mechelen", "Namur", "Charleroi", "Hasselt", "Veurne", "Sint-Niklaas", "Mons", "Verviers", "Roeselare", "Dendermonde", "Tournai", "Oudenaarde", "Soignies", "Tielt", "Thuin", "Dinant", "Maaseik", "Eeklo", "Tongeren", "Mouscron", "Huy", "Ath", "Diksmuide", "Marche-en-Famenne", "Arlon", "Waremme", "Neufchâteau", "Virton", "Ieper", "Bastogne", "Philippeville"))

# Prepare the input dictionary
inputs = {
    "TypeOfProperty": TypeOfProperty,
    "SubtypeOfProperty": SubtypeOfProperty,
    "TypeOfSale": TypeOfSale,
    "LivingArea": LivingArea,
    "PostalCode": PostalCode,
    "BathroomCount": BathroomCount,
    "BedroomCount": BedroomCount,
    "Furnished": Furnished,
    "Fireplace": Fireplace,
    "Kitchen": Kitchen,
    "PEB": PEB,
    "StateOfBuilding": StateOfBuilding,
    "NumberOfFacades": NumberOfFacades,
    "Garden": Garden,
    "GardenArea": GardenArea,
    "SwimmingPool": SwimmingPool,
    "Terrace": Terrace,
    "ConstructionYear": ConstructionYear,
    "District": District
}

if st.button("Predict Price"):
    # Convert categorical values to numerical values as per the original script
    for key, value in inputs.items():
        if value == "Yes":
            inputs[key] = 1
        elif value == "No":
            inputs[key] = 0
        elif value == "House":
            inputs[key] = 1
        elif value == "Appartment":
            inputs[key] = 2

    # Create a DataFrame for the input
    house_df = pd.DataFrame([inputs])

    # Apply the encoder to the categorical columns
    house_df[categoricals_columns] = encoder.transform(house_df[categoricals_columns])

    # Make a prediction
    prediction = model.predict(house_df)

    # Display the result
    st.subheader(f"Predicted Price = {prediction[0]} €")
