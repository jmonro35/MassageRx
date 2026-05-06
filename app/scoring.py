# translator for mySQL & python. scoring data is in the database
import mysql.connector 
# imports my mySQL credentials from my private/safe config file
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

#defining function to be reused whenever i need to pull my mySQL credentials
def get_db():
    #actually makes the connection to the mySQL database. dialing phone number analogy
    return mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME
    )

#defining score_symptoms() functions
def score_symptoms(client_text):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    #splits the clients free text description of symptoms in to individual words for matching the db
    
    words = client_text.lower().split()

    #add scores and rationales to a list.. EMPTY DICTIONARY NOT LIST
    scores = {}
    rationale_fragments = {}

    #action for what to do for each word that the loop loops through
    for word in words:

        #ANOTHER debugging line because it is crashing even earlier
        #print("checking word:", word)
        #cursor.execute allows me to write a sql query that will be executed via the mysql.connector
        cursor.execute(
            "SELECT massage_id, weight, rationale "
            "FROM symptom_keyword WHERE keyword = %s", (word, )
        )
        matches = cursor.fetchall()

        #debugging line....
        print('Matches found:', matches)

        #nested for loop
        for match in matches:
            mid = match['massage_id']

            if mid not in scores:
                scores[mid] = 0
                rationale_fragments[mid] = []

            scores[mid] += match['weight']
            rationale_fragments[mid].append(match["rationale"])

    cursor.close()
    db.close()

    #if no matches found
    if not scores:
        return None

    #rank highest score first; this is the highest recommendation
    ranked = sorted(scores.items(), key = lambda x: x[1], reverse=True)
    top_massage_id = ranked[0][0]
    top_score = ranked [0][1]

    #another debugging line because the key error seems to be coming from BEFORE the second query
    #print("Scores:", scores)
    #print("Ranked:", ranked)
    #print("Top massage id:", top_massage_id)

    #rationale explanation string
    rationale = "This massage type is recommended because" + " , and ".join(rationale_fragments[top_massage_id]) + "."
    
    #pull massage details and price from db
    db = get_db()
    cursor = db.cursor(dictionary=True)

    #debugging line because something is causes a keyerror for 'massage_name'
    #print("Looking for massage_id:", top_massage_id)
    #print("Type:", type(top_massage_id))

    cursor.execute(
        "SELECT massage_name, massage_base_price, massage_description "
        "FROM massage_type WHERE massage_id = %s",
        (top_massage_id,)
    )
    
    massage = cursor.fetchone()
    cursor.close()
    db.close()

    return {
        'massage_id' : top_massage_id,
        'name' : massage['massage_name'],
        'base_price' : float(massage['massage_base_price']),
        'description' : massage['massage_description'],
        'score' : top_score,
        'rationale' : rationale,
        'all_scores': ranked
    }
