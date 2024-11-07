# A 4-6 GHz Low-Power Voltage Controlled Oscillator with Wide Voltage Range Operation 

This project simulates the designed Voltage controlled oscillator circuit to determine its performance characterisitics for pre-layout 

## A Glance at the VCO IP

Voltage Controlled Oscillator is one of the crucial component in communication systems. This paper discusses the design of a low-power VCO tailored for GHz frequency applications. The VCO is developed using CMOS technology and the Sky water 130nm PDK. This VCO operates within a wide voltage range and delivers an output frequency of 4-6 GHz and the designed VCO is expected to consume less than 1mW power at 1.8 V. This low power consumption makes the VCO suitable for applications such as IoT and battery-operated wireless systems, where energy efficiency is essential.

## Block Diagram of the VCO IP
 <p align="center">
  <img width="800" height="600" src="/Images/blackbox.png">
</p>

## Circuit Diagram of the VCO IP
 <p align="center">
  <img width="1000" height="600" src="/Images/circuit.png">
</p>

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

 <p align="center">
  <img width="800" height="600" src="/Images/trans_final.png">
</p>

Here it is observed that ΔVout = Vout_max - Vout_min\
Vout_max = 1.8618\
Vout_min = 0.0465\
ΔVout = 1.815

### VDD vs Frequency @ Vcntrl = 0V
 <p align="center">
  <img width="1000" height="600" src="/Images/vdd_vs_frequency.png">
</p>

### Frequency VS Vcntrl @ VDD = 0V
 <p align="center">
  <img width="800" height="600" src="/Images/freq_vs_vcntrl.png">
</p>

### Frequency VS Power @ Vcntrl = 0V
 <p align="center">
  <img width="800" height="600" src="/Images/freq_vs_power.png">
</p>

`Average Power = (1/T) ∫[0 to T] V(t) * I(t) dt` 
### FFT of Vout @ VDD = 1.6V and Vcntrl = 0v, Window - Hanning
 <p align="center">
  <img width="800" height="600" src="/Images/fft_1_6v.png">
</p>

### FFT of Vout @ VDD = 1.8V and Vcntrl = 0v, Window - Hanning
 <p align="center">
  <img width="800" height="600" src="/Images/fft_1_8v.png">
</p>

### FFT of Vout @ VDD = 2.3V and Vcntrl = 0v, Window - Hanning
 <p align="center">
  <img width="800" height="600" src="/Images/fft_2_3v.png">
</p>

### Inverter circuit
 <p align="center">
  <img width="1000" height="600" src="/Images/inverter_cir.png">
</p>

### Symmetric inverter VTC curve @VDD = 1.8V and Vin = 1.8V
 <p align="center">
  <img width="800" height="600" src="/Images/inv.png">
</p>

The Vth is 0.9V at the specified length and width of nmos and pmos
## Installation
Tools used and step to reproduce all waveforms

The circuit is designed with Xschem and simulated using Ngspice.

For Video Installation of Xschem, Skywater 130nm pdk and Ngspice and other open source tools, refer to this video [Video_link](https://www.youtube.com/watch?v=jEGq7JVHGvQ)
### For Ubuntu:
#### Xschem:
Xschem is an open-source schematic capture tool used for designing electronic circuits. It is popular in the VLSI design community for its intuitive interface and extensive compatibility with circuit simulation tools like ngspice. Xschem supports hierarchical designs, allowing designers to create complex circuits from simpler building blocks. It’s particularly useful for designing and simulating analog, digital, and mixed-signal circuits.

Open your terminal and type the following to install Xschem
```bash
  git clone https://github.com/StefanSchippers/xschem.git xschem
  cd xschem/
  ./configure
  make
  sudo make install
```
To open Xschem:
```bash
  xschem
```
#### Ngspice:

Ngspice is an open-source, mixed-level/mixed-signal electronic circuit simulator based on SPICE (Simulation Program with Integrated Circuit Emphasis). It’s widely used for simulating analog, digital, and RF circuits, supporting a range of analyses like DC, AC, transient, and noise analysis.

Open your terminal and type the following to install Ngspice
```bash
  git clone https://git.code.sf.net/p/ngspice/ngspice ngspice_git
  ls
  cd ngspice_git/
  mkdir release
  ./autogen.sh
  cd release
  cd ../
  sudo apt-get install adms -y
  cd release/
  ../configure --with-x --enable-xspice --disable-debug --enable-cider --with-readline=yes --enable-openmp --enable-osdi --enable-adms
  make
  sudo make install
  sudo apt-get install netgen-lvs -y
```
    
