import streamlit
import pandas as pd 



streamlit.title("My Parents New Healthy Diner")

   
streamlit.header(" Breakfast Menu")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale , Spinach & Rocket Smoothie")
streamlit.text(" 🐔 Hard-Boiled Free-range Egg")
streamlit.text("🥑🍞 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include
default_fruits = ['Avocado', 'Strawberries']
selected_fruits = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), default_fruits)
fruits_to_show = my_fruit_list.loc[selected_fruits]  # Use the correct variable name
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# Normalizing the data from Json fromat 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Displaying data in dataframes
streamlit.dataframe(fruityvice_normalized)

streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

