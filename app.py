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
        
        expe = st.sidebar.slider('ExperienceInCurrentDomain', 0, 1, 2, 3,4,5,6,7)
        if expe  :
            emxpe = 0
        else:
            expe = 1
            
        # envsat = st.selectbox('Environment Satisfaction',['Low', 'Medium','High'])
        # if envsat == "Low" :
        #     env_sat = 1
        # else:
        #     env_sat = 0
            
        gend = st.selectbox('Gender', ['Male', 'Female'])
        if gend == "Male" :
            gender = 1
        else :
            gender = 0
            
        # involve = st.selectbox('Job Involvement',['Low', 'Medium','High','Very High'])
        # if involve == "Low":
        #     job_inv = 1
        # elif involve == "Medium":
        #     job_inv = 2
        # elif involve == "High":
        #     job_inv = 3
        # else :
        #     job_inv = 4
        
        # role = st.selectbox('Job Role', ['Research Director','Manager','Healthcare Representative','Manufacturing Director','Lab Technician','Research Scientist','Sales Executive','HR','Sales Representative'])
        # if role == "Research Director" :
        #     jobrole = 0
        # elif role == "Manager" or "Healthcare Representative" or "Manufacturing Director":
        #     jobrole = 1
        # elif role == "Lab Technician" :
        #     jobrole = 3
        # elif role == "Research Scientist" or "Sales Executive" :
        #     jobrole = 2
        # elif role == "HR" :
        #     jobrole = 4
        # else :
        #     jobrole = 5
            
        EverBenched = st.selectbox('EverBenched', ['Yes','No'])
        if EverBenched == "Yes" :
            EverBenched = 1
        elif EverBenched== "yes" or "No" :
            EverBenched = 2
        else :
            EverBenched = 3
            
        # mar = st.selectbox('Marital Status',['Married','Divorced','Single'])
        # if mar == "Married" or "Divorced" :
        #     mar_stat = 0
        # else :
        #     mar_stat = 1
            
        payment = st.sidebar.slider('PaymentTier', 1, 2, 3)
        
        # num_worked = st.number_input('Number of companies worked',0.,10.,step = 1.)
        # if num_worked <=4 :
        #     num_com = 0
        # else :
        #     num_com = 1
            
        # otime = st.selectbox("Does the employee work overtime?",['No', 'Yes'])
        # if otime == "No" :
        #     overtime = 0
        # else :
        #     overtime = 1
            
        # sol = st.selectbox('Stock of employee in the company', ["No stocks", "Moderate stocks", "Lots of stocks"])
        # if sol == "No stocks" :
        #     stocks = 0 
        # elif sol == "Moderate stocks" :
        #     stocks = 1 
        # else :
        #     stocks = 2
            
        # ExperienceInCurrentDomain = st.number_input("Experience In Current Domain",0.,7.,step = 1.)
        
        # training = st.number_input("Number of times employee did training",0.,7., step = 1.)
        
        # years_com = st.number_input("Number of years spent in company",0.,30., step = 1.)
        
        # years_role = st.number_input("Number of years in current role",0.,30., step = 1.)
        
        # ym = st.number_input("Years with current manager",0.,20., step = 1.)
        # if ym == 0 :
        #     years_man = 0 
        # elif ym < 12 :
        #     years_man = 1
        # else :
        #     years_man = 2
            
        # com = st.selectbox("Communication Skills", ["Poor","Bad","Good", "Better", "Best"])
        # if com == "Poor" :
        #     com_skills = 1
        # elif com == "Bad" :
        #     com_skills = 2
        # elif com == "Good" :
        #     com_skills =3
        # elif com == "Better":
        #     com_skills = 4
        # else :
        #     com_skills = 5
            
        inp = [age,City,education, expe, gender,EverBenched,payment]
        
        return inp
    
    df = input_features()
    model = pickle.load(open('model_pkl.pickle.pkl','rb'))
    ans = model.predict_proba([df])[0][1]
    ans = round(100*ans,2)
    # st.subheader(f'The probability of employee being released is {ans} percent.')
    
if __name__ == "__main__" :
    main()