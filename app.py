from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re
from urllib.parse import urlparse

app = Flask(__name__)
CORS(app)

# Load your saved model
model = joblib.load('rf_model.pkl')

def extract_features(url):
    features = {}
    features['url_length'] = len(url)
    features['count_dots'] = url.count('.')
    features['count_hyphens'] = url.count('-')
    features['has_at_symbol'] = 1 if '@' in url else 0

    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    features['has_ip'] = 1 if re.search(ip_pattern, url) else 0

    features['has_https'] = 1 if url.startswith('https') else 0

    suspicious_words = ['login', 'verify', 'secure', 'account', 'update', 'confirm', 'banking', 'signin']
    url_lower = url.lower()
    features['suspicious_word_count'] = sum(1 for word in suspicious_words if word in url_lower)

    shortening_services = ['bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly', 'is.gd', 'buff.ly']
    features['is_shortened'] = 1 if any(service in url for service in shortening_services) else 0

    try:
        domain = urlparse(url).netloc
        features['subdomain_count'] = domain.count('.')
    except:
        features['subdomain_count'] = 0

    return [features['url_length'], features['count_dots'], features['count_hyphens'],
            features['has_at_symbol'], features['has_ip'], features['has_https'],
            features['suspicious_word_count'], features['is_shortened'], features['subdomain_count']]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data['url']

    features = extract_features(url)
    prediction = model.predict([features])[0]
    probability = model.predict_proba([features])[0]

    result = 'Phishing' if prediction == 1 else 'Legitimate'
    confidence = max(probability)

    return jsonify({
        'url': url,
        'prediction': result,
        'confidence': round(float(confidence), 4)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)