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
car_brand=st.number_input('**Select the brand:** Kia:0, Chevrolet:1, Mercedes:2, Audi:3, Volkswagen:4, Toyota:5, Honda:6, BMW:7, Hyundai:8, Ford:9')
car_model=st.number_input('**Select the model:** Rio:0, Malibu:1, GLA:2, Q5:3, Golf:4, Camry:5, Civic:6, Sportage:7, RAV4:8, 5 Series:9, CR-V:10, Elantra:11, Tiguan:12, Equinox:13, Explorer:14, A3:15, 3 Series:16, Tucson:17, Passat:18, Impala:19, Corolla:20, Optima:21, Fiesta:22, A4:23, Focus:24, E-Class:25, Sonata:26, C-Class:27, X5:28, Accord:29')
car_year=st.number_input('**Year**')
car_fuel=st.number_input('**Type of fuel:** Diesel:0,Hybrid:1, Petrol:2, Electric:3')
car_t_a=st.number_input('**Automatic transmission** Yes=1, No=0')
car_t_m=st.number_input('**Manual transmission** Yes=1, No=0')
car_t_s=st.number_input('**Semi-Automatic transmission** Yes=1, No=0')
car_mileage=st.number_input('**Mileage**')
car_doors=st.number_input('**Number of Doors**')


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