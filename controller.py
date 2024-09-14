from model import CowModel

class CowController:
    def __init__(self, model):
        self.model = model

    def handle_cow_id(self, cow_id): #ค้นหาวัวตาม ID และส่งต่อผลไปที่ View
        cow = self.model.get_cow(cow_id)
        return cow if cow else None

    def milk_cow(self, cow):#สั่งการให้วัวรีดนมและส่งผลลัพธ์ไปยัง View
        return cow.milk()

    def add_lemon(self, cow):#เพิ่มมะนาว
        cow.has_lemon = True
        return "Lemon added!"

    def reset_cow(self, cow):#resetcow
        cow.reset()
        return "Cow reset!"
