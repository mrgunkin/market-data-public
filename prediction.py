import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

def get_bitcoin_february_report():
    # Получаем текущий год
    current_year = datetime.now().year
    
    # Создаем объект для биткоина (BTC-USD)
    btc = yf.Ticker("BTC-USD")
    
    # Получаем данные за последние 10 лет
    start_date = datetime(current_year - 10, 1, 1)
    end_date = datetime.now()
    data = btc.history(start=start_date, end=end_date, interval="1mo")
    
    # Фильтруем данные только для февраля
    february_data = data[data.index.month == 2]
    
    print(f"Анализ данных по биткоину за февраль каждого года ( последние 10 лет ):\n")
    
    for index, row in february_data.iterrows():
        year = index.year
        open_price = row['Open']
        close_price = row['Close']
        high_price = row['High']
        low_price = row['Low']
        volume = row['Volume']
        
        # Вычисляем процентное изменение
        price_change = ((close_price - open_price) / open_price) * 100
        
        # Определяем направление движения
        trend = "рост" if close_price > open_price else "падение"
        
        print(f"Февраль {year}:")
        print(f"Цена открытия: ${open_price:,.2f}")
        print(f"Цена закрытия: ${close_price:,.2f}")
        print(f"Максимум: ${high_price:,.2f}")
        print(f"Минимум: ${low_price:,.2f}")
        print(f"Объем торгов: {volume:,.0f}")
        print(f"Изменение: {price_change:+.2f}% ({trend})")
        print("-" * 50)

def main():
    try:
        print("Получаем данные о биткоине...")
        get_bitcoin_february_report()
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        print("Проверьте подключение к интернету и попробуйте снова.")

if __name__ == "__main__":
    main()
