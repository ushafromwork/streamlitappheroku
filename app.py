#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:48:12 2024

@author: ushagampala
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:19:56 2024

@author: ushagampala
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model=pickle.load(open('diabetes_model.sav','rb'))
heart_model=pickle.load(open('heart_model.sav','rb'))
parkinsons_model=pickle.load(open('parkinsons_model.sav','rb'))



#Side Bar for Navigate

with st.sidebar:
    
    selected=option_menu('Multiple Disease Prediction system',
                         ['Diabetes Prediction','Heart_disease prediction','Parkinsons Prediction'],
                         icons=['activity','heart-pulse-fill','person'],
                         default_index=0)
    
    
    
    
    
#Diabetes Prediction page

if(selected == 'Diabetes Prediction'):
    
    
    #Page Title
    st.title('Diabetes Prediction using ML')
    
    
    
    #Getting input data from user
    #columns for input fields
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose=st.text_input('Glucose Level')
        
        
    with col3:
        BloodPressure=st.text_input('BloodPressure Level')
        
    with col1:
        SkinThickness=st.text_input('SkinThickness value')
        
    with col2:
        Insulin=st.text_input('Insulin Level')
        
        
    with col3:
        BMI=st.text_input('BMI value')
        
        
    with col1:
        DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction value')
        
    with col2:
        Age=st.text_input('Age of the person')
        

    
    
    #code for prediction
    
    diab_diagnosis=''
    
    #creating a button
    
    if st.button('Diabetes Test Result'):
       diab_prediction= diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
       
       if (diab_prediction[0]== 1):
           
           diab_diagnosis='The person is  Diabetic'
           
       else:
        
        diab_diagnosis='The person is not diabetic'
           
        
    st.success(diab_diagnosis)   
    
    
if(selected == 'Heart_disease prediction'):
    
    st.title('Heart_disease prediction using ML')
    
  
    
    #Getting input data from user
    #columns for input fields
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        Age=st.text_input('Age')
        
    with col2:
        sex=st.text_input('sex')
        
        
    with col3:
        cp=st.text_input('chest pain types')
        
    with col1:
        trestbps=st.text_input('SResting blood pressure')
        
    with col2:
        chol=st.text_input('Serum cholestron in mg/dL')
        
        
    with col3:
        fbs=st.text_input('Fasting Blood sugar > 120mg/dL')
        
        
    with col1:
        restecg=st.text_input('Resting Electrocardiographic results')
        
    with col2:
         thalach=st.text_input('Ethala')   
        
        
    with col3:
        exang=st.text_input('Exercise induced angina')
        
    with col1:
        oldpeak=st.text_input('ST depression induced by exercise relative to rest')
        
    with col2:
        slope=st.text_input('The slope of the peak exercise ST segment')
        
    with col3:
        ca=st.text_input('Number of major vessels colored by flourosopy')
        
        
    with col1:
        thal=st.text_input('0=normal 1=fixed defect 2=reversable defect')
        
  
        

    
    
    #code for prediction
    
    heart_diagnosis=''
    
    #creating a button
    
    if st.button('Heart Disease Test Result'):
       heart_prediction= heart_model.predict([[Age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
       
       if (heart_prediction[0] == 1):
           
           heart_diagnosis='The person has heart disease'
           
       else:
        
        heart_diagnosis='The person has heart disease'
           
        
    st.success(heart_diagnosis)   
    
    
    
if(selected == 'Parkinsons Prediction'):

    st.title('Parkinsons Prediction Using ML')
    
    #Getting input data from user
    #columns for input fields
    
    col1,col2,col3,col4,col5=st.columns(5)
    
    with col1:
        fo=st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi=st.text_input('MDVP:Fhi(Hz)')
        
        
    with col3:
        flo=st.text_input('MDVP:FLo(Hz)')
        
    with col4:
        Jitter_percent=st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
        
        
    with col1:
        RAP=st.text_input('MDVP:RAP')
        
        
    with col2:
        PPQ=st.text_input('MDVP:PPQ')
        
    with col3:
        DDP=st.text_input('Jitter:DDP')
        
        
    with col4:
        shimmer=st.text_input('MDVP:shimmer')
        
    with col5:
        shimmerdb=st.text_input('MDVP:Jshimmer(db)')
        
        
    with col1:
        APQ3=st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5=st.text_input('Shimmer:APQ5')
        
        
    with col3:
        APQ=st.text_input('MDVP:APQ')
        
    with col4:
        NHR=st.text_input('NHR')
        
    with col5:
        HNR=st.text_input('HNR')
        
    with col1:
        RPDE=st.text_input('RPDE')
        
    with col2:
        DFA=st.text_input('DFA')
        
        
    with col3:
        spread1=st.text_input('spread1')
        
    with col4:
        spread2=st.text_input('spread2')
        
    with col5:
        D2=st.text_input('D2')
        
    with col1:
        PPE=st.text_input('SPPE')
        

    
    
    #code for prediction
    
    parkinsons_diagnosis=''
    
    #creating a button
    
    if st.button('Parkinsons Test Result'):
       parkinsons_prediction= parkinsons_model.predict([[fo,fhi,flo,Jitter_percent,Jitter_Abs,RAP,PPQ,DDP,shimmer,shimmerdb,APQ3,APQ5,
                                                         APQ,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
       
       if (parkinsons_prediction[0]== 1):
           
           parkinsons_diagnosis='The person has parkinsons'
           
       else:
        
        parkinsons_diagnosis='The person idoes not have parkinsons'
           
        
    st.success(parkinsons_diagnosis) 