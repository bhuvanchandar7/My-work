### **Project Description: Real-Time Lane Line Detection with Video Playback**

**Objective:**  
This project aims to develop a real-time lane detection system using computer vision techniques. The system is designed to process video streams, identify lane lines on roadways, and overlay the detected lanes on the original video. The graphical interface displays both the original and processed videos simultaneously, providing a clear comparison of the input and the detected lane lines.

---

### **Key Features**

1. **Lane Detection Algorithm**  
   - **Color Filtering:** Detects yellow and white lane lines using HSV and grayscale color spaces.  
   - **Canny Edge Detection:** Identifies edges within the frame for precise lane marking extraction.  
   - **Region of Interest (ROI):** Focuses the detection process on the relevant area of the frame (road lanes).  
   - **Hough Transform:** Detects straight lines representing lane boundaries.  
   - **Smoothing & Stabilization:** Uses weighted averaging to smooth lane line predictions across frames, ensuring stability.

2. **Real-Time Video Processing**  
   - Processes two video streams simultaneously:
     - **Input Video:** Displays the original video.
     - **Processed Video:** Displays the video with detected lane lines overlaid.

3. **Interactive Graphical Interface**  
   - Built with **Tkinter**, the GUI provides:
     - Two side-by-side video displays for original and processed streams.
     - A clear, user-friendly interface with dynamic video rendering.
     - A quit button to exit the application.

4. **Error Handling & Robustness**  
   - Handles missing or incomplete lane data by detecting and mitigating errors in real-time.
   - Adaptable to varying road conditions, including curves and minor occlusions.

---

### **Technologies Used**

- **Programming Language:** Python  
- **Libraries:**  
  - **OpenCV**: For image and video processing.  
  - **Numpy**: For numerical operations.  
  - **Tkinter**: For creating the GUI interface.  
  - **Pillow (PIL)**: For image handling in the GUI.  
  - **MoviePy**: For advanced video processing (optional).  

---

### **Applications**

- **Automated Driving Systems**: Assists in lane-keeping functionalities in autonomous or semi-autonomous vehicles.
- **Driver Assistance Systems**: Provides visual lane detection for drivers, improving safety and awareness.
- **Traffic Monitoring**: Helps in analyzing traffic behavior by detecting lane adherence.

---

### **System Workflow**

1. Load two video streams:
   - Input video (original footage).
   - Processed video (lane detection output).

2. Process each frame of the video:
   - Convert the image to grayscale and HSV.
   - Detect yellow and white lane lines.
   - Apply edge detection and region masking.
   - Detect lane lines using the Hough Transform.
   - Overlay lane lines on the original frame.

3. Display the output in the GUI:
   - Left: Original video.
   - Right: Video with detected lanes.

4. Allow users to interact with the GUI and terminate the process as needed.

---

### **Future Improvements**

- Integration with vehicle control systems for lane-following functionality.
- Enhancement to detect dashed lines, multiple lanes, and curved lanes.
- Support for various weather conditions and low-light environments.
- Addition of audio or visual alerts for lane departure warnings.

This project demonstrates the real-world applicability of computer vision in enhancing road safety and supporting autonomous vehicle technologies.
