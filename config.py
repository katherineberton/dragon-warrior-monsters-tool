from dotenv import load_dotenv
import os

# Load environment variables from a .env file if present
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

TORTOISE_ORM = {
    "connections": {
        "default": DATABASE_URL
    },
    "apps": {
        "monsters": {
            "models": ["monsters.models", "aerich.models"],
            "default_connection": "default",
        },
        "gates": {
            "models": ["gates.models", "aerich.models"],
            "default_connection": "default",
        },
        "skills": {
            "models": ["skills.models", "aerich.models"],
            "default_connection": "default",
        },
        "breeding": {
            "models": ["breeding.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}