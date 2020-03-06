class Person:
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
