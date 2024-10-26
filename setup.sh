#!/bin/bash

# Setup script for Linpad

# Step 1: Install dependencies
echo "Installing required dependencies..."
sudo apt update
sudo apt install -y python3 python3.7-tk python3-pil python3-pil.imagetk

# Step 2: Create directories
echo "Setting up directories..."
sudo mkdir -p /usr/local/bin/linpad
sudo mkdir -p /usr/share/applications
sudo mkdir -p /usr/share/icons/hicolor/48x48/apps

# Step 3: Copy application files
echo "Copying application files..."
sudo cp linpad.py /usr/local/bin/linpad/linpad.py
sudo cp lin_logo.webp /usr/local/bin/linpad/lin_logo.webp

# Step 4: Create executable script
echo "Creating executable command..."
echo '#!/bin/bash' | sudo tee /usr/bin/linpad
echo 'python3 /usr/local/bin/linpad/linpad.py' | sudo tee -a /usr/bin/linpad
sudo chmod +x /usr/bin/linpad

# Step 5: Create .desktop entry
echo "Creating desktop entry..."
cat <<EOL | sudo tee /usr/share/applications/linpad.desktop
[Desktop Entry]
Version=1.0
Name=Linpad
Exec=linpad
Icon=/usr/local/bin/linpad/lin_logo.webp
Type=Application
Categories=TextEditor;Utility;
Terminal=false
EOL

# Step 6: Copy icon to appropriate directory
echo "Copying application icon..."
sudo cp lin_logo.webp /usr/share/icons/hicolor/48x48/apps/linpad.webp

# Step 7: Update system icon cache (optional)
echo "Updating icon cache..."
sudo gtk-update-icon-cache /usr/share/icons/hicolor

# Step 8: Final message
echo "Linpad has been installed! You can run it via the applications menu or by typing 'linpad' in the terminal."

