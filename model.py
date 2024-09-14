import csv
import random

class Cow:
    def __init__(self, cow_id, breed, age):
        self.cow_id = cow_id #ID วัว
        self.breed = breed #พันธุ์วัว
        self.age = age #อายุ
        self.is_bsod = False #BSOD
        self.has_lemon = False #เพิ่มมะนาว
        self.milk_bottles = 0 #เก็บจำนวนขวดนมที่รีด
        self.color = "normal" # Default color

    def milk(self): #รีดนมจากวัวและคำนวณBSOD
        if self.is_bsod:
            return "ERROR: This cow is BSOD, you must reset it."

        milk_type = None

        # คำนวณอายุส่วนที่เพี้ยนไปในเดือนสำหรับวัวสีขาว
        age_months = self.age * 12
        age_months_floor = int(self.age) * 12
        months_past = age_months - age_months_floor

        # คำนวณอายุส่วนที่เพี้ยนไปในปีสำหรับวัวสีน้ำตาล
        age_years_floor = int(self.age)
        years_past = self.age - age_years_floor

        if self.breed == 'white': # White cow
            if self.has_lemon:
                milk_type = "sour milk"#เป็นนมเปรี้ยวแล้วนะ
            else:
                milk_type = "plain milk" #นมจืดเฉยๆ
                if random.random() <= 0.005 * months_past:  #โอกาสเกิด BSOD ในวัวสีขาว
                    self.is_bsod = True
                    self.color = "blue"  # เปลี่ยนวัวเป็นสีฟ้า?
                    return "BSOD: This white cow has produced soy milk and is now unusable."

        elif self.breed =='brown':  # Brown cow
            milk_type = "chocolate milk"
            if random.random() <= 0.01 * years_past:  # โอกาสเกิด BSOD ในวัวสีน้ำตาล
                self.is_bsod = True
                self.color = "blue"  # เปลี่ยนวัวเป็นสีฟ้า
                return "BSOD: This brown cow has produced almond milk and is now unusable."

        self.milk_bottles += 1 #+เพิ่มทุกการรีดนมมอๆ
        return f"{milk_type} produced! Total bottles: {self.milk_bottles}"

    def reset(self): #resetวัวBSOD
        self.is_bsod = False
        self.milk_bottles = 0
        self.has_lemon = False


class CowModel:
    def __init__(self, csv_file):
        self.cows = {}
        self.load_cows(csv_file)

    def load_cows(self, csv_file):#โหลดข้อมูลวัวจากไฟล์csv
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # ข้าม header
            for row in reader:
                cow_id = row[0]
                breed = row[1]
                age = float(row[2])
                self.cows[cow_id] = Cow(cow_id, breed, age)

    def get_cow(self, cow_id):#ค้นหาวัวจากID
        return self.cows.get(cow_id)
