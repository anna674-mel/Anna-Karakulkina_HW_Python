class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sey_first_name(self):
        return self.first_name

    def sey_last_name(self):
        return self.last_name

    def sey_full_name(self):
        return f"First_name: {self.first_name}, Last_name: {self.last_name}"
