class Users:
  def __init__(self, first_name, last_name, age, religion, job, skills):
    self.salutation = salutation
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.religion = religion
    self.job = job
    self.skills = skills
  def describe_user(self):
    print(f"{self.salutation}.title() {self.first_name} {self.last_name} is {self.age} years old. He believes in {self.religion}. \
    He works as a {self.job} and his skill is {self.skill}.")
  
