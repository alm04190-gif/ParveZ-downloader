#!/bin/bash
clear
echo "⚙️ Installing Requirements..."
pip install -r requirements.txt

echo "⚙️ Setting up shortcut..."
echo -e '#!/bin/bash\ncd $HOME/ParveZ-downloader && python main.py' > $PREFIX/bin/download
chmod +x $PREFIX/bin/download

clear
echo "========================================"
echo " ✅ Installation Successful!"
echo " 👉 Next time just type: download"
echo "========================================"
echo "🚀 Starting tool now..."
sleep 2
python main.py
