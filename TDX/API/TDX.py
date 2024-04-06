import tkinter as tk

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

        # Pending Repair Button
        self.pending_repair_button = tk.Button(sub_frame, text="Pending Repair", width=25, height=1, bg="white", font=('Helvetica', '15'), bd=2, relief='solid', command=self.repair)
        self.pending_repair_button.grid(row=0, column=0, padx=5, pady=5)

        # Pending Disposal Button
        self.pending_disposal_button = tk.Button(sub_frame, text="Pending Disposal", width=25, height=1, bg="white", font=('Helvetica', '15'), bd=2, relief='solid', command=self.disposal)
        self.pending_disposal_button.grid(row=0, column=1, padx=5, pady=5)
         
        # Serial Number Label
        self.serial_number_label = tk.Label(self.master, text="Device SN", bg="white", font=('Helvetica', '18'))
        self.serial_number_label.grid(row=1, column=0, padx=5, pady=5)

        # Serial Number Entry
        self.serial_number_entry = tk.Entry(self.master, width=30, bd=2, relief='solid', font=('Helvetica', '18'), bg="light blue")
        self.serial_number_entry.grid(row=1, column=1, padx=5, pady=5)

        # HDD SN Label
        self.hdd_sn_label = tk.Label(self.master, text="HDD SN", bg="white", font=('Helvetica', '18'))
        self.hdd_sn_label.grid(row=2, column=0, padx=5, pady=5)

        # HDD SN Entry
        self.hdd_sn_entry = tk.Entry(self.master, width=30, bd=2, relief='solid', font=('Helvetica', '18'), bg="light blue")
        self.hdd_sn_entry.grid(row=2, column=1, padx=5, pady=5)

        # Submit Button
        self.submit_button = tk.Button(self.master, text="Submit", width=30, height=1, bg="light yellow", font=('Helvetica', '15'), bd=2, relief='solid', command=self.submit)
        self.submit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


    def repair(self):
        self.substate = "repair"
        self.pending_repair_button.config(bg="light blue")
        self.pending_disposal_button.config(bg="white")

    def disposal(self):
        self.substate = "disposal"
        self.pending_disposal_button.config(bg="light blue")
        self.pending_repair_button.config(bg="white")


    def submit(self):
        if self.substate == None:
            print("Please select a substate")
            self.pending_repair_button.config(bg="pink")
            self.pending_disposal_button.config(bg="pink")
            return
        print(f"Substate: {self.substate}")
        print(f"Serial Number: {self.serial_number_entry.get()}")
        print(f"HDD SN: {self.hdd_sn_entry.get()}")
        self.serial_number_entry.delete(0, tk.END)
        self.hdd_sn_entry.delete(0, tk.END)
        self.pending_repair_button.config(bg="white")
        self.pending_disposal_button.config(bg="white")
        self.substate = None




def main():
    root = tk.Tk()
    app = TDX(root)
    root.mainloop()

if __name__ == "__main__":
    main()