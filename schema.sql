-- For manual PostgreSQL setup
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

CREATE TABLE IF NOT EXISTS insights (
    id SERIAL PRIMARY KEY,
    insight_text TEXT,
    related_symbol TEXT,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
