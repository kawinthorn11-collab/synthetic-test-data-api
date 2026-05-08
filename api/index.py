from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from faker import Faker

app = FastAPI(
    title="Synthetic Test Data API", 
    description="Generate realistic mock data for testing (Users, Credit Cards, Companies, etc.).", 
    version="1.1"
)

# --- Pydantic Models for Automatic Swagger Documentation ---
class UserResponse(BaseModel):
    name: str
    email: str
    address: str
    job: str
    company: str
    phone_number: str

class CreditCardResponse(BaseModel):
    provider: str
    number: str
    expire: str
    security_code: str

class CompanyResponse(BaseModel):
    company_name: str
    catch_phrase: str
    industry: str

# --- Endpoints ---

@app.get("/", tags=["General"])
def read_root():
    return {
        "status": "online",
        "message": "Welcome to the Synthetic Test Data API.",
        "docs": "/docs",
        "endpoints": [
            "/generate/user",
            "/generate/credit_card",
            "/generate/company",
            "/generate/uuid"
        ]
    }

@app.get("/generate/user", tags=["Mock Data"], response_model=UserResponse)
def generate_user(locale: str = "en_US"):
    """Generate a random synthetic user profile. Supports multiple locales (e.g., en_US, fr_FR, th_TH)."""
    try:
        Faker.seed() 
        local_fake = Faker(locale)
        return UserResponse(
            name=local_fake.name(),
            email=local_fake.email(),
            address=local_fake.address(),
            job=local_fake.job(),
            company=local_fake.company(),
            phone_number=local_fake.phone_number()
        )
    except AttributeError:
        raise HTTPException(status_code=400, detail=f"Unsupported locale: {locale}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/generate/credit_card", tags=["Mock Data"], response_model=CreditCardResponse)
def generate_credit_card():
    """Generate a realistic mock credit card with provider, number, expiry, and CVV."""
    try:
        Faker.seed()
        fake = Faker()
        return CreditCardResponse(
            provider=fake.credit_card_provider(),
            number=fake.credit_card_number(),
            expire=fake.credit_card_expire(),
            security_code=fake.credit_card_security_code()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/generate/company", tags=["Mock Data"], response_model=CompanyResponse)
def generate_company(locale: str = "en_US"):
    """Generate a synthetic company profile including a catchphrase and industry."""
    try:
        Faker.seed()
        fake = Faker(locale)
        return CompanyResponse(
            company_name=fake.company(),
            catch_phrase=fake.catch_phrase(),
            industry=fake.job()
        )
    except AttributeError:
        raise HTTPException(status_code=400, detail=f"Unsupported locale: {locale}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/generate/uuid", tags=["Mock Data"])
def generate_uuid():
    """Generate a random UUIDv4 string for unique identifiers."""
    try:
        Faker.seed()
        return {"uuid": Faker().uuid4()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
