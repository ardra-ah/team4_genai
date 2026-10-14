class SummarizationAgent:
    def __init__(self):
        pass

    def generate_summary(self, extracted_data: dict, validation_results: dict, recommendation: dict) -> dict:
        """Generate a concise AI summary of the claim."""

        patient_name = extracted_data.get("patient_name", "Unknown")
        provider_name = extracted_data.get("provider_name", "Unknown")
        claim_amount = extracted_data.get("claim_amount", 0)
        procedure = extracted_data.get("procedure", "Not specified")
        diagnosis = extracted_data.get("diagnosis", "Not specified")

        rec_status = recommendation.get("recommendation", "pending").upper()
        rec_confidence = recommendation.get("confidence", 0)
        rec_reason = recommendation.get("reason", "No reason provided")

        # Build concise summary
        summary_parts = []
        summary_parts.append(f"👤 Patient: {patient_name}")
        summary_parts.append(f"🏥 Provider: {provider_name}")
        summary_parts.append(f"💉 Procedure: {procedure}")
        summary_parts.append(f"🔬 Diagnosis: {diagnosis}")
        summary_parts.append(f"💰 Amount: ${claim_amount:,.2f}")
        summary_parts.append(f"")
        summary_parts.append(f"✅ Recommendation: {rec_status} ({rec_confidence * 100:.0f}%)")
        summary_parts.append(f"📝 Reason: {rec_reason}")

        return {
            "summary": "\n".join(summary_parts),
            "key_points": {
                "patient": patient_name,
                "provider": provider_name,
                "amount": f"${claim_amount:,.2f}",
                "procedure": procedure,
                "status": rec_status,
                "confidence": f"{rec_confidence * 100:.1f}%"
            }
        }
