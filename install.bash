#!/bin/bash

echo "Unpacking packages..."
sudo cp wrapper.bash /usr/bin/
sudo cp rephrase.py /usr/bin/
sudo cp key.json /usr/bin/
sudo cp app.py /usr/bin/

sudo chmod 755 /usr/bin/rephrase.py
sudo chmod 755 /usr/bin/wrapper.bash
sudo chmod 666 /usr/bin/key.json
sudo chmod 755 /usr/bin/app.py
echo "installing libraries...."
pip install docx
pip install openai
sudo ln -s /usr/bin/wrapper.bash /usr/bin/gptchat
echo "done"

