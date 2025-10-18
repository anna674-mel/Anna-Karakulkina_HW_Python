class Smartphone:
    def __init__(self, brand, model, ph_number):
        self.brand = brand
        self.model = model
        self.ph_number = ph_number

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_ph_number(self):
        return self.ph_number

    def get_smartphone(self):
        return (
            f"Brand: {self.brand}, Model: {self.model}",
            f"Number: {self.ph_number}."
            )
