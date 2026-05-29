

# Example mapping of private personal information used for password risk analysis.
# This dictionary represents data that an attacker might know or guess.
# If any of these values appear in a password, the password is considered riskier.

# private_info_mapping = {
#     "first_name": "John",
#     "last_name": "Doe",
#     "email": "john.doe@example.com",
#     "phone_number": "+1-555-123-4567",
#     "birth_date": "1990-01-01",
#     "address": "123 Main St, Anytown, USA",
#     "username": "JohnDoe90",
#     "pet_name": "Fluffy",
#     "favorite_color": "Blue",
#     "favorite_food": "Pizza",
#     "hobby": "Photography",
#     "school_name": "Anytown High School",
#     "company_name": "Tech Solutions Inc.",
# }



def analyze_password_risk(password, private_info_mapping):
    """Return a risk score and warnings for a password based on personal data exposure."""
    risk_score = 0
    warnings = []

    # Evaluate password against each known personal detail.
    for key, value in private_info_mapping.items():

        if key == "birth_date":
            # Birth date matches are checked separately for year, month, and day.
            for part in value.split("-"):
                if part in password:
                    warnings.append(f"Warning: Password contains part of the birth date ({part}).")
                    risk_score += 15

        if key == "email":
            # Only compare the email local part, not the domain.
            email_username = value.split("@")[0]
            if email_username in password:
                warnings.append(f"Warning: Password contains the email username ({email_username}).")
                risk_score += 15
        
        if key == "phone_number":
            # Normalize phone number to digits before matching.
            phone_digits = ''.join(filter(str.isdigit, value))
            if phone_digits in password:
                warnings.append(f"Warning: Password contains the phone number digits ({phone_digits}).")
                risk_score += 15

        if key == "address":
            # Check each component of the street address separately.
            address_parts = value.split(",")[0].split()
            for part in address_parts:
                if part in password:
                    warnings.append(f"Warning: Password contains part of the address ({part}).")
                    risk_score += 15
        
        # Generic personal information match, case-insensitive.
        if value.lower() in password.lower():
            warnings.append(f"Warning: Password contains {key} which is a common piece of personal information.")
            risk_score += 15
        


    if risk_score >= 50:            
        risk_level = "High Risk"
    elif risk_score >= 20:
        risk_level = "Moderate Risk"
    else:
        risk_level = "Low Risk"

    # Return the overall risk assessment.
    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "warnings": warnings
    }





# #testing
# import PasswordStrengthAssesing
# import BruteForceTimer

# password_to_analyze = "JohnDoe1990!"
# print("Analyzing password risk...") 
# analyzed_password_risk = analyze_password_risk("JohnDoe1990!", private_info_mapping)
# print(analyzed_password_risk["risk_level"], " with a risk score of", analyzed_password_risk["risk_score"], " out of 100.", "Warnings:", analyzed_password_risk["warnings"])
# print("Assessing password strength...")
# PasswordStrengthAssesing.asses_password_strength(password_to_analyze)
# print("Calculating time to brute-force the password...")
# BruteForceTimer.brute_force_timer(1_000_000_000, password_to_analyze)
