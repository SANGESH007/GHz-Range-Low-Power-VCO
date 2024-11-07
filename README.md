# A 4-6 GHz Low-Power Voltage Controlled Oscillator with Wide Voltage Range Operation 

This project simulates the designed Voltage controlled oscillator circuit to determine its performance characterisitics for pre-layout 

## A Glance at the VCO IP

Voltage Controlled Oscillator is one of the crucial component in communication systems. This paper discusses the design of a low-power VCO tailored for GHz frequency applications. The VCO is developed using CMOS technology and the Sky water 130nm PDK. This VCO operates within a wide voltage range and delivers an output frequency of 4-6 GHz and the designed VCO is expected to consume less than 1mW power at 1.8 V. This low power consumption makes the VCO suitable for applications such as IoT and battery-operated wireless systems, where energy efficiency is essential.

## Block Diagram of the VCO IP
![blackbox](https://github.com/user-attachments/assets/d0f7a998-d449-4df0-84bf-1046016c048c)

## Circuit Diagram of the VCO IP
![circuit](https://github.com/user-attachments/assets/f559013b-af7b-4255-b2ba-be5bd3b70682)
# Specifications

| Parameter                   | Symbol | Min Value | Typical Value | Max Value | Unit |
|:---------------------------:|:------:|:---------:|:-------------:|:---------:|:----:|
| Technology                  | -      | -         | 130           | -         | nm   |
| Supply Voltage              | VDD    | 1.6       | 1.8           | 3.4       | V    |
| Operating Temperature Range | T      | -40       | +27           | +85       | °C   |
| Control Voltage             | Vcntrl | 0         | 0.3           | 1         | V    |
| Output VCO Frequency        | Vout   | 4.10 G    | 4.76 G        | 7 G       | Hz   |
| Power consumption           | -      | 0.385     | 0.602         | 3.947     | mW   |

## VCO Performance parameters @ Vcntrl = 0v
| VDD |  ΔVout | Vout_min | Vout_max | Frequency(GHz) | Lock time | Power(mW) |
|   :---:      |     :---:      |   :---:       |    :---:      |    :---:     |    :---:       |    :---:      |
| 1.6 | 1.6580 | 0.0321 | 1.6901 | 4.104  | 1.35ns | 0.385 |    
| 1.7 | 1.740  | 0.0383 | 1.7787 | 4.4498 | 1.07ns | 0.486 |
| 1.8 | 1.815  | 0.0465 | 1.8618 | 4.7621 | 957ps  | 0.602 |
| 1.9 | 1.9    | 0.0523 | 1.9524 | 5.0440 | 1.15ns | 0.722 |
| 2   | 1.9785 | 0.0588 | 2.0374 | 5.3071 | 1.12ns | 0.859 |
| 2.1 | 2.0534 | 0.0654 | 2.1188 | 5.5430 | 1.05ns | 1.008 |
| 2.2 | 2.1235 | 0.0732 | 2.1968 | 5.7567 | 1.07ns | 1.167 |
| 2.3 | 2.2017 | 0.0807 | 2.2824 | 5.9496 | 757ps  | 1.338 |
| 2.4 | 2.2781 | 0.0836 | 2.3665 | 6.1117 | 1ns    | 1.518 |
| 2.5 | 2.3428 | 0.0977 | 2.4405 | 6.2546 | 1.06ns | 1.714 |
| 2.6 | 2.4212 | 0.1076 | 2.5289 | 6.3620 | 1.08ns | 1.916 |
| 2.7 | 2.4911 | 0.1783 | 2.6089 | 6.4736 | 1.05ns | 2.129 |
| 2.8 | 2.5573 | 0.1289 | 2.6862 | 6.5956 | 979ps  | 2.351 |
| 2.9 | 2.6198 | 0.1411 | 2.7610 | 6.6800 | 985ps  | 2.584 |
| 3   | 2.677  | 0.1547 | 2.8325 | 6.7824 | 971ps  | 2.835 |
| 3.1 | 2.7313 | 0.1696 | 2.9009 | 6.8481 | 928ps  | 3.093 |
| 3.2 | 2.7791 | 0.1868 | 2.9660 | 6.8920 | 957ps  | 3.362 |
| 3.3 | 2.8223 | 0.2050 | 3.027  | 6.9606 | 928ps  | 3.644 |
| 3.4 | 2.8591 | 0.2260 | 3.0851 | 7.008  | 1.04ns | 3.947 |





# Pre-Layout Performance characterisitics

### Transient Response of VCO @ VDD = 1.8V and Vcntrl = 0V

![trans_final](https://github.com/user-attachments/assets/ae46a680-8b4e-486b-bbe8-85dd378c5178)
Here it is observed that ΔVout = Vout_max - Vout_min\
Vout_max = 1.8618\
Vout_min = 0.0465\
ΔVout = 1.815
### VDD vs Frequency @ Vcntrl = 0V
![vdd_vs_frequency](https://github.com/user-attachments/assets/c40ab1d6-fa62-4e07-b023-af8f01732a9a)

### Frequency VS Vcntrl @ VDD = 0V
![freq_vs_vcntrl](https://github.com/user-attachments/assets/87623541-d4bf-4a8d-a4a4-4669775b0761)
### Frequency VS Power @ Vcntrl = 0V
![freq_vs_power](https://github.com/user-attachments/assets/73f6c411-4c56-4a38-89d6-0d581d58416b)
`Average Power = (1/T) ∫[0 to T] V(t) * I(t) dt` 
### FFT of Vout @ VDD = 1.6V and Vcntrl = 0v, Window - Hanning
![fft_1_6v](https://github.com/user-attachments/assets/adabedd7-98ab-4ffe-93dc-629162a837a4)
### FFT of Vout @ VDD = 1.8V and Vcntrl = 0v, Window - Hanning
![fft_1_8v](https://github.com/user-attachments/assets/9afc9778-2ab9-427f-8dcd-78fb82a62486)
### FFT of Vout @ VDD = 2.3V and Vcntrl = 0v, Window - Hanning
![fft_2_3v](https://github.com/user-attachments/assets/4474d0e5-bb4a-4489-b344-f46925520e5d)
### Inverter circuit
![inverter_cir](https://github.com/user-attachments/assets/67039c42-5265-430d-b9e4-00043150ff9a)
### Symmetric inverter VTC curve @VDD = 1.8V and Vin = 1.8V
![inv](https://github.com/user-attachments/assets/65504d93-9b49-4bf5-a0bb-433aaa6e8ada)\
The Vth is 0.9V at the specified length and width of nmos and pmos

