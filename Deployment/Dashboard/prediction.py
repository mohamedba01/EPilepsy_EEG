from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np


def app():
    from PIL import Image
    image = Image.open('header.png')
    st.image(image)

    st.title('Seizure Detection')

    model = load_model('deployment_1')

    def predict(models, input_df):
        predictions_df = predict_model(estimator=model, data=input_df)
        predictions = predictions_df['Label'][0]
        return predictions
    file_upload = st.file_uploader("Upload EDF file for predictions")
    if file_upload is not None:
        data = pd.read_csv(file_upload)
        predictions = predict_model(estimator=model, data=data)
        st.write(predictions)
    st.markdown('..')





