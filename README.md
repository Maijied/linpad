# Linpad
Linpad is a simple yet powerful text editor designed for developers and writers. With features like syntax highlighting, word count, and customizable fonts, Linpad aims to enhance your text editing experience. This project is open-source, allowing collaboration to enhance and expand its features.

## Features
- **Syntax Highlighting**: Supports Python syntax highlighting.
- **Word Count**: Displays the number of words and characters in your document.
- **Custom Fonts**: Choose your preferred font and size.
- **Dark Mode**: Toggle between light and dark themes.
- **Undo/Redo**: Keep track of your changes with undo and redo functionality.
- **Find and Replace**: Easily find and replace text in your documents.
- **Zoom In/Out**: Adjust font size for better readability.
- **Print**: Save your documents for printing.
- **Autosave**: Automatically saves your work at regular intervals to prevent data loss.

## Installation
To install Linpad, follow these steps:

1. Download the latest release from the [Releases](https://github.com/Maijied/linpad/releases) page.
2. Follow the installation instructions for your operating system (Windows, macOS, Linux).

### Installation via Setup Script

To install Linpad, you can use the provided `setup.sh` script.

#### How to Use setup.sh

1. **Make the Script Executable:**  
    First, you need to make the `setup.sh` file executable:
    ```bash
    chmod +x setup.sh
    ```

2. **Run the Script:**  
    Then, you can run the setup script with:
    ```bash
    ./setup.sh
    ```

### Building the .deb Package

To build the `.deb` package for Linpad, follow these steps:

1. **Install Required Tools:**  
    Ensure you have `dpkg-deb` installed:
    ```bash
    sudo apt-get install dpkg-deb
    ```

2. **Build the Package:**  
    Navigate to the project directory and run:
    ```bash
    dpkg-deb --build linpad
    ```

3. **Install the Package:**  
    Once the package is built, you can install it using:
    ```bash
    sudo dpkg -i linpad.deb
    ```

## Usage
### Menu Options
- **File Menu**:
    - **New**: Create a new file.
    - **Open**: Open an existing file.
    - **Save**: Save the current file.
    - **Save As**: Save the current file with a new name.
    - **Print**: Prepare the file for printing.
    - **Exit**: Close the application.

- **Edit Menu**:
    - **Undo**: Revert the last action.
    - **Redo**: Redo the last undone action.
    - **Cut/Copy/Paste**: Basic text manipulation commands.
    - **Delete**: Remove the selected text.
    - **Select All**: Select all text in the editor.
    - **Find**: Search for specific text.
    - **Replace**: Replace specified text with new text.
    - **Word Count**: Display the word and character count.

- **Format Menu**:
    - **Font**: Change the font family and size.
    - **Toggle Dark Mode**: Switch between dark and light themes.
    - **Zoom In/Out**: Increase or decrease the font size.

- **Help Menu**:
    - **About**: Display information about Linpad.
    - **Documentation**: Open the online documentation.

### Keyboard Shortcuts
- **New File**: `Ctrl + N`
- **Open File**: `Ctrl + O`
- **Save File**: `Ctrl + S`
- **Save As**: `Ctrl + Shift + S`
- **Print File**: `Ctrl + P`
- **Exit**: `Ctrl + Q`
- **Undo**: `Ctrl + Z`
- **Redo**: `Ctrl + Y`
- **Cut**: `Ctrl + X`
- **Copy**: `Ctrl + C`
- **Paste**: `Ctrl + V`
- **Delete**: `Delete`
- **Select All**: `Ctrl + A`
- **Find**: `Ctrl + F`
- **Replace**: `Ctrl + H`
- **Word Count**: `Ctrl + W`
- **Zoom In**: `Ctrl + =`
- **Zoom Out**: `Ctrl + -`
- **Toggle Dark Mode**: `Ctrl + D`
- **Toggle Underline**: `Ctrl + U`

## Code Structure
### Class: Linpad
The main class `Linpad` is responsible for initializing the text editor and setting up the user interface.

#### Key Methods:
- **`__init__()`**: Initializes the main window and components.
- **`update_status_bar()`**: Updates the status bar with the current line and column.
- **`new_file()`**: Clears the text area for a new document.
- **`open_file()`**: Opens a file dialog to select a file to open.
- **`save_file()`**: Saves the current text area content to a file.
- **`save_as_file()`**: Allows saving the current text area content with a new name.
- **`print_file()`**: Prepares the file for printing.
- **`choose_font()`**: Prompts the user to select a font.
- **`find_text()`**: Searches for specific text within the text area.
- **`replace_text()`**: Replaces specified text with new text.
- **`word_count()`**: Displays the count of words and characters in the text area.
- **`highlight_syntax()`**: Highlights Python keywords in the text area.
- **`toggle_dark_mode()`**: Switches between dark and light modes.
- **`zoom_in()`**: Increases the font size.
- **`zoom_out()`**: Decreases the font size.
- **`show_about()`**: Displays information about the application.
- **`show_documentation()`**: Opens the online documentation.
- **`bind_shortcuts()`**: Binds keyboard shortcuts to various functions.

## About
Linpad is developed by [Miaizied Hasan](mailto:mdshuvo40@gmail.com). This project is open-source, and I welcome any suggestions or contributions to make Linpad even better! Feel free to open issues or submit pull requests.

## License
Linpad is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
Special thanks to the contributors and the open-source community for their support in making Linpad better!

## Folder Structure

```markdown
linpad/
├── CONTRIBUTING.md          # Guidelines for contributing to the project
├── DEBIAN
│   └── control              # Control file for Debian package
├── LICENSE                  # License information for the project
├── lin_logo.webp            # Logo image for Linpad
├── linpad.deb               # Debian package for Linpad
├── linpad.py                # Main Python script for Linpad
├── README.md                # Readme file with project information
├── screenshots
│   └── linpad_screenshot.png # Screenshot of Linpad in action
├── setup.sh                 # Setup script for installing Linpad
├── test
│   └── test_linpad.py       # Test script for Linpad
└── usr
       ├── bin
       │   └── linpad           # Executable binary for Linpad
       └── share
             ├── applications
             │   └── linpad.desktop # Desktop entry for Linpad
             └── icons
                    └── hicolor
                          ├── 128x128
                          │   └── apps
                          │       └── linpad.png # 128x128 icon for Linpad
                          ├── 16x16
                          │   └── apps
                          │       └── linpad.png # 16x16 icon for Linpad
                          ├── 256x256
                          │   └── apps
                          │       └── linpad.png # 256x256 icon for Linpad
                          ├── 32x32
                          │   └── apps
                          │       └── linpad.png # 32x32 icon for Linpad
                          ├── 48x48
                          │   └── apps
                          │       └── linpad.png # 48x48 icon for Linpad
                          └── 64x64
                                └── apps
                                       └── linpad.png # 64x64 icon for Linpad
```

## Download

You can download the `.deb` package for **Linpad** directly from this repository.

[Download Linpad.deb package](https://github.com/Maijied/linpad/releases/download/open-source-ubuntu-text-editor/linpad_v1.0.1-beta.deb)

Alternatively, you can download the latest build artifacts from our GitHub Actions workflow.

## Dependencies

The application requires the following packages to be installed:

- `python3`
- `python3.7-tk`
- `python3-pil`
- `python3-pil.imagetk`

### Installation

You can install these dependencies using the following command:

```bash
sudo apt update
sudo apt install python3 python3.7-tk python3-pil
```

## Contributing

This project is open-source and welcomes contributions from developers! We encourage developers to suggest new features, report issues, and improve functionality. Let me know if you have some good ideas to make Linpad even better.

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature'`.
4. Push to your branch: `git push origin feature-name`.
5. Open a pull request, and we'll review it.

Check out the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details on contributing.

## Future Roadmap

- Add more syntax highlighting languages.
- Improve the user interface.
- Add plugin support for developers to expand Linpad's functionality.

---

## Contact

If you encounter any issues or have suggestions for improvement, feel free to open an issue or reach out.

---

*Linpad is designed to be lightweight and functional, with many features planned for the future. Join us in developing and improving Linpad!*
