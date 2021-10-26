#!/bin/bash

python3 generate_desktop_file.py
chmod +x myApp.desktop
cp myApp.desktop ~/.local/share/applications/
