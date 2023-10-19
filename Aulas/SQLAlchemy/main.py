from pickle import TRUE
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    
    # Atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    # Relacionamento
    adress = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"

class Adress(Base):
    __tablename__ = "address"

    # Atributos
    id = Column(Integer, primary_key=True)
    email_address = Column(String(40), nullable=False)                           # Obrigatório
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)     # Obrigatório

    user = relationship("User", back_populates="address")
    
    def __repr__(self):
        return f"Address (id={self.id}, email={self.email_address})"

print(User.__tablename__)
print(User.__table__)
