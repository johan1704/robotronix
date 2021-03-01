# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 16:01:58 2020
@author: Johan Kouame Agouale
"""

import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import joblib

#pickle=open('model.pkl', 'rb')
#classifier=pickle.load(pickle)

model = joblib.load('model.sav')

#image=Image.open('down.jpg')
#st.image(image,width=500)


st.markdown("<h1 style='text-align: center; color: red;'><strong>CUSTOMER CHURN PREDICTOR</strong></h1>", unsafe_allow_html=True) 

selectbox=st.sidebar.selectbox('Select operation to be performed',['Enter values for prediction','View dataset analysis'])
if selectbox == 'Enter values for prediction':
    
    st.subheader("Enter the appropriate values for each field and press 'Predict' to get the result.")
    
    tenure=st.text_input('tenure(in years)')
    monthlycharges=st.text_input('monthlycharges')
    totalcharges=st.text_input('totalcharges')
    
    gender=st.selectbox('gender',['Female','Male'])
    if gender=='Female':
        gender=0
    else:
        gender=1  
    senior_citizen=st.selectbox('Is he/she senior citizen',['No','Yes'])
    if senior_citizen=='No':
        senior_citizen=0
    else:
        senior_citizen=1  
    partner_yes=st.selectbox('Is a partner',['yes','no'])
    if partner_yes=='yes':
        partner_yes=1
    else:
        partner_yes=0
    dependents_yes=st.selectbox('dependents?',['yes','no'])
    if dependents_yes=='yes':
        dependents_yes=1
    else:
        dependents_yes=0
   
    PhoneService_Yes=st.selectbox('PhoneService available?',['yes','no'])
    if PhoneService_Yes=='yes':
        PhoneService_Yes=1
    else:
        PhoneService_Yes=0
    
    MultiplesLines_Yes=st.selectbox('Available multiple Lines?',['yes','no'])
    if MultiplesLines_Yes=='yes':
        MultiplesLines_Yes=1
    else:
        MultiplesLines_Yes=0
   
    MultiplesLines_No=st.selectbox('multiple Lines?',['No','Yes'])
    if MultiplesLines_No=='No':
        MultiplesLines_No=0
    else:
        MultiplesLines_No=1
        
    InternetService_Fiber=st.selectbox('Is the Internet service a Fiber',['No','Yes'])
    if InternetService_Fiber=='No':
        InternetService_Fiber=0
    else:
        InternetService_Fiber=1
    
    InternetService_No=st.selectbox('Internet Available?',['No','Yes'])
    if InternetService_No=='No':
        InternetService_No=0
    else:
        InternetService_No=1   
        
    OnlineSecurity_No=st.selectbox('Online Security?',['No','Yes'])
    if OnlineSecurity_No=='No':
        OnlineSecurity_No=0
    else:
        OnlineSecurity_No=1
    
    OnlineBackup_No=st.selectbox('Online Backup?',['No','Yes'])
    if OnlineBackup_No=='No':
        OnlineBackup_No=0
    else:
        OnlineBackup_No=1       
        
    Deviceprotection_No=st.selectbox('Is device protected?',['No','Yes'])
    if Deviceprotection_No=='No':
        Deviceprotection_No=0
    else:
        Deviceprotection_No=1
    
    Deviceprotection_NoInternet=st.selectbox('Internet for device Protection?',['No','Yes'])
    if Deviceprotection_NoInternet=='No':
        Deviceprotection_NoInternet=0
    else:
        Deviceprotection_NoInternet=1
        
    TechSupport_No=st.selectbox('Tech Support?',['No','Yes'])
    if TechSupport_No=='No':
        TechSupport_No=0
    else:
        TechSupport_No=1
    
    StreamingTV_Nointernet=st.selectbox('Internet for Streaming TV?',['No','Yes'])
    if StreamingTV_Nointernet=='No':
        StreamingTV_Nointernet=0
    else:
        StreamingTV_Nointernet=1
        
    StreamingTV_Yes=st.selectbox('Is there Streaming TV?',['No','Yes'])
    if StreamingTV_Yes=='No':
        StreamingTV_Yes=0
    else:
        StreamingTV_Yes=1
    
    StreamingMovies_Nointernet=st.selectbox('Internet for Streaming Movies?',['No','Yes'])
    if StreamingMovies_Nointernet=='No':
        StreamingMovies_Nointernet=0
    else:
        StreamingMovies_Nointernet=1   
    
    StreamingMovies_Yes=st.selectbox('Is there Streaming Movies?',['No','Yes'])
    if StreamingMovies_Yes=='No':
        StreamingMovies_Yes=0
    else:
        StreamingMovies_Yes=1   
        
    contract1=st.selectbox('Is it a Contract month to month ',['No','Yes'])
    if contract1 =='No':
        contract1=0
    else:
        contract1=1
    
    contract2=st.selectbox('Is it a contract for year?',['No','Yes'])
    if contract2=='No':
        contract2=0
    else:
        contract2=1   
    
    paperless=st.selectbox('Paper less billing?',['No','Yes'])
    if paperless=='No':
        paperless=0
    else:
        paperless=1
    
    payment_method=st.selectbox('Is payment method electronic check?',['No','Yes'])
    if payment_method=='No':
        payment_method=0
    else:
        payment_method=1   
    
    input_dict={'tenure':tenure, 'monthlycharges': monthlycharges, 'totalcharges':totalcharges, 'gender':gender, 'senior_citizen':senior_citizen, 'partner_yes':partner_yes, 
                'dependents_yes':dependents_yes,'PhoneService_Yes':PhoneService_Yes,'InternetService_Fiber':InternetService_Fiber,'InternetService_No':InternetService_No,
                'OnlineSecurity_No':OnlineSecurity_No,'OnlineBackup_No':OnlineBackup_No,
                'Deviceprotection_No':Deviceprotection_No,'Deviceprotection_NoInternet':Deviceprotection_NoInternet,
                'MultiplesLines_No':MultiplesLines_No, 'MultiplesLines_Yes':MultiplesLines_Yes, 'TechSupport_No':TechSupport_No,
                'StreamingTV_Yes': StreamingTV_Yes,' StreamingTV_Yes': StreamingTV_Yes,
                'StreamingMovies_Nointernet':StreamingMovies_Nointernet,'StreamingMovies_Yes':StreamingMovies_Yes,
                'contract1':contract1,'contract2':contract2,' paperless': paperless,
                'payment_method': payment_method}
    
    input_df=pd.DataFrame([input_dict])
    
    if st.button("Predict"):
        output=model.predict(input_df)
        prob=model.predict_proba(input_df)
        if int(output)==0:
            st.error('Not leaving! The probability of customer NOT leaving is {}%'.format(round(prob[0][0]*100,2)))
        else:
            st.error('The probability of customer leaving is {}%, please review his profile.'.format(round(prob[0][1]*100)))
    
            

if selectbox == 'View dataset analysis':
    graph=st.selectbox('Select graph to be displayed',['graph1','graph2',
                                                       'graph3'])
                                                 
    if graph == 'graph1':
        image2=Image.open('inp.png')
        st.image(image2, width=800)
    if graph == 'graph2':
        image3=Image.open('kde4.png')
        st.image(image3,width=900)
    
    if graph =='graph3':
        image4=Image.open('par.png')
        st.image(image4,width=800)
    

st.markdown("""
<style>
body {

    background-color: orange;
}

</style>
    """, unsafe_allow_html=True)
    
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#f5ee0a,#f5ee0a);
}
</style>
""",
    unsafe_allow_html=True,
)
        
st.markdown('<style> body {font-weight:bold;background-image: url("https://cdn.pixabay.com/photo/2017/10/29/09/51/background-2899263_960_720.jpg"); background-size:cover;}</style>',unsafe_allow_html=True)