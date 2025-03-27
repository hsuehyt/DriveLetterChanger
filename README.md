# Drive Letter Changer

## Overview

Drive Letter Changer is a user-friendly Python application that allows you to easily change the drive letter of portable drives in Windows. With a simple graphical interface, you can quickly select a drive and assign it a new drive letter.

![Application Screenshot](images/Screenshot%202025-03-27%20104943.png)

## Features

- 🖥️ Automatic detection of the current drive
- 📂 Manual drive selection via file browser
- 🔤 Customizable drive letter assignment
- 🛡️ User confirmation before drive letter change
- 🚨 Error handling and informative messages

## Prerequisites

- Python 3.x
- Windows Operating System
- `pywin32` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hsuehyt/DriveLetterChanger.git
   ```

2. Install required dependencies:
   ```bash
   pip install pywin32
   ```

## Usage

1. Run the script:
   ```bash
   python Drive_Letter_Changer.py
   ```

2. Select your portable drive:
   - By default, the script selects the drive where it's located
   - Click "Browse Drive" to choose a different drive

3. Enter a new drive letter (default is "H")

4. Click "Apply" and confirm the change

## Requirements

- Administrative privileges may be required
- Ensure no conflicts with existing drive letters

## Caution

- Changing drive letters can affect system configurations
- Always backup important data before modifying drive letters

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/hsuehyt/DriveLetterChanger/issues).

## License

This project is open-source under the MIT License.

## Author

[hsuehyt](https://github.com/hsuehyt)
