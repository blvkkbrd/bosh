import streamlit as st
import pandas as pd

st.title('Bosch Productivity predictions')

st.write("""
This application was designed to improve process

👈 On your left, you will have a menu that will move you over to waht you want to do!


🔐 First you will need a login to navigate through this application

📊 Then you will have acces to the data loading

📈 And after your data is loaded you will be able to make predictions

📋 Once your data has been predicted, you will be able to export your predicted values as a .csv file

🙋🏼‍♂️ 🙋🏻‍♀️ If you have any questions feel free to ask our support members!

""")



# def main_page():

#     st.markdown("# Main page 🎈")
#     st.sidebar.markdown("# Main page 🎈")

# def page2():
#     st.markdown("# Prediction ❄️")
#     st.sidebar.markdown("# Page 2 ❄️")
    
# page_names_to_funcs = {
#     "Main Page": main_page,
#     "Prediction page": page2,}

# selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()




# def load_data():
#     uploaded_file = st.file_uploader("Choose a file")
#     if uploaded_file is not None:
#         df = pd.read_csv(uploaded_file)
#         return df

# def check_data():
#     if st.button('See your data'):
#         st.write(df)

# df = load_data()
    
# check_data()