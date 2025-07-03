import pandas as pd
import numpy as np
import streamlit as st
import pickle

#opening the pickle files from the trained model
pickle_in = open('sleep.pkl','rb')
classifier = pickle.load(pickle_in)
scl = open('scaler.pkl','rb')
scaler = pickle.load(scl)
    

st.title("Sleep Disorder Risk Assessment")
st.subheader("Dear (Un)concerned, Kindly Enter Your details")


#making the text boxes, with Labels:
gender = st.selectbox("Gender", ["Male", "Female"], index=None,placeholder="Select")
age = st.number_input("Age", 18,80, value=None,step=1,placeholder="Enter")
slp_duration = st.number_input("Sleep Duration/-day (in hrs)",0.0,24.0,value=0.0,step=0.5)

st.write("I hope it isn't more than 12hrs..")
if slp_duration >= 12 :
    st.write("...what u doin with ur lyf bro...")
    
slp_quality = st.slider("Quality of Sleep(Subjective scale)",1,10)
phy_activity = st.number_input("Physical Activity(in minutes/-day)",value=None,placeholder="Enter")
stress = st.slider("Stress Levels(Subjective scale)",1,10)
bmi = st.selectbox("BMI Category", ["Normal", "Overweight",'Obese'], index=None,placeholder="Select")
heart_rate = st.number_input("Heart rate(in bpm)",25,value=None,placeholder="Enter")
steps = st.number_input("Daily Steps",value=None,step=100,placeholder="Enter")
max_bp = st.number_input("Systolic BP",value=None,placeholder="Ex.: Type 120, if the reading is 120/80mm hg")
min_bp = st.number_input("Diastolic BP",value=None,placeholder="Ex.: Type 80, if the reading is 120/80mm hg")


input_df = pd.DataFrame({
    'Gender':[gender],
    'Age':[age],
    'Sleep Duration':[slp_duration],
    'Quality of Sleep':[slp_quality],
    'Physical Activity Level':[phy_activity],
    'Stress Level':[stress],
    'BMI Category':[bmi],
    'Heart Rate':[heart_rate],
    'Daily Steps':[steps],
    'Upper BP':[max_bp],
    'Lower BP':[min_bp]
    })

#Encoding the categorical variables
input_df['Gender'] = input_df['Gender'].map({'Male':1, 'Female':0})
input_df['BMI Category'] = input_df['BMI Category'].map({'Normal':0,
                                                         'Overweight':1,
                                                         'Obese':2})

#Scaling the features based on the model
input_df = scaler.transform(input_df)

#Buttons, to make the prediction
#Necessary to fill all the fields
    
if st.button("Assess Risk!"):        
    if (gender and age and slp_duration and phy_activity and bmi and heart_rate and steps and max_bp and min_bp) != None:
        
        #final prediction!!
        pred = classifier.predict_proba(input_df)[0]
        probab = pd.DataFrame({'Disorder': ['Insomnia','No Disorder','Sleep Apnea'],
                               'Risk %': np.round((pred*100),1)})
        
        st.subheader("Result:")
        st.write(probab)
        st.image('insert.png',caption='Feature Importance')
        st.subheader("Thank you. That's all")
        
    else:
        st.write("Please Fill all fields!")
    
if st.button("Click here! Click here!"):
    st.link_button(label="I PROMISE ITS NOTHING...",url="https://shorturl.at/ONets")



