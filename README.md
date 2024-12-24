<div align="center">
  <h1>UTC Time Display Widget</h1>
</div>

A super lightweight Python script to display the current UTC date and time in a transparent, draggable window on your **Windows desktop**. Designed for simplicity and portability, this tool is perfect for anyone who needs a quick, unobtrusive UTC clock.

---

## Features
- **Real-time UTC updates**: Accurate to the second.
- **Transparent background**: Blends seamlessly into your desktop.
- **Draggable and resizable**: Fully customizable positioning and size.
- **Lightweight and simple**: No unnecessary clutter—just the time.

<div align="center">

![Python](https://img.shields.io/badge/language-Python-blue.svg)  
![License](https://img.shields.io/badge/license-MIT-green.svg)  
![Version](https://img.shields.io/badge/version-1.0-yellow.svg)

</div>

---

## Screenshot
<div align="center">
  <img src="widget_screenshot.png" alt="UTC Time Display Widget" width="80%">
</div>

---

## Prerequisites
1. **Python 3.x**: Ensure Python is installed on your system. [Download Python](https://www.python.org/downloads/)
2. **tkinter**: Pre-installed with most Python distributions. Verify by running:
   ```bash
   python -m tkinter
   ```
   If not installed, use:
   ```bash
   pip install tk
   ```

---

## Usage
1. **Clone the repository**:
   ```bash
   git clone https://github.com/TemplarPirate/UTC-Time-and-date-widget.git
   ```
2. **Navigate to the directory**:
   ```bash
   cd UTC-Time-and-date-widget
   ```
3. **Run the script**:
   ```bash
   python utc_display_widget.pyw
   ```

---

## Customization
- **Font size and style**: Adjust the `font` parameter in the `label` setup:
  ```python
  font=("Helvetica", 20)
  ```
- **Transparency**: Modify the `-alpha` value (0.0 to 1.0) for desired opacity.
- **Window positioning**: Change `x_position` and `y_position` for different alignments.

---

## Compatibility
This script is designed for Windows environments. While it may work on other operating systems (e.g., Linux or macOS), the transparent background and some UI behaviors are specific to Windows and might not function as expected elsewhere.

---

## Quick Start
1. Clone the repository:
   ```bash
   git clone https://github.com/TemplarPirate/UTC-Time-and-date-widget.git
   ```
2. Run the script directly:
   ```bash
   python utc_display_widget.pyw
   ```

---

## Future Development
- 🌍 Expand compatibility for Linux/macOS.  
- 🎨 Add themes for personalizing the look and feel.  
- 🕐 Include additional time zones for the global nomads.  
- 🚀 Build a one-click installer for effortless setup.

---

## Contribution
Contributions are welcome and strongly encouraged (I'd love upgrade contributions)! If you have suggestions, find issues, or would like to collaborate, feel free to:
- Submit a pull request.
- Open an issue.

---

## License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software as long as proper attribution is given.

---

## ⭐ Please Star
If you like this project, please **⭐ star it** to show your support and help others discover it!

---

## Support Me
If this little thing-a-ma-bob brought joy or utility to your digital life, consider supporting my work!  
Your encouragement helps keep the caffeine flowing and ideas growing.

[☕ Buy me a coffee](https://www.buymeacoffee.com/scofflaw)
```
