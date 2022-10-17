Use nok20;

DROP TABLE IF EXISTS paitent;
DROP TABLE IF EXISTS visit_procedure;
DROP TABLE IF EXISTS visit;
DROP TABLE IF EXISTS procedure_;
DROP TABLE IF EXISTS doctor;
DROP TABLE IF EXISTS visit_diagnosis;
DROP TABLE IF EXISTS diagnosis;


CREATE TABLE IF NOT EXISTS paitent (
	paitent_uuid INT NOT NULL PRIMARY KEY
    ) Engine = InnoDB;
    
CREATE TABLE IF NOT EXISTS visit (
	visit_uuid INT NOT NULL PRIMARY KEY,
    fk_doctor_uuid INT NOT NULL,
    fk_paitent_uuid INT NOT NULL
    ) Engine = InnoDB;
    
CREATE TABLE IF NOT EXISTS visit_procedure (
	fk_visit_uuid INT NOT NULL,
    fk_procedure_uuid INT NOT NULL,
    FOREIGN KEY (fk_visit_uuid) REFERENCES visit (visit_uuid) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (fk_procedure_uuid) REFERENCES visit (visit_uuid) ON DELETE CASCADE ON UPDATE CASCADE    
    ) Engine = InnoDB;

CREATE TABLE IF NOT EXISTS procedure_ (
	procedure_uuid INT NOT NULL PRIMARY KEY
    ) Engine = InnoDB;
    
CREATE TABLE IF NOT EXISTS doctor (
	doctor_uuid INT NOT NULL PRIMARY KEY
    ) Engine = InnoDB;
    
CREATE TABLE IF NOT EXISTS diagnosis (
	diagnosis_uuid INT NOT NULL PRIMARY KEY
    ) Engine = InnoDB;    
    
CREATE TABLE IF NOT EXISTS visit_diagnosis (
	fk_visit_uuid INT NOT NULL,
    fk_diagnosis_uuid INT NOT NULL,
    FOREIGN KEY (fk_visit_uuid) REFERENCES visit (visit_uuid) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (fk_diagnosis_uuid) REFERENCES diagnosis (diagnosis_uuid) ON DELETE CASCADE ON UPDATE CASCADE    
    ) Engine = InnoDB;

    