import cv2

def main():
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("Error: Could not open video device.")
        return

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break


if __name__ == "__main__":
    main()
