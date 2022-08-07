import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('🥣 Breakfast Favorites')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')

import pandas

streamlit.title('🍌Build Your Own Fruit Smoothie🥝')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

#New Section to display fruitvice api response

import requests

streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit whould you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Normalized JSON response from fruityvice_response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#return response as table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector


