# 🏠 ImmoEliza - Real Estate Price Predictor
Introduction
ImmoEliza is a web application designed to predict real estate prices based on various property features. The application leverages machine learning models to provide accurate price estimates for different types of properties across Belgium.

## The project consists of two main components:

- A FastAPI backend that serves the prediction model.
- A Streamlit frontend that provides a user interface for inputting property features and displaying the predicted price.
Features
- Property Features: Input key features of the property like the type, subtype, living area, number of bedrooms, bathrooms, kitchen type, etc.
- Real-time Price Prediction: Get instant price predictions based on the provided property features.
- User-Friendly Interface: Easy-to-use Streamlit interface for interacting with the prediction model.
## Installation
### Prerequisites
Ensure you have the following installed:

- Python 3.7+
- Pip (Python package installer)
- Setup
- Clone the repository:

```bash
git clone https://github.com/antoineservais1307/ImmoElizaApp.git
```
- go to the folder 
```bash
cd ImmoElizaApp
```
Install the required packages:

```bash
pip install -r requirements.txt
```
Ensure you have the trained model and encoder files in the project directory:

- trained_model.joblib
- encoder.joblib
- Usage
- Running the Application
- Start the FastAPI Server: The FastAPI server will run in a separate thread to handle predictions.

### Launch the Streamlit Frontend:

```bash
streamlit run app.py
```
### Open your browser and navigate to http://localhost:8501 to access the Streamlit interface.

## Predicting a Price
### 1. Fill in the property details using the dropdowns and input boxes.
### 2. Click on the "Predict Price" button to get the estimated price of the property.
### 3. The predicted price will be displayed in the interface.

![Alt Text](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnM0bmIxcHd4Z2pmbW41MDcycmhzeXJ5emNneWRtM3JrcjVjaWdtZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0HTYUmU67pLWv1a8/giphy.gif)




## API Endpoints
### The FastAPI backend exposes the following endpoint:

POST /predict: Predicts the price of a property.

### Request Body:

```json

{
    "BathroomCount": int,
    "BedroomCount": int,
    "Fireplace": "Yes" | "No",
    "Furnished": "Yes" | "No",
    "Garden": "Yes" | "No",
    "GardenArea": int,
    "LivingArea": int,
    "NumberOfFacades": int,
    "SwimmingPool": "Yes" | "No",
    "Terrace": "Yes" | "No",
    "PostalCode": int,
    "TypeOfProperty": "House" | "Appartment",
    "Kitchen": "NOT_INSTALLED" | "INSTALLED" | "USA_INSTALLED" | "SEMI_EQUIPPED" | "USA_SEMI_EQUIPPED" | "HYPER_EQUIPPED" | "USA_HYPER_EQUIPPED",
    "PEB": "A++" | "A+" | "A" | "B" | "C" | "D" | "E" | "F" | "G",
    "StateOfBuilding": "AS_NEW" | "GOOD" | "TO_BE_DONE_UP" | "TO_RENOVATE" | "JUST_RENOVATED" | "TO_RESTORE",
    "SubtypeOfProperty": str,
    "TypeOfSale": "residential_sale" | "residential_monthly_rent",
    "ConstructionYear": int,
    "District": str
}
```
### Response:

```json
{
    "predicted_price": float
}
```
### Contributing
Contributions are welcome! Please open an issue or submit a pull request with your changes.



### Acknowledgments
Special thanks to the open-source community for their valuable tools and libraries.