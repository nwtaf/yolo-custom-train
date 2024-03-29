# Minimalist Approach to Training Custom YOLOv8 model with Images

## Description

Simple and minmized implementation of how to modify a yolov8n.pt model into a custom model. 
I recommend using the [apple tree dataset](https://github.com/RoyVoetman/generated-apple-trees-fine-tuning) as a starter dataset, which includes annotations that adhere to the yolo format for 535 images of apple trees. 

This project also includes the use of [ClearML](https://clear.ml/docs/latest/docs/getting_started/mlops/mlops_first_steps/?utm_campaign=Signup%20Onboarding&utm_medium=email&_hsmi=234908432&_hsenc=p2ANqtz-9su_0Lu03rS1PJgSus3HmJKQoVU1VMAzfp3BM7Vje904BzFpog3MILNiHCETGbXXyTluuHVLQ374r5hbBjb8loARXwmA&utm_content=234908432&utm_source=hs_automation). 

## Installation

Follow these steps to install and set up the project:

1. **Clone the repository**

   First, clone the repository to your local machine. Open your terminal, navigate to the directory where you want to clone the repository and run:

   ```bash
   git clone https://github.com/username/repository.git

2. Navigate to the project directory

    Change your current directory to the project's directory:
   ```
    cd repository
   ```

    Replace repository with the name of your repository.

4. Create a virtual environment (Optional but recommended)

    It's recommended to create a virtual environment to keep the project's dependencies isolated from other Python projects. When working with Python-version specific libraries, this is best handeled with a virutual environment so there are not conflicts with other projects on your machine. If you're using venv module, you can create a virtual environment using the following command:

    `python -m .venv env`

    Then, activate the virtual environment. On macOS and Linux:
    `source env/bin/activate`

    On Windows:
    `.\env\Scripts\activate`

5. Install the dependencies

    The project's dependencies are listed in the requirements.txt file. You can install them with:
    `pip install -r requirements.txt` 

## Usage

In the 'src' directory there are several files:
* train.py: used to train the model.
* annotationtest.py: verify that annotations match the image
* main.py: depreciated, may eventually automate workflow

It is recommended to split a dataset into training, validation, and testing sets using the common rule of thumb: the 70-15-15 rule, where 70% of images are used for training, 15% are used for validation, and 15% are used for testing. For example, if the apple dataset with 535 images and annotations is used, 375 would be used for training, 80 for validation, and 79 images with annotations for testing. Make sure the image and corresponding annotation make it into the proper data folders (e.g. the same data/images/testing needs to have the same corresponding annotations in data/images/testing).

## License

Nothing yet. Please feel free to use any part of my work!
