# 🏠 ImmoEliza Price Predictor
ImmoEliza Price Predictor is a web application that allows users to predict real estate prices based on various property features. This app is built using Streamlit, a framework that turns Python scripts into shareable web apps in minutes.

## 🚀 Features
User-Friendly Interface: Simple and intuitive UI for predicting property prices.
Fast Predictions: Predict the price of a property with just a few clicks.
Customizable Inputs: Input various property features such as type, area, number of bedrooms, etc.
Instant Results: Get the predicted price of the property in real-time.
## 📋 Prerequisites
To run this project locally, you will need to have the following installed on your system:

Python 3.7+
Required Python packages (listed in requirements.txt)
📦 Installation
Clone the repository:

bash
Copier le code
git clone 
cd immoeliza-price-predictor
Install the dependencies:

bash
Copier le code
pip install -r requirements.txt
Download the trained model and encoder files:

Ensure you have trained_model.joblib and encoder.joblib in the root directory of the project. These files contain the pre-trained model and the encoder used for predictions.
🛠️ Usage
Run the application:

bash
 Copier le code
streamlit run app.py
Open the web app:

Once the app is running, it will open in your default web browser. If not, you can manually navigate to http://localhost:8501 in your browser.

Use the interface:

Select the property features from the dropdowns and input fields.
Click on the "Predict Price" button to get the estimated price of the property.
The predicted price will be displayed in the app.
📝 Application Overview
Input Fields:
TypeOfProperty: Choose between House or Appartment.
SubtypeOfProperty: Select the specific subtype of the property, such as villa, duplex, penthouse, etc.
TypeOfSale: Choose between residential_sale or residential_monthly_rent.
LivingArea: Enter the living area in square meters.
PostalCode: Input the postal code where the property is located.
BathroomCount: Specify the number of bathrooms.
BedroomCount: Specify the number of bedrooms.
Furnished: Indicate whether the property is furnished (Yes/No).
Fireplace: Indicate whether the property has a fireplace (Yes/No).
Kitchen: Select the type of kitchen installed.
PEB: Choose the energy performance certificate (PEB) rating.
StateOfBuilding: Indicate the condition of the building.
NumberOfFacades: Input the number of facades.
Garden: Indicate whether the property has a garden (Yes/No).
GardenArea: Specify the garden area in square meters.
SwimmingPool: Indicate whether the property has a swimming pool (Yes/No).
Terrace: Indicate whether the property has a terrace (Yes/No).
ConstructionYear: Enter the year the property was constructed.
District: Select the district where the property is located.
Output:
Predicted Price: The estimated price of the property based on the inputs.
🎨 Screenshots

Description of the screenshot.


Description of the screenshot.

🤝 Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
📜 License
Distributed under the MIT License. See LICENSE for more information.

📧 Contact
Your Name

Email: your-email@example.com
LinkedIn: Your LinkedIn
Project Link: GitHub Repository
🌟 Acknowledgements
Streamlit for providing the easy-to-use web framework.
Pandas, Scikit-learn, and Joblib for making data processing and model deployment straightforward.
The creators and maintainers of all the open-source libraries used in this project.
