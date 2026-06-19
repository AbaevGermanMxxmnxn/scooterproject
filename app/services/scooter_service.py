def analyze_scooter(speed: float, battery: int) -> dict:
    if battery < 20:
        return {
            "status": "low_battery",
            "recommendation": "Return to charging station"
        }

    if speed > 25:
        return {
            "status": "speed_warning",
            "recommendation": "Reduce speed for safety"
        }

    return {
        "status": "ok",
        "recommendation": "Scooter is operating normally"
    }
