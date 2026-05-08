# Synthetic Test Data API

A fully functional, zero-cost REST API for generating realistic mock data (users, credit cards, etc.) intended for software testing and QA. Built with FastAPI and Python Faker.

## Features
- **Zero Cost**: Built entirely on MIT-licensed open-source libraries.
- **Fast**: Built on FastAPI.
- **Localization**: Supports multiple locales (e.g., `en_US`, `th_TH`, `es_ES`).
- **Deployable**: Pre-configured for free Vercel serverless deployment.

## Endpoints
- `GET /` - API Status
- `GET /generate/user?locale=en_US` - Generate a synthetic user profile.
- `GET /generate/credit_card` - Generate synthetic credit card details.
- `GET /docs` - Interactive Swagger API documentation.

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
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to see the interactive UI.

## Free Deployment (Vercel)
This project includes a `vercel.json` file. To deploy for free:
1. Push this folder to a GitHub repository.
2. Sign in to Vercel (vercel.com) using your GitHub account.
3. Import the repository. Vercel will automatically detect the Python configuration and deploy it for free.