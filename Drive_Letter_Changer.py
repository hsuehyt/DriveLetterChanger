import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

class DriveLetterChanger:
    def __init__(self, root):
        self.root = root
        self.root.title("Drive Letter Changer")
        
        # Default values
        self.default_drive = os.path.splitdrive(os.getcwd())[0]
        self.default_letter = "H"
        
        # Create GUI elements
        self.create_widgets()
    
    def create_widgets(self):
        # Configure grid to center all elements
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        
        # Row 0: Select Portable Drive label
        tk.Label(self.root, text="Select Portable Drive").grid(row=0, column=0, columnspan=3, padx=5, pady=(10,0), sticky="w")
        
        # Row 1: Drive path entry and browse button
        self.drive_path = tk.StringVar(value=self.default_drive)
        drive_entry = tk.Entry(self.root, textvariable=self.drive_path, width=30)
        drive_entry.grid(row=1, column=0, columnspan=2, padx=(5,0), pady=(0,10), sticky="ew")
        
        browse_button = tk.Button(self.root, text="Browse", command=self.browse_drive)
        browse_button.grid(row=1, column=2, padx=(0,5), pady=(0,10), sticky="ew")
        
        # Row 2: New Drive Letter label
        tk.Label(self.root, text="New Drive Letter").grid(row=2, column=0, columnspan=3, padx=5, pady=(10,0), sticky="w")
        
        # Row 3: Drive letter entry and apply button
        self.new_letter = tk.StringVar(value=self.default_letter)
        letter_entry = tk.Entry(self.root, textvariable=self.new_letter, width=5)
        letter_entry.grid(row=3, column=0, padx=(5,0), pady=(0,10), sticky="w")
        
        # Apply button - matching Browse button style with new size
        apply_button = tk.Button(
            self.root, 
            text="Apply", 
            command=self.apply_changes, 
            bg=browse_button.cget('bg'),  # Same color as Browse button
            width=6,
            height=3
        )
        apply_button.grid(row=3, column=1, columnspan=2, padx=5, pady=(0,10), sticky="ew")
        
        # Add empty row for better vertical alignment
        self.root.grid_rowconfigure(4, weight=1)
    
    def browse_drive(self):
        # Let user select a drive (Windows shows drives in file dialog)
        selected_path = filedialog.askdirectory(initialdir=self.default_drive)
        if selected_path:
            drive = os.path.splitdrive(selected_path)[0]
            self.drive_path.set(drive)
    
    def apply_changes(self):
        drive_path = self.drive_path.get().strip()
        new_letter = self.new_letter.get().strip().upper()
        
        # Validate inputs
        if not drive_path or len(drive_path) != 2 or drive_path[1] != ":":
            messagebox.showerror("Error", "Invalid drive path. Please select a drive like 'C:'")
            return
        
        if len(new_letter) != 1 or not new_letter.isalpha():
            messagebox.showerror("Error", "Invalid drive letter. Please enter a single letter (A-Z)")
            return
        
        # Confirm with user
        confirm = messagebox.askyesno(
            "Confirm", 
            f"Are you sure you want to change drive {drive_path} to {new_letter}:?\n"
            "This requires administrator privileges."
        )
        
        if not confirm:
            return
        
        try:
            # Change drive letter using diskpart
            script = f"""
            select volume {drive_path[0]}
            assign letter={new_letter}
            exit
            """
            
            # Run diskpart as admin
            process = subprocess.Popen(
                ["diskpart"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=True
            )
            
            stdout, stderr = process.communicate(script)
            
            if process.returncode == 0:
                messagebox.showinfo("Success", f"Drive letter changed to {new_letter}: successfully!")
            else:
                messagebox.showerror("Error", f"Failed to change drive letter.\nError: {stderr}")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DriveLetterChanger(root)
    root.mainloop()