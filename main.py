from database import init_db, engine
from models import User, InformationPlug
from sqlmodel import Session

def run_app():
    init_db()
    with Session(engine) as session:
        # Your logic to handle user inputs or exchange info goes here
        print("Plugs Database is live.")

if __name__ == "__main__":
    run_app()