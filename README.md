# Minimalist Approach to Training YOLOv8 model with Images

## Description

Simple and minmized implementation of how to modify a yolov8n.pt model into a custom model. 
I recommend using the [apple tree dataset](https://github.com/RoyVoetman/generated-apple-trees-fine-tuning) as a starter dataset, which includes annotations that adhere to the yolo format for 535 images of apple trees. 
This project also includes the use of [ClearMl](https://clear.ml/docs/latest/docs/getting_started/mlops/mlops_first_steps/?utm_campaign=Signup%20Onboarding&utm_medium=email&_hsmi=234908432&_hsenc=p2ANqtz-9su_0Lu03rS1PJgSus3HmJKQoVU1VMAzfp3BM7Vje904BzFpog3MILNiHCETGbXXyTluuHVLQ374r5hbBjb8loARXwmA&utm_content=234908432&utm_source=hs_automation). 

## Installation

Follow these steps to install and set up the project:

1. **Clone the repository**

   First, clone the repository to your local machine. Open your terminal, navigate to the directory where you want to clone the repository and run:

   ```bash
   git clone https://github.com/username/repository.git

2. Navigate to the project directory

    Change your current directory to the project's directory:

    `cd repository`

    Replace repository with the name of your repository.

3. Create a virtual environment (Optional but recommended)

    It's recommended to create a virtual environment to keep the project's dependencies isolated from other Python projects. When working with Python-version specific libraries, this is best handeled with a virutual environment so there are not conflicts with other projects on your machine. If you're using venv module, you can create a virtual environment using the following command:

    `python -m .venv env`

    Then, activate the virtual environment. On macOS and Linux:
    `source env/bin/activate`

    On Windows:
    `.\env\Scripts\activate`

4. Install the dependencies

    The project's dependencies are listed in the requirements.txt file. You can install them with:
    `pip install -r requirements.txt` 

## Usage

In the 'src' directory there are several files:
* train.py: used to train the model.
* annotationtest.py: verify that annotations match the image
* main.py: depreciated, may eventually automate workflow

## License

Nothing yet. Please feel free to use any part of my work!
