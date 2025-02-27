# Pi Sequence Finder

## Description

Pi Sequence Finder is a web application built with **Flask** and **mpmath** that allows users to search for a sequence of digits within the first 100 digits of **pi**. It displays the position of the sequence or notifies users if the sequence isn't found. This project demonstrates web development and mathematical operations.

## Features

- Search for a numeric sequence within the first 100 digits of pi.
- Displays the position of the sequence or a message if not found.
- Built with **Flask** and **mpmath** for backend functionality.

## Requirements

- Python 3.x
- Flask
- mpmath

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/dgaray01/pi-sequence-finder.git
   ```
2. Install packages:
   ```bash
   pip install flask mpmath
   ```
3. Run code:
   ```
   python pi.py
   ```
4. Access website at port 5000
   
### Disclaimer
To generate more digits of pi, adjust the ``mp.dps`` value in *pi.py*. However, increasing the precision requires more computational resources and memory, which can significantly slow down processing times, especially with high values. The higher the precision, the more time and resources it will consume.
