import pymysql
from _ast import If

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='python',
                       db='python', port=3304, charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def selectList(self):
        sql = """
        select * from emp
        """
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list
    
    
    def selectOne(self, e_id):
        sql = f"""
        SELECT 
            e_id,
            e_name,
            gen,
            addr
        FROM emp 
        WHERE 
            e_id = '{e_id}'
        """
        self.curs.execute(sql)
    
        list = self.curs.fetchall()
        return list[0]
    
    
    def insert(self, e_id, e_name, gen, addr):
        sql = f"""
            INSERT INTO emp 
                (e_id, e_name, gen, addr)  
            VALUES 
                ('{e_id}', '{e_name}', '{gen}', '{addr}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
    
        return cnt
    
    
    def update(self, e_id, e_name, gen, addr):
        sql = f"""
            UPDATE emp
            SET 
                e_name = '{e_name}', 
                gen = '{gen}', 
                addr = '{addr}'
            WHERE 
                e_id = '{e_id}'
        """
        print("sql",sql)
    
        cnt = self.curs.execute(sql)
        self.conn.commit()
    
        return cnt
    
    
    def delete(self, e_id):
        sql = f"""
            DELETE FROM emp
            WHERE 
                e_id = '{e_id}'
        """
    
        cnt = self.curs.execute(sql)
        self.conn.commit()
    
        return cnt


    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__=='__main__':
    de = DaoEmp()
    cnt = de.insert('2','2','2','2')
    print(cnt)
