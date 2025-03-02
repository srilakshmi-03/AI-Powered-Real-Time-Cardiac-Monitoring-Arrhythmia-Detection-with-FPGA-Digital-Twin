# Synthetic ECG Generation & Detection on Xilinx ARTY Z7-20 FPGA

This project implements synthetic ECG signal generation and QRS detection using the Pan-Tompkins method on the Xilinx ARTY Z7-20 FPGA. The implementation generates normal and arrhythmic ECG waveforms, processes them in real-time, and outputs results via LED indicators and the Vivado TCL console.

## 📌 Features
- ECG Signal Generation: FPGA-based synthetic ECG generation without ROM.
- Pan-Tompkins Algorithm: Real-time QRS detection and classification.
- Multiple ECG Modes:
  - Mode 0: Normal ECG → "No Cardiac Arrhythmia"
  - Mode 1, 2, 3: Different Arrhythmia Types (Displayed in the TCL console)
- FPGA Output:
  - LED Indicators: Shows real-time detection results.
  - Vivado TCL Console: Prints the classification result.

---

## 🚀 Setup & Execution Guide

### 1️⃣ Prerequisites
Ensure you have the following:
- Vivado 2024.1 (or compatible version)
- Xilinx ARTY Z7-20 FPGA Board
- Micro-USB cable for programming
- Verilog/VHDL knowledge (for understanding modifications)

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/synthetic-ecg-fpga.git
cd synthetic-ecg-fpga
```

### 3️⃣ Open the Project in Vivado
1. Launch Vivado and create a new project.
2. Select "RTL Project" (No Block Design required).
3. Add Verilog Files (`ecg_generator.v`, `pan_tompkins.v`, `top_module.v`).
4. Set ARTY Z7-20 as the Target Device (`xc7z020clg400-1`).
5. Run Synthesis & Implementation.

### 4️⃣ Generate the Bitstream
After successful synthesis and implementation:
```sh
write_bitstream -force ecg_project.bit
```

### 5️⃣ Upload to the FPGA
Connect the ARTY Z7-20 FPGA via USB and program it:
```sh
open_hw
connect_hw_server
open_hw_target
set_property PROGRAM.FILE {ecg_project.bit} [current_hw_device]
program_hw_devices
```

### 6️⃣ Observe Output
- LEDs: Indicate normal/arrhythmic ECG detection.
- Vivado TCL Console: Displays classification messages.

---

