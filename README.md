Sims4LinkHelper

Sims4LinkHelper is a Python GUI tool that allows you to expand your Sims 4 Mods folder storage by creating an additional symbolic link to another location (e.g., another hard drive). This helps players who are running low on space in the default Mods folder but want to add more custom content.
Features

    Easy-to-use graphical interface for selecting folders
    Allows you to create an additional Mods folder link on another drive
    Keeps the original Mods folder in place, while expanding storage capacity
    Automatically requests admin privileges on Windows to create symbolic links

Requirements

    Python 3.x (Download here)
    tkinter (usually included with Python on Windows)
    Administrator privileges are required to create symbolic links.

Installation

    Clone the repository:

    bash

git clone https://github.com/swaric/sims4symlinkhelper.git

Navigate to the folder:

bash

cd Sims4LinkHelper

Run the script:

bash

    python sims4symlinkhelper.py

Usage

    Original Sims 4 Mods Folder: Browse to select the existing Mods folder in your Sims 4 directory (e.g., Documents\Electronic Arts\The Sims 4\Mods).
    Additional Mods Folder on Another Drive: Choose a folder on another drive where you want to store extra mods.
    Click Create Additional Mods Link. This will add a symbolic link from the additional folder into your original Mods directory, allowing The Sims 4 to load mods from both locations.

Screenshots

Sims4LinkHelper GUI
Troubleshooting

    Symbolic link creation failed: Ensure you’re running the script with administrator privileges. (Script will request admin privileges on start)
    Target folder not recognized: Double-check that the paths are correct and that the Sims 4 game has read permissions on the additional drive.

Contributing

Feel free to open issues or submit pull requests to improve the functionality of Sims4LinkHelper. Contributions are welcome!
License

This project is licensed under the MIT License. See the LICENSE file for details.
