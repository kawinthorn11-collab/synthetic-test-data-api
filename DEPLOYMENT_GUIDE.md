# Deployment & Monetization Guide

Follow these exact steps to deploy the Synthetic Test Data API for free and list it on RapidAPI for monetization.

---

## 1. Push to GitHub (Requires your account)
Since you need to connect your GitHub account to Vercel, the code must live in your GitHub account.

1. Go to [GitHub.com/new](https://github.com/new) and log in.
2. Create a new repository named: `synthetic-test-data-api`
3. Set visibility to **Public** (required for Vercel's free tier).
4. Do NOT check "Add a README" (we already have one).
5. Open your terminal, paste the following commands, and hit Enter:

```powershell
cd C:\Users\kawinthorn11\Desktop\AssetScanner\synthetic_data_api
git remote add origin https://github.com/YOUR-GITHUB-USERNAME/synthetic-test-data-api.git
git branch -M main
git push -u origin main
```

*(Note: If prompted, log into GitHub via the terminal popup.)*

---

## 2. Deploy to Vercel (Free Hosting)
1. Go to [Vercel.com](https://vercel.com) and log in with your GitHub account.
2. Click **Add New...** -> **Project**.
3. You will see `synthetic-test-data-api` in the list of your GitHub repositories. Click **Import**.
4. Leave all settings exactly as they are (Vercel automatically reads our `vercel.json`).
5. Click **Deploy**.
6. Wait ~60 seconds. Vercel will provide you with a live URL (e.g., `https://synthetic-test-data-api.vercel.app`).

**Troubleshooting Vercel:**
- *Error: "Python 3.x not found"*: This won't happen because we pinned `fastapi` and `uvicorn` in `requirements.txt` and used the official `@vercel/python` builder in `vercel.json`.
- *Error: 404 on all routes*: Ensure the root `vercel.json` file was pushed to GitHub correctly.

---

## 3. Monetize on RapidAPI
1. Go to [RapidAPI Studio](https://rapidapi.com/hub) and log in.
2. Click **Add New API**.
3. **Name**: `Synthetic Test Data API`
4. **Description**: Open `RAPID_API_LISTING.md` and paste the contents here.
5. **Base URL**: Paste the URL you got from Vercel in Step 2.
6. **Endpoints**:
   - Manually add a GET route for `/generate/user`
   - Manually add a GET route for `/generate/credit_card`
   - Manually add a GET route for `/generate/company`
   - Manually add a GET route for `/generate/ecommerce`
   - Manually add a GET route for `/generate/crypto`
   - Manually add a GET route for `/generate/uuid`
7. **Monetize Tab**:
   - Open `MONETIZATION_PLAN.md` and set up the Free, Pro ($9), and Ultra ($29) tiers exactly as outlined.
8. Click **Make API Public**.

You are now earning passive income every time a developer subscribes to your Pro or Ultra tier.