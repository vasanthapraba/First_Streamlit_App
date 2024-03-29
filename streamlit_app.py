import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents New Healthy Dinner')

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    normalized_json = pandas.json_normalize(fruityvice_response.json())
    return normalized_json
    
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
        return my_cur.fetchall()

def add_row_to_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("Insert into pc_rivery_db.public.fruit_load_list values('"+new_fruit+"')")
        return 'Thank you for adding '+new_fruit
        
    
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

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please select a fruit to get information....')
  else:
    streamlit.dataframe(get_fruityvice_data(fruit_choice))

except URLError as e:
  streamlit.error()

streamlit.header('View our Fruite List - Add your favourite!')
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)

add_fruit = streamlit.text_input("What fruit would you like to add?")
if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = add_row_to_snowflake(add_fruit)
    my_cnx.close()
    streamlit.text(back_from_function)

streamlit.stop()
