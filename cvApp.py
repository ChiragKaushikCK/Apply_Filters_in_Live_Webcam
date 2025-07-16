import cv2
import numpy as np

def apply_filters(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Sobel Filter
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.convertScaleAbs(np.sqrt(sobelx**2 + sobely**2))

    # Prewitt Filter
    kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    prewittx = cv2.filter2D(gray, -1, kernelx)
    prewitty = cv2.filter2D(gray, -1, kernely)
    prewitt = cv2.convertScaleAbs(np.sqrt(prewittx.astype(np.float32)**2 + prewitty.astype(np.float32)**2))

    # Gaussian Blur
    gaussian = cv2.GaussianBlur(gray, (5, 5), 0)

    # Laplacian Filter
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)

    return gray, sobel, prewitt, gaussian, laplacian

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.resize(frame, (320, 240))
    gray, sobel, prewitt, gaussian, laplacian = apply_filters(frame)

    # Convert grayscale filters to BGR so we can stack them with original
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    sobel_bgr = cv2.cvtColor(sobel, cv2.COLOR_GRAY2BGR)
    prewitt_bgr = cv2.cvtColor(prewitt, cv2.COLOR_GRAY2BGR)
    gaussian_bgr = cv2.cvtColor(gaussian, cv2.COLOR_GRAY2BGR)
    laplacian_bgr = cv2.cvtColor(laplacian, cv2.COLOR_GRAY2BGR)

    # Stack horizontally and vertically
    top_row = np.hstack((frame, sobel_bgr))
    bottom_row = np.hstack((prewitt_bgr, gaussian_bgr, laplacian_bgr))

    # Resize bottom row to match top row width
    bottom_row = cv2.resize(bottom_row, (top_row.shape[1], top_row.shape[0]))

    # Final stacked image
    combined = np.vstack((top_row, bottom_row))

    cv2.imshow("Live Webcam Filters - Press 'q' to quit", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
