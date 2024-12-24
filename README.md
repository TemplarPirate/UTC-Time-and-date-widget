# UTC Time Display Widget

A lightweight Python script to display the current UTC date and time in a transparent, draggable window on your **Windows desktop**. Designed for simplicity and portability, this tool is perfect for anyone who needs a quick, unobtrusive UTC clock.

## Features
- **Real-time UTC updates**: Refreshes every second to ensure accurate time display.
- **Transparent background**: Seamlessly blends into your desktop environment.
- **Draggable window**: Click and drag to position the display anywhere on your screen.
- **Top-right alignment**: Defaults to the top-right corner of your screen with a 10px margin.
- **Windows compatibility**: Designed and tested on Windows 11, but may work on other versions.

## Prerequisites
- **Python 3.x**: Ensure Python is installed on your system.
- **tkinter**: Pre-installed with most Python distributions. Verify by running:
  ```bash
  python -m tkinter
  ```
  If not installed, use your package manager (e.g., `pip install tk`).

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/TemplarPirate/UTC-Time-and-date-widget.git
   ```
2. Navigate to the directory:
   ```bash
   cd UTC-Time-and-date-widget
   ```
3. Run the script:
   ```bash
   python utc_time_display.py
   ```

## Customization
- **Font size and style**: Adjust the `font` parameter in the `label` setup:
  ```python
  font=("Helvetica", 20)
  ```
- **Transparency**: Modify the `-alpha` value (0.0 to 1.0) for desired opacity.
- **Window positioning**: Change `x_position` and `y_position` for different alignments.

## Compatibility
This script is designed for Windows environments. While it may work on other operating systems (e.g., Linux or macOS), the transparent background and some UI behaviors are specific to Windows and might not function as expected elsewhere.

## How It Works
- The script leverages the `tkinter` library to create a GUI window.
- It uses `datetime` to fetch the current UTC time and updates the display every second.
- Transparency and positioning are managed using `tkinter` attributes.

## Contribution
Feel free to submit issues or fork the repository for enhancements. Contributions are welcome and encouraged!

## License
This project is open-source and available under the [MIT License](LICENSE).
