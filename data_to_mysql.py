import pymysql
import getpass, glob, re
import pandas as pd
import csv
import ast
import random
from faker import Faker

random.seed(10)

def parse_sql(sql_file_path):
    with open(sql_file_path, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
    stmt = ''
    stmts = []
    for line in data:
        if line:
            if line.startswith('--'):
                continue
            stmt += line.strip() + ' '
            if ';' in stmt:
                stmts.append(stmt.strip())
                stmt = ''     
    return stmts

def get_disciplines(path):
    discipline_file = open(path, 'r', encoding='utf8')
    discipline = discipline_file.read()
    discipline_list = discipline.split(',')    
    return discipline_list

def get_notes(path):
    with open(path, "r", encoding='utf8') as inFile:
        data = ast.literal_eval(inFile.read())
        return data
        
def insert_disciplines(disciplines, cur):
    for discipline in disciplines:
        period = random.randint(1,8)
        data = (discipline, period)
        sql = "INSERT INTO disciplina (nome, periodo) VALUES (%s, %s)"
        cur.execute(sql, data)

def insert_texts(pages, disciplines, cur):
    Faker.seed(0)
    fake = Faker()
    fake.seed_instance(0)
    count_disc = 1
    remove_list = ('Wikipédia', "ISO")
    for page in pages:
        for key, value in page.items():
            if(key.startswith(remove_list)):
                continue
            creation_date = fake.date_time_between(start_date="-3y",end_date="-30d")
            last_changed = fake.date_time_between(start_date=creation_date,end_date="+1d")
            number_of_changes = random.randint(5,22)
            data = (key, value, creation_date, last_changed, number_of_changes, count_disc)
            sql = "INSERT INTO nota (titulo, texto, ultima_modificacao, data_criacao, numero_edicoes, disciplina) VALUES (%s, %s, %s, %s, %s, %s)"
            cur.execute(sql, data)
        count_disc+=1

def main():
    notes = get_notes("data/texts.txt")
    disciplines = get_disciplines("data/disciplines.txt")
    password = getpass.getpass()

    database = 'notes_app'
    user = 'root'
    host='localhost'
    
    con = pymysql.connect(host=host, user=user, passwd=password)
    cur = con.cursor()
    con.autocommit(True)

    sql_creation_stmts = parse_sql("db/schema.sql")
    for stmt in sql_creation_stmts:
        cur.execute(stmt)

    con_notes = pymysql.connect(host=host, user=user, passwd=password, database=database)
    cur_notes = con.cursor()
    con_notes.autocommit(True)

    insert_disciplines(disciplines, cur_notes)
    insert_texts(notes, disciplines, cur_notes)

main()
