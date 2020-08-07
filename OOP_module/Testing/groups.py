class Person:
    id_counter = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.id = Person.id_counter
        Person.id_counter += 1

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self):
        return f"Person {self.id}: {self.name} {self.surname}"

    def __str__(self):
        return self.name + ' ' + self.surname


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([str(p) for p in self.people])}"

    def __getitem__(self, item):
        return self.people[item].__repr__()

    def __add__(self, other):
        return Group(self.name, self.people + other.people)


import unittest


class TestPerson(unittest.TestCase):
    def setUp(self):
        Person.id_counter = 0
        self.person = Person("Pesho", "Peshev")

    def test_repr(self):
        result = repr(self.person)
        self.assertEqual(result, "Person 0: Pesho Peshev")

    def test_str(self):
        result = str(self.person)
        self.assertEqual(result, "Pesho Peshev")

    def test_add(self):
        self.person2 = Person("Gosho", "Goshev")
        person3 = self.person + self.person2
        self.assertEqual(person3.name, "Pesho")
        self.assertEqual(person3.surname, "Goshev")

    def test_auto_incremented_id(self):
        person_id = Person.id_counter
        person2_id = Person("Vtori", "Vtori")
        self.assertEqual(person_id, 1)
        self.assertEqual(person2_id.id, 1)
        self.assertEqual(Person.id_counter, 2)


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.person = Person("Pesho", "Peshev")
        self.person2 = Person("Gosho", "Goshev")
        self.group = Group("test", [self.person, self.person2])

    def test_len(self):
        self.assertEqual(len(self.group), 2)

    def test_add(self):
        person3 = Person("Ivan", "Ivanov")
        group2 = Group("test2", [person3])
        group3 = group2 + self.group
        self.assertEqual(len(group3), 3)

    def test_get_item(self):
        result = self.group[1]
        self.assertIn("Gosho", result)
        self.assertEqual(result, "Person 1: Gosho Goshev")

    def test_repr(self):
        result = repr(self.group)
        self.assertEqual(result, "Group test with members Pesho Peshev, Gosho Goshev")


if __name__ == "__main__":
    unittest.main()
