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
