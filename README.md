# Apply_Filters_in_Live_Webcam

````markdown
<h1 align="center" style="font-size: 2.8em; color: #2980b9;">📸 Real-Time Webcam Filter Application</h1>

<p align="center">
  <img src="https://img.shields.io/badge/OpenCV-Live%20Filters-green?style=for-the-badge&logo=opencv">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Edge%20Detection-Sobel%20%7C%20Prewitt%20%7C%20Laplacian-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Webcam-Live%20Stream-lightgrey?style=for-the-badge&logo=webcam">
</p>

---

## ➤ Project Summary

This project uses **OpenCV and NumPy** to apply **real-time edge detection and filtering** techniques to webcam input. Users can view the effects of multiple filters side-by-side as the camera captures frames.

> 🎯 Perfect for understanding visual edge detection techniques in action.

---

## ➤ Filters Implemented

| Filter Name     | Description |
|----------------|-------------|
| ➤ Grayscale     | Converts the frame to black-and-white |
| ➤ Sobel Filter  | Detects edges using gradient in X and Y direction |
| ➤ Prewitt Filter| Similar to Sobel but uses different kernels |
| ➤ Gaussian Blur | Smoothens the image using Gaussian convolution |
| ➤ Laplacian     | Second derivative method for edge detection |

Each filter is applied in real-time on each webcam frame, then displayed side-by-side in a single combined window.

---

## ➤ Features

✔️ Live webcam streaming  
✔️ Multi-filter visualization in real-time  
✔️ Frame resizing for smooth performance  
✔️ Keyboard-interrupt based clean shutdown (`q` key)  
✔️ Custom preprocessing using NumPy & OpenCV  

---

## ➤ How it Works

➤ OpenCV reads frames from your webcam  
➤ Each frame is resized and processed using various filters  
➤ Output from filters is stacked horizontally and vertically  
➤ Final output is shown in a window named `"Live Webcam Filters"`  
➤ Press `'q'` to safely exit and release the camera

---

## ➤ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/webcam-filters-app.git
cd webcam-filters-app

# Install required packages
pip install opencv-python numpy
````

---

## ➤ Run the Application

```bash
python cvApp.py
```

> Press `q` in the window to close the stream and release your webcam.

---

## ➤ Sample Output Layout

```
┌──────────────────────┬──────────────────────┐
│     Original Frame    │      Sobel Filter    │
├──────────────────────┴──────────────────────┤
│ Prewitt | Gaussian | Laplacian (stacked row)│
└─────────────────────────────────────────────┘
```

---

## ➤ Author

**Chirag Kaushik**
*Data Science, Computer Vision & ML Enthusiast*
🔗 [LinkedIn Profile](https://www.linkedin.com/in/chirag-kaushik-profile)

---

## ➤ License

This project is for educational and experimentation purposes only.
Feel free to fork, explore, and modify as needed.

```
