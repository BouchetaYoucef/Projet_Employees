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

def prediction(Education, JoiningYear, City, Age, Gender, EverBenched, ExperienceInCurrentDomain):
        
    #Pre-Processing user input
    ## For Education
    Education = ('Bachelors','Masters','PHD')
    Education = list(range(len(Education)))
    Education = st.selectbox("Education", Education, format_func=lambda x: Education[x])
    
    ## For JoiningYear
    JoiningYear = ('','')
    JoiningYear = list(range(len(JoiningYear)))
    JoiningYear = st.selectbox("JoiningYear",JoiningYear, format_func=lambda x: JoiningYear[x])
    
     ## For City
    City = ('Bangalore','Pune','New Delhi')
    City = list(range(len(City)))
    City = st.selectbox("City",City, format_func=lambda x: City[x])
    
    ## For Age
    Age = ('','')
    Age = list(range(len(Age)))
    Age = st.selectbox("Age",Age, format_func=lambda x: Age[x])
    
    ## For EverBenched
    EverBenched = ('','')
    EverBenched = list(range(len(EverBenched)))
    EverBenched = st.selectbox("EverBenched",EverBenched, format_func=lambda x: EverBenched[x])
    
    ## For ExperienceInCurrentDomain
    ExperienceInCurrentDomain = ('','')
    ExperienceInCurrentDomain = list(range(len(ExperienceInCurrentDomain)))
    ExperienceInCurrentDomain = st.selectbox("ExperienceInCurrentDomain",ExperienceInCurrentDomain, format_func=lambda x: EverBenched[x])

    ## For Credit Score
    # cred_display = ('Between 300 to 500','Above 500')
    # cred_options = list(range(len(cred_display)))
    # cred = st.selectbox("Credit Score",cred_options, format_func=lambda x: cred_display[x])

    ## Applicant Monthly Income
    mon_income = st.number_input("ApplicantIncome",value=0)

    ## Co-Applicant Monthly Income
    co_mon_income = st.number_input("CoApplicantIncome",value=0)

    ## Loan AMount
    loan_amt = st.number_input("Loan Amount",value=0)

    ## loan duration
    dur_display = ['2 Month','6 Month','8 Month','1 Year','16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration",dur_options, format_func=lambda x: dur_display[x])

    # if st.button("Submit"):
    
    # Making predictions
    prediction = classifier.predict(
        [[Gender, Education, JoiningYear, City, Age, Gender, EverBenched, ExperienceInCurrentDomain]])
    
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred

# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """
    <div style ="background-color:blue;padding:13px">
    <h1 style ="color:white;text-align:center;">Bank Simplonien</h1>
    </div>
    """
    
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html= True)
    
    # following lines create boxes in which user can enter data required to make prediction
    Gender = st.selectbox('Gender',('Male','Female'))
    Married = st.selectbox('Marital Status',('Unmarried','Maried'))
    Dependents = st.selectbox('Dependents', ('1', '2', '3', '+' ))
    Employment_Status = st.selectbox('Employment Status',('Job','Business'))
    ApplicantIncome = st.number_input('Applicants monthly income')
    LoanAmount = st.number_input('Total loan amount')
    Credit_History = st.selectbox('Credit_History',('Unclear Debts','No Unclear Debts'))
    result =""
    
    df = input_features()
    model = pickle.load(open('model_pkl.pickle.pkl','rb'))
    ans = model.predict_proba([df])[0][1]
    ans = round(100*ans,2)
    # st.subheader(f'The probability of employee being released is {ans} percent.')
    
if __name__ == "__main__" :
    main()