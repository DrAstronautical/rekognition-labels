import boto3
import argparse

def detect_labels_local_image(image_path, max_labels=10, min_confidence=80):
    client = boto3.client('rekognition', region_name='us-east-1')  # Adjust your region
    
    with open(image_path, 'rb') as img_file:
        image_bytes = img_file.read()

    response = client.detect_labels(
        Image={'Bytes': image_bytes},
        MaxLabels=max_labels,
        MinConfidence=min_confidence
    )

    print("\nDetected Labels:")
    for label in response['Labels']:
        print(f"{label['Name']} ({label['Confidence']:.2f}%)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect labels in an image using AWS Rekognition")
    parser.add_argument("image_path", help="Path to the image file (e.g., car.jpg)")
    parser.add_argument("--max-labels", type=int, default=10, help="Maximum number of labels to return")
    parser.add_argument("--min-confidence", type=float, default=80.0, help="Minimum confidence for labels")

    args = parser.parse_args()

    detect_labels_local_image(args.image_path, args.max_labels, args.min_confidence)
