import json

def main(event: str):
    message = json.loads(event)
    # Example preprocessing: Filter out invalid data
    if message["temperature"] > 0 and message["smoke"] > 0:
        return json.dumps(message)
    else:
        return None
