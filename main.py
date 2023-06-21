import math
import sqlite3
import pandas as pd
from flask import Flask, request

# Створити клас Circle(x,y,radius). Додати метод contains.
#  Цей метод приймає екземпляр класу Point(x,y). Цей метод має повертати
#  True or False. Якшо точка в колі то True якшо поза колом то False.

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point):
        distance = math.sqrt((point['x'] - self.x) ** 2 + (point['y'] - self.y) ** 2)
        if distance <= self.radius:
            return True
        else:
            return False

a = Circle(1, 1, 12)
point_true = {'x': 3, 'y': 0}
point_false = {'x': 34, 'y': -2}
print(a.contains(point_true)) #True
print(a.contains(point_false)) #False

# 2. Створити view яка на вхід приймає стиль музики. Має вивести місто
# в якому найбільше слухають цей стиль музики. Якшо жанра немає вивести повідомлення.
# genre - обов'язковий параметер.
# /stats_by_city?genre=HipHop

app = Flask(__name__)

def query_output(query, file='chinook.db'):
    conn = sqlite3.connect(file)
    query = query
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

@app.route('/stats-by-city')
def stats_by_city():
    genre = request.args.get('genre', '')
    if not genre:
        return "Please provide a genre parameter."

    query = f"""
            SELECT 
                invoices.BillingCity,
                genres.Name AS Genre,
                COUNT(*) AS UsageCount
            FROM 
                invoices
                INNER JOIN invoice_items ON invoice_items.InvoiceId = invoices.InvoiceId
                INNER JOIN tracks ON tracks.TrackId = invoice_items.TrackId
                INNER JOIN genres ON tracks.GenreId = genres.GenreId
            WHERE
                genres.Name like '{genre}%'
            GROUP BY
                invoices.BillingCity, genres.Name
            ORDER BY
                UsageCount DESC
            LIMIT 1

            """

    df = query_output(query, file='chinook.db')

    return f"The city with the highest purchases for genre '{df.Genre[0]}' is {df.BillingCity[0]}. Total purchases: {df.UsageCount[0]}."

if __name__ == '__main__':
    app.run()