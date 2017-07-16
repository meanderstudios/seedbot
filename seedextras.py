def is_question(parts):
    if "," in parts[1]:
        questions = []
        partsofparts = parts[1].split(",")
        for part in partsofparts:
            questions.append("Is " + parts[0].lower() + " " + part.lower() + "?")
    else:    
        return "Is " + parts[0].lower() + " " + parts[1].lower() + "?"


