import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, Table , MetaData

metadata = MetaData()


#Session = sessionmaker(bind=engine)



#hostname = 'echo.db.elephantsql.com'
#username = 'mlwqkqui'
#password = 'snbVGjtG2F_Oa5FY476S7WTllbx--Lr2'
#database = 'mlwqkqui'

#mySQLConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
def getCustomerDetails(id):
    DATABASE_URI = 'postgres+psycopg2://mlwqkqui:snbVGjtG2F_Oa5FY476S7WTllbx--Lr2@echo.db.elephantsql.com:5432/mlwqkqui'
    engine=create_engine(DATABASE_URI)
    #print(engine.table_names())
    connection=engine.connect()
    loans = Table('loans', metadata, autoload=True, autoload_with=engine)
    stmt=select([loans])
    stmt=stmt.where(loans.columns.loan_id == id)
    results = connection.execute(stmt).fetchall()
    print(results)
    connection.close()
#Session = sessionmaker(bind=engine)
#s = Session()
#s.query(mlwqkqui.loans).first()
#census = Table('loans', metadata, autoload=True, autoload_with=engine)
#stmt=select([census])

#results = mySQLConnection.execute(stmt)
#print(results)
#s.close()
    ##cursor.close()
    #mySQLConnection.close()


getCustomerDetails('1')