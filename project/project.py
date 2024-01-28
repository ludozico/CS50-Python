""" Final project by Luiz Fillipe Pinto da Silva for CS50 Python 2024"""

import csv
import datetime
import os
import tkinter as tk
import tkinter.font as tkFont
import re
import random
import io
import webbrowser
import time
from tkinter.scrolledtext import ScrolledText
from pyfiglet import Figlet
from emoji import emojize
from cryptography.fernet import Fernet
from fpdf import FPDF


class PROTEKTOR3000:
    """ class to encrypt and decrypt data using Fernet (learned from https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/) """
    def __init__(self, key_path):
        self.key = self.load_key(key_path)
        self.fernet = Fernet(self.key)

    def load_key(self,key_path):
        """function to load the key from the file or create it if it doesn't exist"""
        # if key don't exist, create it
        if not os.path.exists(key_path):
            key = Fernet.generate_key()
            with open(key_path, 'wb') as key_file:
                key_file.write(key)
            return key
        #load key
        with open(key_path, 'rb') as key_file:
            return key_file.read()
    #function to encrypt
    def encrypt(self, data):
        """function to encrypt data"""
        return self.fernet.encrypt(data.encode())
    #function to decrypt
    def decrypt(self, data):
        """function to decrypt data"""
        return self.fernet.decrypt(data).decode()
class Patient:
    """ class to store the patients consult information and potentially 
    implement more cool features in the future"""
    def __init__(self, name, date_of_birth, appointment_date, height, weight, current_complain,
        comorbidities, meds, surgical_procedures, allergies, family_hx,
        miscellaneous, temp=None, hr=None, rr=None, sbp=None, dbp=None, subjective=None,
        objective=None, assessment=None, plan=None, id=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.appointment_date = appointment_date
        self.height = height
        self.weight = weight
        self.current_complain = current_complain
        self.comorbidities = comorbidities
        self.meds = meds
        self.surgical_procedures = surgical_procedures
        self.allergies = allergies
        self.family_hx = family_hx
        self.miscellaneous = miscellaneous
        self.temp = temp
        self.hr = hr
        self.rr = rr
        self.sbp = sbp
        self.dbp = dbp
        self.subjective = subjective
        self.objective = objective
        self.assessment = assessment
        self.plan = plan
        self.id = id

    def age(self):
        """ Returns the age of the patient in years."""
        today = datetime.date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) <
                                                (self.date_of_birth.month, self.date_of_birth.day))

    def __str__(self):
        str0 = f"{self.appointment_date} appointment summary:\n"
        str1 = f"Patient: {self.name}, Age: {self.age()}, Complain: {self.current_complain}\n"
        str2 = f"Comorbidities: {self.comorbidities}, Current medications: {self.meds} \n"
        str3 = f"Allergies: {self.allergies}, BP: {self.sbp}/{self.dbp} mmHg,"
        str4 = " HR: {self.hr} bpm, RR: {self.rr} bpm \n\n"
        str5 = f"FILE SUCESSFULLY SAVED! ID: {self.id}"
        final = str0 + str1 + str2 + str3 + str4 + str5
        return final

# Initialize my cryptographic robot PROTEKTOR3000 to protect my patients data
PROTEKTOR3000_ACTIVATED = PROTEKTOR3000('fernet_key.key')

def main():
    """# main function to run the GUI"""
    # create the window
    root.mainloop()

def save_consult():
    """# function to save the consult data in the CSV well protected by PROTEKTOR3000"""
    # Create the patient object
    patient = Patient(
    name=entries['name'].get(),
    date_of_birth=datetime.datetime.strptime(entries["date_of_birth_"].get(), '%d-%m-%Y').date(),
    appointment_date=datetime.datetime.strptime(entries["appointment_date"].get(),
                                                '%d-%m-%Y').date(),
    height=entries["height_"].get(),
    weight=entries["weight_"].get(),
    current_complain=entries["current_complain"].get(),
    comorbidities=entries['comorbidities'].get(),
    meds=entries['medications'].get(),
    surgical_procedures=entries['surgical_procedures'].get(),
    allergies=entries['allergies'].get(),
    family_hx=entries['family_history'].get(),
    miscellaneous=entries['miscellaneous_notes'].get(),
    temp=entries["temperature_"].get(),
    hr=entries["heart_rate_"].get(),
    rr=entries["respiratory_rate_"].get(),
    sbp=entries['blood_pressure'].get().split('/')[0],
    dbp=entries['blood_pressure'].get().split('/')[1],
    subjective=entries['subjective'].get("1.0", tk.END).strip(),
    objective=entries['objective'].get("1.0", tk.END).strip(),
    assessment=entries['assessment'].get("1.0", tk.END).strip(),
    plan=entries['plan'].get("1.0", tk.END).strip(),
    id=random.randint(0, 1000000))

    # display the summary
    summary.delete(1.0, tk.END)
    summary.insert(1.0, str(patient))

    # create the consult data dictionary
    patient_data = { 'Name': patient.name,
    'Date of Birth': patient.date_of_birth.strftime('%d-%m-%Y'),
    'Appointment Date': patient.appointment_date.strftime('%d-%m-%Y'),
    'ID':patient.id, 'Height': patient.height, 'Weight': patient.weight,
    'Current Complain': patient.current_complain, 'Comorbidities': patient.comorbidities,
    'Medications': patient.meds, 'Surgical Procedures': patient.surgical_procedures,
    'Allergies': patient.allergies, 'Family History': patient.family_hx,
    'Miscellaneous': patient.miscellaneous, 'Temperature' : patient.temp, 'Heart Rate' : patient.hr,
    'Respiratory Rate' : patient.rr, 'Systolic Blood Pressure' : patient.sbp,
    'Diastolic Blood Pressure' : patient.dbp, 'Subjective' : patient.subjective,
    'Objective' : patient.objective, 'Assessment' : patient.assessment, 'Plan' : patient.plan}

    # check if consult already exists
    is_duplicate = False
    decrypted_data = ''
    if os.path.isfile('patients.csv'):
        with open('patients.csv', 'rb') as csvfile:
            encrypted_data = csvfile.read()
            decrypted_data = PROTEKTOR3000_ACTIVATED.decrypt(encrypted_data)
            reader = csv.DictReader(io.StringIO(decrypted_data))
            for row in reader:
                if all(value == row[key] for key, value in patient_data.items() if key != 'ID'):
                    is_duplicate = True
                    break
    if is_duplicate:
        summary.delete(1.0, tk.END)
        summary.insert(tk.END, 'This consult already exists\n')
    # if the consult doesnt exist, save it
    else:
        patient_data_csv = io.StringIO()
        writer = csv.DictWriter(patient_data_csv, fieldnames=patient_data.keys())
        # if there is no file, write the header
        if not os.path.isfile('patients.csv'):
            writer.writeheader()
        # finally, save the consult data ENCRPYTED! OH YEAH BOY :D getting good
        writer.writerow(patient_data)
        decrypted_data += patient_data_csv.getvalue()
        encrypted_data = PROTEKTOR3000_ACTIVATED.encrypt(decrypted_data)
        with open('patients.csv', 'wb') as csvfile:
            csvfile.write(encrypted_data)

    # update the listbox
    trigger_search(search_entry, entry_listbox_6)

def clear_fields():
    """# function to clear all fields in the GUI"""
    keys_to_clear = ["name", "current_complain", "comorbidities", "medications", "date_of_birth_",
    "appointment_date", "height_", "weight_", "allergies", "family_history", "miscellaneous_notes", 
    "surgical_procedures", "temperature_", "heart_rate_", "respiratory_rate_", "blood_pressure"]
    for key in keys_to_clear:
        if key in entries:
            entries[key].delete(0, tk.END)
    summary.delete('1.0', 'end')
    text_9_2.delete('1.0', 'end')
    text_9_6.delete('1.0', 'end')
    text_11_2.delete('1.0', 'end')
    text_11_6.delete('1.0', 'end')
    entry_listbox_6.delete(0, tk.END)
    search_entry.delete(0, tk.END)

def search(pattern, text_box):
    """# search function"""
    file_exists = os.path.isfile('patients.csv')
    if file_exists:
        with open('patients.csv', 'rb') as csvfile:
            encrypted_data = csvfile.read()
            decrypted_data = PROTEKTOR3000_ACTIVATED.decrypt(encrypted_data)
            reader = csv.DictReader(io.StringIO(decrypted_data))
            history = []
            for row in reader:
                row = {key: value.strip() for key, value in row.items()}
                match_found = False
                for field in row.values():
                    if re.search(pattern, str(field), re.IGNORECASE) and not match_found:
                        fll1 = f"Name: {row['Name']}, Appointment date: {row['Appointment Date']},"
                        fll2 = f" ID: {row['ID']}"
                        fixinglongline = fll1 + fll2
                        history.append(fixinglongline)
                        text_box.insert(tk.END, fixinglongline + '\n')
                        match_found = True
                        break
            print(history)
            return history


def trigger_search(searchentry, text_box):
    """function to trigger the search from the GUI when the button is clicked"""
    pattern = searchentry.get()
    text_box.delete(0, tk.END)
    search(pattern, text_box)

def on_select(_):
    """# function to select a consult from the listbox and display the data"""
    # get the selected consult ID
    consult = entry_listbox_6.get(entry_listbox_6.curselection())
    consult_id = consult.split('ID: ')[1]
    display_consult(consult_id)
    return consult_id

def display_consult(consult_id):
    """# function to display the consult data in the GUI"""    
    #find the matching patient record
    with open('patients.csv', 'rb') as csvfile:
        encrypted_data = csvfile.read()
        decrypted_data = PROTEKTOR3000_ACTIVATED.decrypt(encrypted_data)
        reader = csv.DictReader(io.StringIO(decrypted_data))
        for row in reader:
            if consult_id.strip() == row['ID'].strip():
                entry_2_2.delete(0, tk.END)
                entry_2_2.insert(tk.END, row['Name'])
                entry_2_4.delete(0, tk.END)
                entry_2_4.insert(tk.END, row['Date of Birth'])
                entry_3_2.delete(0, tk.END)
                entry_3_2.insert(tk.END, row['Current Complain'])
                entry_3_4.delete(0, tk.END)
                entry_3_4.insert(tk.END, row['Appointment Date'])
                entry_4_4.delete(0, tk.END)
                entry_4_4.insert(tk.END, row['Height'])
                entry_5_4.delete(0, tk.END)
                entry_5_4.insert(tk.END, row['Weight'])
                entry_4_2.delete(0, tk.END)
                entry_4_2.insert(tk.END, row['Comorbidities'])
                entry_5_2.delete(0, tk.END)
                entry_5_2.insert(tk.END, row['Medications'])
                entry_2_6.delete(0, tk.END)
                entry_2_6.insert(tk.END, row['Allergies'])
                entry_3_6.delete(0, tk.END)
                entry_3_6.insert(tk.END, row['Family History'])
                entry_4_6.delete(0, tk.END)
                entry_4_6.insert(tk.END, row['Miscellaneous'])
                entry_5_6.delete(0, tk.END)
                entry_5_6.insert(tk.END, row['Surgical Procedures'])
                entry_2_8.delete(0, tk.END)
                entry_2_8.insert(tk.END, row['Temperature'])
                entry_3_8.delete(0, tk.END)
                entry_3_8.insert(tk.END, row['Heart Rate'])
                entry_4_8.delete(0, tk.END)
                entry_4_8.insert(tk.END, row['Respiratory Rate'])
                entry_5_8.delete(0, tk.END)
                entry_5_8.insert(tk.END, row['Systolic Blood Pressure'] + '/'
                                 + row['Diastolic Blood Pressure'])
                text_9_2.delete('1.0', tk.END)
                text_9_2.insert(tk.END, row['Subjective'])
                text_9_6.delete('1.0', tk.END)
                text_9_6.insert(tk.END, row['Objective'])
                text_11_2.delete('1.0', tk.END)
                text_11_2.insert(tk.END, row['Assessment'])
                text_11_6.delete('1.0', tk.END)
                text_11_6.insert(tk.END, row['Plan'])
                summary.delete('1.0', 'end')
                bd = datetime.datetime.strptime(row['Date of Birth'], '%d-%m-%Y').date()
                age = datetime.date.today().year - bd.year - (
                    (datetime.date.today().month,datetime.date.today().day) < (bd.month, bd.day))
                summary.insert(tk.END, f"{row['Appointment Date']} appointment summary:\n"
                        f"Patient: {row['Name']}, Age: {age}, "
                        f"IMC: {round(float(row['Weight']) / ((float(row['Height']) / 100) ** 2), 2)}\n"
                        f"Complain: {row['Current Complain']}, "
                        f"Comorbidities: {row['Comorbidities']}\n"
                        f"Current medications: {row['Medications']}\n"
                        f"Allergies: {row['Allergies']}, "
                        f"BP:{row['Systolic Blood Pressure']}/{row['Diastolic Blood Pressure']}mmHg"
                        f"HR: {row['Heart Rate']} bpm, RR: {row['Respiratory Rate']} bpm \n")

def is_valid_entry():
    """# validate the entry fields before saving"""
    valid = True
    summary.delete(1.0, tk.END)
    if not entries['name'].get() or not re.match("^[A-Za-z ]+$", entries['name'].get()):
        summary.insert(tk.END, 'Name must contain only letters and spaces\n')
        valid = False
    try:
        datetime.datetime.strptime(entries["date_of_birth_"].get(), '%d-%m-%Y')
    except ValueError:
        summary.insert(tk.END, 'Invalid format for Date of Birth. Expected format: DD-MM-YYYY\n')
        valid = False
    try:
        datetime.datetime.strptime(entries["appointment_date"].get(), '%d-%m-%Y')
    except ValueError:
        summary.insert(tk.END, 'Invalid format for Appointment Date. Expected format: DD-MM-YYYY\n')
        valid = False
    if not entries['height_'].get() or not entries['height_'].get().isdigit():
        summary.insert(tk.END,'Height must be a number in centimeters\n')
        valid = False
    if not entries['weight_'].get() or not re.match(r"^[0-9]+(\.)?[0-9]+$",
                                                    entries['weight_'].get()):
        summary.insert(tk.END,'Weight must be a number in kilograms\n')
        valid = False
    if not entries['temperature_'].get() or not re.match(r"^[0-9]+(\.)?[0-9]+$",
                                                         entries['temperature_'].get()):
        summary.insert(tk.END,'Temperature must a number in Celsius\n')
        valid = False
    if not entries['heart_rate_'].get() or not entries['heart_rate_'].get().isdigit():
        summary.insert(tk.END,'Heart Rate must be a number\n')
        valid = False
    if not entries['respiratory_rate_'].get() or not entries['respiratory_rate_'].get().isdigit():
        summary.insert(tk.END,'Respiratory Rate must be a number\n')
        valid = False
    if not entries['blood_pressure'].get() or not re.match(r"^[0-9]+/[0-9]+$",
                                                           entries['blood_pressure'].get()):
        summary.insert(tk.END,'Blood Pressure must be in the format: Systolic/Diastolic\n')
        valid = False
    if not entries['current_complain'].get():
        summary.insert(tk.END,'Current Complain cannot be empty\n')
        valid = False
    if not entries['comorbidities'].get():
        summary.insert(tk.END,'Comorbidities cannot be empty\n')
        valid = False
    if not entries['medications'].get():
        summary.insert(tk.END,'Medications cannot be empty\n')
        valid = False
    if not entries['allergies'].get() or not re.match(r"^[A-Za-z - \- : ,]+$",
                                                      entries['allergies'].get()):
        summary.insert(tk.END,
        'Allergies must contain only letters, spaces, this chars (- : ,) and cannot be empty\n')
        valid = False
    if not entries['family_history'].get() or not re.match(r"^[A-Za-z - \- : ,]+$",
                                                           entries['family_history'].get()):
        summary.insert(tk.END,
        'Family history only acceppts letters, spaces, this chars (- : ,) and cannot be empty\n')
        valid = False
    if not entries['miscellaneous_notes'].get():
        summary.insert(tk.END,'Miscellaneous Notes cannot be empty\n')
        valid = False
    if not entries['surgical_procedures'].get():
        summary.insert(tk.END,'Surgical Procedures cannot be empty\n')
        valid = False
    if not entries['subjective'].get("1.0", tk.END).strip():
        summary.insert(tk.END, 'Subjective cannot be empty\n')
        valid = False
    if not entries['objective'].get("1.0", tk.END).strip():
        summary.insert(tk.END, 'Objective cannot be empty\n')
        valid = False
    if not entries['assessment'].get("1.0", tk.END).strip():
        summary.insert(tk.END, 'Assessment cannot be empty\n')
        valid = False
    if not entries['plan'].get("1.0", tk.END).strip():
        summary.insert(tk.END, 'Plan cannot be empty\n')
        valid = False
        raise ValueError('Plan cannot be empty')
    if valid:
        save_consult()
    else:
        pass
    return valid

def print_record():
    """# function to print that patient full medical record"""
    # get the selected consults under that patient name
    consult = entry_listbox_6.get(entry_listbox_6.curselection())
    full_record = consult.split(',')[0].split('Name: ')[1]
    # create the pdf to save the full record
    medical_record = FPDF(orientation='P')
    medical_record.set_font("helvetica", size=8)
    line_height = medical_record.font_size * 1.5
    #find the matching patient record
    with open('patients.csv', 'rb') as csvfile:
        encrypted_data = csvfile.read()
        decrypted_data = PROTEKTOR3000_ACTIVATED.decrypt(encrypted_data)
        reader = csv.DictReader(io.StringIO(decrypted_data))
        # defining which columns i want to ignore
        ignore = {'ID'}
        # defining the vital signs so I can move them up
        vital_signs = {
            'Temperature': None,
            'Heart Rate': None,
            'Respiratory Rate': None,
            'Systolic Blood Pressure': None,
            'Diastolic Blood Pressure': None
            }
        with open(f"{full_record}.csv", 'w', newline='', encoding='utf-8') as csvfile:
            writer = None
            for row in reader:
                filtered = {k: v for k, v in row.items() if k not in ignore}
                if full_record.strip() == row['Name'].strip():
                    if not writer:
                        # write headers for csv
                        writer = csv.DictWriter(csvfile, fieldnames=filtered.keys())
                        writer.writeheader()
                    # write the consult data for csv
                    writer.writerow(filtered)
                    # write the consult data for pdf
                    medical_record.add_page()
                    top_row_fields = [key for key in list(filtered.keys())[:5]] + [key for key in vital_signs.keys()]
                    top_row_values = [filtered[key] for key in top_row_fields if key in filtered]
                    # creates the final text to print in the first cell by
                    # zipping the keys and values into a list of tuples
                    first_row_text = ' '.join(f"**{key}**: {value}" for key,
                                              value in zip(top_row_fields, top_row_values))
                    # finally prints it
                    medical_record.multi_cell(105, line_height, first_row_text,
                                              border=1, markdown=True)
                    # little space for style
                    medical_record.ln(line_height)
                    # Print the rest of the columns
                    for key, value in filtered.items():
                        if key not in top_row_fields:
                            row_text = f"**{key}**: {value}"
                            medical_record.multi_cell(185, line_height,
                                                      row_text, border=0, markdown=True)
                            medical_record.ln(line_height)
        # save the pdf
        medical_record.output(f"{full_record}.pdf")
        # update user
        summary.delete(1.0, tk.END)
        summary.insert(tk.END, "Full record saved and ready to print!\n")
        time.sleep(2)
        webbrowser.open(os.path.abspath(f"{full_record}.pdf"))

def delete_consult():
    """# function to delete a consult"""
    # get the selected consult ID
    consult = entry_listbox_6.get(entry_listbox_6.curselection())
    consult_name = consult.split(',')[0].split('Name: ')[1]
    consult_id = consult.split('ID: ')[1]
    with open('patients.csv', 'rb') as csvfile:
        encrypted_data = csvfile.read()
        decrypted_data = PROTEKTOR3000_ACTIVATED.decrypt(encrypted_data)

    # store my data temporarily to compare
    reader = csv.DictReader(io.StringIO(decrypted_data))
    rows = list(reader)

    # DE-LE-TED!
    updated_rows = [row for row in rows if row['ID'].strip() != consult_id.strip()]

    # Summon PROTEKTOR3000
    updated_data = io.StringIO()
    writer = csv.DictWriter(updated_data, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(updated_rows)
    encrypted_updated_data = PROTEKTOR3000_ACTIVATED.encrypt(updated_data.getvalue())

    with open('patients.csv', 'wb') as csvfile:
        csvfile.write(encrypted_updated_data)

    # Updates GUI
    clear_fields()
    summary.delete(1.0, tk.END)
    summary.insert(tk.END, "Consult deleted!\n")
    search_entry.delete(0, tk.END)
    search_entry.insert(tk.END, f"{consult_name}")
    trigger_search(search_entry, entry_listbox_6)


#########################################################################################
# creating my GUI
root = tk.Tk()
root.title("Medical Records System")
root.configure(background='#0B0B0B')
# Create my fonts objects
font1 = tkFont.Font(family="Helvetica", size=12, weight="bold")
font2 = tkFont.Font(family="Helvetica", size=16, weight="bold")
larger_font = tkFont.Font(family="Helvetica", size=16)

# Using figlet in my "Title" as reference to the problem set "Frank, Ian and Glen's
# Letters" and an emoji in my "subtitle" as a referene to the emojize <3
f = Figlet()
f.setFont(font='big')
f.width = 400
title = f.renderText('Arlong Medical Records')
TitleWidget = tk.Text(root, height=13, width=120, relief=tk.SOLID, borderwidth=1,
                       background='#000000', foreground='#FF6EB4',wrap=tk.NONE)
TitleWidget.grid(row=0, column=1, columnspan=14, rowspan=1, sticky="ns")
TitleWidget.insert(tk.END,'\n' + title)
subtitle_out = f"\nDeveloped by @luizfillipeps {emojize(':sunglasses:', language='alias')}"
TitleWidget.insert(tk.END, subtitle_out)
SUBTITLE_IN = TitleWidget.search(subtitle_out, "1.0", tk.END)
TitleWidget.tag_add("larger_font", SUBTITLE_IN, tk.END)
TitleWidget.tag_config("larger_font", font=larger_font)
TitleWidget.tag_add("titleandsubtitle", "1.0", "end")
TitleWidget.tag_configure("titleandsubtitle", justify='center')
TitleWidget.config(state=tk.DISABLED)

# Create empty labels for spacing
label_y = tk.Label(root, text="", height=2, background='#0B0B0B')
label_y.grid(row=1, column=0, columnspan=14)
label_x = tk.Label(root, text="", width=5,background='#0B0B0B')
label_x.grid(row=0, column=0, rowspan=8)
label_middle = tk.Label(root, text="", height=2,background='#0B0B0B')

label_middle.grid(row=7, column=0, columnspan=14)
label_bottom = tk.Label(root, text="", height=1,background='#0B0B0B')
label_bottom.grid(row=12, column=0, columnspan=14)

# initialize my dictionary to store consult data from the GUI
entries = {}

# Name
label_2_1 = tk.Label(root, text="Name:",background='#0B0B0B', foreground='#FF6EB4',font=font1)
label_2_1.grid(row=2, column=1, sticky="nse", padx=2, pady=2)
entry_2_2 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                     background='#1d1f1d', foreground='white')
entry_2_2.grid(row=2, column=2, stick="w", padx=2, pady=2)
entries["name"] = entry_2_2

# Current Complaint
label_3_1 = tk.Label(root, text="Current Complaint:",background='#0B0B0B',
                         foreground='#FF6EB4',font=font1)
label_3_1.grid(row=3, column=1, sticky="nse", padx=2, pady=2)
entry_3_2 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_3_2.grid(row=3, column=2, stick="w", padx=2, pady=2)
entries["current_complain"] = entry_3_2

# Comorbidities
label_4_1 = tk.Label(root, text="Comorbidities:",background='#0B0B0B',
                        foreground='#FF6EB4',font=font1)
label_4_1.grid(row=4, column=1, sticky="nse", padx=2, pady=2)
entry_4_2 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_4_2.grid(row=4, column=2, stick="w", padx=2, pady=2)
entries["comorbidities"] = entry_4_2

# Medications
label_5_1 = tk.Label(root, text="Medications:",background='#0B0B0B',
                        foreground='#FF6EB4',font=font1)
label_5_1.grid(row=5, column=1, sticky="nse", padx=2, pady=2)
entry_5_2 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_5_2.grid(row=5, column=2, stick="w", padx=2, pady=2)
entries["medications"] = entry_5_2

# Date of Birth (DD-MM-YYYY)
label_2_3 = tk.Label(root, text="             Birthday (DD-MM-YYYY):",
                        background='#0B0B0B', foreground='#FF6EB4',font=font1)
label_2_3.grid(row=2, column=3, sticky="nse", padx=2, pady=2)
entry_2_4 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_2_4.grid(row=2, column=4, stick="w", padx=2, pady=2)
entries["date_of_birth_"] = entry_2_4

# Appointment Date (DD-MM-YYYY)
label_3_3 = tk.Label(root, text="     Appointment (DD-MM-YYYY):",background='#0B0B0B',
                        foreground='#FF6EB4',font=font1)
label_3_3.grid(row=3, column=3, sticky="nse", padx=2, pady=2)
entry_3_4 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_3_4.grid(row=3, column=4, stick="w", padx=2, pady=2)
entries["appointment_date"] = entry_3_4

# Height (cm)
label_4_3 = tk.Label(root, text="Height (cm):",background='#0B0B0B',
                        foreground='#FF6EB4',font=font1)
label_4_3.grid(row=4, column=3, sticky="nse", padx=2, pady=2)
entry_4_4 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_4_4.grid(row=4, column=4, stick="w", padx=2, pady=2)
entries["height_"] = entry_4_4

# Weight (kg)
label_5_3 = tk.Label(root, text="Weight (kg):",background='#0B0B0B',
                        foreground='#FF6EB4',font=font1)
label_5_3.grid(row=5, column=3, sticky="nse", padx=2, pady=2)
entry_5_4 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_5_4.grid(row=5, column=4, stick="w", padx=2, pady=2)
entries["weight_"] = entry_5_4

# Allergies
label_2_5 = tk.Label(root, text="Allergies:",background='#0B0B0B',
                        foreground='#FF6EB4',font=font1)
label_2_5.grid(row=2, column=5, sticky="nse", padx=2, pady=2)
entry_2_6 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_2_6.grid(row=2, column=6, stick="w", padx=2, pady=2)
entries["allergies"] = entry_2_6

# Family History
label_3_5 = tk.Label(root, text="Family History:", background='#0B0B0B',
                        foreground='#FF6EB4',font=font1)
label_3_5.grid(row=3, column=5, sticky="nse", padx=2, pady=2)
entry_3_6 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_3_6.grid(row=3, column=6, stick="w", padx=2, pady=2)
entries["family_history"] = entry_3_6

# Miscellaneous Notes
label_4_5 = tk.Label(root, text="Miscellaneous Notes:", background='#0B0B0B',
                        foreground='#FF6EB4',font=font1)
label_4_5.grid(row=4, column=5, sticky="nse", padx=2, pady=2)
entry_4_6 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_4_6.grid(row=4, column=6, stick="w", padx=2, pady=2)
entries["miscellaneous_notes"] = entry_4_6

# Surgical Procedures
label_5_5 = tk.Label(root, text="Surgical Procedures:", background='#0B0B0B',
                        foreground='#FF6EB4',font=font1)
label_5_5.grid(row=5, column=5, sticky="nse", padx=2, pady=2)
entry_5_6 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_5_6.grid(row=5, column=6, stick="w", padx=2, pady=2)
entries["surgical_procedures"] = entry_5_6

# Temperature (°C)
label_2_7 = tk.Label(root, text="Temperature (°C):",background='#0B0B0B',
                        foreground='#FF6EB4',font=font1)
label_2_7.grid(row=2, column=7, sticky="nse", padx=2, pady=2)
entry_2_8 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_2_8.grid(row=2, column=8, stick="w", padx=2, pady=2)
entries["temperature_"] = entry_2_8

# Heart Rate (bpm)
label_3_7 = tk.Label(root, text="Heart Rate (bpm):", background='#0B0B0B',
                        foreground='#FF6EB4',font=font1)
label_3_7.grid(row=3, column=7, sticky="nse", padx=2, pady=2)
entry_3_8 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_3_8.grid(row=3, column=8, stick="w", padx=2, pady=2)
entries["heart_rate_"] = entry_3_8

# Respiratory Rate (bpm)
label_4_7 = tk.Label(root, text="Respiratory Rate (rpm):", background='#0B0B0B',
                        foreground='#FF6EB4',font=font1)
label_4_7.grid(row=4, column=7, sticky="nse", padx=2, pady=2)
entry_4_8 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_4_8.grid(row=4, column=8, stick="w", padx=2, pady=2)
entries["respiratory_rate_"] = entry_4_8

# BP (mmHg)
label_5_7 = tk.Label(root, text="Blood Pressure (mmHg):", background='#0B0B0B',
                        foreground='#FF6EB4',font=font1)
label_5_7.grid(row=5, column=7, sticky="nse", padx=2, pady=2)
entry_5_8 = tk.Entry(root, width=35,relief=tk.SOLID, borderwidth=2,
                        background='#1d1f1d', foreground='white')
entry_5_8.grid(row=5, column=8, stick="w", padx=2, pady=2)
entries['blood_pressure'] = entry_5_8

# Subjective SOAP
label_8_2 = tk.Label(root, text="Subjective: ", background='#0B0B0B',
                        foreground='#FF6EB4',font=font2)
label_8_2.grid(row=8, column=2, sticky="se", padx=2, pady=2)
text_9_2 = ScrolledText(root, height=14, width=60, relief=tk.SOLID,
                        borderwidth=0,background='#DCDCDC',foreground='#0B0B0B')
text_9_2.grid(row=9, column=2, columnspan=2, sticky="n", padx=2, pady=2)
entries['subjective'] = text_9_2

# Objective SOAP
label_8_6 = tk.Label(root, text="Objective: ", background='#0B0B0B',
                        foreground='#FF6EB4',font=font2)
label_8_6.grid(row=8, column=4, sticky="se", padx=2, pady=2)
text_9_6 = ScrolledText(root, height=14, width=60, relief=tk.SOLID,
                        borderwidth=0,background='#DCDCDC',foreground='#0B0B0B')
text_9_6.grid(row=9, column=4, columnspan=2, sticky="n", padx=2, pady=2)
entries['objective'] = text_9_6

# Assessment SOAP
label_10_2 = tk.Label(root, text="Assessment: ", background='#0B0B0B',
                        foreground='#FF6EB4',font=font2)
label_10_2.grid(row=10, column=2, sticky="se", padx=2, pady=2)
text_11_2 = ScrolledText(root, height=6, width=60, relief=tk.SOLID, borderwidth=0,
                            background='#DCDCDC',foreground='#0B0B0B')
text_11_2.grid(row=11, column=2, columnspan=2, padx=2, pady=2)
entries['assessment'] = text_11_2

# Plan SOAP
label_10_6 = tk.Label(root, text="Plan: ", background='#0B0B0B',
                        foreground='#FF6EB4',font=font2)
label_10_6.grid(row=10, column=4, sticky="se", padx=2, pady=2)
text_11_6 = ScrolledText(root, height=6, width=60,relief=tk.SOLID,
                            borderwidth=0,background='#DCDCDC',foreground='#0B0B0B')
text_11_6.grid(row=11, column=4, columnspan=2, padx=2, pady=2)
entries['plan'] = text_11_6

# Buttons to perform actions
save_button = tk.Button(root, text="Save", command=is_valid_entry, background='White')
clear_button = tk.Button(root, text="Clear", command=clear_fields, background='White')
DeleteRecord_button = tk.Button(root, text="Delete Consult", command=delete_consult,
                                background='White')
medical_record_button = tk.Button(root, text="Print Record", command=print_record,
                                    background='White')
search_entry = tk.Entry(root, width=30,relief=tk.SOLID, borderwidth=2)
search_button = tk.Button(root, text="Search",
                            command=lambda: trigger_search(search_entry, entry_listbox_6))
save_button.grid(row=6, rowspan=2, column=1, columnspan=2, pady=10)
clear_button.grid(row=6, rowspan=2, column=2, columnspan=2, pady=10)
DeleteRecord_button.grid(row=6, rowspan=2, column=4, columnspan=2, pady=10)
medical_record_button.grid(row=6, rowspan=2, column=5, columnspan=2, pady=10)
search_entry.grid(row=6, rowspan=2, column=6, sticky="e",columnspan=2, padx=2, pady=10)
search_button.grid(row=6, rowspan=2, column=8, sticky="w", padx=2, pady=10)

# summary textbox
summary = tk.Label(root, text="Summary:",background='#0B0B0B', foreground='#FF6EB4',font=font1)
summary.grid(row=13, column=0, columnspan=7, sticky="ns")
summary = tk.Text(root, height=10, width=80,relief=tk.SOLID, borderwidth=5,
                    background='#DCDCDC',foreground='#0B0B0B')
summary.grid(row=14, column=0, columnspan=7, padx=2, pady=2)

# listbox lets goo! we're learning boys =D
label_listbox_6 = tk.Label(root, text="Previous consults: ", background='#0B0B0B',
                        foreground='#FF6EB4',font=font2)
label_listbox_6.grid(row=8, column=6, sticky="se", padx=2, pady=2)
entry_listbox_6 = tk.Listbox(root, height=6, width=60,background='#DCDCDC',
                            foreground='#0B0B0B')
entry_listbox_6.grid(row=9, rowspan=13, column=6, columnspan=6, sticky="nswe", padx=2, pady=2)
entry_listbox_6.bind('<<ListboxSelect>>', on_select)
scrollbar_listbox = tk.Scrollbar(root,highlightcolor='#0B0B0B',
                                    troughcolor='#0B0B0B', background='#0B0B0B')
scrollbar_listbox.grid(row=9, column=6, rowspan=13, columnspan=6, sticky="nse")
entry_listbox_6.config(yscrollcommand=scrollbar_listbox.set)
scrollbar_listbox.config(command=entry_listbox_6.yview)

# trying to make my grid responsive, not sure if its working tho
for col in range(14):
    root.grid_columnconfigure(col, weight=1)
for row in range(15):
    root.grid_rowconfigure(row, weight=1)

if __name__ == '__main__':
    main()