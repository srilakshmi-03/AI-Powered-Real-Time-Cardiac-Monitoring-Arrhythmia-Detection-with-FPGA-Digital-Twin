Real-time ECG Processing and Detection of Cardiac Arrhythmia  

This project uses the AD8232 ECG sensor and ESP32 to capture heart rate signals, process them, and classify ECG patterns as normal or abnormal using a machine learning model. The system uses VS Code, Tkinter, and Python for ECG signal acquisition, image analysis, and classification.  

---

Features  
- Real-time ECG Signal Acquisition: Uses AD8232 & ESP32.  
- Image-based ECG Classification: Machine learning model predicts normal/abnormal.  
- GUI for Image Upload & Classification: Built with Tkinter.  
- Training & Prediction: Uses TensorFlow/Keras and NumPy.  

---

Setup & Execution Guide  

1️⃣ Prerequisites  
Ensure you have the following:  
- ESP32 Microcontroller  
- AD8232 ECG Sensor Module  
- ECG Electrodes & Connecting Wires  
- Arduino IDE, Python 3.7, VS Code  
- Tkinter (for GUI & Image Uploads)  

2️⃣ Upload Arduino Code  
- Open sketch_feb28a.ino in Arduino IDE.  
- Connect Arduino and upload the code.  
- Open the Serial Plotter to view real-time ECG data.  

3️⃣ Train the Deep Learning Model  
```sh
python train_model.py
```  
Trains an ECG classification model and saves it as ecg_model.h5.  

4️⃣ Run ECG Classification GUI  
```sh
python predict_image.py
```  
Upload an ECG image and get classification results (Normal / Abnormal).  

---

Example Output  

- Input ECG Signal (Image Upload)  
- Classification Result  
- Prediction: NORMAL (when done using a normal patient heart ECG signals.)  

---

This project integrates real-time ECG acquisition with machine learning to provide a portable cardiac monitoring system.  
