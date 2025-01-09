import cv2
import numpy as np

def main():
    video_capture = cv2.VideoCapture(0)
    
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
            
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Stronger blur to reduce noise from card designs
        blurred = cv2.GaussianBlur(gray, (7, 7), 0)
        
        # Adaptive threshold instead of Canny
        thresh = cv2.adaptiveThreshold(
            blurred, 255, 
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 11, 2
        )
        
        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Keep track of found cards
        found_cards = []
        
        for contour in contours:
            area = cv2.contourArea(contour)
            # Adjust these values based on your camera and cards
            if area > 20000 and area < 200000:  
                peri = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
                
                if len(approx) == 4:
                    # Draw red outline around cards
                    cv2.drawContours(frame, [approx], -1, (0, 0, 255), 3)
                    found_cards.append(approx)
        
        # Show how many cards we found
        cv2.putText(frame, f"Cards found: {len(found_cards)}", 
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                    1, (0, 255, 0), 2)
        
        cv2.imshow('Original', frame)
        cv2.imshow('Threshold', thresh)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()