class Guest:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Guest(name={self.name}, email={self.email})"

    # Additional methods for interacting with guest data can be added here.