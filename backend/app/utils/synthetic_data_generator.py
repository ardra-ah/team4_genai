import random
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

# Sample data for generating realistic synthetic claims
PATIENT_FIRST_NAMES = ['John', 'Mary', 'Robert', 'Patricia', 'Michael', 'Jennifer', 'David', 'Linda', 'James', 'Barbara']
PATIENT_LAST_NAMES = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']

PROVIDERS = ['City Medical Center', 'Riverside Hospital', 'Memorial Care', 'Health Plus Clinic', 'St. Mary Medical', 'Central Hospital', 'Wellness Medical Group']

PROCEDURES = [
    'General Physical Exam',
    'Complete Blood Work',
    'X-Ray (Chest)',
    'MRI (Head)',
    'CT Scan (Abdomen)',
    'Ultrasound (Abdomen)',
    'EKG',
    'Orthopedic Consultation',
    'Dental Cleaning',
    'Routine Vaccination'
]

DIAGNOSES = [
    'Hypertension',
    'Type 2 Diabetes',
    'Hyperlipidemia',
    'Arthritis',
    'Influenza',
    'Common Cold',
    'Bronchitis',
    'Gastritis',
    'Migraine',
    'Back Pain'
]

class SyntheticDataGenerator:
    @staticmethod
    def generate_synthetic_claims(count: int = 5) -> list:
        """Generate synthetic insurance claims for testing."""
        claims_data = []

        for i in range(count):
            try:
                claim = SyntheticDataGenerator._create_claim(i)
                claims_data.append(claim)
            except Exception as e:
                logger.error(f"Error generating claim {i}: {str(e)}")
                continue

        return claims_data

    @staticmethod
    def _create_claim(index: int) -> dict:
        """Create a single synthetic claim."""
        service_date = datetime.now() - timedelta(days=random.randint(1, 30))
        claim_amount = random.randint(500, 15000)

        return {
            'claim_number': f'CLM-{service_date.strftime("%Y%m%d")}-{index:04d}',
            'patient_name': f"{random.choice(PATIENT_FIRST_NAMES)} {random.choice(PATIENT_LAST_NAMES)}",
            'patient_age': random.randint(25, 85),
            'provider_name': random.choice(PROVIDERS),
            'service_date': service_date.strftime('%Y-%m-%d'),
            'procedure': random.choice(PROCEDURES),
            'diagnosis': random.choice(DIAGNOSES),
            'claim_amount': claim_amount,
            'copay': random.randint(20, 100),
            'deductible_met': random.choice([True, False]),
            'authorization_required': random.choice([True, False])
        }

    @staticmethod
    def get_recommendation(claim_data: dict) -> dict:
        """Generate recommendation for synthetic claim."""
        amount = claim_data.get('claim_amount', 0)

        # Simple heuristic rules
        if amount > 10000:
            return {
                'recommendation': 'FLAGGED',
                'reason': f'High claim amount (${amount:,.0f}) requires additional review',
                'confidence': 0.95
            }
        elif amount < 500:
            return {
                'recommendation': 'APPROVED',
                'reason': f'Low claim amount (${amount:,.0f}) within standard parameters',
                'confidence': 0.99
            }
        else:
            approval_chance = random.random()
            if approval_chance > 0.7:
                return {
                    'recommendation': 'APPROVED',
                    'reason': f'Claim amount (${amount:,.0f}) and procedures are within policy guidelines',
                    'confidence': round(0.85 + random.random() * 0.1, 2)
                }
            else:
                return {
                    'recommendation': 'APPROVED',
                    'reason': f'Standard claim review completed. Authorization verified',
                    'confidence': round(0.80 + random.random() * 0.15, 2)
                }
