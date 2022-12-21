import streamlit as st
from PIL import Image
import pickle
# model = pickle.load(open('model1.pkl', 'rb'))

def run():
    # img1 = Image.open('image4.jpg')
    # img1 = img1.resize((200, 200))
    # st.image(img1, use_column_width=False)

    # st.sidebar.("L'application qui prédit le départ des employées")

    new_title = '<p style="font-family:sans-serif; color:red; font-size: 20px;">Leave or Not</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    # title = '<p style="font-family:sans-serif; color:orange; font-size: 30px;">B SIMPLONIEN</p>'
   
    gen_display = ('Female','Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])
    
    mar_display = ('Bachelors', 'Masters', 'PHD')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Education", mar_options, format_func=lambda x: mar_display[x])
    
    join_display = ('2012', '2013', '2014', '2015', '2016', '2017', '2018')
    join_options = list(range(len(join_display)))
    join = st.selectbox("JoiningYear ", join_options, format_func=lambda x: join_display[x])

    city_display = ('Bangalore', 'Pume', 'New Delhi')
    city_options = list(range(len(city_display)))
    city = st.selectbox("City", city_options, format_func=lambda x: city_display[x])
    
    emp_display = ('Yes', 'No')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Self_Employed", emp_options, format_func=lambda x: emp_display[x])

    paym_display = ('1', '2', '3')
    paym_options = list(range(len(paym_display)))
    paym = st.selectbox("PaymentTier", paym_options, format_func=lambda x: paym_display[x])
    
    expe_display = ('1', '2', '3')
    expe_options = list(range(len(expe_display)))
    expe = st.selectbox("PaymentTier", expe_options, format_func=lambda x: expe_display[x])
    
    ever_display = ('No', 'Yes')
    ever_options = list(range(len(ever_display)))
    ever = st.selectbox("PaymentTier", ever_options, format_func=lambda x: ever_display[x])
    
    age_display = ('22', '23', '24', '25', '26', '27','28', '29', '30','31','32', '33', '34', '35', '36', '37', '38', '39', '40', '41' )
    age_options = list(range(len(age_display)))
    age = st.selectbox("Age", age_options, format_func=lambda x: age_display[x])
    
    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Hello " + fn +' you will not get a loan as per the calculations of the bank.'
            )
        else:
            st.success(
                "Hello " + fn + ' '+' Congratulations!! you will get the loan from Bank'
            )
run()