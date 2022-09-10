import streamlit as st

st.set_page_config(page_title="Sales Prediction",page_icon='⚕️',layout="wide",initial_sidebar_state='collapsed')
# title of the streamlit web app
st.title('*Sales Prediction for Rossmann Pharmaceuticals*')

# create single-line text input widgets
# returns current value of the text input widget
store_id = st.text_input(label="Store ID", value="0", max_chars=4, key='store_id', help="Store ID")
# upload csv file
# returns None or UploadedFile or list of UploadedFile
st.file_uploader(label="CSV file", type= ['csv'] , accept_multiple_files=False, key="csv_file", help="CSV file upload")
# st.write('The current movie title is', title)

# predict button - on click send features to model for prediction
clicked = st.button(label="Predict", key="predict", help="Predict Sales", on_click=None)

if clicked:
    st.write("Predicting...")

def get_store_sales(storeID):
    pass