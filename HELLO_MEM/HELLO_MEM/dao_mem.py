import pymysql
from _ast import If

class DaoMem:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='python',
                       db='python', port=3304, charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def selectList(self):
        sql = """
        select * from mem
        """
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list
    
    
    def selectOne(self, m_id):
        sql = f"""
        SELECT 
            m_id,
            m_nm,
            tel,
            addr
        FROM mem
        WHERE 
            m_id = '{m_id}'
        """
        self.curs.execute(sql)
    
        list = self.curs.fetchall()
        return list[0]
    
    
    def insert(self, m_id, m_nm, tel, addr):
        sql = f"""
            INSERT INTO mem
                (m_id, m_nm, tel, addr)  
            VALUES 
                ('{m_id}', '{m_nm}', '{tel}', '{addr}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
    
        return cnt
    
    
    def update(self, m_id, m_nm, tel, addr):
        sql = f"""
            UPDATE mem
            SET 
                m_nm = '{m_nm}', 
                tel = '{tel}', 
                addr = '{addr}'
            WHERE 
                m_id = '{m_id}'
        """
    
        cnt = self.curs.execute(sql)
        self.conn.commit()
    
        return cnt
    
    
    def delete(self, m_id):
        sql = f"""
            DELETE FROM mem
            WHERE 
                m_id = {m_id}
        """
    
        cnt = self.curs.execute(sql)
        self.conn.commit()
    
        return cnt


    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__=='__main__':
    de = DaoMem()
    cnt = de.insert('2','2','2','2')
    print(cnt)
