import uuid
import json
import pymysql
import unittest 
from flask import Flask


class Config:
    # Configuration file handler
    def __init__(self):
        con_params = self.__read_config()
        self.db_conn = pymysql.connect(host=con_params["host"],
                             user=con_params["user"],
                             password=con_params["password"],
                             db=con_params["db"],
                             charset=con_params["charset"],
                             cursorclass=pymysql.cursors.DictCursor)

    def __read_config(self):
        # Read config file for accessing sql database

        try:
            with open("config.txt", "r")as file_name:
                data = file_name.read()
                return dict(json.loads(data))
        finally:
            file_name.close()


class Doctor:
    # specify and load doctor entity from file or user input
    def __init__(self, doctor_id="", f_name="", l_name=""):
        self.__fist_name = f_name
        self.__last_name = l_name
        ''' if doctor id is not specified or does not exist generate doctor
            id and insert values into approrpiate table
        '''
        if doctor_id == "":
            self.__doctor_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn

                # prameterize arguements

                with con.cursor() as cur:
                    qry = 'INSERT INTO doctor (doctor_uuid, first_name, last_name)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__doctor_id, self.__fist_name, self.__last_name))
                    con.commit()
            finally:
                pass
        else:
            # Get
            self.__doctor_id = doctor_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM doctor WHERE doctor_uuid = '" + doctor_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__doctor_id = row["doctor_uuid"]
                        self.__fist_name = row["first_name"]
                        self.__last_name = row["last_name"]
            finally:
                con.close()

    def get_doctor_id(self):
        return self.__doctor_id
    
    def get_first_name(self):
        # get first name value
        return self.__fist_name

    def set_first_name(self, f_name):
        # set value for doctor
        self.__fist_name = f_name

        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET first_name = %s WHERE doctor_uuid = %s;'
                print(qry)
                cur.execute(qry, (self.__fist_name, self.__doctor_id))
                con.commit()
        finally:
            pass

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, l_name):
        self.__last_name = l_name

        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET last_name = %s WHERE doctor_uuid = %s;'
                print(qry)
                cur.execute(qry, (self.__last_name, self.__doctor_id))
                con.commit()
        finally:
            pass

    def to_json(self):
        fields_data = {
            "doctor_id": self.__doctor_id,
            "first_name": self.__fist_name,
            "last_name": self.__last_name
        }
        return json.dumps(fields_data)


class Patient:
    def __init__(self, patient_id="", f_name="", l_name="", symptoms=""):
        self.__fist_name = f_name
        self.__last_name = l_name
        self.__symptoms = symptoms
        ''' if doctor id is not specified or does not exist generate patient
            id and insert values into approrpiate table
        '''

        if patient_id == "":
            self.__patient_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO patient (patient_uuid, first_name, last_name, symptoms)'
                    qry = qry + 'VALUES(%s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__patient_id, self.__fist_name,
                                      self.__last_name, self.__symptoms))
                    con.commit()
            finally:
                pass
        else:
            self.__patient_id = patient_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM patient WHERE patient_uuid = '" + patient_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__patient_id = row["patient_uuid"]
                        self.__fist_name = row["first_name"]
                        self.__last_name = row["last_name"]
                        self.__symptoms = row["symptoms"]
            finally:
                pass

    def get_first_name(self):
        # get first name value
        return self.__fist_name

    def set_first_name(self, f_name):
        # set first name value
        self.__fist_name = f_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET first_name = %s WHERE patient_uuid = %s;'
                print(qry)
                cur.execute(qry, (self.__fist_name, self.__patient_id))
                con.commit()
        finally:
            pass

    def get_last_name(self):
        # get last name value
        return self.__last_name

    def set_last_name(self, l_name):
        # set last name value
        self.__last_name = l_name

        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET last_name = %s WHERE patient_uuid = %s;'
                print(qry)
                cur.execute(qry, (self.__last_name, self.__patient_id))
                con.commit()
        finally:
            pass
        
    def get_patient_id(self):
        return self.__patient_id

    def get_symptoms(self):
        # get symptom value
        return self.__symptoms

    def set_symptoms(self, symptoms):
        # set symptom value
        self.__symptoms = symptoms

        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET symptoms = %s WHERE patient_uuid = %s;'
                print(qry)
                cur.execute(qry, (self.__symptoms, self.__patient_id))
                con.commit()
        finally:
            pass

    def to_json(self):
        # dump dictionary value as a string
        fields_data = {
            "patient_id": self.__patient_id,
            "first_name": self.__fist_name,
            "last_name": self.__last_name,
            "symptoms": self.__symptoms
        }
        return json.dumps(fields_data)


class Visit:
    def __init__(self, visit_id="", visit_date="", doctor_id="", patient_id=""):
        self.__visit_date = visit_date
        self.__doctor_id = doctor_id
        self.__patient_id = patient_id
        if visit_id == "":
            self.__visit_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO visit (visit_uuid, visit_date, fk_doctor_uuid, fk_patient_uuid)'
                    qry = qry + 'VALUES(%s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__visit_id, self.__visit_date, self.__doctor_id, self.__patient_id))
                    con.commit()
            finally:
                pass
        else:
            self.__visit_id = visit_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM visit WHERE visit_uuid = '" + visit_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__visit_id = row["visit_id"]
                        self.__visit_date = row["visit_date"]
                        self.__doctor_id = row["fk_doctor_uuid"]
                        self.__patient_id = row["fk_patient_uuid"]
            finally:
                pass

    def get_visit_date(self):
        # get visit date
        return self.__visit_date

    def set_visit_date(self, visit_date):
        # set visit date and update table
        self.__visit_date = visit_date
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE visit SET visit_date = %s WHERE visit_uuid = %s;'
                print(qry)
                cur.execute(qry, (self.__visit_date, self.__visit_id))
                con.commit()
        finally:
            pass

    def set_visit_fk_doctor_id(self, doctor_id):
        # set visit date and update table
        self.__doctor_id = doctor_id

        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE visit SET fk_doctor_uuid = %s WHERE visit_uuid = %s;'
                print(qry)
                cur.execute(qry, (self.__doctor_id, self.__visit_id))
                con.commit()
        finally:
            pass

    def set_fk_patient_id(self, patient_id):
        # set visit date and update table
        self.__patient_id = patient_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE visit SET fk_patient_uuid = %s WHERE visit_uuid = %s;'
                print(qry)
                cur.execute(qry, (self.__patient_id, self.__visit_id))
                con.commit()
        finally:
            pass

    def to_json(self):
        fields_data = {
            "visit_id": self.__visit_id,
            "visit_date": self.__visit_date,
            "fk_patient_id": self.__doctor_id,
            "fk_doctor_id": self.__patient_id
            
        }
        return json.dumps(fields_data)


class Diagnosis:
    def __init__(self, diagnosis_id="", diagnosis=""):
        self.__diagnosis = diagnosis
        if diagnosis_id == "":
            self.__diagnosis_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO diagnosis (diagnosis_uuid, diagnosis)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__diagnosis_id, self.__diagnosis))
                    con.commit()
            finally:
                con.close()
        else:
            self.__diagnosis_id = diagnosis_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM diagnosis WHERE diagnosis_uuid = '" + diagnosis_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__diagnosis_id = row["diagnosis_uuid"]
                        self.__diagnosis = row["diagnosis_name"]
            finally:
                con.close()

    def get_diagnosis(self):
        # get diagnosis value
        return self.__diagnosis

    def set_diagnosis(self, patient_id):
        # set diagnosis value and update table
        self.__diagnosis_id = patient_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE diagnosis SET diagnosis = %s WHERE diagnosis_uuid = %s;'
                print(qry)
                cur.execute(qry, (self.__diagnosis, self.__diagnosis_id))
                con.commit()
        finally:
            con.close()

    def to_json(self):
        fields_data = {
            "diagnosis_id": self.__diagnosis_id,
            "diagnosis": self.__diagnosis
        }
        return json.dumps(fields_data)


class Procedure:
    def __init__(self, procedure_id="", p_name=""):
        self.__procedure_name = p_name
        if procedure_id == "":
            self.__procedure_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO procedure_ (procedure_uuid, procedure_name)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__procedure_id, self.__procedure_name))
                    con.commit()
            finally:
                con.close()
        else:
            self.__procedure_id = procedure_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM procedure_ WHERE procedure_uuid = '" + procedure_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__procedure_id = row["procedure_uuid"]
                        self.__procedure_name = row["procedure_name"]
            finally:
                con.close()

    def get_procedure_name(self):
        # get procedure value
        return self.__procedure_name

    def set_procedure_name(self, p_name):
        # set procedure value and update table
        self.__procedure_id = p_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE procedure SET procedure_name = %s WHERE procedure_uuid = %s;'
                print(qry)
                cur.execute(qry, (self.__procedure_name, self.__procedure_id))
                con.commit()
        finally:
            con.close()

    def to_json(self):
        fields_data = {
            "procedure_id": self.__procedure_id,
            "procedure_name": self.__procedure_name
        }
        return json.dumps(fields_data)


# proc = Procedure(procedure_id="", p_name="liver transplant")
# proc = Procedure(procedure_id="", p_name="Colonoscopy")
# proc = Procedure(procedure_id="", p_name="chemotherapy")
# print(proc.to_json())
# 
# doc = Doctor(doctor_id="", f_name="Rob", l_name="West")
# doc = Doctor(doctor_id="", f_name="Berry", l_name="East")
# doc = Doctor(doctor_id="", f_name="Jason", l_name="North")
# print(doc.to_json())
# 
# diag = Diagnosis(diagnosis_id="", diagnosis="ligma")
# diag = Diagnosis(diagnosis_id="", diagnosis="updog")
# diag = Diagnosis(diagnosis_id="", diagnosis="cancer")
# print(diag.to_json())
# 
# patient = Patient(patient_id="", f_name="Bob", l_name="Smith", symptoms="chills")
# patient = Patient(patient_id="", f_name="Vicky", l_name="Poll", symptoms="fever")
# patient = Patient(patient_id="", f_name="Tim", l_name="Beach", symptoms="rapid weight loss")
# print(patient.to_json())
# 
# visit = Visit(visit_id="", visit_date="2022-08-10", doctor_id=doc.get_doctor_id(), patient_id=patient.get_patient_id())
# visit = Visit(visit_id="", visit_date="2022-08-11", doctor_id=doc.get_doctor_id(), patient_id=patient.get_patient_id())
# visit = Visit(visit_id="", visit_date="2022-08-12", doctor_id=doc.get_doctor_id(), patient_id=patient.get_patient_id())
# print(visit.to_json())

app = Flask(__name__)


@app.route('/')
def index():
    patient = Patient(patient_id="", f_name="Bruce", l_name="Banner", symptoms="green skin")
    doc = Doctor(doctor_id="", f_name="Foo", l_name="Bar")
    visit = Visit(visit_id="", visit_date="2022-10-10", doctor_id=doc.get_doctor_id(), 
                  patient_id=patient.get_patient_id())
    visit2 = Visit(visit_id="", visit_date="2022-10-12", doctor_id=doc.get_doctor_id(),
                   patient_id=patient.get_patient_id())
    
    dict = {
        "patient": (patient.get_first_name(), patient.get_last_name(), patient.get_patient_id()),
        "Doctor": (doc.get_first_name(), doc.get_last_name(), doc.get_doctor_id()),
        "Visit 1": visit.to_json(),
        "Visit 2": visit2.to_json()
    }
    
    return json.dumps(dict)


app.run()


class Tester(unittest.TestCase):
    def select_doctor(self):
        fname = Doctor(f_name="Rob")
        self.run(fname)

    def update_doctor_name(self):
        re_name = Doctor(f_name="Rob")
        re_name.set_last_name(l_name="Stark")
        self.run(re_name)

    def new_doctor(self):
        new_entry = Doctor(f_name="Tony", l_name="Stark")
        self.run(print(new_entry.to_json()))

    def furlough(self):
        unlucky_doc = "Tony"
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = "DELETE * FROM doctor WHERE first_name = '" + unlucky_doc + "'"
                print(qry)
                cur.execute(qry)
        finally:
            con.close()
        self.run(furlough())


#unittest.main()
