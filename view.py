import tkinter as tk
from tkinter import messagebox

class CowView:
    def __init__(self, root, controller):
        self.controller = controller

        # สร้างหน้าจอหลัก
        self.root = root
        self.root.title("Cow Milking System")

        # Show the ID entry 
        self.show_id_entry_view()

    def show_id_entry_view(self):#แสดงหน้าจอรับID
       
        for widget in self.root.winfo_children(): # Clear current widgets
            widget.destroy()

        self.id_label = tk.Label(self.root, text="Enter Cow ID:")
        self.id_label.pack() 

        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack() #ช่องใส่ID

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.pack() #ปุ่มSubmitหาวัว

    def submit(self): #ส่งIDไปController เพื่อหาวัว
        cow_id = self.id_entry.get()
        if not cow_id.isdigit() or len(cow_id) != 8 or cow_id.startswith('0'): #checkข้อมูลที่รับมา ว่าตรงตามเงื่อนไขหรือไม่
            messagebox.showerror("Error", "Invalid Cow ID. Must be 8 digits and not start with 0.")
        else:
            cow = self.controller.handle_cow_id(cow_id)
            if cow:
                self.show_cow_view(cow)
            else:
                messagebox.showerror("Error", "Cow not found") #ขึ้นErrorเมื่อไม่เจอวัว

    def show_cow_view(self, cow): #แสดงข้อมูลวัว
        for widget in self.root.winfo_children():
            widget.destroy()

        cow_info = f"Cow ID: {cow.cow_id}, Breed: {cow.breed}, Age: {cow.age} years"
        self.cow_info_label = tk.Label(self.root, text=cow_info)
        self.cow_info_label.pack()

        self.milk_button = tk.Button(self.root, text="Milk", command=lambda: self.milk_cow(cow))
        self.milk_button.pack()        
       

        if cow.is_bsod: #BSOD
            self.reset_button = tk.Button(self.root, text="Reset Cow", command=lambda: self.reset_cow(cow))
            self.reset_button.pack()
            messagebox.showerror("Error", "This cow is BSOD. Please reset before milking.") #แสดงเมื่อวัวเป็นBSOD
            return

        if cow.breed == 'white': #White
            self.add_lemon_button = tk.Button(self.root, text="Add Lemon", command=lambda: self.add_lemon(cow))
            self.add_lemon_button.pack() #ปุ่มเพิ่มมะนาวสำหรับวัวตัวสีขาว

        
        self.back_button = tk.Button(self.root, text="Back", command=self.show_id_entry_view)
        self.back_button.pack() #กลับหน้าใส่ID

        

      
    def milk_cow(self, cow):#ส่งคำสั่งรีดนมไปที่ Controller และแสดงผล
        result = self.controller.milk_cow(cow)
        messagebox.showinfo("Milk Result", result)

    def add_lemon(self, cow):#เพิ่มมะนาวแล้วแสดงผล
        result = self.controller.add_lemon(cow)
        messagebox.showinfo("Info", result)

    def reset_cow(self, cow):#resetวัวแล้วแสดงผล
        result = self.controller.reset_cow(cow)
        messagebox.showinfo("Info", result)
