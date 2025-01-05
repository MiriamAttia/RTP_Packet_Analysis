# Problem 1: Data Engineering and Presentation

## Project Overview
This project involves analysing and visualising network traffic data from real-time audio-video applications. Using Python, the program processes datasets (`targetA.csv` and `targetB.csv`) containing Real-Time Protocol (RTP) packet information. The program generates various statistical and graphical outputs to analyse packet delays, sequence numbers, and distribution of packet lengths.

---

## Features
1. **Data Parsing**:
   - Reads and processes data from `targetA.csv` and `targetB.csv` using the Pandas library.

2. **Graphical Visualisation**:
   - Sequence numbers over time.
   - Probability of packet lengths.
   - Distribution of packet lengths (CDF and PDF).
   - Packet delays.

3. **Statistical Analysis**:
   - Calculates the mean, mode, and standard deviation of packet lengths.

4. **Delay Analysis**:
   - Computes delays between packet departure and arrival times for each sequence number.
   - Plots delays to evaluate network performance.

---

## How to Run

### Prerequisites
- Python 3.x installed.
- Required libraries: `pandas`, `matplotlib`, and `numpy`.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/MiriamAttia/RTP_Packet_Analysis.git
