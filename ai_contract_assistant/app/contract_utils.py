
import re

def extract_clauses(text: str):
    clauses = re.split(r"\n\d+\.\s+|\n•\s+", text)
    return [cl.strip() for cl in clauses if len(cl.strip()) > 20]
