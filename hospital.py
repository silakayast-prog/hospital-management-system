# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 20:57:52 2026

@author: LENOVO
"""

class Patient:
    def __init__(self, name, tc):
        self.name = name
        self.tc = tc

    def __str__(self):
        return "{} - ID: {}".format(self.name, self.tc)


class Doctor:
    def __init__(self, name, specialty, daily_limit):
        self.name = name
        self.specialty = specialty
        self.daily_limit = daily_limit
        self.patient_count = 0

    def __str__(self):
        return "{} ({})".format(self.name, self.specialty)


class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def __str__(self):
        return "{} -> {} | {}".format(
            self.patient.name,
            self.doctor.name,
            self.date
        )


patients = []
doctors = []
appointments = []


def add_patient():
    name = input("Patient name: ")
    tc = input("ID (TC): ")

    for patient in patients:
        if patient.tc == tc:
            print("This ID is already registered!")
            return

    new_patient = Patient(name, tc)
    patients.append(new_patient)

    print("Patient registered.")


def add_doctor():
    name = input("Doctor name: ")
    specialty = input("Specialty: ")
    limit = int(input("Daily patient limit: "))

    new_doctor = Doctor(name, specialty, limit)
    doctors.append(new_doctor)

    print("Doctor registered.")


def create_appointment():

    if len(patients) == 0 or len(doctors) == 0:
        print("You must add patients and doctors first.")
        return

    print("\nPatients:")
    for i in range(len(patients)):
        print(i + 1, "-", patients[i])

    patient_no = int(input("Select patient: ")) - 1
    selected_patient = patients[patient_no]

    print("\nDoctors:")
    for i in range(len(doctors)):
        print(i + 1, "-", doctors[i])

    doctor_no = int(input("Select doctor: ")) - 1
    selected_doctor = doctors[doctor_no]

    if selected_doctor.patient_count >= selected_doctor.daily_limit:
        print("Doctor has reached daily limit!")
        return

    date = input("Appointment date: ")

    new_appointment = Appointment(
        selected_patient,
        selected_doctor,
        date
    )

    appointments.append(new_appointment)

    selected_doctor.patient_count += 1

    print("Appointment created.")


def list_appointments():

    if len(appointments) == 0:
        print("No appointments found.")
        return

    print("\n--- Appointments ---")

    for appointment in appointments:
        print(appointment)


def save_to_file():

    file = open("data.txt", "w", encoding="utf-8")

    file.write("PATIENTS\n")
    for patient in patients:
        file.write(str(patient) + "\n")

    file.write("\nDOCTORS\n")
    for doctor in doctors:
        file.write(str(doctor) + "\n")

    file.write("\nAPPOINTMENTS\n")
    for appointment in appointments:
        file.write(str(appointment) + "\n")

    file.close()

    print("Data saved to text file.")


while True:

    print("\n--- HOSPITAL SYSTEM ---")
    print("1- Add Patient")
    print("2- Add Doctor")
    print("3- Create Appointment")
    print("4- List Appointments")
    print("5- Save to File")
    print("0- Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        add_doctor()

    elif choice == "3":
        create_appointment()

    elif choice == "4":
        list_appointments()

    elif choice == "5":
        save_to_file()

    elif choice == "0":
        print("Program closed.")
        break

    else:
        print("Invalid choice!")