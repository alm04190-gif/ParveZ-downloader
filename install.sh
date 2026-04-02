#!/bin/bash
echo "Installing Requirements..."
pip install -r requirements.txt

echo "Setting up shortcut..."
echo -e '#!/bin/bash\ncd $HOME/ParveZ-downloader && python main.py' > $PREFIX/bin/download
chmod +x $PREFIX/bin/download

clear
echo "========================================"
echo " ✅ Installation Successful!"
echo " 👉 Now just type: download"
echo "========================================"
