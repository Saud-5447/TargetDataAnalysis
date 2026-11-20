import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
password = "root"
engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/ecom"
)
list_csvs=[
    ('customers','customers.csv'),
    ('geolocation','geolocation.csv'),
    ('order_items','order_items.csv'),
    ('orders','orders.csv'),
    ('payments','payments.csv'),
    ('products','products.csv'),
    ('sellers','sellers.csv')
]

for table,file in list_csvs:
    filePath=f'./files/{file}'
    df = pd.read_csv(filePath)
    df.to_sql(
        name = table,
        con = engine,
        if_exists = 'replace',
        index = False
    )

    print(f"Imported {file} successfully into {table}")
engine.dispose()