import streamlit as st
import pickle 
import pandas as pd

st.title('Car Price Prediction')
#st displays all we want
st.write('This web app predicts **Car Price**')

#to read the model from the pickle file
with open('model_lr_cp_c0922989.pkl', 'rb') as file:
    model_cp = pickle.load(file)
#model_cp=pickle.load(open('model_lr_cp_c0922989.pkl','rb'))

#get the input from the users
car_brand=st.number_input('Brand')
car_model=st.number_input('Model')
car_year=st.number_input('Year')
car_fuel=st.number_input('Type of fuel')
car_t_a=st.number_input('Automatic transmission Yes=1, No=0')
car_t_m=st.number_input('Manual transmission Yes=1, No=0')
car_t_s=st.number_input('Semi-Automatic transmission Yes=1, No=0')
car_mileage=st.number_input('Mileage')
car_doors=st.number_input('Number of Doors')


#with this code we can request the input but we need to convert those inputs into dataframes
#to do that we would need to use pandas
#convert the user input to a dataframe
car_data=pd.DataFrame({'Brand':car_brand, 'Model':car_model, 'Year':car_year, 'Fuel_Type':car_fuel, 'Mileage':car_mileage, 
                        'Doors':car_doors, 'Transmission_Automatic':car_t_a, 'Transmission_Manual':car_t_m, 
                        'Transmission_Semi-Automatic':car_t_s},index=[0])
#Keys should be the same as column names and also the sequence should be the same

#Predict the house price
prediction=model_cp.predict(car_data)

#display the result
if st.button('Predict'):
    st.write(f'The predicted car price is {prediction[0]*1000000}')