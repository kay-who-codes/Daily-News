from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your actual News API key
NEWS_API_KEY = 'your_news_api_key_here'
NEWS_API_URL = 'https://newsapi.org/v2/everything'

@app.route('/')
def home():
    query = "UK Test"
    params = {
        'q': query,
        'apiKey': NEWS_API_KEY,
        'sortBy': 'publishedAt',
        'language': 'en'
    }
    
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()  # Raise error for bad responses
        news_data = response.json().get('articles', [])
    except requests.exceptions.RequestException as e:
        news_data = []
        print(f"Error fetching news: {e}")
    
    return render_template('home.html', news_data=news_data)

if __name__ == '__main__':
    app.run(debug=True)
