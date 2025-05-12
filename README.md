# Color-Detection-With-OpenCV
In this repo I use openCV to detect traffic light colors.

# 🚦 Traffic Light Color Detection with OpenCV

This project detects traffic light colors — **Red**, **Yellow**, and **Green** — in a video using OpenCV. When a green light is detected, the script overlays a message `"Green : GO!"` on the video. The processed video is saved as a new file.

## 🎯 Features

- Detects Red, Yellow, and Green lights using HSV color space.
- Draws bounding boxes around each detected light.
- Displays `"Green : GO!"` message when green light appears.
- Saves annotated video as `TrafficLight.mp4`.

---

## 📁 Files

- `traffic_light_detection.py` – Main detection script.
- `TrafficLight.mp4` – Output video with detection results (generated after running the script).
- Input video – Replace the path in the script with your own video file.

---

## 🧰 Requirements

Install the required Python libraries:

```bash
pip install opencv-python numpy pillow

