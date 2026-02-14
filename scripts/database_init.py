import duckdb
from loguru import logger

DB_PATH = "warehouse.duckdb"

def main():
    with duckdb.connect(DB_PATH) as con:
        con.execute("CREATE SCHEMA IF NOT EXISTS raw")

        con.execute("""
            CREATE TABLE IF NOT EXISTS raw.people (
                person_id VARCHAR,
                first_name VARCHAR,
                age INTEGER,
                language VARCHAR,
                current_region INTEGER,
                household_id VARCHAR,
                family_name VARCHAR
            )
        """)

        con.execute("""
            CREATE TABLE IF NOT EXISTS raw.regions (
                Region_ID INTEGER,
                Ancient_Name VARCHAR,
                Current_Faction VARCHAR,
                Era_Tag VARCHAR,
                Full_Name VARCHAR,
                Colloquial_Name VARCHAR,
                Founding_Era VARCHAR,
                Density_Tier VARCHAR,
                Capital VARCHAR,
                Primary_Industry VARCHAR,
                Founding_Story VARCHAR,
                Vote_History_Last3 VARCHAR,
                Key_Pressure_Points VARCHAR,
                Unbound_Presence VARCHAR
            )
        """)

        logger.info("Schema 'raw' and tables 'people', 'regions' created.")

if __name__ == "__main__":
    main()
