from sqlalchemy import Column, Integer, Boolean, Text
from database import Base


class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(Text)
    note = Column(Text)
    created_date = Column(Date)
    due_date = Column(Date)
    
    def __repr__(self):
        return '<Todo %r>' % (self.id)
