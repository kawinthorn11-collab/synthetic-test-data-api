from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from faker import Faker

app = FastAPI(
    title="Synthetic Test Data API", 
    description="Generate realistic mock data for testing (Users, Credit Cards, etc.).", 
    version="1.0"
)

# Root endpoint
@app.get("/", tags=["General"])
def read_root():
    return {
        "status": "online",
        "message": "Welcome to the Synthetic Test Data API.",
        "docs": "/docs",
        "endpoints": ["/generate/user", "/generate/credit_card"]
    }

# User generation endpoint
@app.get("/generate/user", tags=["Mock Data"])
def generate_user(locale: str = "en_US"):
    try:
        Faker.seed() # Ensure randomness per call
        local_fake = Faker(locale)
        return JSONResponse(content={
            "name": local_fake.name(),
            "email": local_fake.email(),
            "address": local_fake.address(),
            "job": local_fake.job(),
            "company": local_fake.company(),
            "phone_number": local_fake.phone_number()
        })
    except AttributeError:
        raise HTTPException(status_code=400, detail=f"Unsupported locale: {locale}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Credit card generation endpoint
@app.get("/generate/credit_card", tags=["Mock Data"])
def generate_credit_card():
    try:
        Faker.seed()
        fake = Faker()
        return JSONResponse(content={
            "provider": fake.credit_card_provider(),
            "number": fake.credit_card_number(),
            "expire": fake.credit_card_expire(),
            "security_code": fake.credit_card_security_code()
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
