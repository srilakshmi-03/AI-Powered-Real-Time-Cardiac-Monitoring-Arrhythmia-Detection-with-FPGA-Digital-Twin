## Clock Signal (100 MHz)
set_property PACKAGE_PIN H16 [get_ports clk]
set_property IOSTANDARD LVCMOS33 [get_ports clk]

## Switch Inputs for ECG Mode Selection
set_property PACKAGE_PIN M20 [get_ports sw[0]]  ; # SW0
set_property IOSTANDARD LVCMOS33 [get_ports sw[0]]

set_property PACKAGE_PIN M19 [get_ports sw[1]]  ; # SW1
set_property IOSTANDARD LVCMOS33 [get_ports sw[1]]

## LED Outputs for Arrhythmia Indication
set_property PACKAGE_PIN R14 [get_ports led[0]]  ; # LED0
set_property IOSTANDARD LVCMOS33 [get_ports led[0]]

set_property PACKAGE_PIN P14 [get_ports led[1]]  ; # LED1
set_property IOSTANDARD LVCMOS33 [get_ports led[1]]
