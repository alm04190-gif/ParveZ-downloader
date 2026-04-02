#!/bin/bash
clear
echo "⚙️ Downloading Tool Files..."
cd $HOME
rm -rf ParveZ-downloader
git clone https://github.com/alm04190-gif/ParveZ-downloader.git
cd ParveZ-downloader

echo "⚙️ Installing Requirements..."
pip install -r requirements.txt

echo "⚙️ Setting up shortcut..."
echo -e '#!/bin/bash\ncd $HOME/ParveZ-downloader && python main.py' > $PREFIX/bin/download
chmod +x $PREFIX/bin/report

clear
echo "========================================"
echo " ✅ Installation Successful!"
echo " 👉 Next time just type: download"
echo "========================================"
echo "🚀 Starting tool now..."
sleep 2
python main.py
