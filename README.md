# 🛡️ PhishGuard AI — Phishing URL Detector

A machine learning system that analyzes a URL's structure and predicts whether it's likely phishing or legitimate — built end-to-end from raw data to a live API and web interface.

## What it does

You enter a URL, and the system extracts 9 structural features from the text (no need to visit the actual site), passes them to a trained ML model, and returns a prediction with a confidence score.

## Why I built this

Phishing remains one of the most common ways attackers steal credentials and money. I wanted to understand, hands-on, how far you can get at detecting phishing using *only* the structure of a URL — no domain reputation lookups, no visiting the page — and to build a complete pipeline from raw data to a deployed, usable tool.

## Features engineered from each URL

- URL length
- Count of dots and hyphens
- Presence of `@` symbol
- IP address used instead of a domain
- HTTPS vs HTTP
- Count of suspicious keywords (login, verify, secure, etc.)
- Whether a URL shortener was used
- Subdomain count

## Models trained and compared

| Model | Accuracy |
|---|---|
| Logistic Regression | [add your number] |
| Random Forest | [add your number] |
| XGBoost | 0.8054 |

Random Forest was selected for the deployed API.

## Tech stack

Python, scikit-learn, XGBoost, pandas, NumPy, Flask, Render (backend hosting), Vercel (frontend hosting), HTML/CSS/JS.

## Live demo

- Frontend: https://phishing-detector-87s9.vercel.app
- Backend API: https://phishing-detector-api-kyrr.onrender.com

## How to run locally
git clone https://github.com/prathikshaganiyar/phishing-detector.git
cd phishing-detector
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
Then open `index.html` in your browser.

## Known limitations (found through real testing)

Testing the deployed model against well-known legitimate sites (google.com, amazon.com, wikipedia.org) revealed it frequently misclassifies them as phishing with high confidence (75-100%).

Initial investigation pointed to `url_length` as the cause, but retraining a version of the model without that feature entirely did not fix the issue — `google.com` was still classified as phishing with 100% confidence. This showed the bias was deeper than a single feature.

Digging into the training data directly, I found the root cause: legitimate URLs in the training set average a `subdomain_count` of essentially 0.000, meaning the dataset's legitimate examples almost never include a "www." prefix or any subdomain. Since real-world legitimate sites are very commonly accessed as "www.example.com", this creates a mismatch — the model correctly learned the pattern present in its training data, but that pattern doesn't reflect real-world URL conventions, causing it to flag common, harmless "www." URLs as suspicious.

This is a dataset construction limitation rather than a flaw in the model or feature engineering: the "legitimate" class in the source dataset likely excluded or stripped "www." subdomains during collection, while the "phishing" class did not undergo the same normalization.

## Future improvements

- Normalize/strip "www." consistently across both classes during preprocessing, or explicitly test whether this feature should be excluded
- Incorporate domain age / WHOIS reputation data
- Add page content analysis, not just URL structure
- Rebalance or re-collect training data with more representative, real-world legitimate URL examples
- Try a different confidence threshold instead of the default 50%

## Disclaimer

Built for educational purposes. Predictions should not be treated as a definitive security verdict.
