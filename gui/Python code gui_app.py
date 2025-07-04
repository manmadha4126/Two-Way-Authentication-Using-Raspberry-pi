import tkinter as tk
from tkinter import messagebox
import time
import threading

class AuthGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Two-Way Authentication")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.status_label = tk.Label(root, text="Status: Waiting...", font=("Segoe UI", 14))
        self.status_label.pack(pady=30)

        self.otp_label = tk.Label(root, text="Enter OTP:", font=("Segoe UI", 12))
        self.otp_label.pack()

        self.otp_entry = tk.Entry(root, font=("Segoe UI", 12))
        self.otp_entry.pack(pady=5)

        self.verify_button = tk.Button(root, text="Verify OTP", command=self.verify_otp, font=("Segoe UI", 12))
        self.verify_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Segoe UI", 12))
        self.result_label.pack(pady=10)

    def verify_otp(self):
        otp = self.otp_entry.get()
        if otp == "123456":  # Simulated check (replace with Firebase logic)
            self.status_label.config(text="Status: OTP Verified")
            self.result_label.config(text="Access Granted!", fg="green")
        else:
            self.status_label.config(text="Status: Invalid OTP")
            self.result_label.config(text="Access Denied", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = AuthGUI(root)
    root.mainloop()
