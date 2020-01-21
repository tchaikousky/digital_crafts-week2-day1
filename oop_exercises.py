class Person:
    greeting_count = 0
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.unique_person_greeted = []

    def __str__(self):
        return "Person: {} {} {}".format(self.name, self.email, self.phone)
    
    def num_unique_people_greeted(self):
        return print(len(self.unique_person_greeted))

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        if other_person.name not in self.unique_person_greeted:
            self.unique_person_greeted.append(other_person.name)

    def print_contact_info(self):
        print("{}'s email: {}, {}'s phone number: {}".format(self.name, self.email, self.name, self.phone))

    def add_friend(self, friend):
        return self.friends.append(friend)

    def num_friends(self):
        return print(len(self.friends))

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
mike = Person("Mike", "mike@gmail.com", "337-867-0101")

sonny.greet(jordan)
jordan.greet(sonny)
sonny.print_contact_info()
jordan.print_contact_info()
print(jordan)
jordan.greet(sonny)
jordan.add_friend(sonny)
sonny.add_friend(jordan)
jordan.num_friends()
jordan.add_friend(mike)
jordan.num_friends()
jordan.num_unique_people_greeted()
jordan.greet(mike)
jordan.greet(sonny)
jordan.num_unique_people_greeted()



class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print(self.year, self.make, self.model)

    
    


