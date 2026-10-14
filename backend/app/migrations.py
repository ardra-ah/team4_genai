"""Database migrations - add missing columns"""
from sqlalchemy import text
from .database import engine

def migrate_add_ai_summary():
    """Add ai_summary column to claims table if it doesn't exist"""
    with engine.connect() as conn:
        # Check if column exists
        try:
            conn.execute(text("SELECT ai_summary FROM claims LIMIT 1"))
            print("✓ ai_summary column already exists")
        except Exception:
            # Column doesn't exist, add it
            try:
                conn.execute(text("ALTER TABLE claims ADD COLUMN ai_summary TEXT"))
                conn.commit()
                print("✓ Added ai_summary column to claims table")
            except Exception as e:
                print(f"✗ Error adding ai_summary column: {e}")

def run_migrations():
    """Run all migrations"""
    print("Running database migrations...")
    migrate_add_ai_summary()
    print("Migrations complete!")
