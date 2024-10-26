# Linpad Documentation
**Linpad** is a minimalist text editor for Ubuntu, featuring syntax highlighting, word count functionality, and a clean user interface. It's designed for developers and casual users alike, providing basic text editing functions with plans for continuous improvement.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
    - [Install via `.deb` Package](#install-via-deb-package)
    - [Manual Installation](#manual-installation)
3. [Usage](#usage)
    - [Opening Linpad](#opening-linpad)
    - [File Operations](#file-operations)
    - [Editing Operations](#editing-operations)
    - [Formatting Options](#formatting-options)
    - [Help Menu](#help-menu)
4. [Contributing](#contributing)
5. [License](#license)
6. [Contact](#contact)

## Features

- Syntax highlighting for Python keywords.
- Word count functionality.
- Replace and find functionality.
- Toggle between dark and light modes.
- Zoom in and out.
- Font customization.
- Open-source and available for community contributions.

## Installation

### Install via `.deb` Package

1. Clone the repository:
    ```bash
    git clone https://github.com/Maijied/linpad
    cd linpad
    ```

2. Build and install the `.deb` package:
    ```bash
    dpkg-deb --build linpad
    sudo dpkg -i linpad.deb
    ```

3. Run Linpad:
    ```bash
    linpad
    ```

4. Alternatively, launch it from your desktop applications menu.

### Manual Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Maijied/linpad
    cd linpad
    ```

2. Install dependencies:
    ```bash
    sudo apt update
    sudo apt install python3 python3-tk python3-pil
    ```

3. Run the application:
    ```bash
    python3 linpad.py
    ```

## Usage

### Opening Linpad

To open Linpad, you can either run the command `linpad` from your terminal or launch it from your desktop applications menu.

### File Operations

- **New File:** Create a new file by selecting `File > New` or pressing `Ctrl+N`.
- **Open File:** Open an existing file by selecting `File > Open` or pressing `Ctrl+O`.
- **Save File:** Save the current file by selecting `File > Save` or pressing `Ctrl+S`.
- **Save As:** Save the current file with a new name by selecting `File > Save As` or pressing `Ctrl+Shift+S`.
- **Print File:** Save the current file as a PostScript file for printing by selecting `File > Print` or pressing `Ctrl+P`.

### Editing Operations

- **Undo/Redo:** Undo or redo the last action by selecting `Edit > Undo` or `Edit > Redo` or pressing `Ctrl+Z` or `Ctrl+Y`.
- **Cut/Copy/Paste:** Cut, copy, or paste text by selecting the respective options under `Edit` or pressing `Ctrl+X`, `Ctrl+C`, or `Ctrl+V`.
- **Delete:** Delete selected text by pressing `Del`.
- **Select All:** Select all text by selecting `Edit > Select All` or pressing `Ctrl+A`.
- **Find/Replace:** Find or replace text by selecting `Edit > Find` or `Edit > Replace` or pressing `Ctrl+F` or `Ctrl+H`.
- **Word Count:** View the word and character count by selecting `Edit > Word Count` or pressing `Ctrl+W`.

### Formatting Options

- **Font:** Change the font family and size by selecting `Format > Font`.
- **Toggle Dark Mode:** Switch between dark and light modes by selecting `Format > Toggle Dark Mode` or pressing `Ctrl+D`.
- **Zoom In/Out:** Increase or decrease the font size by selecting `Format > Zoom In` or `Format > Zoom Out` or pressing `Ctrl+=` or `Ctrl+-`.

### Help Menu

- **About:** View information about Linpad by selecting `Help > About`.
- **Documentation:** View the documentation by selecting `Help > Documentation`.

## Contributing

This project is open-source and welcomes contributions from developers! We encourage developers to suggest new features, report issues, and improve functionality.

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature'`.
4. Push to your branch: `git push origin feature-name`.
5. Open a pull request, and we'll review it.

Check out the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details on contributing.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you encounter any issues or have suggestions for improvement, feel free to open an issue or reach out.

---

*Linpad is designed to be lightweight and functional, with many features planned for the future. Join us in developing and improving Linpad!*

