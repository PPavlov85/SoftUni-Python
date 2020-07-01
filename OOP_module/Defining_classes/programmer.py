class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if language not in self.language:
            return f"{self.name} does not know {language}"
        self.skills += skills_earned
        return f"{self.name} watched {course_name}"

    def change_language(self, new_language, needed_skills):
        if needed_skills <= self.skills and new_language not in self.language:
            previous_language = self.language
            self.language = new_language
            return f"{self.name} switched from {previous_language} to {new_language}"

        elif new_language in self.language and needed_skills <= self.skills:
            return f"{self.name} already knows {self.language}"

        elif self.skills < needed_skills:
            needed_skills -= self.skills
            return f"{self.name} needs {needed_skills} more skills"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
