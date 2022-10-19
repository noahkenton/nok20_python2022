Use nok20;


DROP TABLE IF EXISTS visit_procedure;
DROP TABLE IF EXISTS visit_diagnosis;
DROP TABLE IF EXISTS visit;
DROP TABLE IF EXISTS patient;
DROP TABLE IF EXISTS procedure_;
DROP TABLE IF EXISTS doctor;
DROP TABLE IF EXISTS diagnosis;


CREATE TABLE IF NOT EXISTS patient (
		patient_uuid VARCHAR(100) PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    symptoms VARCHAR(30) NOT NULL
    ) Engine = InnoDB;
    
CREATE TABLE IF NOT EXISTS doctor (
		doctor_uuid VARCHAR(100) PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL
    ) Engine = InnoDB;
    
CREATE TABLE IF NOT EXISTS visit (
			visit_uuid VARCHAR(100) PRIMARY KEY,
		visit_date DATETIME NOT NULL,
		fk_doctor_uuid VARCHAR(100),
		fk_patient_uuid VARCHAR(100),
    FOREIGN KEY (fk_doctor_uuid) REFERENCES doctor (doctor_uuid) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (fk_patient_uuid) REFERENCES patient (patient_uuid) ON DELETE CASCADE ON UPDATE CASCADE 
    ) Engine = InnoDB;
 
CREATE TABLE IF NOT EXISTS procedure_ (
		procedure_uuid VARCHAR(100) PRIMARY KEY,
    procedure_name VARCHAR(30) NOT NULL
    ) Engine = InnoDB;
    
CREATE TABLE IF NOT EXISTS visit_procedure (
		fk_visit_uuid VARCHAR(50),
		fk_procedure_uuid VARCHAR(50),
    FOREIGN KEY (fk_visit_uuid) REFERENCES visit (visit_uuid) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (fk_procedure_uuid) REFERENCES procedure_ (procedure_uuid) ON DELETE CASCADE ON UPDATE CASCADE    
    ) Engine = InnoDB;
    
CREATE TABLE IF NOT EXISTS diagnosis (
	diagnosis_uuid VARCHAR(100) NOT NULL PRIMARY KEY,
    diagnosis VARCHAR(30) NOT NULL
    ) Engine = InnoDB;    
    
CREATE TABLE IF NOT EXISTS visit_diagnosis (
	fk_visit_uuid VARCHAR(100),
    fk_diagnosis_uuid VARCHAR(100),
    FOREIGN KEY (fk_visit_uuid) REFERENCES visit (visit_uuid) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (fk_diagnosis_uuid) REFERENCES diagnosis (diagnosis_uuid) ON DELETE CASCADE ON UPDATE CASCADE    
    ) Engine = InnoDB;

    