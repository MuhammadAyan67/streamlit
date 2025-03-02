import streamlit as st

st.title("🌍Unit Converter App")
st.write("### Welcome to the Unit Convertor App! ")
st.write("##### Converts Length, Weight, Temperature And Time Instantly")
category_type = ["Length", "Weight", "Time","Temperature"]
category = st.selectbox("Choose a categoty", category_type)

if category == "Length":
       length_unit = ["Meter", "Kilometer", "Inche","Centimeter" ,"feet"]
       input_value = st.number_input("Enter the value to convert:", min_value=0.0,format="%.2f")
       from_unit = st.selectbox("From", length_unit)
       to_unit = st.selectbox("To", length_unit) 
      
       length_conversion = {"Meter":1, "Kilometer":1000, "Inche":0.0254, "Centimeter":0.01, "feet":0.3048}
      
       if st.button("Convert"):
        result = input_value * length_conversion[from_unit] /length_conversion[to_unit]
        st.success(f"{input_value} {from_unit} is equal to {result:.2f} {to_unit}")


elif category == "Weight":
         weight_unit = ["Kilogram", "Gram", "Pound","Ounce"]
         input_value = st.number_input("Enter the value to convert:", min_value=0.0,format="%.2f")
         from_unit = st.selectbox("From", weight_unit)
         to_unit = st.selectbox("To", weight_unit) 
      
         weight_conversion = {"Kilogram":1, "Gram":0.001, "Pound":0.453592, "Ounce":0.0283495}

         if st.button("Convert"):
          result = input_value * (weight_conversion[from_unit] /weight_conversion[to_unit])
          st.success(f"{input_value} {from_unit} is equal to {result:.2f} {to_unit}")

elif category == "Temperature":
        temperature_unit = ["Celsius", "Fahrenheit", "Kelvin"]
        input_value = st.number_input("Enter the value to convert:", min_value=0,format="%.2f")
        from_unit = st.selectbox("From",temperature_unit)
        to_unit = st.selectbox("To", temperature_unit) 
      
        def convert_temperature(input_value, from_unit, to_unit):
         if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
             return (input_value * 9/5) + 32
            elif to_unit == "Kelvin":
                return input_value + 273.15
          
         elif from_unit == "Fahrenheit": 
            if to_unit == "Celsius":
             return (input_value - 32) * 5/9
            elif to_unit == "Kelvin":
                    return (input_value - 32) * 5/9 + 273.15
         elif from_unit == "Kelvin":
                if to_unit == "Celsius":
                    return input_value - 273.15
                elif to_unit == "Fahrenheit":
                 return (input_value - 273.15) * 9/5 + 32
                return input_value
           
        if st.button("Convert"):
                    result = convert_temperature(input_value, from_unit, to_unit)
                    st.write(f"{input_value} {from_unit} is equal to {result} {to_unit}")


elif category == "Time":
        time_unit = ["Second", "Minute", "Hour","Day"]
        input_value = st.number_input("Enter the value to convert:", min_value=0,format="%.2f")
        from_unit = st.selectbox("From",time_unit)
        to_unit = st.selectbox("To", time_unit) 
      
        time_conversion = {"Second":1, "Minute":60, "Hour":3600, "Day":86400}
      
        if st.button("Convert"):
            result = input_value * time_conversion[from_unit] /time_conversion[to_unit]
            st.success(f"{input_value} {from_unit} is equal to {result:.2f} {to_unit}")

st.feedback("thumbs")
st.warning("◂◂     ▪    Made by Aγαπ 😊    ▪     ▸▸ ") 