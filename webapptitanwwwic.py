# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 11:09:57 2022

@author: navug
"""
import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open('','rb'))

def titanic_prediction(input_data):
    
   
   input_data_as_numpy_array = np.asarray(input_data)


   input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

   prediction = loaded_model.predict(input_data_reshaped)
   print(prediction)

   if (prediction[0] == 0):
     
     return('The person did not survive')
   else:
     return('The person survived')  
# Sex = st.text_input('Ticket class ,male=0 and female=1')

def change(sex):
    if sex=='male':
        return 0
    elif sex=='female':
        return 1
        
       

def main():
    
    st.title('Titanic Survival Prediction Web app')
    
    Pclass =st.text_input('Ticket class')                
    

    Sex = change(st.selectbox('Select the gender of the passenger', ['male','female']))
    
    Age =st.slider('Age of the passenger') 
            
    SibSp =st.text_input('Number of Siblings/Spouses Aboard')              
    Parch = st.text_input('Number of Parents/Children Aboard')   
 
               
    Result=''
    
    if st.button('Result'):
        Result=titanic_prediction([ Pclass , Sex , Age , SibSp , Parch])
        
    st.success(Result)
    
    
    
 
if __name__== '__main__':
    main()
    
  
