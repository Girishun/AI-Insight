import requests
from datetime import datetime, timedelta
import google.generativeai as genai
from config import FINNHUB_API_KEY, GOOGLE_API_KEY
from database import get_connection, create_tables

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

def fetch_news(symbol):
    to_date = datetime.now().date()
    from_date = to_date - timedelta(days=5)
    url = f"https://finnhub.io/api/v1/company-news?symbol={symbol}&from={from_date}&to={to_date}&token={FINNHUB_API_KEY}"
    return requests.get(url).json()

def save_news(news, symbol):
    conn = get_connection()
    cur = conn.cursor()
    for item in news:
        cur.execute("""
            INSERT INTO company_news (headline, summary, url, source, datetime, symbol)
            VALUES (%s, %s, %s, %s, to_timestamp(%s), %s)
        """, (
            item.get("headline"),
            item.get("summary", ""),
            item.get("url"),
            item.get("source"),
            item.get("datetime") / 1000,
            symbol
        ))
    conn.commit()
    cur.close()
    conn.close()

def summarize(news, symbol):
    content = "\n".join([f"{i+1}. {n['headline']} - {n['summary']}" for i, n in enumerate(news[:5])])
    prompt = f"Summarize and give market insight for {symbol} from recent news:\n\n{content}"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

def save_insight(text, symbol):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO insights (insight_text, related_symbol) VALUES (%s, %s)", (text, symbol))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_tables()
    symbol = "AAPL"
    news = fetch_news(symbol)
    save_news(news, symbol)
    insight = summarize(news, symbol)
    save_insight(insight, symbol)
    print("\n🧠 Market Insight:\n", insight)
