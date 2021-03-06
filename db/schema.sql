DROP SCHEMA IF EXISTS notes_app;
CREATE SCHEMA IF NOT EXISTS notes_app DEFAULT CHARACTER SET utf8;
USE notes_app;

CREATE TABLE IF NOT EXISTS notes_app.disciplina (
  id_disciplina INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(200) NOT NULL,
  periodo INT NOT NULL,
  PRIMARY KEY (id_disciplina));


CREATE TABLE IF NOT EXISTS notes_app.nota (
  id_nota INT NOT NULL AUTO_INCREMENT,
  titulo VARCHAR(200) NOT NULL,
  texto TEXT NOT NULL,
  ultima_modificacao DATETIME NOT NULL,
  data_criacao DATETIME NOT NULL,
  numero_edicoes INT NOT NULL,
  disciplina INT NOT NULL,
  PRIMARY KEY (id_nota),
  INDEX fk_nota_disciplina_idx (disciplina ASC) VISIBLE,
  CONSTRAINT fk_nota_disciplina
    FOREIGN KEY (disciplina)
    REFERENCES notes_app.disciplina (id_disciplina)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
