from sqlalchemy import Column, Engine, ForeignKey, Integer, MetaData, create_engine, Table, String, text, engine

engine = create_engine('sqlite:////:memory')

metadata_obj = MetaData()

# Criando as tabelas
user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),  # Instância obrigatória
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False)    # Instância obrigatória
)

user_prefs = Table(
    'user_prefs', metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False), # Instância obrigatória
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)

print("\nInfo da Tabela user_prefs")
print(user_prefs.primary_key)
print(user_prefs.constraints)
print("\n")
print(metadata_obj.tables)
print("\n")

for table in metadata_obj.sorted_tables:
    print(table)

# metadata_obj.create_all(engine)

metadata_bd_obj = MetaData()
financial_info = Table(
    'financial_info',
    metadata_bd_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False)    # Instância obrigatória
)

print("\nInfo da Tabela financial_info")
print(financial_info.primary_key)
print(financial_info.constraints)

# +++++++++++++++++++++++++++++++++++++++++++++++++
#               STATEMENT IN SQL
# +++++++++++++++++++++++++++++++++++++++++++++++++

# print("\n Executando Statement SQL")
# sql = text('select * from user')
# result = engine.execute(sql)
# for row in result:
#   print(row)

# print(engine.execute(sql))    # Diferente do ORM

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  + Column('user_id', Integer, primary_key=True),        +
#  + Column('user_name', String(40), nullable=False),     +
#  + Column('email_address', String(60)),                 +
#  + Column('nickname', String(50), nullable=False)       +
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Inserindo Informações na tabela User
#                                            id   Nome          Email          Nickname
# sql_insert = text('insert into user values(1, 'Gustavo', 'email@email.com', 'gu')")