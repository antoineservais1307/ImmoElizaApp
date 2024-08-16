# 🏠 ImmoEliza - Real Estate Price Predictor 💶

Welcome to **ImmoEliza**, a powerful real estate price prediction tool that helps you estimate the price of a property based on its features. This application is built with **Streamlit** and uses a pre-trained machine learning model to predict property prices in Belgium.

## ✨ Features

- **User-Friendly Interface**: Easy-to-use interface for selecting property features.
- **Real-Time Price Prediction**: Get instant price predictions based on the selected property features.
- **Customizable Inputs**: Select from various property features like type, subtype, living area, bathroom count, kitchen type, and more.
- **Model-Based Prediction**: Powered by a machine learning model trained on a rich dataset, ensuring accurate and reliable predictions.

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/immoeliza.git
cd immoeliza
```
### 2. Install Dependencies

make sure you have Python installed. Then, install the required packages:

```sh
pip install -r requirements.txt
```

### 3. Run the Application
```sh
streamlit run app.py
```

### 4. Interact with the App

Once the app is running, you can open your browser and got to

- http://localhost:8501

### PS: if you don't want to go trought all these steps you can just go to :
- https://immoelizaapp-8aptk6uokejkabx6bmb955.streamlit.app/

## 🛠️ Project Structure

### Here's a brief overview of the project structure:

```
immoeliza/
│
├── app.py               # Main Streamlit application
├── trained_model.joblib # Pre-trained machine learning model
├── encoder.joblib       # Target Encoder for categorical features
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

#### app.py :
- This is the main file that runs the Streamlit app. It contains the logic for taking user inputs, transforming them, and feeding them into the trained model to predict the property price.
#### trained_model.joblib : 
- This file contains the pre-trained machine learning model used for making predictions.

#### encoder.joblib
- This file contains the target encoder used to transform categorical features into a format suitable for the model.

#### requirements.txt
- This file lists all the Python dependencies required to run the app. These can be installed using pip install -r requirements.txt.

## 📊 Input Features
Here are the input features you can customize in the app:

* Type of Property: House or Appartment
* Subtype of Property: Various subtypes such as villa, duplex, loft, etc.
* Type of Sale: Residential sale or residential monthly rent
* Living Area: The total living area in square meters
* Postal Code: The postal code of the property's location
* Bathroom Count: Number of bathrooms in the property
* Bedroom Count: Number of bedrooms in the property
* Furnished: Whether the property is furnished or not
* Fireplace: Presence of a fireplace
* Kitchen Type: The type of kitchen installed
* PEB: The energy efficiency rating (A++ to G)
* State of Building: Condition of the building (e.g., AS_NEW, GOOD, TO_RENOVATE)
* Number of Facades: The number of facades
* Garden: Presence of a garden
* Garden Area: The area of the garden in square meters
* Swimming Pool: Presence of a swimming pool
* Terrace: Presence of a terrace
* Construction Year: The year the property was constructed
* District: The district where the property is located
## 👨‍💻 Contributors
Antoine Servais,
antoineservais1307 on github

## 🌟 Acknowledgments
Thanks to the creators of Streamlit for their awesome library.
Special thanks to the data science community for inspiration and support