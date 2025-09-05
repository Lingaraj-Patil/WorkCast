import requests
import json

# Define the URL of your Flask API's prediction endpoint
# Make sure the Flask app is running before you run this script.
api_url = "http://127.0.0.1:5000/predict"

# Sample resume text to be classified
sample_resume = """
Education Details
2018-2022: Bachelor of Science in Computer Science, University of California, Berkeley.

Experience
June 2022 - Present: Software Engineer at TechCorp.
- Developed and maintained full-stack web applications using React and Node.js.
- Implemented RESTful APIs and integrated with various databases (PostgreSQL, MongoDB).
- Collaborated with a team of 5 developers using Git for version control.

Skills
Languages: JavaScript, Python, Java
Frameworks: React, Express, Django
Databases: PostgreSQL, MongoDB, Redis
Tools: Git, Docker, AWS
"""

# Create the JSON payload with the resume text
payload = {
    "resume_text": sample_resume
}

print("Sending request to the Flask API...")

try:
    # Send the POST request to the API
    response = requests.post(api_url, json=payload)
    
    # Check if the request was successful
    response.raise_for_status()
    
    # Parse the JSON response
    result = response.json()
    
    # Print the result
    print("\n--- API Response ---")
    print(json.dumps(result, indent=4))
    
except requests.exceptions.RequestException as e:
    # Handle any errors that occur during the request
    print(f"Error: Could not connect to the API. Please ensure the Flask app is running at {api_url}")
    print(f"Details: {e}")
