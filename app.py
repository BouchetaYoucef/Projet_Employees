import streamlit as st
import pandas as pd
import pickle

with open('model_pkl2.pickle', 'rb') as f:
    model = pickle.load(f)
    
img1 = open('Employees.jpg')
img1 = img1.resize((200, 150))
st.image(img1, use_column_width=False)

Education = st.number_input('Education',step=1)

JoiningYear = st.number_input('JoiningYear', step=1)

City = st.number_input('City',step=1)
# ## For City
# City = ('Bangalore','Pune','New Delhi')
# City = list(range(len(City)))
# City = st.selectbox("City",City, format_func=lambda x: City[x])

PaymentTier = st.number_input('PaymentTier',step=1)

Age = st.number_input('Age', step=1)

# ## For Age
# Age = ('22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41')
# Age = list(range(len(Age)))
# Age = st.selectbox("Age",Age, format_func=lambda x: Age[x])

Gender = st.number_input('Gender',step=1)

EverBenched = st.number_input('EverBenched', step=1)

ExperienceInCurrentDomain = st.number_input('ExperienceInCurrentDomain',step=1)

# lat = st.text_input('latitude')


if st.button(label="Prediction"):
    
    data = pd.DataFrame([[Education, JoiningYear, City, PaymentTier, Age, 
                            Gender, EverBenched, ExperienceInCurrentDomain]], 
                            columns=['Education', 'JoiningYear', 'City', 'PaymentTier', 'Age', 'Gender',
                                    'EverBenched', 'ExperienceInCurrentDomain'])
    prediction = model.predict(data)
    st.write(prediction[0])

# streamlit run app.py --server.maxUploadSize=1028
### fonction pour les tests ###
# def load.model()
# model = pickle.load()
# return model

# def tes_load.model()
# model = load.model()
# assert model! = None
#########################
