<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>

<h1>TextOnImageApp</h1>

<h2>Overview</h2>
<p><strong>TextOnImageApp</strong> is a user-friendly graphical application built using Python's Tkinter library. This app allows users to add text to multiple images, adjust the font size, change the text position, and resize images. It also includes features to ensure the processed images do not exceed 500KB in size. All text in the application is displayed in Arabic, making it accessible for Arabic-speaking users.</p>

<h2>Features</h2>
<ul>
    <li><strong>Multiple Image Selection</strong>: Easily select multiple images at once for processing.</li>
    <li><strong>Font Size Adjustment</strong>: Use the input field to specify the desired font size for the text.</li>
    <li><strong>Text Position Adjustment</strong>: Drag and drop the text on the preview image to set its position manually.</li>
    <li><strong>Resolution Adjustment</strong>: Use the slider to adjust the resolution of the images before saving.</li>
    <li><strong>Save Location Selection</strong>: Choose a directory to save the processed images.</li>
    <li><strong>Progress Bar</strong>: Monitor the progress of the image processing tasks.</li>
    <li><strong>Notification</strong>: Get a notification once the processing is successfully completed.</li>
    <li><strong>Arabic Interface</strong>: All user interface elements are in Arabic for better accessibility.</li>
</ul>

<h2>Installation</h2>
<h3>Prerequisites</h3>
<p>Python 3.6 or higher</p>

<h3>Steps</h3>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/yourusername/TextOnImageApp.git
cd TextOnImageApp
        </code></pre>
    </li>
    <li>(Optional) Create a virtual environment:
        <pre><code>python -m venv env
source env/bin/activate   # On Windows: .\env\Scripts\activate
        </code></pre>
    </li>
    <li>Install the required packages:
        <pre><code>pip install -r requirements.txt
        </code></pre>
    </li>
    <li>Run the application:
        <pre><code>python add_text_to_images.py
        </code></pre>
    </li>
    <li>(Optional) Create an executable using PyInstaller:
        <pre><code>pyinstaller --onefile --windowed add_text_to_images.py
        </code></pre>
    </li>
</ol>

<h2>Usage</h2>
<ol>
    <li><strong>Select Images</strong>: Click the "اختر الصور" button to select multiple images.</li>
    <li><strong>Set Font Size</strong>: Enter the desired font size in the "حجم الخط" input field.</li>
    <li><strong>Adjust Resolution</strong>: Use the slider to set the image resolution percentage.</li>
    <li><strong>Select Save Location</strong>: Click the "اختر مكان الحفظ" button to choose where to save the processed images.</li>
    <li><strong>Start Processing</strong>: Click the "ابدأ المعالجة" button to start adding text to images and resizing them.</li>
    <li><strong>Drag Text</strong>: Use the mouse to drag the text on the preview image to the desired position.</li>
</ol>

<h2>Dependencies</h2>
<ul>
    <li>Pillow</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the MIT License.</p>

</body>
</html>
