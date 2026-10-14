from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    from .models import Claim, ClaimReview, AuditLog
    from sqlalchemy import text

    Base.metadata.create_all(bind=engine)

    # Add ai_summary column if it doesn't exist
    with engine.connect() as conn:
        try:
            conn.execute(text("SELECT ai_summary FROM claims LIMIT 1"))
        except Exception:
            try:
                conn.execute(text("ALTER TABLE claims ADD COLUMN ai_summary TEXT"))
                conn.commit()
            except Exception as e:
                pass
