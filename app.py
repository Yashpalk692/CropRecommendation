import base64 # for styling
import streamlit as st
import joblib

# Load the trained model
model_path = 'model.joblib'
RF = joblib.load(model_path)

st.title("AgroTech")
# Crop Model

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('bg1.png')


# Load the trained model
model_path = 'model.joblib'
RF = joblib.load(model_path)

def main():
    st.subheader("Crop Recommendation App")
    # User input features
    N, P, K, temperature, humidity, ph, rainfall = get_user_input()

    # Make prediction
    if st.button("Predict", key='Corp'):
        result = make_prediction(RF, N, P, K, temperature, humidity, ph, rainfall)
        st.success(f"#### The recommended crop is {result}")


def get_user_input():

    st.sidebar.header("User Input Features")

    N = st.sidebar.text_input("Nitrogen (N)", 50)
    P = st.sidebar.text_input("Phosphorus (P)", 50)
    K = st.sidebar.text_input("Potassium (K)", 50)
    temperature = st.sidebar.text_input("Temperature", 25.0)
    humidity = st.sidebar.text_input("Humidity", 50)
    ph = st.sidebar.text_input("pH", 7.0)
    rainfall = st.sidebar.text_input("Rainfall", 50.0)

    st.markdown("""
        <style>
            [data-testid=stSidebar] {
                background-color: #aaf0aa;
            }
        </style>
    """, unsafe_allow_html=True)

    return N, P, K, temperature, humidity, ph, rainfall


def make_prediction(RF, N, P, K, temperature, humidity, ph, rainfall):
    new_data = [[N, P, K, temperature, humidity, ph, rainfall]]
    prediction = RF.predict(new_data)
    return prediction[0]

if __name__ == "__main__":
    main()


st.markdown("---")
#Crop file ends


#
# def main():
#     st.title("Crop Recommendation App")
#
#     # User input features
#     N, P, K, temperature, humidity, ph, rainfall = get_user_input()
#
#     # Make prediction
#     if st.button("Predict"):
#         result = make_prediction(RF, N, P, K, temperature, humidity, ph, rainfall)
#         st.success(f"The recommended crop is {result}")
# # For Slider
# # def get_user_input():
# #     st.sidebar.header("User Input Features")
# #
# #     N = st.sidebar.slider("Nitrogen (N)", 0, 100, 50)
# #     P = st.sidebar.slider("Phosphorus (P)", 0, 100, 50)
# #     K = st.sidebar.slider("Potassium (K)", 0, 100, 50)
# #     temperature = st.sidebar.slider("Temperature", 0.0, 100.0, 25.0)
# #     humidity = st.sidebar.slider("Humidity", 0, 100, 50)
# #     ph = st.sidebar.slider("ph", 0.0, 14.0, 7.0)
# #     rainfall = st.sidebar.slider("Rainfall", 0.0, 100.0, 50.0)
# #
# #     return N, P, K, temperature, humidity, ph, rainfall
#
# # For input from the user Left side verticle
# def get_user_input():
#     st.sidebar.header("User Input Features")
#
#     N = st.sidebar.text_input("Nitrogen (N)", 50)
#     P = st.sidebar.text_input("Phosphorus (P)", 50)
#     K = st.sidebar.text_input("Potassium (K)", 50)
#     temperature = st.sidebar.text_input("Temperature", 25.0)
#     humidity = st.sidebar.text_input("Humidity", 50)
#     ph = st.sidebar.text_input("pH", 7.0)
#     rainfall = st.sidebar.text_input("Rainfall", 50.0)
#
#     return N, P, K, temperature, humidity, ph, rainfall
#
# # For input from the user Horizontal
# # def get_user_input():
# #     st.header("User Input Features")
# #
# #     N = st.text_input("Nitrogen (N)", 50)
# #     P = st.text_input("Phosphorus (P)", 50)
# #     K = st.text_input("Potassium (K)", 50)
# #     temperature = st.text_input("Temperature", 25.0)
# #     humidity = st.text_input("Humidity", 50)
# #     ph = st.text_input("pH", 7.0)
# #     rainfall = st.text_input("Rainfall", 50.0)
# #
# #     return N, P, K, temperature, humidity, ph, rainfall
#
# def make_prediction(RF, N, P, K, temperature, humidity, ph, rainfall):
#     new_data = [[N, P, K, temperature, humidity, ph, rainfall]]
#     prediction = RF.predict(new_data)
#     return prediction[0]
#
# if __name__ == "__main__":
#     main()
#

