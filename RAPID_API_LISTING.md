# Synthetic Test Data API (RapidAPI Listing Draft)

## Name
Synthetic Test Data API (Fast & Localized)

## Description
Stop hardcoding test data. The Synthetic Test Data API provides ultra-fast, randomized mock data for developers, QA testers, and database administrators. Instantly generate realistic user profiles, localized names, addresses, credit cards, companies, and UUIDs to populate your applications safely without exposing real PII (Personally Identifiable Information).

## Features
- **Multi-Language Support**: Generate data in specific locales by passing the `?locale=` query parameter (e.g., `en_US`, `th_TH`, `ja_JP`).
- **RESTful Architecture**: Simple, fast GET requests.
- **Enterprise-Ready Mocking**: Includes full credit card mock-ups, company catchphrases, and accurate job titles.
- **No Setup Required**: Plugs directly into your test suites, Postman, or frontend prototypes.

## Category
Testing / Data / Developer Tools

## Endpoints Include
- `GET /generate/user`
- `GET /generate/credit_card`
- `GET /generate/company`
- `GET /generate/uuid`
