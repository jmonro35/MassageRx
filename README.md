# MassageRx

A clinical decision support tool for massage therapy services. MassageRx takes a client's symptom description, screens for safety contraindications, and returns a personalized massage recommendation with rationale and pricing.

---

## Why I Built This

New massage therapy clients often don't know which service is right for them. This uncertainty creates friction in the booking process and increases the likelihood of a client selecting the wrong service, leading to dissatisfaction or no booking at all. MassageRx removes that friction by guiding the client to the right service based on how they actually feel, not a generic menu.

From a clinical standpoint, certain massage types are better suited to specific conditions and body areas. MassageRx encodes that knowledge into a scoring engine so clients receive an informed recommendation rather than a guess.

---

## Features

- **Free text symptom intake** — client describes how they feel in their own words
- **Safety screening** — 4 clinically informed yes/no questions with hard stop logic
- **Keyword scoring engine** — matches symptoms to massage types using a weighted rulebook stored in MySQL
- **Personalized recommendation** — returns top massage type with rationale explaining why
- **Price estimate** — base price pulled directly from the database
- **Clinical hard stops** — pregnancy, recent injury, blood clot history, and uncontrolled blood pressure immediately halt the session and redirect to a physician

---

## Tech Stack

| Python 3 | Scoring logic and database interaction |
| Flask | Web framework and routing |
| MySQL | Data storage — all prices, keywords, and rules |
| mysql-connector-python | Bridge between Python and MySQL |
| HTML / CSS | Client facing interface |
| GitHub | Version control |

**Core design principle: logic lives in Python, data lives in the database.**

---

## How to Run

1. Clone this repo
2. Copy `config.example.py` to `config.py` and add your MySQL credentials
3. Run `database/schema.sql` in MySQL to build the database
4. Run `database/seed_data.sql` to populate lookup data
5. Install dependencies:
```
pip install flask mysql-connector-python
```
6. Start the app:
```
python run.py
```
7. Open your browser to `http://127.0.0.1:5000`

> Note: `config.py` is gitignored and will never be committed. Never share your credentials.

---

## Project Structure

```
massagerx/
├── app/
│   ├── __init__.py       # Flask app initialization
│   ├── routes.py         # URL routing and request handling
│   └── scoring.py        # Keyword scoring engine and DB connection
├── database/
│   ├── schema.sql        # Database structure — all CREATE TABLE statements
│   └── seed_data.sql     # Lookup data — massage types, keywords, safety questions
├── templates/
│   ├── index.html        # Symptom intake form
│   ├── screening.html    # Safety screening questions
│   ├── results.html      # Recommendation display
│   └── blocked.html      # Safety hard stop message
├── static/
│   └── style.css         # Application styling
├── tests/
│   └── test_scoring.py   # Scoring engine tests
├── config.example.py     # Credential template — safe to commit
├── config.py             # Real credentials — gitignored, never committed
└── run.py                # Application entry point
```

---

## Clinical Design Decisions

All safety screening conditions are treated as **hard stops** — no massage services are recommended when any contraindication is disclosed. This follows a conservative safety-first approach consistent with standard massage therapy intake protocols.

Conditions that trigger a hard stop:
- Pregnancy
- Recent surgery or injury within 6 weeks
- History of blood clots or cardiovascular condition
- Uncontrolled high or low blood pressure

Each hard stop returns a specific, clinically appropriate message that acknowledges the client, explains the reason, and redirects them to the appropriate healthcare provider.

---

## How the Scoring Engine Works

1. Client's free text is split into individual words
2. Each word is looked up in the `symptom_keyword` table
3. Matching keywords contribute their weight to the associated massage type's running score
4. All four massage types are ranked by total score
5. The highest scoring massage type becomes the recommendation
6. Rationale is assembled from the matched keyword explanations

Because the scoring rules live in the database instead of the code, the engine is easily updated because there is no need to change the scoring logic. 

---

## Future Enhancements

- Add-on services with pricing (cupping, CBD oil, stretching)
- Session history — track past recommendations per client
- Detailed safety response audit table for full clinical documentation
- Expanded keyword library for broader symptom coverage
- Admin dashboard showing keyword weights and scoring breakdown


---

## Author
Jasmin Monroe
Healthcare Informatics — HMI 7540 Introduction to Data Systems