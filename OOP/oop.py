class User:
    active_users = 0
    allowed = ['brazil', 'russia', 'colombia'] #attributes exists on * e v e r y * object, as the same
    def __init__(self, first, last, age, nation):
        if nation not in User.allowed:
            raise ValueError("You cant be from that country")
        else:
            self.first = first
            self.last = last
            self.age = age

    def get_full_name(self):
        return self.first + ' ' + self.last

    def get_initials(self):
        return "{}.{}.".format(self.first[0], self.last[0])


user = User("John", "Nilast", 42, "brazil")
user2 = User("Carl", "Smirnov", 24, "russia")
User.allowed.append("Portugal")
user3 = User("Carl", "Smirnov", 24, "Portugal")

