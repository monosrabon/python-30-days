# utils.py
def format_time(seconds):
    """Convert seconds into MM:SS format"""
    mins, secs = divmod(seconds, 60)
    return f"{mins:02d}:{secs:02d}"
