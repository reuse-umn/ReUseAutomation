import tkinter as tk
from base64 import b64encode
from dotenv import load_dotenv
from datetime import datetime
import requests
import os
import sys

class TDX:
    def __init__(self, master):
        self.master = master
        self.master.title("TDX")
        self.master.geometry("600x300")
        self.master.resizable(False, False)
        self.master.config(bg="white")
        self.substate = None

        # Structure:
        # (Pending Repair - Button) (Pending Disposal - Button) 
        # (Label: Serial Number) (Serial Number - Entry) 
        # (Label: HDD SN) (HDD Serial Number - Entry) 
        # (Button: Submit)

        # Create a sub frame
        sub_frame = tk.Frame(self.master, bg="white")
        sub_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Hotkeys
        self.master.bind('<F1>', self.on_press)
        self.master.bind('<F2>', self.on_press)
        self.master.bind('<Escape>', self.on_press)

        # Pending Repair Button
        self.pending_repair_button = tk.Button(sub_frame, text="Pending Repair", width=25, height=1, bg="white", font=('Helvetica', '15'), bd=2, relief='solid', command=self.repair)
        self.pending_repair_button.grid(row=0, column=0, padx=5, pady=5)

        # Pending Disposal Button
        self.pending_disposal_button = tk.Button(sub_frame, text="Pending Disposal", width=25, height=1, bg="white", font=('Helvetica', '15'), bd=2, relief='solid', command=self.disposal)
        self.pending_disposal_button.grid(row=0, column=1, padx=5, pady=5)

        # x500 Label
        self.x500_label = tk.Label(self.master, text="Operator (x500)", bg="white", font=('Helvetica', '18'))
        self.x500_label.grid(row=1, column=0, padx=5, pady=5)

        # x500 Entry
        self.x500_entry = tk.Entry(self.master, width=30, bd=2, relief='solid', font=('Helvetica', '18'), bg="light blue")
        self.x500_entry.grid(row=1, column=1, padx=5, pady=5)
        self.x500_entry.focus()
         
        # Serial Number Label
        self.serial_number_label = tk.Label(self.master, text="Device SN", bg="white", font=('Helvetica', '18'))
        self.serial_number_label.grid(row=2, column=0, padx=5, pady=5)
        
        # Serial Number Entry
        self.serial_number_entry = tk.Entry(self.master, width=30, bd=2, relief='solid', font=('Helvetica', '18'), bg="light blue")
        self.serial_number_entry.grid(row=2, column=1, padx=5, pady=5)

        # HDD SN Label
        self.hdd_sn_label = tk.Label(self.master, text="HDD SN", bg="white", font=('Helvetica', '18'))
        self.hdd_sn_label.grid(row=3, column=0, padx=5, pady=5)

        # HDD SN Entry
        self.hdd_sn_entry = tk.Entry(self.master, width=30, bd=2, relief='solid', font=('Helvetica', '18'), bg="light blue")
        self.hdd_sn_entry.grid(row=3, column=1, padx=5, pady=5)

        # Submit Button
        self.submit_button = tk.Button(self.master, text="Submit", width=30, height=1, bg="light yellow", font=('Helvetica', '15'), bd=2, relief='solid', command=self.submit)
        self.submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def on_press(self, event):
        match event.keysym:
            case 'F1':
                self.repair()
            case 'F2':
                self.disposal()
            case 'Escape':
                self.submit()
        
    def repair(self):
        self.substate = "repair"
        self.pending_repair_button.config(bg="light blue")
        self.pending_disposal_button.config(bg="white")

    def disposal(self):
        self.substate = "disposal"
        self.pending_disposal_button.config(bg="light blue")
        self.pending_repair_button.config(bg="white")


    def submit(self):
        invalid = False
        if self.substate == None:
            print("Please select a substate")
            self.pending_repair_button.config(bg="pink")
            self.pending_disposal_button.config(bg="pink")
            invalid = True
        if not self.serial_number_entry.get().strip():
            print("Please enter the serial number")
            self.serial_number_entry.config(bg="pink")
            invalid = True
        if not self.x500_entry.get().strip():
            print("Please enter your x500")
            self.x500_entry.config(bg="pink")
            invalid = True
        if invalid:
            return
        HDD_sn = self.hdd_sn_entry.get().strip().upper()
        HDD_sn = HDD_sn if len(HDD_sn) > 0 else 'N/A'
        PC_sn = self.serial_number_entry.get().strip().upper()
        print(f"\nSubstate: {self.substate}")
        print(f"Serial Number: {PC_sn}")
        print(f"HDD SN: {HDD_sn}")
        self.serial_number_entry.delete(0, tk.END)
        self.hdd_sn_entry.delete(0, tk.END)
        self.pending_repair_button.config(bg="white")
        self.pending_disposal_button.config(bg="white")
        self.serial_number_entry.config(bg="light blue")
        self.serial_number_entry.focus()
        self.x500_entry.config(bg="light blue")
        self.update_asset(PC_sn, HDD_sn)
        self.substate = None

    def update_asset(self, PC_sn, HDD_sn):
        substate_id = "5210" if self.substate == 'repair' else "5207"
        post_json = {
            "HDDSerialNumber": HDD_sn,
            "SerialNumber": PC_sn,
            "Substate": substate_id,
            "Comments": f"---\n {datetime.now()}\nReceived by ReUse.\nOperator: {self.x500_entry.get().strip()}\n---"
        }
        post_headers = {
            "x-api-key" : os.getenv('API_KEY'),
            "Authorization" : self.basic_auth(os.getenv('API_USER'), os.getenv('API_PASS'))
        }
        response = requests.post(url=os.getenv('UPDATE_ENDPOINT'), json=post_json, headers=post_headers)
        if not response.text:
            print('Sent')
        else:
            print(f'Error: {response.text}')
    

    def basic_auth(self, username, password):
        token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
        return f'Basic {token}'



def main():
    exe_path = os.path.dirname(sys.executable)
    env_path = os.path.join(exe_path, ".env")
    load_dotenv(env_path)
    # load_dotenv()

    if os.getenv('UPDATE_ENDPOINT') is None:
        print(f"Environment variables not configured: Please place .env file in {exe_path}.")
        return

    root = tk.Tk()
    app = TDX(root)
    root.mainloop()

if __name__ == "__main__":
    main()