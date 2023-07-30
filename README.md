# BizCardX
Business Card Information Extraction using Streamlit and EasyOCR

BizCardX is a Streamlit application designed to effortlessly extract relevant information from business cards using the power of easyOCR. The application allows users to upload an image of a business card, perform text extraction, and display the extracted information in a user-friendly graphical user interface (GUI). Users can also store multiple entries, each with its own business card image and extracted information, in a database using SQLite or MySQL.

## Workflow

1. **Home Page**:
   - The application opens with a home page that welcomes the users to BizCardX.
   - The user is provided with an overview of the application's capabilities and features.
   - The home page also showcases the technologies and tools used in the project, including Python, Streamlit, easyOCR, and SQLite/MySQL.
   - <img width="859" alt="image" src="https://github.com/SushreeSangitaPanda/BizCardX/assets/50452901/5c7681d0-8083-495b-8503-b3e9aa58ec46">


2. **Image Data Extraction**:
   - Users can navigate to the "Image Data" menu from the sidebar to extract information from a business card image.
   - The user can upload an image of the business card (in jpg, jpeg, or png format) using the file uploader.
   - Once the image is uploaded, the application uses easyOCR and OpenCV to perform text extraction on the image.
   - Extracted information includes the card holder's name, designation, company name, contact number, email address, website URL, address, city, state, and pin code.
   - The extracted information is displayed in a structured format on the GUI.
   - Users have the option to view a bounding box around the detected text for verification purposes.
   - The extracted data can be saved to the database by clicking the "EXTRACT & UPLOAD" button. The data, along with the uploaded image, is inserted into the SQLite database.
     
<img width="847" alt="image" src="https://github.com/SushreeSangitaPanda/BizCardX/assets/50452901/989673a6-1401-4292-b09f-ec91cdeab12a">

3. **Database Management**:
   - Users can access the "Database" menu from the sidebar to manage the stored data.
   - The application fetches data from the SQLite database and displays it in a DataFrame format, showcasing the saved business card entries.
   - Users have three options in the "Database" menu: "Image data," "Update data," and "Delete data."
     - "Image data": Users can select a name and designation from the database and view the associated business card image.
     - "Update data": Users can select a name and designation to update from the database and modify specific fields (e.g., name, designation, contact number, email, etc.).
     - "Delete data": Users can select a name and designation from the database and delete the corresponding entry.
       
<img width="847" alt="image" src="https://github.com/SushreeSangitaPanda/BizCardX/assets/50452901/8dc58883-08a7-4afa-b887-b6c6c642e9a9">

4. **Disclaimer and Info**:
   - A disclaimer message informs users that the detected text on the image might not always be accurate due to ongoing development and improvements in the OCR technology.
   - An informative message at the end of the page reiterates that the application is not perfect, and results may vary depending on image quality and card layout complexity.

## Execution

1. Install the required dependencies mentioned in the project environment (Python, Streamlit, easyOCR, OpenCV).
2. Create a database (SQLite or MySQL) to store the extracted business card data.
3. Ensure the necessary images ("biz1.png," "ocr.png," "data.png") are present in the project directory.
4. Run the "app.py" file to start the Streamlit application.
5. The application will launch in the default web browser, and the user can interact with the GUI.
6. The user can select the desired menu from the sidebar and follow the instructions to extract data from business card images and manage the database entries.

Please note that the application is under development, and improvements are continuously being made to enhance the accuracy of the OCR results.
