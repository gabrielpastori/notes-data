import pymysql
import getpass, glob, re
import pandas as pd
import csv
import ast
import random
from faker import Faker

def get_disciplines(path):
    discipline_file = open(path, 'r')
    discipline = discipline_file.read()
    discipline_list = discipline.split(',')    
    return discipline_list

def get_notes(path):
    with open(path, "r") as inFile:
        data = ast.literal_eval(inFile.read())
        return data
        
def insert_disciplines(disciplines, cur):
    for discipline in disciplines:
        period = random.randint(0,10)
        data = (discipline, period)
        sql = "INSERT INTO disciplina (nome, periodo) VALUES (%s, %s)"
        cur.execute(sql, data)

def insert_texts(pages, disciplines, cur):
    fake = Faker()
    count_disc = 1
    for page in pages:
        for key, value in page.items():
            creation_date = fake.date_time_between(start_date="-3y",end_date="-30d")
            last_changed = fake.date_time_between(start_date=creation_date,end_date="+1d")
            data = (key, value, creation_date, last_changed, count_disc)
            sql = "INSERT INTO nota (titulo, texto, ultima_modificacao, data_criacao, disciplina) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(sql, data)
        count_disc+=1

def main():
    notes = get_notes("data/texts.txt")
    disciplines = get_disciplines("data/disciplines.txt")
    password = getpass.getpass()

    database = 'notes'
    user = 'root'
    host='localhost'
    
    con = pymysql.connect(host=host, user=user, passwd=password, database=database)
    cur = con.cursor()
    con.autocommit(True)

    insert_disciplines(disciplines, cur)
    insert_texts(notes, disciplines, cur)

main()