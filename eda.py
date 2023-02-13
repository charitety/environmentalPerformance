from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pandas as pd
from config import epiForEngine
from config import HDI

#preparing connection with database using the 'create_engine'
engine = create_engine(epiForEngine)

#mapping the database into a Python class
base = automap_base()

#getting db into automapper
base.prepare(engine, reflect=True)

#disposing engine
engine.dispose()

#reading the HDI dataset from code saved in config and importing it to Postgres 
df = HDI
"""df.to_sql("HDI", engine)
table_name = "HDI"
df.to_sql(table_name, engine, if_exists='replace', index=False)
"""
#saving classes as variables, prepare classes
EPIcountry = base.classes.epi_country
HDI = base.classes.HDI

#querying the database 
session = Session(engine)
print(HDI.head())

"""resultsEPI = session.query(EPIcountry.country, EPIcountry.air_h, EPIcountry.population07, EPIcountry.water_h, EPIcountry.biodiversity, EPIcountry.fisheries, EPIcountry.geo_subregion).all()

GDPcountry = session.query(GDP.country, GDP.subject, GDP.value)
rowsGDP = GDPcountry.all()

GDPdf = pd.DataFrame(rowsGDP, columns=['country', 'subject', 'value'])

EPIdf = pd.DataFrame(resultsEPI, columns=['country', 'air_h', 'population07', 'water_h', 'biodiversity', 'fisheries', 'geo_subregion'])

GDPdf["subject"] == "Gross Domestic Product (GDP); millions"

GDPmill = GDPdf.groupby("subject").get_group("Gross Domestic Product (GDP); millions")

#joining EPIdf  and GDPmill on country
GDPEPI = GDPmill.merge(EPIdf, how="left", on="country")

GDPEPI.dropna(inplace=True)

GDPEPI.head(10)

# sort by GDP 
GDPsorted = GDPEPI.sort_values(by="value", ascending=False)

# plot bar plot
GDPsorted.head(10).plot.bar(x="country", y="value")

# sort by GDP 
waterSorted = GDPEPI.sort_values(by="water_h", ascending=False)

# plot bar plot
waterSorted.head(10).plot.bar(x="country", y="water_h")

GDPEPI.plot.scatter(x='value',y='water_h')

GDPEPI.plot.scatter(x='value',y='biodiversity')

GDPEPI.plot.scatter(x='value',y='population07')

# disposing the engine
engine.dispose()
"""