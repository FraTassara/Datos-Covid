
import pandas as pd

for i in range(N_DIAS):
fecha = (datetime.datetime.strptime(FECHA_INI,'%Y-%m-%d')+datetime.timedelta(days=i)).strftime("%Y-%m-%d")
print(fecha)
