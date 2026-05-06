# run this test file from the terminal with 'python -m tests.test_scoring' this tells it look for the test_scoring file in my whole project not just a specific folder

from app.scoring import score_symptoms

result = score_symptoms("my neck is tight and my lower back pain is aching")

if result: 
    print("Top suggestion:", result['name'])
    print("Price:", result["base_price"])
    print("Rationale", result["rationale"])
else:
    print("No keywords matched - add more keywords to symptom_keyword table")