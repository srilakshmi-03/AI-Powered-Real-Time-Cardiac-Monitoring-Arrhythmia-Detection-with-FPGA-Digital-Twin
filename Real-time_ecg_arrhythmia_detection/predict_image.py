import numpy as np
import tensorflow as tf
import tkinter as tk
from tkinter import filedialog, Label, messagebox
from PIL import Image, ImageTk
import cv2

# Load the trained model
model_path = r"C:\Users\hp\Desktop\ecg_classification\models\ecg_classifier_model.h5"
try:
    model = tf.keras.models.load_model(model_path)
except Exception as e:
    messagebox.showerror("Model Error", f"Failed to load model: {e}")
    exit()

def predict_ecg_from_image(image_path):
    try:
        # Read and preprocess the image
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, (188, 188))
        image = np.mean(image[89:99, :], axis=0)  # Middle 10 rows average
        image = image / 255.0
        image = np.reshape(image, (1, 188))

        # Debugging: Check processed image shape
        print("Processed Image Shape:", image.shape)

        # Make prediction
        pred = model.predict(image)
        
        # Debugging: Print model output
        print("Raw Model Prediction:", pred)

        # Check prediction output shape
        if len(pred.shape) == 2 and pred.shape[1] == 2:
            print("Interpreting as softmax output (2-class classification).")
            confidence = pred[0][0]
        elif len(pred.shape) == 1 or pred.shape[1] == 1:
            print("Interpreting as sigmoid output (binary classification).")
            confidence = pred[0]  # Use directly if single output neuron
        else:
            print("Unexpected prediction shape:", pred.shape)
            return "Error: Model output shape incorrect"

        print(f"Confidence for Normal: {confidence}")

        # Apply threshold-based decision
        if confidence > 0.65:
            print("Final Decision: NORMAL")
        else:
            print("Final Decision: ABNORMAL")

    except Exception as e:
        print(f"Error during prediction: {e}")
        return f"Error: {e}"


# Function to handle image upload and prediction
def upload_and_predict():
    file_path = filedialog.askopenfilename(
        title="Select ECG Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    if file_path:
        prediction = predict_ecg_from_image(file_path)
        result_label.config(text=f"Prediction: {prediction}")

# Set up Tkinter GUI
root = tk.Tk()
root.title("ECG Image Classification")

# Set window size and prevent resizing
root.geometry("400x500")
root.resizable(False, False)

# Set custom icon for the window
icon_path = r"C:\Users\hp\Desktop\ecg_classification\The star.png"  # Path to your icon file
try:
    icon_image = Image.open(icon_path)
    icon_image_tk = ImageTk.PhotoImage(icon_image)
    root.iconphoto(False, icon_image_tk)
except Exception as e:
    print(f"Warning: Could not load icon - {e}")

# Set up the background image
bg_image_path = r"C:\Users\hp\Desktop\ecg_classification\gradient wave.png"  # Path to background image
try:
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((400, 500), Image.Resampling.LANCZOS)  # Resize to fit window
    bg_image_tk = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_image_tk)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Stretch the background image to fill the window
except Exception as e:
    print(f"Warning: Could not load background image - {e}")

# Button to upload image and label to display prediction
upload_button = tk.Button(root, text="Upload ECG Image", command=upload_and_predict)
upload_button.pack(pady=10)

result_label = Label(root, text="Prediction: None", font=("Arial", 16), bg="black", fg="white")
result_label.pack(pady=10)

# Keep the Tkinter GUI running
root.mainloop()
