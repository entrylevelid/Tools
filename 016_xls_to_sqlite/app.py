# =============================================
#  Entry Level ID
# =============================================

import pandas as pd
import sqlite3

excel_file = 'ip_address.xlsx'
df = pd.read_excel(excel_file, sheet_name='ip_address')

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

table_name = 'data'
df.to_sql(table_name, conn, if_exists='replace', index=False)

conn.close()

print("Data has been successfully saved to the SQLite database.")