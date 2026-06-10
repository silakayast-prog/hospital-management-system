# hospital-management-system
Hospital management system developed in Python using object-oriented programming. Includes patient registration, doctor scheduling, appointment creation, and file storage.
#  Hospital Management System

A simple Python-based hospital management system that handles patients, doctors, and appointment scheduling. This project is built using Object-Oriented Programming (OOP) and file handling concepts.

---

## Features

- Add new patients with unique ID (TC number)
- Add doctors with specialties and daily appointment limits
- Create appointments between patients and doctors
- Prevent exceeding doctor’s daily patient limit
- List all appointments
- Save all data to a text file (`data.txt`)

---

## How It Works

The system manages three main entities:

- **Patient** → Name and ID (TC)
- **Doctor** → Name, specialty, and daily patient limit
- **Appointment** → Links a patient with a doctor and a date

Users interact with the system through a console menu to manage hospital operations.

---

## How to Run

1. Make sure Python (3.x) is installed
2. Clone this repository:
```bash
git clone https://github.com/your-username/hospital-management-system.git
