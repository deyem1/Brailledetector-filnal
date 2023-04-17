# Brailledetector filnal
 A CNN approach to detect braille in an image

The Braille detector is a group project for Artificial Intelligence coursework. The project aims to aid accessibility 
of visually impaired individuals and aid integration into the society.

# Braille Detection and transcription
The project uses convolutional neural network to recognize Braille characters from images and individually translates each braille character.

# Dataset
The dataset is for the 
braille detection is in my google drive which can be found at (https://drive.google.com/drive/folders/1vHuEg5pr3S8fvYu0RCi27C4NsFPrMV-x?usp=sharing)
while the transcription dataset can be found in a public kaaggle dataset (https://www.kaggle.com/datasets/shanks0465/braille-character-dataset)
The braille detection dataset consist of augmented braille images.

# Installation
To run successfully this project, you would need to install the dependencies found in requirements.txt file:

# Usage
To use this project, follow these steps:

Web app - Streamlit
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. navigate and open main.py
4. To run the file, in the terminal, enter streamlit run main.py
5. Ensure the trained Models(brailledetect2.h5) should be in the same folder  
6. running the app, the app redirects to your local browser 

Live tracker
1. Install the dependencies in the requirements.txt
2. In a code editor, preferably pycharm, run the script.
3. If the camera window does not pop up, change the following code:
        # Starts camera
        cap = cv2.VideoCapture(0) #<< change 0 to 1 or 2


# Models
A vgg16 model for braille detection and Sequential model for transcription which are in the Brai Detection - Copy.ipynb and
Braille-character-transcription-cnn.ipynb respectively.

# Credits
The Braille character dataset used in this project was obtained from Kaggle and https://github.com/IlyaOvodov/AngelinaDataset.
The neural network architecture was inspired by https://github.com/nicknochnack/FaceDetection and
  https://www.kaggle.com/code/amanrosekaursethi/braille-character-detection-using-cnn.
