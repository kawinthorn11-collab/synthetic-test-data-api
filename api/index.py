from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from faker import Faker
import random

app = FastAPI(
    title="Synthetic Test Data API", 
    description="Generate ultra-realistic mock data for developers, QA, and database testing. Supports multiple locales.", 
    version="1.2",
    contact={
        "name": "API Support",
        "url": "https://github.com/synthetic-test-data",
    }
)

# --- Pydantic Models for Automatic Swagger Documentation ---
class UserResponse(BaseModel):
    name: str = Field(..., example="John Doe")
    email: str = Field(..., example="john.doe@example.com")
    address: str = Field(..., example="123 Main St, Springfield, IL 62701")
    job: str = Field(..., example="Software Engineer")
    company: str = Field(..., example="Tech Corp")
    phone_number: str = Field(..., example="+1-555-555-5555")

class CreditCardResponse(BaseModel):
    provider: str = Field(..., example="VISA 16 digit")
    number: str = Field(..., example="4000123456789010")
    expire: str = Field(..., example="12/26")
    security_code: str = Field(..., example="123")

class CompanyResponse(BaseModel):
    company_name: str = Field(..., example="Globex Corporation")
    catch_phrase: str = Field(..., example="Synergistic management solutions")
    industry: str = Field(..., example="Manufacturing")

class EcommerceResponse(BaseModel):
    product_name: str = Field(..., example="Ergonomic Concrete Keyboard")
    price: float = Field(..., example=199.99)
    barcode: str = Field(..., example="1234567890123")

class CryptoResponse(BaseModel):
    currency: str = Field(..., example="Bitcoin")
    address: str = Field(..., example="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

# --- Endpoints ---

@app.get("/", tags=["General"])
def read_root():
    return {
        "status": "online",
        "message": "Welcome to the Synthetic Test Data API.",
        "docs_url": "/docs",
        "endpoints": [
            "/generate/user",
            "/generate/credit_card",
            "/generate/company",
            "/generate/ecommerce",
            "/generate/crypto",
            "/generate/uuid"
        ]
    }

@app.get("/users", tags=["Identity"])
def generate_user(
    locale: str = Query("en_US", description="Locale code (e.g., en_US, fr_FR, th_TH)"),
    count: int = Query(1, ge=1, le=100, description="Number of users to generate (max 100)")
):
    """Generate random synthetic user profiles. Supports localization."""
    try:
        Faker.seed() 
        local_fake = Faker(locale)
        results = []
        for _ in range(count):
            results.append({
                "name": local_fake.name(),
                "email": local_fake.email(),
                "address": local_fake.address(),
                "job": local_fake.job(),
                "company": local_fake.company(),
                "phone_number": local_fake.phone_number()
            })
        return {"count": len(results), "data": results}
    except AttributeError:
        raise HTTPException(status_code=400, detail=f"Unsupported locale: {locale}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/credit_cards", tags=["Finance"])
def generate_credit_card(count: int = Query(1, ge=1, le=100, description="Number to generate (max 100)")):
    """Generate realistic mock credit cards with provider, number, expiry, and CVV."""
    try:
        Faker.seed()
        fake = Faker()
        results = []
        for _ in range(count):
            results.append({
                "provider": fake.credit_card_provider(),
                "number": fake.credit_card_number(),
                "expire": fake.credit_card_expire(),
                "security_code": fake.credit_card_security_code()
            })
        return {"count": len(results), "data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/generate/company", tags=["Business"], response_model=CompanyResponse)
def generate_company(locale: str = Query("en_US", description="Locale code")):
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

@app.get("/generate/ecommerce", tags=["Commerce"], response_model=EcommerceResponse)
def generate_ecommerce():
    """Generate a synthetic e-commerce product."""
    try:
        Faker.seed()
        fake = Faker()
        adj = fake.word(ext_word_list=['Ergonomic', 'Rustic', 'Intelligent', 'Gorgeous', 'Sleek'])
        mat = fake.word(ext_word_list=['Steel', 'Wooden', 'Concrete', 'Plastic', 'Cotton'])
        prod = fake.word(ext_word_list=['Chair', 'Car', 'Computer', 'Keyboard', 'Mouse', 'Bike'])
        return EcommerceResponse(
            product_name=f"{adj} {mat} {prod}",
            price=round(random.uniform(5.0, 500.0), 2),
            barcode=fake.ean(length=13)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/generate/crypto", tags=["Finance"], response_model=CryptoResponse)
def generate_crypto():
    """Generate mock cryptocurrency addresses (BTC/ETH)."""
    try:
        Faker.seed()
        fake = Faker()
        coin = random.choice(["Bitcoin", "Ethereum"])
        # Fallback to standard hex generation if cryptocurrency provider isn't loaded in faker base
        address = "1" + "".join(random.choices("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz", k=33)) if coin == "Bitcoin" else "0x" + "".join(random.choices("0123456789abcdef", k=40))
        return CryptoResponse(
            currency=coin,
            address=address
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/generate/uuid", tags=["Developer Tools"])
def generate_uuid():
    """Generate a random UUIDv4 string for unique identifiers."""
    try:
        Faker.seed()
        return {"uuid": Faker().uuid4()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
