import numpy as np
import pandas as pd
import pickle
import streamlit as st
from PIL import Image

model = pickle.load (open ('model.pkl','rb'))

def run():
    img1 = Image.open('Employees.jpg')
    img1 = img1.resize((700,300))
    st.image(img1,use_column_width=False)
    # st.title("Bank Simplonien ")
run()

def main():
    st.header('Employee Attrition Predictor')
    # st.subheader(""" Made with :heart: by Pranav Garg and Swapnil Srivastava """)
    def input_features() :
        st.sidebar.header('Slide the sliders to change the variables.')
        age = st.sidebar.slider('Age of employee', 22,41,35)
        
        City = st.selectbox('City', ['Bangalor', 'Pume City', 'New Delhi'])
        if City == "" or "" :
            City = 0
        else :
            City = 1
        
        # distancefromhome = st.sidebar.slider('Distance from home(km)',0,50,5)
        
        educ = st.selectbox('Education',['Bachelors','Masters','PHD'])
        if educ == "" or "" or "" :
            education = 1
        else :
            education = 0
        
        en = st.sidebar.slider('Number of people in the team', 1, 2000, 100)
        if en <1495 :
            employeenumber = 0
        else:
            employeenumber = 1
            
        gend = st.selectbox('Gender', ['Male', 'Female'])
        if gend == "Male" :
            gender = 1
        else :
            gender = 0

            
        # EverBenched = st.selectbox('EverBenched', ['Yes','No'])
        # if EverBenched == "Yes" :
        #     EverBenched = 1
        # elif EverBenched== "yes" or "No" :
        #     EverBenched = 2
        # else :
        #     EverBenched = 3
            
        JoiningYear = st.sidebar.slider('JoiningYear', 2012, 2013,2014,2015,2016,2017,2018)
            
        inp = [age,City,education, JoiningYear, gender]
        
        return inp
    
    df = input_features()
    model = pickle.load(open('model_pkl.pickle.pkl','rb'))
    ans = model.predict_proba([df])[0][1]
    ans = round(100*ans,2)
    # st.subheader(f'The probability of employee being released is {ans} percent.')
    
if __name__ == "__main__" :
    main()