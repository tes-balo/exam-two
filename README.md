# Medical Appointment System API

The application is to facilitate appointment bookings between Patients and Doctors.

## Features

The API provides CRUD endpoints for patients and doctors which include:

- Register a new patient.
- Create Appointment with Doctor.
- Complete an appointment.
- Cancel an appointment before completion
- Update Patient Info.
- Update Appointment
- Set doctor availability status pre appointment and post appointment

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

It's best to install Python projects in a Virtual Environment. Once you have set up a VE, clone this project

```sh
git clone https://github.com/Ho011/small_sms_api.git
```

```sh
cd small_sms_api
```

```sh
pip install -r requirements.txt
```

### Get Up and running

Once the prerequisites are met, The following steps can be used to get the application up and running. All commands are run from the root directory of the project

```sh
uvicorn src.main:app --reload
```

## Note

This project is in [AltSchool](https://www.altschoolafrica.com/) Exam project done in partial fulfillment for the degree of Backend Engineering (Python).

The project is still in progress, so there may be several bugs.
So if you discover that there are any errors, please fix them, and if you want to improve or add something, your **contribution is welcome.**
