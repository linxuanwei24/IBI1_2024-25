class patients:
    def __init__(self , patient_name , age , date_of_latest_admission , medical_history):
        self.patient_name = patient_name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history
    def print_details(self):
        print(f"patient name: {self.patient_name}, age: {self.age}, date of latest admission: {self.date_of_latest_admission}, medical history: {self.medical_history}")
# example:        
a = patients("A" , "18" , "9.14" , "aspirin")
a.print_details()