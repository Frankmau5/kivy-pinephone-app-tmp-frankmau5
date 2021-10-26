#!/bin/python3
# coding: utf-8

from os.path import abspath


def generate_desktop_file():
    with open("myApp.desktop", "w") as dkp_file:
        # Get the application directory
        exec_path = abspath('main.py')

        parameters = {"Categories": "Utility;Application;",
                      "Comment": "Battery Monitor for Pine64 Devices",
                      "Exec": f"python3 '{exec_path}'",
                      "GenericName": "",
                      "Icon": "battery", 
                      "MimeType": "",
                      "Name": "myApp",
                      "Path": "",
                      "StartupNotify": "true",
                      "Terminal": "false", 
                      "TerminalOptions": "",
                      "Type": "Application",
                      "Version": "1.0",
                      "X-DBUS-ServiceName": "",
                      "X-DBUS-StartupType": "",
                      "X-KDE-SubstituteUID": "false", 
                      "X-KDE-Username": ""}

        dkp_file.write("[Desktop Entry]\n")
        for p in parameters:
            dkp_file.write(f"{p}={parameters[p]}\n")


if __name__ == "__main__":
    generate_desktop_file()

