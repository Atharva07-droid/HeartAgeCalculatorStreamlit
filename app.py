import streamlit as st

def calculate_heart_age(data):
    # Your existing calculation logic
    heart_age = data["age"]

    # Add weights based on gender
    if data["gender"] == 'male':
        heart_age += 3
    elif data["gender"] == 'female':
        heart_age += 2

    # Add weights based on ethnic group
    if data["ethnicGroup"] == 'Indian':
        heart_age += 4
    elif data["ethnicGroup"] == 'White':
        heart_age += 3
    elif data["ethnicGroup"] == 'Other Asian':
        heart_age += 2

    # Add weight based on BMI (Body Mass Index)
    height_m = data["height"] / 100
    bmi = data["weight"] / (height_m ** 2)
    if bmi > 30:
        heart_age += 5
    elif bmi > 25:
        heart_age += 3
    else:
        heart_age += 1

    # Add weight based on smoking history
    if data["smoking"] == 'yes':
        if data["smokingStartAge"] == 'under15':
            heart_age += 5
        elif data["smokingStartAge"] == '15-20':
            heart_age += 4
        elif data["smokingStartAge"] == '21-30':
            heart_age += 3
        elif data["smokingStartAge"] == 'over30':
            heart_age += 2
        
        if data["cigarettesPerDay"] == '01-05':
            heart_age += 2
        elif data["cigarettesPerDay"] == '06-10':
            heart_age += 3
        elif data["cigarettesPerDay"] == '11-20':
            heart_age += 4
        elif data["cigarettesPerDay"] == 'moreThan20':
            heart_age += 5

    # Add weights for health conditions
    if data["diabetes"] == 'yes': heart_age += 5
    if data["hypertension"] == 'yes': heart_age += 4
    if data["hypertension Medication"] == 'yes': heart_age += 3
    if data["arthritis"] == 'yes': heart_age += 2
    if data["kidney Disease"] == 'yes': heart_age += 4
    
    # Add weights for family history
    if data["family History"] == 'coronary Artery Disease': heart_age += 4
    if data["family History"] == 'peripheral Artery Disease': heart_age += 4
    if data["family History"] == 'stroke': heart_age += 4
    if data["family History"] == 'premature Coronary Disease': heart_age += 5

    # Add weights for symptoms
    symptoms = data.get("symptoms", [])
    if 'Shortness of breath' in symptoms: heart_age += 3
    if 'Chest pain' in symptoms: heart_age += 4
    if 'Persistent coughing' in symptoms: heart_age += 2
    if 'Fatigue' in symptoms: heart_age += 2
    if 'None' in symptoms: heart_age -= (len(symptoms) - 1) * 2

    # Add weights for other conditions
    if data["Atrial Fibrillation"] == 'yes': heart_age += 4
    if data["lipid Profile"] == 'high': heart_age += 5
    if data["lipid Profile"] == 'low': heart_age += 2

    # Add weights for exercise
    exercise = data["exercise"]
    if exercise == 'daily': heart_age -= 3
    elif exercise == 'several Times': heart_age -= 2
    elif exercise == 'once a week': heart_age -= 1
    elif exercise == 'rarely': heart_age += 1
    elif exercise == 'never': heart_age += 3

    # Add weights for diet
    diet = data["diet"]
    if diet == 'balanced': heart_age -= 2
    elif diet == 'moderate': heart_age += 1
    elif diet == 'unhealthy': heart_age += 3
    elif diet == 'very unhealthy': heart_age += 5

    return heart_age

def main():
    st.title("Heart Age Calculator")

    # Input fields
    age = st.number_input("Age (30-95)", min_value=30, max_value=95)
    gender = st.selectbox("Gender", options=["male", "female"])
    ethnicGroup = st.selectbox("Ethnic Group", options=["Indian", "White", "Other Asian"])
    height = st.number_input("Height (cm)", min_value=0)
    weight = st.number_input("Weight (kg)", min_value=0)

    smoking = st.selectbox("Do you smoke or use tobacco products?", options=["no", "yes"])

    smokingStartAge = None
    cigarettesPerDay = None
    if smoking == 'yes':
        smokingStartAge = st.selectbox("At what age did you start smoking or using tobacco products?", 
                                      options=["under 15", "15-20", "21-30", "over 30"])
        cigarettesPerDay = st.selectbox("How many cigarettes or tobacco products do you consume per day?", 
                                        options=["01-05", "06-10", "11-20", "more Than 20"])

    diabetes = st.selectbox("Diabetes:", options=["yes", "no"])
    hypertension = st.selectbox("Hypertension:", options=["yes", "no"])
    hypertensionMedication = st.selectbox("Medications for Hypertension:", options=["yes", "no"])
    arthritis = st.selectbox("Rheumatoid Arthritis:", options=["yes", "no"])
    kidneyDisease = st.selectbox("Chronic Kidney Disease:", options=["yes", "no"])

    familyHistory = st.selectbox("Family history of cardiovascular disease (age < 60 years)", 
                                 options=["none", "coronary Artery Disease", "peripheral Artery Disease", "stroke", "Premature Coronary Disease"])

    symptoms = st.multiselect("Any of the following symptoms? (Select all that apply)", 
                              options=["Shortness of breath", "Chest pain", "Persistent coughing", "Fatigue", "None"])

    atrialFibrillation = st.selectbox("Atrial Fibrillation:", options=["yes", "no"])
    lipidProfile = st.selectbox("Lipid Profile:", options=["normal", "high", "low"])
    exercise = st.selectbox("How often do you engage in physical exercise?", 
                            options=["daily", "several Times", "once a week", "rarely", "never"])
    diet = st.selectbox("How would you describe your diet?", 
                        options=["balanced", "moderate", "unhealthy", "very unhealthy"])

    # Validate input
    if st.button("Calculate Heart Age"):
        if not (height and weight and age):
            st.error("Please ensure that all fields are filled in, including height and weight.")
        elif not symptoms:
            st.error("Please select at least one symptom.")
        else:
            data = {
                "age": age,
                "gender": gender,
                "ethnicGroup": ethnicGroup,
                "height": height,
                "weight": weight,
                "smoking": smoking,
                "smoking Start Age": smokingStartAge,
                "cigarettesPerDay": cigarettesPerDay,
                "diabetes": diabetes,
                "hypertension": hypertension,
                "hypertension Medication": hypertensionMedication,
                "arthritis": arthritis,
                "kidney Disease": kidneyDisease,
                "family History": familyHistory,
                "symptoms": symptoms,
                "Atrial Fibrillation": atrialFibrillation,
                "lipid Profile": lipidProfile,
                "exercise": exercise,
                "diet": diet
            }

            # Calculate heart age
            heart_age = calculate_heart_age(data)
            st.write(f"Your calculated heart age is: {heart_age}")

if __name__ == "__main__":
    main()
