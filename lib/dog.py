class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age
    self.checkups = [] # Checkups data including -> vets name, checkup_date, notes
    self.vets = [] # Vets names

  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self,value):
    if type(value) is int and 0 <= value:
      self._age = value
    else:
      raise ValueError("Not valid age")
    
  def add_checkup(self, vet, date, notes):
    if vet not in self.vets:
      self.vets.append(vet)
      
    new_checkup = {
        'vet': vet,
        'date': date,
        'notes': notes
      }
    self.checkups.append(new_checkup)
    
  def find_checkup(self, date):
    for checkup in self.checkups:
      if date == checkup['date']:
        print(f"Checkup on {date} by {checkup['vet']}: {checkup['notes']}")
        return 
    
    else:
      print(f"No checkup found on {date}!")
      
fido = Dog(
  name= "Fido",
  age= 3,\
  breed= "Golden Retriever"
)
fido.add_checkup("Doolittle", "02/20/22", "Good Health")
print(fido.vets)
print(fido.checkups)
fido.find_checkup("02/20/22")
fido.find_checkup("03/22/24")