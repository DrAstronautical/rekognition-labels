import boto3

def detect_labels_local_image(image_path, max_labels=10, min_confidence=80):
    # Create a Rekognition client
    client = boto3.client('rekognition')

    # Open the image file
    with open(image_path, 'rb') as img_file:
        image_bytes = img_file.read()

    # Call Rekognition to detect labels
    response = client.detect_labels(
        Image={'Bytes': image_bytes},
        MaxLabels=max_labels,
        MinConfidence=min_confidence
    )

    # Print the detected labels and their confidence scores
    print("\nDetected Labels:")
    for label in response['Labels']:
        print(f"- {label['Name']} ({label['Confidence']:.2f}%)")

    return response['Labels']


# Run the function
if __name__ == "__main__":
    image_path = input("Enter the path to your image file: ")
    detect_labels_local_image(image_path)
