import os
import sys
import ctypes
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

class Sims4LinkHelper:
    def __init__(self, root):
        self.root = root
        self.root.title("Sims 4 Link Helper")
        self.root.geometry("550x250")
        
        # Variables for paths
        self.original_path = tk.StringVar()
        self.additional_mods_path = tk.StringVar()
        
        # GUI Elements
        tk.Label(root, text="Original Sims 4 Mods Folder:").pack(pady=5)
        tk.Entry(root, textvariable=self.original_path, width=60).pack(pady=5)
        tk.Button(root, text="Browse", command=self.browse_original_folder).pack(pady=5)
        
        tk.Label(root, text="Additional Mods Folder on Another Drive:").pack(pady=5)
        tk.Entry(root, textvariable=self.additional_mods_path, width=60).pack(pady=5)
        tk.Button(root, text="Browse", command=self.browse_additional_mods_folder).pack(pady=5)
        
        tk.Button(root, text="Create Additional Mods Link", command=self.create_additional_symlink).pack(pady=10)

    def browse_original_folder(self):
        path = filedialog.askdirectory(title="Select the Original Mods Folder")
        if path:
            self.original_path.set(path)

    def browse_additional_mods_folder(self):
        path = filedialog.askdirectory(title="Select the Additional Mods Folder")
        if path:
            self.additional_mods_path.set(path)

    def create_additional_symlink(self):
        original_mods = self.original_path.get()
        additional_mods = self.additional_mods_path.get()

        # Basic validation
        if not original_mods or not additional_mods:
            messagebox.showerror("Error", "Please select both the original and additional mods folders.")
            return

        # Create the symbolic link
        additional_mods_link = os.path.join(original_mods, "Additional_Mods")
        if os.path.exists(additional_mods_link):
            messagebox.showinfo("Info", "Link already exists. Nothing to do.")
            return

        try:
            cmd = f'mklink /d "{additional_mods_link}" "{additional_mods}"'
            subprocess.run(cmd, shell=True, check=True)
            messagebox.showinfo("Success", "Symbolic link created successfully!")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to create symbolic link. Please make sure you have administrator privileges.")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    script = os.path.abspath(sys.argv[0])
    params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)

if __name__ == "__main__":
    if not is_admin():
        run_as_admin()
        sys.exit(0)

    root = tk.Tk()
    app = Sims4LinkHelper(root)
    root.mainloop()
