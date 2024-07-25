TextOnImageApp
Overview
TextOnImageApp is a user-friendly graphical application built using Python's Tkinter library. This app allows users to add text to multiple images, adjust the font size, change the text position, and resize images. It also includes features to ensure the processed images do not exceed 500KB in size. All text in the application is displayed in Arabic, making it accessible for Arabic-speaking users.

Features
Multiple Image Selection: Easily select multiple images at once for processing.
Font Size Adjustment: Use the input field to specify the desired font size for the text.
Text Position Adjustment: Drag and drop the text on the preview image to set its position manually.
Resolution Adjustment: Use the slider to adjust the resolution of the images before saving.
Save Location Selection: Choose a directory to save the processed images.
Progress Bar: Monitor the progress of the image processing tasks.
Notification: Get a notification once the processing is successfully completed.
Arabic Interface: All user interface elements are in Arabic for better accessibility.
Installation
Prerequisites
Python 3.6 or higher
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/TextOnImageApp.git
cd TextOnImageApp
(Optional) Create a virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate   # On Windows: .\env\Scripts\activate
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python add_text_to_images.py
(Optional) Create an executable using PyInstaller:

bash
Copy code
pyinstaller --onefile --windowed add_text_to_images.py
Usage
Select Images: Click the "اختر الصور" button to select multiple images.
Set Font Size: Enter the desired font size in the "حجم الخط" input field.
Adjust Resolution: Use the slider to set the image resolution percentage.
Select Save Location: Click the "اختر مكان الحفظ" button to choose where to save the processed images.
Start Processing: Click the "ابدأ المعالجة" button to start adding text to images and resizing them.
Drag Text: Use the mouse to drag the text on the preview image to the desired position.
Dependencies
Pillow
License
This project is licensed under the MIT License.
