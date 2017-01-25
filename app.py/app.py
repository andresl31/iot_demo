import web
import pymysql
import pyfirmata 
from time import sleep
import os

urls=(
    '/','Arduino'    
)

app = web.application(urls, globals())
render = web.template.render('Templates',base='base')

class Arduino:
   
    def GET(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='12345', db='arduino')
        cur = conn.cursor()
        cur.execute("SELECT * FROM data WHERE id=1")
        values = ''
        for row in cur:
            print(row)
            print row[0], "id"
            print row[1], "update"
            print row[2], "value"
            values=row[2],' - fecha: ',row[1]
        cur.close()
        conn.close()
        #print values,' -gfjh'      
        #return render.index(values)
        arr = [1,2,3]
        return values

if __name__=='__main__':
    web.config.debug= True
    app.run()






