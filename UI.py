import os
import streamlit as st
import pickle
import numpy as np
import pandas as pd
from streamlit_navigation_bar import st_navbar

diabetes_model = pickle.load(open('pickle/DiabetesClassifier.pkl', 'rb'))
heart_disease_model = pickle.load(open('pickle/HeartDiseaseClassifier.pkl', 'rb'))
stroke_model = pickle.load(open('pickle/StrokeClassifier.pkl', 'rb'))

st.set_page_config(page_title="Health Prediction System", initial_sidebar_state="collapsed",page_icon="Pics/healthcare.svg")

pages = ["Home", "Diabetes", "Heart Disease", "Stroke"]
logo_path = "Pics/healthcare1.svg"
styles = {
    "nav": {
        "background-color": "royalblue",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    logo_path=logo_path,
    styles=styles,
    options=options,
)

if page == "Home":
    st.markdown(
        """
        <h1 style='text-align: center; color: royalblue;'>Welcome to the Health Prediction System</h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .big-font {
            font-size:24px !important;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('''
            <p class="big-font">
            Your one-stop platform for predicting health risks related to Diabetes, Heart Disease, and Stroke using advanced Machine Learning models.
            </p>
            ''', unsafe_allow_html=True)    
    st.image("Pics/healthcare_banner.jpg", use_column_width=True)

    st.subheader("Our Features:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("Pics/diabetes_icon.jpg", width=100)
        st.write("**Diabetes Prediction**")
        st.write("Predict the likelihood of diabetes with key health indicators.")
    with col2:
        st.image("Pics/heart_icon.jpg", width=100)
        st.write("**Heart Disease Prediction**")
        st.write("Get insights into heart disease risks using medical data.")
    with col3:
        st.image("Pics/stroke_icon.jpg", width=100)
        st.write("**Stroke Prediction**")
        st.write("Assess stroke risks based on lifestyle and health inputs.")
    st.subheader("About Us:")
    st.write("""
        Our team is passionate about leveraging Machine Learning to improve healthcare outcomes. 
        Here are the key members of our group:
    """)

    team_members = [
        {"name": "Khizar Ali", "github": "https://github.com/Alikhizar142", "linkedin": "https://www.linkedin.com/in/akrcy/"},
        {"name": "Kashif Khan", "github": "https://github.com/kashifsahilks906", "linkedin": "https://www.linkedin.com/in/kashif-khan-626a28249/"},
    ]

    # Display team members with icons
    for member in team_members:
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <span style="font-size: 18px; font-weight: bold; margin-right: 10px;">{member['name']}</span>
                <a href="{member['github']}" target="_blank" style="text-decoration: none; margin-right: 10px;">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="25" style="vertical-align: middle;">
                </a>
                <a href="{member['linkedin']}" target="_blank" style="text-decoration: none;">
                    <img src="https://cdn-icons-png.flaticon.com/512/61/61109.png" alt="LinkedIn" width="25" style="vertical-align: middle;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

elif page == "Diabetes":
    st.markdown(
        """
        <h1 style='text-align: center; color: royalblue;'>Diabetes Prediction</h1>
        """,
        unsafe_allow_html=True
    )
    st.write("Fill in the details to predict the likelihood of diabetes.")

    age = st.number_input("Age", 0, 120)

    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
    with col2:
        polyuria = st.selectbox("Polyuria (Excessive Urination)", ["Yes", "No"])

    col3, col4 = st.columns(2)
    with col3:
        polydipsia = st.selectbox("Polydipsia (Excessive Thirst)", ["Yes", "No"])
    with col4:
        sudden_weight_loss = st.selectbox("Sudden Weight Loss", ["Yes", "No"])

    col5, col6 = st.columns(2)
    with col5:
        weakness = st.selectbox("Weakness", ["Yes", "No"])
    with col6:
        polyphagia = st.selectbox("Polyphagia (Excessive Hunger)", ["Yes", "No"])

    col7, col8 = st.columns(2)
    with col7:
        genital_thrush = st.selectbox("Genital Thrush", ["Yes", "No"])
    with col8:
        visual_blurring = st.selectbox("Visual Blurring", ["Yes", "No"])

    col9, col10 = st.columns(2)
    with col9:
        itching = st.selectbox("Itching", ["Yes", "No"])
    with col10:
        irritability = st.selectbox("Irritability", ["Yes", "No"])

    col11, col12 = st.columns(2)
    with col11:
        delayed_healing = st.selectbox("Delayed Healing", ["Yes", "No"])
    with col12:
        partial_paresis = st.selectbox("Partial Paresis", ["Yes", "No"])

    col13, col14 = st.columns(2)
    with col13:
        muscle_stiffness = st.selectbox("Muscle Stiffness", ["Yes", "No"])
    with col14:
        alopecia = st.selectbox("Alopecia (Hair Loss)", ["Yes", "No"])

    obesity = st.selectbox("Obesity", ["Yes", "No"])

    st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: royalblue;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px 20px;
        display: block;
        margin: 0 auto;  /* Center the button */
    }
    div.stButton > button:first-child:hover {
        background-color: #0059b3;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    if st.button("Predict Diabetes"):
        features_dict = {
            "Age": [age],
            "Gender": [gender],
            "Polyuria": [polyuria],
            "Polydipsia": [polydipsia],
            "sudden weight loss": [sudden_weight_loss],
            "weakness": [weakness],
            "Polyphagia": [polyphagia],
            "Genital thrush": [genital_thrush],
            "visual blurring": [visual_blurring],
            "Itching": [itching],
            "Irritability": [irritability],
            "delayed healing": [delayed_healing],
            "partial paresis": [partial_paresis],
            "muscle stiffness": [muscle_stiffness],
            "Alopecia": [alopecia],
            "Obesity": [obesity],
        }
        features_df = pd.DataFrame(features_dict)

        prediction = diabetes_model.predict(features_df)
        
        if prediction[0]:  
            st.error("Diabetes Detected! ⚠️")
            st.write("### Precautions and Recommendations:")
            st.markdown("""
            - Schedule a consultation with your doctor immediately.
            - Maintain a balanced diet with controlled carbohydrate intake.
            - Engage in regular physical activity to manage blood sugar levels.
            - Monitor your blood sugar levels daily.
            - Avoid sugary beverages and high-carb foods.
            - Drink plenty of water and stay hydrated.
            - Consider the following tests:
                - HbA1c Test
                - Fasting Blood Sugar Test
                - Oral Glucose Tolerance Test (OGTT)
                - Lipid Profile
            """)
            st.image("Pics/diabetes_management_tips.jpg", caption="Healthy Lifestyle Tips", use_column_width=True)
        else:  
            st.success("Congratulations! No Diabetes Detected. 🎉")
            st.write("### Keep Up the Good Work!")
            st.markdown("""
            - Maintain a healthy lifestyle to reduce the risk of diabetes in the future.
            - Eat a balanced diet rich in vegetables, lean proteins, and whole grains.
            - Exercise regularly (at least 30 minutes daily).
            - Stay hydrated and get enough sleep.
            - Avoid excessive sugar and processed foods.
            """)
            st.image("Pics/healthy_lifestyle.jpg", caption="Stay Healthy!", use_column_width=True)
            
elif page == "Heart Disease":
    st.markdown(
        """
        <h1 style='text-align: center; color: royalblue;'>Heart Disease Prediction</h1>
        """,
        unsafe_allow_html=True
    )
    st.write("Fill in the details to predict the likelihood of heart disease.")

    age = st.number_input("Age", 0, 120, step=1)

    col1, col2 = st.columns(2)
    with col1:
        resting_blood_pressure = st.number_input("Resting Blood Pressure (mm Hg)", 0, 200, step=1)
    with col2:
        cholestoral = st.number_input("Serum Cholesterol (mg/dl)", 0, 600, step=1)

    col3, col4 = st.columns(2)
    with col3:
        Max_heart_rate = st.number_input("Maximum Heart Rate Achieved", 0, 220, step=1)
    with col4:
        oldpeak = st.number_input("ST Depression Induced by Exercise (Oldpeak)", 0.0, 6.0, step=0.1)

    col5, col6 = st.columns(2)
    with col5:
        sex = st.selectbox("Sex", ["Male", "Female"])
    with col6:
        chest_pain_type = st.selectbox("Chest Pain Type", ["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"])

    col7, col8 = st.columns(2)
    with col7:
        fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
    with col8:
        rest_ecg = st.selectbox("Resting ECG Results", ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])

    col9, col10 = st.columns(2)
    with col9:
        exercise_induced_angina = st.selectbox("Exercise-Induced Angina", ["No", "Yes"])
    with col10:
        slope = st.selectbox("Slope of Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])

    col11, col12 = st.columns(2)
    with col11:
        vessels_colored_by_flourosopy = st.selectbox("Number of Major Vessels (0-4)", ["Zero", "One", "Two", "Three", "Four"])
    with col12:
        thalassemia = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect",'No'])

    st.markdown(
        """
        <style>
        div.stButton > button:first-child {
            background-color: royalblue;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 20px;
            display: block;
            margin: 0 auto;  /* Center the button */
        }
        div.stButton > button:first-child:hover {
            background-color: #0059b3;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button("Predict Heart Disease"):
        features_dict = {
            'age': [age],
            'resting_blood_pressure': [resting_blood_pressure],
            'cholestoral': [cholestoral],
            'Max_heart_rate': [Max_heart_rate],
            'oldpeak': [oldpeak],
            'sex': [sex],
            'chest_pain_type': [chest_pain_type],
            'fasting_blood_sugar': ["Greater than 120 mg/ml" if fasting_blood_sugar == "Yes" else "Lower than 120 mg/ml"],
            'rest_ecg': [rest_ecg],
            'exercise_induced_angina': [exercise_induced_angina],
            'slope': [slope],
            'vessels_colored_by_flourosopy': [vessels_colored_by_flourosopy],
            'thalassemia': [thalassemia]
        }

        features_df = pd.DataFrame(features_dict)


        prediction = heart_disease_model.predict(features_df)

        if prediction[0]: 
            st.error("Heart Disease Detected! ⚠️")
            st.write("### Precautions and Recommendations:")
            st.markdown("""
            - Consult a cardiologist immediately.
            - Follow a heart-healthy diet low in sodium and saturated fats.
            - Engage in regular physical activity as recommended by your doctor.
            - Avoid smoking and excessive alcohol consumption.
            - Monitor your blood pressure, cholesterol, and blood sugar levels regularly.
            - Consider the following diagnostic tests:
                - Electrocardiogram (ECG)
                - Echocardiogram
                - Stress Test
                - Coronary Angiography
            """)
            st.image("Pics/healthy_heart_tips.jpg", caption="Heart Health Tips", use_column_width=True)
        else: 
            st.success("Congratulations! No Heart Disease Detected. 🎉")
            st.write("### Keep Your Heart Healthy!")
            st.markdown("""
            - Maintain a balanced diet rich in fruits, vegetables, and whole grains.
            - Exercise regularly (at least 30 minutes daily).
            - Avoid excessive stress and practice relaxation techniques like yoga or meditation.
            - Keep your cholesterol, blood pressure, and weight in check.
            - Get regular medical checkups.
            """)
            st.image("Pics/healthy_lifestyle.jpg", caption="Tips for a Healthy Heart", use_column_width=True)


elif page == "Stroke":
    st.markdown(
        """
        <h1 style='text-align: center; color: royalblue;'>Stroke Prediction</h1>
        """,
        unsafe_allow_html=True
    )
    st.write("Fill in the details to predict the likelihood of a stroke.")

    age = st.number_input("Age", 0, 120)

    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
    with col2:
        hypertension = st.selectbox("Hypertension", ["No", "Yes"])

    col3, col4 = st.columns(2)
    with col3:
        heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
    with col4:
        ever_married = st.selectbox("Ever Married", ["No", "Yes"])

    col5, col6 = st.columns(2)
    with col5:
        work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "Children", "Never_worked"])
    with col6:
        residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])

    col7, col8 = st.columns(2)
    with col7:
        avg_glucose_level = st.number_input("Average Glucose Level", 0.0, 300.0)
    with col8:
        bmi = st.number_input("BMI", 0.0, 70.0)

    smoking_status = st.selectbox("Smoking Status", ["Never Smoked", "Formerly Smoked", "Smokes", "Unknown"])

    st.markdown(
        """
        <style>
        div.stButton > button:first-child {
            background-color: royalblue;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 20px;
            display: block;
            margin: 0 auto;  /* Center the button */
        }
        div.stButton > button:first-child:hover {
            background-color: #0059b3;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button("Predict Stroke"):
        hypertension = 1 if hypertension == "Yes" else 0
        heart_disease = 1 if heart_disease == "Yes" else 0

        features_dict = {
            'age': [age],
            'hypertension': [hypertension],
            'heart_disease': [heart_disease],
            'avg_glucose_level': [avg_glucose_level],
            'bmi': [bmi],
            'gender': [gender],
            'ever_married': [ever_married],
            'work_type': [work_type],
            'Residence_type': [residence_type],
            'smoking_status': [smoking_status.lower()]
        }

        features_df = pd.DataFrame(features_dict)

        try:
            prediction = stroke_model.predict(features_df)
            if prediction[0]==1: 
                st.error("Stroke Risk Detected! ⚠️")
                st.write("### Precautions and Recommendations:")
                st.markdown("""
                - Consult a neurologist immediately.
                - Monitor your blood pressure and blood sugar levels regularly.
                - Adopt a healthy diet low in salt, sugar, and saturated fats.
                - Exercise regularly as recommended by your doctor.
                - Avoid smoking and limit alcohol consumption.
                - Manage stress through relaxation techniques like yoga or meditation.
                - Consider the following diagnostic tests:
                    - Brain MRI or CT Scan
                    - Carotid Ultrasound
                    - Echocardiogram
                    - Blood Tests (e.g., cholesterol, sugar levels)
                """)
                st.image("Pics/stroke_management_tips.jpeg", caption="Stroke Prevention Tips", use_column_width=True)
            else:
                st.success("Congratulations! No Stroke Risk Detected. 🎉")
                st.write("### Keep Your Brain Healthy!")
                st.markdown("""
                - Maintain a healthy lifestyle to reduce the risk of stroke.
                - Eat a balanced diet with plenty of fruits, vegetables, and whole grains.
                - Stay physically active and maintain a healthy weight.
                - Avoid excessive stress and stay hydrated.
                - Get regular medical checkups to monitor your overall health.
                """)
                st.image("Pics/healthy_brain_tips.jpg", caption="Tips for a Healthy Brain", use_column_width=True)
        except ValueError as e:
            st.error(f"Error: {str(e)}")
