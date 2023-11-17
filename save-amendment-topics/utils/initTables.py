import sqlite3


def initTables():
    conn = sqlite3.connect("emendas.db")

    cursor = conn.cursor()

    cursor.execute("create table if not exists model_topics( id integer primary key autoincrement not null,"
                   "projectLaw VARCHAR(100),"
                   "topic_id VARCHAR(100),"
                   "terms VARCHAR(1000),"
                   "configuration VARCHAR(100))")
    
    cursor.execute("create table if not exists consultant_topics(id integer primary key autoincrement not null,"
                   "projectLaw VARCHAR(100),"
                   "topic_id VARCHAR(100),"
                   "topic VARCHAR(100),"
                   "topic_description VARCHAR(1000),"
                   "matConsultant VARCHAR(100),"
                   "dataAlteracao TIMESTAMP)")


    conn.commit()
    conn.close()


