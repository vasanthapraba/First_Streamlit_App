import streamlit
import pandas

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Fruit Smoothie 🥝🍇')
myfruitlist = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
myfruitlist = my_fruit_list.set_index('Fruit')

#Allow the user to select some fruits
streamlit.multiselect("Choose some furits",list(myfruitlist.index))

#display in page
streamlit.dataframe(myfruitlist)
