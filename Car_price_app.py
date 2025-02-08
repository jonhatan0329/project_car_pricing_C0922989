import streamlit as st
import pickle 
import pandas as pd

st.title('Car Price Prediction')
#st displays all we want
st.write('This web app predicts **Car Price** based in some references, please select the correct option.')

#to read the model from the pickle file
with open('model_lr_cp_c0922989.pkl', 'rb') as file:
    model_cp = pickle.load(file)
#model_cp=pickle.load(open('model_lr_cp_c0922989.pkl','rb'))

car_brand = st.selectbox('Select the Brand:', options=label_encoders['Brand'].classes_)
car_model = st.selectbox('Select the Model:', options=label_encoders['Model'].classes_)
car_year = st.number_input('Year', min_value=1990, max_value=2023, step=1)
car_fuel = st.selectbox('Type of Fuel:', options=label_encoders['Fuel_Type'].classes_)
car_transmission = st.selectbox('Transmission Type:', options=label_encoders['Transmission'].classes_)
car_mileage = st.number_input('Mileage', min_value=0)
car_doors = st.number_input('Number of Doors', min_value=2, max_value=5, step=1)

# Convert user inputs to encoded values
car_data_input = pd.DataFrame({
    'Brand': [label_encoders['Brand'].transform([car_brand])[0]],
    'Model': [label_encoders['Model'].transform([car_model])[0]],
    'Year': [car_year],
    'Fuel_Type': [label_encoders['Fuel_Type'].transform([car_fuel])[0]],
    'Transmission': [label_encoders['Transmission'].transform([car_transmission])[0]],
    'Mileage': [car_mileage],
    'Doors': [car_doors]
})

# Predict and display result
if st.button('Predict'):
    prediction = model_cp.predict(car_data_input)
    formatted_prediction = f"${prediction[0]:,.2f}"
    st.write(f'The predicted car price is {formatted_prediction}')

# Enhanced Data Visualization
st.subheader('Data Visualizations')

# Pairplot
sns.pairplot(car_data)
plt.suptitle('Pairplot of Car Pricing Data', y=1.02)
st.pyplot(plt.gcf())

# Correlation Matrix
correlation_matrix = car_data.corr()
st.write('Correlation Matrix:', correlation_matrix)

# Heatmap of Correlations
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Car Pricing Data')
st.pyplot(plt.gcf())