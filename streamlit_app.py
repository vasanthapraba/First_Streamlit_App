import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My Parents New Healthy Dinner')


streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Fruit Smoothie 🥝🍇')
myfruitlist = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
myfruitlist = myfruitlist.set_index('Fruit')

#Allow the user to select some fruits
fruit_selected = streamlit.multiselect("Choose some furits",list(myfruitlist.index),['Grapes','Apple'])

fruit_toshow = myfruitlist.loc[fruit_selected]

#display in page
streamlit.dataframe(fruit_toshow)

#New section to show the fruityvice fruites list
streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#Normalize the json
normalized_json = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(normalized_json)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


