import datetime
import sqlite3
import pandas as pd
from flask import Flask, request

app = Flask(__name__)

def query_output(query, file='chinook.db'):
    conn = sqlite3.connect(file)
    query = query
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

@app.route('/invoices')
def sum_of_invoices():
    country = request.args.get('country', '')
    conn = sqlite3.connect('chinook.db')
    df = query_output(query='''
    SELECT 
        invoices.BillingCountry AS Country,
        SUM(invoices.Total) AS TotalSales
    FROM 
        invoices
    GROUP BY 
        invoices.BillingCountry
    ORDER BY 
        TotalSales DESC
    ''')
    if country in df.Country.values:
        return df.query(f'Country == "{country}"').to_html()
    else:
        return df.to_html()

@app.route('/track-info')
def track_info():
    track_id = request.args.get('track_id', '1')
    max_track = query_output(query='''
        SELECT MAX(TrackId) as max_trackid FROM tracks
        ''').max_trackid[0]
    if int(track_id) not in range (max_track+1):
        return f"Enter valid track_id (1-{max_track})"
    df = query_output(query=f'''
        SELECT 
            tracks.TrackId,
            tracks.Name AS TrackName,
            artists.Name AS ArtistName,
            albums.Title AS AlbumTitle,
            tracks.Composer,
            genres.Name AS Genre,
            media_types.Name AS MediaType,
            tracks.Milliseconds,
            tracks.Bytes,
            invoice_items.UnitPrice,
            COUNT(invoice_items.InvoiceLineId) AS TotalPurchases,
            SUM(invoice_items.UnitPrice) AS TotalRevenue
        FROM 
            tracks
            INNER JOIN albums ON tracks.AlbumId = albums.AlbumId
            INNER JOIN artists ON albums.ArtistId = artists.ArtistId
            INNER JOIN genres ON tracks.GenreId = genres.GenreId
            INNER JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
            INNER JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
        WHERE 
            tracks.TrackId = {track_id}
        GROUP BY 
            tracks.TrackId, tracks.Name, artists.Name, albums.Title, tracks.Composer, genres.Name, 
            media_types.Name, tracks.Milliseconds, tracks.Bytes, invoice_items.UnitPrice
        ''')
    df = pd.DataFrame({'Key': df.columns, 'Value': df.values.flatten()})
    return df.to_html()

@app.route('/total-duration')
def total_duration():
    duration_ms = query_output(query='''
            SELECT SUM(Milliseconds) as duration_ms FROM tracks
            ''').duration_ms[0]
    total_seconds = int(datetime.timedelta(milliseconds=int(duration_ms)).total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"Total duration of all tracks is {hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    app.run(debug=True)