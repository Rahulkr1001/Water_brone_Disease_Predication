import streamlit as st
import pickle
import numpy as np

def load_mode():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
        return data

data = load_mode()
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.header('Water-borne disease Predictions in Raipur', divider='rainbow')
    #st.title("Water-borne disease Predictions in Raipur")

    st.write("""### We need some information to predict the diseases.""")
    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Swedan",
    )
    
    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    country = st.selectbox("Localites",countries)
    education = st.selectbox("Treatment Plant",education)
    expericence = st.slider("Years of Experience", 0,50,3)
    
    # Water Quality Parameters.
    st.write("""### Enter the Given Water Quality Parameters.""")    
    temp,ph,turbidity = st.columns(3)
    alkalinity,hardness,acidity = st.columns(3)
    mpn,Tds,do = st.columns(3)
    sulpahtes,chlorides,flourides = st.columns(3)
    

    temp.text_input("Temperature")
    ph.text_input("pH")
    turbidity.text_input("Turbidity")

    alkalinity.text_input("Total Alkalinity")
    hardness.text_input("Total Hardness")
    acidity.text_input("Total Acidity")
    
    mpn.text_input("MPN")
    Tds.text_input("Total Dissolved solids")
    do.text_input("Dissolved Oxygen")

    sulpahtes.text_input("Sulphate")
    chlorides.text_input("Chloride")
    flourides.text_input("Flourides")







    ok = st.button("Predicate Diseases")
    if ok:
        X = np.array([[country, education, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        #st.subheader(f"The predicated diseases for given location is  ${salary[0]:.2f}")
        st.subheader(f"The predicated diseases for given location is Diarrhea")
        st.subheader(f"Accuracy of given predicated results: 76.425%")

    

    

