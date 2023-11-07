from flask import Flask, render_template, request, redirect, url_for, Response
import pandas as pd
import jellyfish
import json
import webview

app = Flask(__name__)
window = webview.create_window('LDCS - OpenFields Checker', app, width=1920, height=1080)

# Variables for tracking elements
valid_count = 0
invalid_count = 0
elements_tested = 0
last_element = ""
last_score = 0.0
all_elements = []

tolerance = 0.5
example_pattern = " "
fn=" "

@app.route('/')
def index():
    all_patterns = load_patterns()
    return render_template('index.html', elements_tested=elements_tested, last_element=last_element, last_score=last_score, average_score=calculate_average_score(), valid_count=valid_count, invalid_count=invalid_count, all_elements=all_elements, all_patterns=all_patterns, tolerance=tolerance, fn=fn)

@app.route('/get_pattern')
def get_pattern():
    return example_pattern

@app.route('/get_tolerance')
def get_tolerance():
    return str(tolerance)

@app.route('/save_settings', methods=['POST'])
def save_settings():
    global tolerance, example_pattern

    selected_pattern = request.form.get('selectedPattern')
    
    new_tolerance = float(request.form.get('toleranceValue'))

    if selected_pattern:
        example_pattern = selected_pattern

    tolerance = new_tolerance
    print("[1]Setting saved : ", tolerance, example_pattern)

    save_settings_to_file(all_patterns)

    return redirect(url_for('index'))

@app.route('/process_csv', methods=['POST'])
def process_csv():
    global elements_tested, last_element, last_score, all_elements, valid_count, invalid_count  # Ajoutez ces deux lignes

    valid_count = 0  # Réinitialisez le compteur valide
    invalid_count = 0  # Réinitialisez le compteur invalide

    if 'file' in request.files:
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            print(f"[1]File uploaded: {uploaded_file.filename}")
            fn = uploaded_file.filename
            df = pd.read_csv(uploaded_file, encoding='latin1')


            # List to store the similarity scores
            similarity_scores = []

            # Iterate through the CSV rows
            for index, row in df.iterrows():
                # Convert the 'Opportunity Name' to a string
                opportunity_name = str(row[0])

                # Calculate the Jaro-Winkler similarity between the opportunity name and the example pattern
                similarity = jellyfish.jaro_winkler_similarity(opportunity_name, example_pattern)


                similarity_scores.append(similarity)
                elements_tested += 1
                last_element = opportunity_name
                last_score = similarity

                if similarity >= tolerance:
                    valid_count += 1
                else:
                    invalid_count += 1

                # Store the element and score for display
                all_elements.append({'element': opportunity_name, 'score': similarity})

            # Export the results to a CSV file
            df['Jaro-Winkler Similarity'] = similarity_scores
            df.to_csv('results.csv', index=False)

            # Redirect to the dashboard with statistics
            return redirect(url_for('index'))

    return redirect(url_for('index'))

@app.route('/export_results', methods=['GET'])
def export_results():
    df = pd.DataFrame(all_elements)
    csv = df.to_csv(index=False)
    response = Response(
        csv,
        content_type='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=all_results.csv'
        }
    )
    return response

@app.route('/reset_tool', methods=['GET'])
def reset_tool():
    global valid_count, invalid_count, elements_tested, last_element, last_score, all_elements

    valid_count = 0
    invalid_count = 0
    elements_tested = 0
    last_element = ""
    last_score = 0.0
    all_elements = []
    example_pattern=" "
    tolerance = 0.5


    return redirect(url_for('index'))


def calculate_average_score():
    if all_elements:
        total_score = sum(item['score'] for item in all_elements)
        return total_score / len(all_elements)
    return 0.0

def load_patterns():
    try:
        with open("patterns.txt", "r") as file:
            
            test = []
            for line in file:
                test.append(line.strip())

            for element in test:
                
                return test
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_settings_to_file(patterns):
    settings = {"patterns": patterns}
    with open("patterns.txt", "w") as file:
        for pattern in patterns:
            file.write(pattern + "\n")

if __name__ == '__main__':
    all_patterns = load_patterns()
    app.run()
    #webview.start()


