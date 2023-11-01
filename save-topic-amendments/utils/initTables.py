import sqlite3


def initTables():
    conn = sqlite3.connect("emendas.db")

    cursor = conn.cursor()

    cursor.execute("create table if not exists feedback_model( id integer primary key autoincrement not null,"
                   " projectLaw VARCHAR(100),"
                   " amendment VARCHAR(100),"
                   "topic VARCHAR(100),"
                   "score_standardized NUMERIC)")
    cursor.execute("create table if not exists feedback_consultant(id integer primary key autoincrement not null,"
                   "projectLaw VARCHAR(100),"
                   "amendment VARCHAR(100),"
                   "topic VARCHAR(100),"
                   "matConsultant VARCHAR(100),"
                   "dataAlteracao TIMESTAMP)")


    conn.commit()
    conn.close()


