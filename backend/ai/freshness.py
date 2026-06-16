from datetime import datetime

def calculate_freshness_score(prepared_time: str, pickup_deadline: str) -> dict:
    try:
        # Handle both formats with T and with space
        prepared_time = prepared_time.replace('T', ' ')
        pickup_deadline = pickup_deadline.replace('T', ' ')

        # Try multiple formats
        formats = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M"]
        
        prepared = None
        deadline = None
        
        for fmt in formats:
            try:
                prepared = datetime.strptime(prepared_time, fmt)
                break
            except:
                continue
                
        for fmt in formats:
            try:
                deadline = datetime.strptime(pickup_deadline, fmt)
                break
            except:
                continue

        if not prepared or not deadline:
            return {
                "freshness_score": 50.0,
                "status": "Moderate ⚠️",
                "safe_for_donation": True
            }

        now = datetime.now()
        total_window = (deadline - prepared).total_seconds()
        time_passed = (now - prepared).total_seconds()

        if total_window <= 0:
            score = 0.0
        else:
            score = max(0.0, 1.0 - (time_passed / total_window))

        score = round(score * 100, 2)

        if score >= 70:
            status = "Fresh ✅"
            safe = True
        elif score >= 40:
            status = "Moderate ⚠️"
            safe = True
        else:
            status = "Not Safe ❌"
            safe = False

        return {
            "freshness_score": score,
            "status": status,
            "safe_for_donation": safe
        }

    except Exception as e:
        return {
            "freshness_score": 50.0,
            "status": "Moderate ⚠️",
            "safe_for_donation": True,
            "error": str(e)
        }