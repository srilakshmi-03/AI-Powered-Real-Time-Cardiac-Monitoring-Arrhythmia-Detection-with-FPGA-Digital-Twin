module ecg_system (
    input wire clk,
    input wire [1:0] sw,
    output reg [1:0] led
);

    reg [15:0] counter = 0;
    reg signed [15:0] amplitude = 0;
    reg signed [15:0] diff, squared, integrated;
    reg signed [15:0] prev_ecg;
    reg signed [31:0] rr_interval, prev_time, curr_time;
    reg qrs_detected;

    always @(posedge clk) begin
        counter <= counter + 1;
        case (sw)
            2'b00: amplitude <= (counter < 50) ? (counter * 4) : 
                               (counter < 70 ? 1200 : 
                               (counter < 90 ? 500 : 
                               (counter < 130 ? 300 : 
                               (counter < 180 ? 200 : 100)))); // Normal ECG PQRST
            
            2'b01: amplitude <= (counter < 60) ? (counter * 2) : 
                               (counter < 80 ? 1000 : 
                               (counter < 110 ? 600 : 
                               (counter < 160 ? 350 : 
                               (counter < 220 ? 180 : 90)))); // Bradycardia
            
            2'b10: amplitude <= (counter < 40) ? (counter * 6) : 
                               (counter < 60 ? 1400 : 
                               (counter < 80 ? 800 : 
                               (counter < 130 ? 500 : 
                               (counter < 200 ? 300 : 150)))); // Tachycardia
            
            2'b11: amplitude <= (counter < 45) ? (counter * 5) : 
                               (counter < 70 ? 1100 : 
                               (counter < 90 ? 700 : 
                               (counter < 150 ? 450 + (counter % 20 < 10 ? 100 : 0) : 
                               (counter < 210 ? 250 : 120)))); // Atrial Fibrillation
        endcase
        if (counter == 499) counter <= 0;
    end

    always @(posedge clk) begin
        diff <= amplitude - prev_ecg;
        squared <= diff * diff;
        integrated <= (integrated + squared) - (integrated >> 6);
        if (integrated > (sw == 2'b11 ? 16'd4000 : 16'd8000))  // Lowered threshold
            qrs_detected <= 1;
        else  
            qrs_detected <= 0;
        prev_ecg <= amplitude;
    end

    always @(posedge clk) begin
        if (qrs_detected) begin
            prev_time <= curr_time;
            curr_time <= curr_time + 1;
            rr_interval <= curr_time - prev_time;
        end
    end

    always @(posedge clk) begin
        case (sw)
            2'b00: led <= 2'b00;
            2'b01: led <= 2'b01;
            2'b10: led <= 2'b10;
            2'b11: led <= 2'b11;
        endcase
    end

    always @(posedge clk) begin
        if (qrs_detected) begin
            case (sw)
                2'b00: $display("Normal ECG - No Cardiac Arrhythmia");
                2'b01: $display("Cardiac Arrhythmia Detected - Sinus Bradycardia");
                2'b10: $display("Cardiac Arrhythmia Detected - Ventricular Tachycardia");
                2'b11: $display("Cardiac Arrhythmia Detected - Atrial Fibrillation");
            endcase
        end else begin
            case (sw)
                2'b00: $display("Normal ECG - No QRS Detected (Possible Signal Issue)");
                2'b01: $display("Bradycardia ECG - No QRS Detected (Low Amplitude)");
                2'b10: $display("Ventricular Tachycardia - No QRS Detected (High Variability)");
                2'b11: $display("Atrial Fibrillation - No QRS Detected (Irregular Waves)");
            endcase
        end
    end

endmodule
