# Rekognition Labels CLI Tool

A command-line Python app that uses **Amazon Rekognition** to detect objects, scenes, and concepts in images.

Built using `boto3`, this tool lets you analyze any local image and returns a list of labels with confidence scores.

---

## 📸 Example Output

    $ python main.py car.jpg --max-labels 5 --min-confidence 85

    Detected Labels:
    Car (100.00%)
    Coupe (100.00%)
    Sports Car (100.00%)
    Vehicle (100.00%)
    Mustang (92.97%)

---

## ✅ Requirements

- Python 3.10+
- AWS account and credentials
- AWS CLI installed and configured (`aws configure`)
- `boto3` Python library

---

## 🔧 Installation

(Optional) Create and activate a virtual environment:

    python -m venv venv

    # Windows
    .\venv\Scripts\activate

    # macOS/Linux
    source venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

---

## 🚀 Usage

Run the CLI tool with an image path and optional parameters:

    python main.py car.jpg --max-labels 5 --min-confidence 85

- `car.jpg`: Path to your image file  
- `--max-labels`: Maximum number of labels to detect (default: 10)  
- `--min-confidence`: Minimum confidence threshold percentage (default: 80)  

---

## 🔐 AWS Setup

1. Go to the AWS Console and create a new IAM user.  
2. Attach the **AmazonRekognitionFullAccess** policy to the user.  
3. Download the user's Access Key ID and Secret Access Key.  
4. Run this command and enter the keys when prompted:

    aws configure

5. Choose your preferred AWS region (e.g., `us-east-1`).  
6. This creates the `.aws/credentials` file used by the script to authenticate.  

---

## 📂 Project Structure

    rekognition-labels/
    ├── car.jpg                  # Sample image for testing
    ├── main.py                  # CLI app entry point
    ├── label_detector.py        # Rekognition logic module
    ├── requirements.txt         # Python dependencies
    └── README.md                # This documentation file

---

## 📽️ Demo

https://github.com/DrAstronautical/rekognition-labels/blob/main/demo.mp4

---

## 📄 License

MIT License. Feel free to use, modify, and distribute this project.

---

Feel free to open issues or submit pull requests if you want to improve the project!
