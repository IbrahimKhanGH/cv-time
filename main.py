import cv2

def main():
    webcam = cv2.VideoCapture(0)
    if not webcam.isOpened():
        print("Error: Could not open video device.")
        return

    count = 0

    while True:
        ret, frame = webcam.read()
        if not ret:
            break
    
        cv2.imshow('FunCam', frame)

        count += 1
        print(count)

        # Wait for 1ms and check if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite(f'frame_{count}.jpg', frame)


    webcam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
