def categorize(text):
    if not text:
        return "Other"

    t = text.lower()

    if any(x in t for x in ["uber", "lyft", "gas"]):
        return "Transport"

    if any(x in t for x in ["amazon", "walmart", "target"]):
        return "Shopping"

    if any(x in t for x in ["starbucks", "mcdonald", "doordash", "restaurant"]):
        return "Food"

    if any(x in t for x in ["netflix", "spotify", "hulu"]):
        return "Subscriptions"

    if any(x in t for x in ["rent", "electric", "water", "internet"]):
        return "Bills"

    return "Other"