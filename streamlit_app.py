import streamlit
import pandas
import requests

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

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

#Normalize the json
normalized_json = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(normalized_json)


