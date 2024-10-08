from flask import Flask, request, render_template
import pickle
import numpy as np
from urllib.parse import urlparse

# Load the trained model
model_path = 'model.pickle'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)


# Feature extraction function from URL
def extract_features_from_url(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Feature 1: URL length
    url_length = len(url)

    # Feature 2: Number of '?'
    total_of_question_mark = url.count('?')

    # Feature 3: Number of 'www'
    total_of_www = url.count('www')

    # Feature 4: Ratio of digits in the URL to total length
    ratio_digits_url = sum(c.isdigit() for c in url) / len(url)

    # Feature 5: Phishing hints (count of phishing keywords in URL)
    phishing_keywords = ['login', 'secure', 'account', 'bank', 'update']
    phish_hints = sum(1 for word in phishing_keywords if word in url.lower())

    # Feature 6: Number of hyperlinks (estimate based on slashes)
    nb_hyperlinks = url.count('/')

    # Feature 7: Domain in title (placeholder, assuming we fetch the title using the domain)
    domain_in_title = int(parsed_url.netloc.lower() in url.lower())

    # Feature 8: Domain age (using WHOIS)
    domain_age = get_domain_age(parsed_url.netloc)

    # Feature 9: Google index (check if the URL is indexed by Google)
    google_index = check_google_index(url)

    # Feature 10: Page rank (placeholder, as page rank isn't directly available anymore)
    page_rank = get_page_rank(url)

    # Return a feature array (adjust based on your model's expectations)
    return np.array([[url_length, total_of_question_mark, total_of_www, ratio_digits_url, int(phish_hints),
                      nb_hyperlinks, domain_in_title, domain_age, google_index, page_rank]])

# Function to calculate the domain age
def get_domain_age(domain):
    try:
        whois_info = whois.whois(domain)
        creation_date = whois_info.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]  # Handle list of creation dates
        domain_age_days = (datetime.now() - creation_date).days
        return domain_age_days
    except Exception as e:
        print(f"Error in fetching domain age: {e}")
        return -1  # Return -1 if the domain age can't be determined

# Function to get page rank (currently a placeholder, as PageRank isn't available directly)
def get_page_rank(url):
    # Placeholder for demonstration; you can replace this with an actual API call if needed
    return 5

# Function to check if a URL is indexed by Google (mock example, real implementation would require Google Search API)
def check_google_index(url):
    try:
        search_result = requests.get(f'https://www.google.com/search?q=site:{url}')
        return 1 if search_result.status_code == 200 else 0
    except:
        return 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the URL from form input
    url = request.form['url']

    # Extract features from the URL
    features = extract_features_from_url(url)

    # Make a prediction
    try:
        prediction = model.predict(features)
        prediction_label = 'Phishing' if prediction[0] == 1 else 'Not Phishing'
    except ValueError as e:
        print(f"Error: {e}")
        prediction_label = "Error in prediction: Check input format or model compatibility."

    # Render the result on the webpage
    return render_template('index.html', prediction=prediction_label)


if __name__ == '__main__':
    app.run(debug=True)