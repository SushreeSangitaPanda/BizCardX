# BizCardX
Business Card Information Extraction using Streamlit and EasyOCR

BizCardX is a Streamlit application designed to effortlessly extract relevant information from business cards using the power of easyOCR. The application allows users to upload an image of a business card, perform text extraction, and display the extracted information in a user-friendly graphical user interface (GUI). Users can also store multiple entries, each with its own business card image and extracted information, in a database using SQLite or MySQL.

## Workflow

1. **Home Page**:
   - The application opens with a home page that welcomes the users to BizCardX.
   - The user is provided with an overview of the application's capabilities and features.
   - The home page also showcases the technologies and tools used in the project, including Python, Streamlit, easyOCR, and SQLite/MySQL.
     
     <img width="931" alt="image" src="https://github.com/SushreeSangitaPanda/BizCardX/assets/50452901/f4e5e4db-1bc4-42f1-9180-529d911c2fec">


2. **Image Data Extraction**:
   - Users can navigate to the "Image Data" menu from the sidebar to extract information from a business card image.
   - The user can upload an image of the business card (in jpg, jpeg, or png format) using the file uploader.
   - Once the image is uploaded, the application uses easyOCR and OpenCV to perform text extraction on the image.
   - Extracted information includes the card holder's name, designation, company name, contact number, email address, website URL, address, city, state, and pin code.
   - The extracted information is displayed in a structured format on the GUI.
   - Users have the option to view a bounding box around the detected text for verification purposes.
   - The extracted data can be saved to the database by clicking the "EXTRACT & UPLOAD" button. The data, along with the uploaded image, is inserted into the SQLite database.
     
<img width="931" alt="image" src="https://github.com/SushreeSangitaPanda/BizCardX/assets/50452901/989673a6-1401-4292-b09f-ec91cdeab12a">

3. **Database Management**:
   - Users can access the "Database" menu from the sidebar to manage the stored data.
   - The application fetches data from the SQLite database and displays it in a DataFrame format, showcasing the saved business card entries.
   - Users have three options in the "Database" menu: "Image data," "Update data," and "Delete data."
     - "Image data": Users can select a name and designation from the database and view the associated business card image.
     - "Update data": Users can select a name and designation to update from the database and modify specific fields (e.g., name, designation, contact number, email, etc.).
     - "Delete data": Users can select a name and designation from the database and delete the corresponding entry.
       
<img width="931" alt="image" src="https://github.com/SushreeSangitaPanda/BizCardX/assets/50452901/8dc58883-08a7-4afa-b887-b6c6c642e9a9">

4. **Disclaimer and Info**:
   - A disclaimer message informs users that the detected text on the image might not always be accurate due to ongoing development and improvements in the OCR technology.
   - An informative message at the end of the page reiterates that the application is not perfect, and results may vary depending on image quality and card layout complexity.

## Execution of the BizCardX Streamlit application based on the provided code:

1. **Set Up Environment**: Ensure that Python, Streamlit, and other required libraries (OpenCV, easyOCR, etc.) are installed in the environment.

2. **Prepare Images**: Have a set of business card images in a suitable format (jpg, jpeg, or png) ready for testing the application.

3. **Database Creation**: Run the application code to create an SQLite database named "business_cards1.db" (if it doesn't already exist) and create a table named "card_data" to store extracted business card information and images.

4. **Start the Application**: Run the Streamlit application using the command: `streamlit run your_script.py` (replace "your_script.py" with the filename of the code).

5. **Home Page**: The application will open with a home page displaying the application title ("BizCardX") and an introduction describing the purpose of the application, technologies used, and a brief overview of features.

6. **Navigation**: On the left sidebar, users can find three main menu options: "Home," "Image Data," and "Database." The "Home" option is selected by default.

7. **Image Data**: If the user selects "Image Data," they will be able to upload a business card image using the file uploader. Once the image is uploaded, the application will display the image and provide options to perform OCR text bounding and text extraction.

8. **OCR Text Bounding**: By clicking the "TEXT BOUNDING" button, the application will highlight the detected text regions using green rectangles. Note that this feature may not be perfectly accurate as the application is still under development.

9. **OCR Text Extraction**: By clicking the "EXTRACT & UPLOAD" button, the application will use the easyOCR library to extract relevant information from the business card image. The extracted data, such as name, designation, company, contact, email, website, address, city, state, and pin code, will be displayed on the screen.

10. **Database Operations**: If the user selects "Database," the application will display the extracted business card information stored in the SQLite database in a tabular format.

11. **View Image Data**: Users can select a specific name and designation from the displayed data and click the "Show Image" button to view the corresponding business card image.

12. **Update Data**: To update data in the database, users can select a name and designation, choose a specific column to update (e.g., name, designation, company), and enter the new data in the input field. Clicking the "Update" button will apply the changes to the selected row in the database.

13. **Delete Data**: To delete data from the database, users can select a name and designation and click the "DELETE" button to remove the corresponding row.

14. **Disclaimer and Info Message**: At the end of the application, there will be a disclaimer regarding the accuracy of the detected text and a general info message.

15. **Application Behavior**: Throughout the application, Streamlit's interactive and reactive behavior ensures that the GUI responds to user actions in real-time, updating the displayed content accordingly.

16. **Termination**: The application will continue running until the user stops it explicitly or closes the terminal where it is running.

Remember that the application might still be a work in progress, and improvements to text extraction accuracy and additional features may be continuously added based on ongoing development efforts.
