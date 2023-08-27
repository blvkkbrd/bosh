import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import pickle 
from pathlib import Path

import xgboost as xgb

names = ["Admin", "Cedric SERRA"]
usernames = ["admin", "cserra83"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)


def load_model():
    # model = pickle.load(open("model.pkl", "rb"))
    # return model

    model_path = Path(__file__).parent / "modelxgb.pkl"
    with model_path.open("rb") as model:
        modelxgb = pickle.load(model)

    return modelxgb



authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

# if authentication_status:
#     try:
#         if authenticator.reset_password(username, 'Reset password'):
#             st.success('Password modified successfully')
#     except Exception as e:
#         st.error(e)

if authentication_status == None: 
    st.warning("Please enter your username and password")

if authentication_status == True:
    st.sidebar.title(f"Welcome {name}")
    st.write("hello")
    authenticator.logout("Logout", "sidebar")
   
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        st.write("""

        👌 Your data has been loaded succesfully 

        """)

        modelxgb = load_model()

        
        

        if st.button("Start predictions"):
            pred = modelxgb.predict(df)
            df['response'] = pred
            st.write(df)
            st.write("The predicted value is now added to your data")
            

            
            if st.download_button(label="Télécharger le dataset",
                      data=df.to_csv(index=False),
                      key='csv_download_button',  # Une clé unique pour l'élément
                      file_name="dataset.csv"):  # Nom du fichier téléchargé  

                pass