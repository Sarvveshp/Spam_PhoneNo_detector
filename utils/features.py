def extract_features(number):
    features = {
        "has_repeated_digits": len(set(number)) < 4,
        "starts_with_9": number.startswith("9"),
        "contains_sequence": "1234" in number or "9876" in number,
        "length": len(number)
    }
    return list(features.values())
