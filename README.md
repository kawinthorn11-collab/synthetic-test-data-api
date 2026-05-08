# Synthetic Test Data API

A fully functional, zero-cost REST API for generating realistic mock data. Designed to help developers, QA testers, and database administrators instantly populate their apps with safe, non-PII data.

## Live API

This project is available on RapidAPI with a free tier:

[Use the Synthetic Test Data API on RapidAPI](https://rapidapi.com/kawinthorn11collab/api/synthetic-test-data-api)

Live backend:

```text
https://synthetic-test-data-api.vercel.app
```

Core endpoints:

```text
GET /generate/user
GET /generate/credit_card
GET /credit_cards?count=10
GET /generate/company
GET /generate/ecommerce
GET /generate/crypto
GET /generate/uuid
```

## Features
- **Zero Cost**: Built entirely on MIT-licensed open-source libraries (FastAPI, Python Faker).
- **Interactive Docs**: Auto-generated Swagger UI for easy endpoint testing.
- **Localization**: Supports multiple locales (e.g., `en_US`, `th_TH`, `es_ES`, `ja_JP`) via query parameters.
- **Production Ready**: Configured for immediate serverless deployment on Vercel.

## Endpoints
- `GET /` - API Status & Routes
- `GET /generate/user?locale=en_US` - User profiles (Name, Email, Job, Address, Phone)
- `GET /generate/credit_card` - Credit card details (Provider, Number, Expiry, CVV)
- `GET /generate/company?locale=en_US` - Company details (Name, Catchphrase, Industry)
- `GET /generate/ecommerce` - Product details (Name, Price, EAN-13 Barcode)
- `GET /generate/crypto` - Cryptocurrency addresses (BTC/ETH)
- `GET /generate/uuid` - Standard UUIDv4 identifiers

## Local Execution Instructions

1. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server locally:**
   ```bash
   uvicorn api.index:app --reload
   ```

3. **Test the API:**
   Navigate to `http://127.0.0.1:8000/docs` in your browser.

## Deployment
See the `DEPLOYMENT_GUIDE.md` file for step-by-step instructions on deploying this to Vercel for free and monetizing it on RapidAPI.
