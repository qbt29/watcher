from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select, and_, update, or_, insert
class SQL:
    def __init__(self):
        self.engine = create_engine("sqlite:///Users.db", echo=False)
        self.users_meta = MetaData(self.engine)
        self.db = Table("Users", self.users_meta, autoload=True)
    def get_petitions(self, id:int):
        con = self.engine.connect()
        s = select([self.db.c.petitions]).where(self.db.c.id==id)
        s = con.execute(s).fetchone()
        con.close()
        return s
    def get_signs(self, id:int):
        con = self.engine.connect()
        s = select([self.db.c.signs]).where(self.db.c.id == id)
        s = con.execute(s).fetchone()
        con.close()
        return s
    def get_status(self, id:int)->str:
        con = self.engine.connect()
        s = select([self.db.c.status]).where(self.db.c.id == id)
        s = con.execute(s).fetchone()
        con.close()
        return s
    def get_kicks(self, id:int)->int:
        con = self.engine.connect()
        s = select([self.db.c.kicks]).where(self.db.c.id == id)
        s = con.execute(s).fetchone()
        con.close()
        return s
    def get_user(self, id:int)->dict:
        user={}
        user['id'] = id
        user['kicks'] = self.get_kicks(id)
        user['signs'] = self.get_signs(id)
        user['petitions'] = self.get_petitions(id)
        return user
    def kick(self, id:int):
        con = self.engine.connect()
        s = update(self.db).values(petitions=[], result="кикнут", kicks=self.get_kicks(id)+1).where(self.db.c.id==id)
        con.execute(s)
        con.close()
    def insert(self, id:int):
        con = self.engine.connect()
        ins = insert(self.db).values(id=id)
        con.execute(ins)
        con.close()
    def increase(self, id:int, who:int):
        con = self.engine.connect()
        s = select([self.db.c.petitions]).where(self.db.c.id == id)
        s:list = con.execute(s).fetchone()
        if who not in s:
            s.append(who)
            upd = [update(self.db).values(id=id, petitions=s).where(self.db.c.id==id), update(self.db).values(id=who, signs=self.get_signs(who) + [id]).where(self.db.c.id==who)]
            con.execute(upd)
        con.close()
        return len(s)