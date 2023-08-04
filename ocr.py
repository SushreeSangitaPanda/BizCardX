#!/usr/bin/env python
# coding: utf-8

# In[13]:


import streamlit as st
import easyocr
import cv2
import re
import pandas as pd
import sqlite3
import numpy as np
import time
from streamlit_option_menu import option_menu
from PIL import Image
import os

# Set page configuration
icon = Image.open("biz1.png")

# Set Streamlit page configuration
st.set_page_config(page_title= "BizCardX",
                   page_icon= icon,
                   layout= "centered",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# BizCardX: Extracting Business Card Data with OCR"""})



# CSS styles for the application background and text
app_bg = """
<style>
body {
    background-color: #f0f0f0;
    color: #333333;
}
h1 {
    font-family: "Arial", sans-serif;
    font-size: 48px;
    font-weight: bold;
    color: #FF5733;
}
h2 {
    font-family: "Arial", sans-serif;
    font-size: 36px;
    font-weight: bold;
    color: #333333;
}
p {
    font-family: "Arial", sans-serif;
    font-size: 20px;
    color: #555555;
}
.logo {
    text-align: center;
    margin-bottom: 30px;
}
.logo img {
    width: 200px;
    border-radius: 50%;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
}
.main-btn {
    text-align: center;
    margin-top: 30px;
}
.main-btn button {
    font-family: "Arial", sans-serif;
    font-size: 24px;
    font-weight: bold;
    color: #ffffff;
    background-color: #FF5733;
    padding: 15px 40px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}
.main-btn button:hover {
    background-color: #FF754F;
}

/* New button styles */
.button-style {
    font-family: "Arial", sans-serif;
    font-size: 20px;
    font-weight: bold;
    color: #ffffff;
    background-color: #FF5733;
    padding: 10px 30px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
    margin-top: 10px;
    margin-right: 10px;
}
.button-style:hover {
    background-color: #FF754F;
}
</style>
"""
st.markdown(app_bg, unsafe_allow_html=True)
# Create a sidebar with navigation options

with st.sidebar:
    selected_menu = option_menu("BizCardX", ["Home", "Image Data", "Database"],
                         icons=['house', 'images', 'database-fill'],
                         menu_icon="person-vcard", default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#ADD8E6"},
        "icon": {"color": "#007BA7", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#B0E0E6"},
    }
    )

# Depending on the selected menu, display different content
if selected_menu == "Home":
    # Center the image using a container
    with st.container():
        st.image("biz1.png", width=725)

   # Application introduction
    st.markdown("<h1 style='text-align: center; color: #4169E1;'>Welcome to BizCardX!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>BizCardX is a powerful Streamlit application designed to effortlessly extract relevant information from business cards using the cutting-edge technology of easyOCR.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Experience a smooth and intuitive graphical user interface (GUI) that organizes and presents the extracted data in a user-friendly manner, streamlining your business card data management.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Effortlessly store multiple entries, complete with uploaded business card images and extracted information, in a robust database using SQLite or MySQL.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Throughout this project, we leverage image processing, OCR, GUI development, and database management skills to create an application that is scalable, maintainable, and extensible.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>With a focus on clean code organization and comprehensive documentation, we ensure a high-quality and user-friendly experience for our valued users.</p>", unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")

# Technologies and Tools Used
    st.markdown("<p style='text-align: center; font-size: 20px; color: #4169E1; font-weight: bold;'>Technologies and Tools Used:</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px; color: #4169E1;'>Python, Streamlit, easyOCR, SQLite/MySQL</p>", unsafe_allow_html=True)


elif selected_menu == "Image Data":
    # Image Data menu selected
    st.markdown("<h1 style='text-align: center; color: #4169E1; font-size: 48px;'>BizCardX - Image Data</h1>", unsafe_allow_html=True)
    # Center the image
    st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
    st.image("ocr.png", width=625)
    st.markdown("</div>", unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    # Upload a business card image
    uploaded_file = st.file_uploader("Choose an image of a business card", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
         # Read the uploaded image and display it
        file_bytes = uploaded_file.read()

        # Original image
        nparr = np.frombuffer(file_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        st.image(image, channels='BGR', use_column_width=True)

        # Text extraction bounding image
        if st.button('TEXT BOUNDING'):
            with st.spinner('Detecting text...'):
                time.sleep(1)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            new, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            contours, new = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for i in contours:
                x, y, w, h = cv2.boundingRect(i)
                color = (0, 255, 0)
                new = cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            st.write('Compare the images')
            st.image(new, use_column_width=True)
            st.info('Image might be inaccurate detection of text')

    # Text extraction and data processing
    if st.button('EXTRACT & UPLOAD'):
        with st.spinner('Extracting text...'):
            reader = easyocr.Reader(['en'])
            results = reader.readtext(image)
            card_info = [i[1] for i in results]
            demilater = ' '
            card = demilater.join(card_info)

            # Text processing using regular expressions
            replacement = [
                (";", ""),
                (',', ''),
                ("WWW ", "www."),
                ("www ", "www."),
                ('www', 'www.'),
                ('www.', 'www'),
                ('wwW', 'www'),
                ('wWW', 'www'),
                ('.com', 'com'),
                ('com', '.com'),
            ]
            for old, new in replacement:
                card = card.replace(old, new)

            # Extract specific data from the text using regex patterns
            # ... (code to extract and process data)

            # Phone
            ph_pattern = r"\+*\d{2,3}-\d{3}-\d{4}"
            ph = re.findall(ph_pattern, card)
            Phone = ''
            for num in ph:
                Phone = Phone + ' ' + num
                card = card.replace(num, '')

            # Email
            mail_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}\b"
            mail = re.findall(mail_pattern, card)
            Email_id = ''
            for ids in mail:
                Email_id = Email_id + ids
                card = card.replace(ids, '')

            # Website
            url_pattern = r"www\.[A-Za-z0-9]+\.[A-Za-z]{2,3}"
            url = re.findall(url_pattern, card)
            URL = ''
            for web in url:
                URL = URL + web
                card = card.replace(web, '')

            # Pincode
            pin_pattern = r'\d+'
            match = re.findall(pin_pattern, card)
            Pincode = ''
            for code in match:
                if len(code) == 6 or len(code) == 7:
                    Pincode = Pincode + code
                    card = card.replace(code, '')

            # Name, Designation, Company
            name_pattern = r'^[A-Za-z]+ [A-Za-z]+$|^[A-Za-z]+$|^[A-Za-z]+ & [A-Za-z]+$'
            name_data = []
            for i in card_info:
                if re.findall(name_pattern, i):
                    if i not in 'WWW':
                        name_data.append(i)
                        card = card.replace(i, '')

            name = name_data[0] if len(name_data) > 0 else ""
            designation = name_data[1] if len(name_data) > 1 else ""

            if len(name_data) > 2:
                company = name_data[2]
                card = card.replace(name_data[2], '')  # Remove company from the card text
                if len(name_data) > 3:
                    company += ' ' + name_data[3]  # Append the extra part of the company name
            else:
                company = ""

            # City, State, Address
            new = card.split()
            if new[4] == 'St':
                city = new[2]
            else:
                city = new[3]

            if new[4] == 'St':
                state = new[3]
            else:
                state = new[4]

            if new[4] == 'St':
                s = new[2]
                s1 = new[4]
                new[2] = s1
                new[4] = s
                Address = new[0:3]
                Address = ' '.join(Address)
            else:
                Address = new[0:3]
                Address = ' '.join(Address)

            st.write('')
            st.write('###### :red[Name]         :', name)
            st.write('###### :red[Designation]  :', designation)
            st.write('###### :red[Company name] :', company)
            st.write('###### :red[Contact]      :', Phone)
            st.write('###### :red[Email id]     :', Email_id)
            st.write('###### :red[URL]          :', URL)
            st.write('###### :red[Address]      :', Address)
            st.write('###### :red[City]         :', city)
            st.write('###### :red[State]        :', state)
            st.write('###### :red[Pincode]      :', Pincode)

            # Insert data into database
            conn = sqlite3.connect("business_cards.db")
            c = conn.cursor()
            sql = "INSERT INTO card_data (name, designation, company, contact, email, website, address, city, state, pincode, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            val = (name, designation, company, Phone, Email_id, URL, Address, city, state, Pincode, file_bytes)
            c.execute(sql, val)
            conn.commit()
            conn.close()
            st.success('Text extracted & successfully uploaded to the database')

elif selected_menu == "Database":
    # Database menu selected
    st.markdown("<h1 style='text-align: center; color: #4169E1; font-size: 48px;'>BizCardX - Database</h1>", unsafe_allow_html=True)
    # Center the image
    st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
    st.image("data.png", width=625)
    st.markdown("</div>", unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    st.write(" ")

    # Database navigation and operations
    # Check if the database file exists, if not, create a new one

    db_file = "business_cards.db"
    if not os.path.exists(db_file):
        conn = sqlite3.connect(db_file)
        conn.close()
    conn = sqlite3.connect(db_file)
    mycursor = conn.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS card_data (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, designation TEXT, company TEXT, contact TEXT, email TEXT, website TEXT, address TEXT, city TEXT, state TEXT, pincode TEXT, image BLOB)")
    conn.commit()

    mycursor.execute("SELECT * FROM card_data")
    myresult = mycursor.fetchall()
    df = pd.DataFrame(myresult, columns=['id', 'name', 'designation', 'company', 'contact', 'email', 'website', 'address', 'city', 'state', 'pincode', 'image'])
    df.set_index('id', drop=True, inplace=True)
    st.write(df)

    option = st.selectbox("Choose an operation:", ['Image data', 'Update data', 'Delete data'])

    if option == 'Image data':
        mycursor.execute("SELECT name, designation FROM card_data")
        rows = mycursor.fetchall()
        row_name = [row[0] for row in rows]
        row_designation = [row[1] for row in rows]

        # Display the selection box
        selection_name = st.selectbox("Select name", row_name)
        selection_designation = st.selectbox("Select designation", row_designation)
        if st.button('Show Image'):
            sql = "SELECT image FROM card_data WHERE name = ? AND designation = ?"
            mycursor.execute(sql, (selection_name, selection_designation))
            result = mycursor.fetchone()
            if result is not None:
		
                image_data = result[0]
                nparr = np.frombuffer(image_data, np.uint8)
                image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                st.image(image, channels="BGR", use_column_width=True)
            else:
                st.error("Image not found for the given name and designation.")
    
    

    elif option == 'Update data':
        mycursor.execute("SELECT name, designation FROM card_data")
        rows = mycursor.fetchall()
        row_name = [row[0] for row in rows]
        row_designation = [row[1] for row in rows]

        # Display the selection box
        selection_name = st.selectbox("Select name to update", row_name)
        selection_designation = st.selectbox("Select designation to update", row_designation)

        # Get the column names from the table
        mycursor.execute("PRAGMA table_info(card_data)")
        columns = mycursor.fetchall()
        column_names = [i[1] for i in columns if i[1] not in ['id', 'image', 'name', 'designation']]

        # Display the selection box for column name
        selection = st.selectbox("Select specific column to update", column_names)
        new_data = st.text_input(f"Enter the new {selection}")

        if st.button("Update"):
            sql = f"UPDATE card_data SET {selection} = ? WHERE name = ? AND designation = ?"
            mycursor.execute(sql, (new_data, selection_name, selection_designation))
            conn.commit()
            st.success("Updated successfully")

    else:
        mycursor.execute("SELECT name, designation FROM card_data")
        rows = mycursor.fetchall()
        row_name = [row[0] for row in rows]
        row_designation = [row[1] for row in rows]

        # Display the selection box
        selection_name = st.selectbox("Select name to delete", row_name)
        selection_designation = st.selectbox("Select designation to delete", row_designation)

        if st.button('DELETE'):
            sql = "DELETE FROM card_data WHERE name = ? AND designation = ?"
            mycursor.execute(sql, (selection_name, selection_designation))
            conn.commit()
            st.success('Deleted successfully')

    conn.close()
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
# Info about detected text and application status
st.markdown("<h3 style='color: #FF5733;'>Disclaimer:</h3>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 18px;'>The detected text on the image might be inaccurate as the application is still under development and fixing bugs. There is a lot to explore in EasyOCR and OpenCV, and improvements are continuously being made to enhance the accuracy.</p>", unsafe_allow_html=True)
st.write(" ")
st.write(" ")





# Place the st.info message at the end of the page using CSS styles
info_styles = """
    <style>
    .info-message {
        max-width: 90%;
    }
    </style>
"""
st.markdown(info_styles, unsafe_allow_html=True)

st.container()  # Start custom container
st.info("The application is not perfect, and the results may vary depending on the image quality and the complexity of the business card layout.")
st.container()  # End custom container

