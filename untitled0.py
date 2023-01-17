# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:24:22 2023

@author: navug
"""
import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open(r"C:\Users\navug\Desktop\ml project\titanic\Titanic_trained_model (1).sav",'rb'))


def titanic_prediction(input_data):
    
    input_data= np.asarray(input_data,dtype=float)


    input_data = input_data.reshape(1,-1)
    prediction = loaded_model.predict(input_data)
    print(prediction)
    
    if (prediction[0] == 0):
      
      return('The person did not survive')
    else:
      return('The person survived')  
  
def change(Gender):
    if Gender=='male':
        return 0
    elif Gender=='female':
        return 1

def je(Embarked):
    if Embarked=='Southampton':
        return 0
    elif Embarked=='Cherbourg':
        return 1
    elif Embarked=='Queenstown':
        return 2

def main():
    
    st.title('Titanic Survival Prediction Web app')
    
    Pclass =st.selectbox(label='Ticket class', options=(1,2,3))              
    

    Gender = change(st.selectbox('Select the gender of the passenger', ['male','female']))
    
    Age =st.slider('Age of the passenger') 
            
    SibSp =st.text_input('Number of Siblings/Spouses Aboard')              
    Parch = st.text_input('Number of Parents/Children Aboard')  
    Embarked=je(st.selectbox('select the boarding port',['Southampton','Cherbourg','Queenstown']))
 
               
    Result=''
    
    if st.button('Result'):
        Result=titanic_prediction([ Pclass , Gender , Age , SibSp , Parch,Embarked])
        
    st.success(Result)
    
    
    
 
if __name__== '__main__':
    main()