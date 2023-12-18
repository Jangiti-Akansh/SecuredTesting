import subprocess
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os
import winreg

class ExamIntegrity:
    def _init_(self, root, password):
        self.root = root
        self.root.title("Exam Integrity Control Panel")

        self.check_password(password)

        style = ttk.Style()
        style.theme_use('clam')

        self.notebook = ttk.Notebook(root)
        self.notebook.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.usb_frame = ttk.Frame(self.notebook)
        self.wifi_frame = ttk.Frame(self.notebook)
        self.ethernet_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.usb_frame, text="USB Control")
        self.notebook.add(self.wifi_frame, text="Wi-Fi Control")
        self.notebook.add(self.ethernet_frame, text="Ethernet Control")

        self.setup_usb_tab()
        self.setup_wifi_tab()
        self.setup_ethernet_tab()

    def check_password(self, correct_password):
        while True:
            password = simpledialog.askstring("Password", "Enter the password:", show='*')
            if password == correct_password:
                break
            elif password is None:
                exit()
            else:
                messagebox.showerror("Incorrect Password", "Incorrect password. Please try again.")

    def setup_usb_tab(self):
        tk.Label(self.usb_frame, text="USB Control", font=('Helvetica', 14, 'bold')).pack(pady=10)
        ttk.Button(self.usb_frame, text="Enable USB", command=self.enable_usb).pack(pady=5)
        ttk.Button(self.usb_frame, text="Disable USB", command=self.disable_usb).pack()

    def setup_wifi_tab(self):
        tk.Label(self.wifi_frame, text="Wi-Fi Control", font=('Helvetica', 14, 'bold')).pack(pady=10)
        ttk.Button(self.wifi_frame, text="Enable Wi-Fi", command=self.enable_wifi).pack(pady=5)
        ttk.Button(self.wifi_frame, text="Disable Wi-Fi", command=self.disable_wifi).pack()

    def setup_ethernet_tab(self):
        tk.Label(self.ethernet_frame, text="Ethernet Control", font=('Helvetica', 14, 'bold')).pack(pady=10)
        ttk.Button(self.ethernet_frame, text="Enable Ethernet", command=self.enable_ethernet).pack(pady=5)
        ttk.Button(self.ethernet_frame, text="Disable Ethernet", command=self.disable_ethernet).pack()


    def enable_usb(self):
        key_path = r"SYSTEM\CurrentControlSet\Services\USBSTOR"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, 3)  
        winreg.CloseKey(key)
        messagebox.showinfo("USB Ports Enabled", "All USB ports are enabled.")
        



    def disable_usb(self):
        key_path = r"SYSTEM\CurrentControlSet\Services\USBSTOR"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, 4)  
        winreg.CloseKey(key)
        messagebox.showinfo("USB Ports Disabled", "All USB ports are disabled.")
        


    def enable_ethernet(self):
        result = subprocess.run('netsh interface set interface "ethernet" enable', check=False, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Ethernet Enabled", "Ethernet is enabled.")
        else:
            messagebox.showerror("Error", f"Failed to enable Ethernet:\n{result.stdout}\n{result.stderr}")


    def disable_ethernet(self):
        result = subprocess.run('netsh interface set interface "ethernet" disable', check=False, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Ethernet Disabled", "Ethernet is disabled.")
        else:
            messagebox.showerror("Error", f"Failed to disable Ethernet:\n{result.stdout}\n{result.stderr}")


    def enable_wifi(self):
        result = subprocess.run('netsh interface set interface "Wi-Fi" enable', check=False, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Wi-Fi Enabled", "Wi-Fi is enabled.")
        else:
            messagebox.showerror("Error", f"Failed to enable Wi-Fi")


    def disable_wifi(self):
        result = subprocess.run('netsh interface set interface "Wi-Fi" disable', check=False, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Wi-Fi Disabled", "Wi-Fi is disabled.")
        else:
            messagebox.showerror("Error", f"Failed to disable Wi-Fi")



if __name__ == "__main__":
    correct_password = "cmrcet" 
    root = tk.Tk()
    app = ExamIntegrity(root, correct_password)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()
