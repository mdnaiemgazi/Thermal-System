# Fast Fourier Transform (FFT) Analysis of Damped Sinusoidal Signals

## 📊 Visual Overview

![FFT Analysis Plot](fft_analysis_plot.png)

*Figure 1: Time domain signal (top) and its frequency spectrum (bottom) showing the FFT analysis of a damped sine wave*

---

## 📋 Project Overview

This project demonstrates the application of Fast Fourier Transform (FFT) for analyzing damped sinusoidal signals. By generating a test signal combining exponential decay with high-frequency oscillation, the code illustrates how FFT decomposes complex time-domain signals into their constituent frequency components. This technique is fundamental in signal processing, vibration analysis, and mechanical system diagnostics.

## 🎯 Problem Statement

In engineering and scientific applications, signals often contain multiple frequency components embedded in noise or modulated by envelopes. Understanding the frequency content of such signals is critical for:
- Identifying resonant frequencies in mechanical systems
- Analyzing vibration patterns in rotating machinery
- Extracting meaningful information from sensor data
- Detecting anomalies in system behavior

Traditional time-domain analysis alone cannot reveal the frequency composition; hence, frequency domain analysis via FFT is essential.

## ✅ Objectives

- Generate a test signal combining exponential decay and sinusoidal oscillation
- Implement FFT to convert time-domain signal to frequency domain
- Visualize both original signal and its frequency spectrum
- Demonstrate the relationship between time and frequency domain representations
- Provide a foundation for more advanced signal processing applications

## 🔬 Methodology / Approach

### Signal Generation
1. **Time Array Creation**: Generate time points from -10 to 10 seconds
2. **Envelope Function**: Create exponential decay using `exp(-|t|/width)`
3. **Carrier Signal**: Generate 50 Hz sine wave
4. **Test Signal**: Multiply envelope and sine wave to create damped oscillation

### Frequency Analysis
1. **FFT Computation**: Apply Fast Fourier Transform using scipy.fftpack
2. **Frequency Axis**: Generate corresponding frequency values using `fftfreq`
3. **Spectrum Analysis**: Extract imaginary part of FFT for visualization

### Visualization
- Dual subplot display showing:
  - Top: Original time-domain signal
  - Bottom: Frequency spectrum (imaginary component)

## 🛠️ Tools & Technologies Used

| Category | Technology | Purpose |
|----------|------------|---------|
| **Language** | Python 3.x | Core programming |
| **Numerical Computing** | NumPy | Array operations and mathematical functions |
| **Signal Processing** | SciPy FFTpack | Fast Fourier Transform implementation |
| **Visualization** | Matplotlib | Plot generation and customization |

## 📂 Input & Output Explanation

### Input Parameters
The script uses internally defined parameters:
- `t`: Time array from -10 to 10 seconds (200 points)
- `freq = 50 Hz`: Carrier frequency of the sine wave
- `width = 2`: Decay constant for exponential envelope

### Output
- **Time Domain Plot**: Shows the damped sinusoidal signal with exponential envelope
- **Frequency Spectrum Plot**: Displays the imaginary part of FFT, revealing frequency components
- The spectrum shows peak at ±50 Hz corresponding to the input signal frequency

## 📈 Results / Outcomes

### Key Observations
- **Time Domain**: The signal shows a high-frequency oscillation (50 Hz) with amplitude modulated by exponential decay
- **Frequency Domain**: The FFT reveals a clear peak at ±50 Hz, confirming the dominant frequency component
- **Spectral Leakage**: Minor side lobes appear due to finite sampling and signal truncation
- **Symmetry**: The spectrum shows conjugate symmetry around zero frequency (characteristic of real signals)

### Engineering Significance
- Demonstrates FFT capability to identify dominant frequencies in complex signals
- Foundation for applications in:
  - Vibration analysis in mechanical systems
  - Acoustic signal processing
  - Condition monitoring of rotating machinery
  - Modal analysis in structural dynamics

---

## 👨‍🔬 Author Information

**MD Naiem Gazi**  
*Mechanical Engineering Graduate*  

📧 **Email**: [mdnaiemgazi@outlook.com](mailto:mdnaiemgazi@outlook.com)  
🌐 **Portfolio**: [https://mdnaiemgazi.github.io/portfolio/](https://mdnaiemgazi.github.io/portfolio/)  

**Research Interests**: Signal Processing, Mechanical Vibrations, Data-Driven Engineering, System Dynamics

---

## 📁 Repository Structure
