import psycopg2
from config import DATABASE_URL

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def create_tables():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS company_news (
                    id SERIAL PRIMARY KEY,
                    headline TEXT,
                    summary TEXT,
                    url TEXT,
                    source TEXT,
                    datetime TIMESTAMP,
                    symbol TEXT,
                    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS insights (
                    id SERIAL PRIMARY KEY,
                    insight_text TEXT,
                    related_symbol TEXT,
                    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
        conn.commit()
