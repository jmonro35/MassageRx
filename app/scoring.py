# MAIN LOGIC FOR MASSAGERX

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
    db = get_db() #establishing variable
    cursor = db.cursor(dictionary=True) #establishing variable that allows me to write queries to sql... dictionary piece keeps the label/key with the result organization

    #splits the clients free text description of symptoms in to individual words for matching the db
    words = client_text.lower().split()

    #add scores and rationales to a list.. EMPTY DICTIONARY NOT LIST
    scores = {}
    rationale_fragments = {}

    #action for what to do for each word that the loop loops through
    for word in words:

        #ANOTHER debugging line because it is crashing even earlier
        #print("checking word:", word)
        
        #cursor.execute allows me to write and execute query statements via the mysql.connector
        cursor.execute(
            "SELECT massage_id, weight, rationale "
            "FROM symptom_keyword WHERE keyword = %s", (word, ) #%s is a place holder that will be filled with whatever "word" is at that time
        )

        matches = cursor.fetchall() # returns all of the matches (entire row) found in the database

        #debugging line....
        #print('Matches found:', matches)

        #nested for loop
        for match in matches: #because matches was ALL of the results found but I still need to manipulate and rank each match based on scoring logic
            mid = match['massage_id'] # mid = the value of whatever the massage_id in this iteration of the for match in matches loop

            if mid not in scores:
                scores[mid] = 0 #scores defined as an empty dictionary earlier in the program. establishes a value of zero to that mid value if it is not already in the dictionary
                rationale_fragments[mid] = [] #remember mid=match['massage_id'] so the program is searching for the rationale that is associated with the given massage_id and adds it to the dictionary of rationales

            scores[mid] += match['weight'] # if that massage_id was already found in a different iteration of the loop, the program would continue to add the weight to that number and until the loop is complete
            rationale_fragments[mid].append(match["rationale"]) # the program will append the dictionary to include each rationale found in the ROW of match variable

    cursor.close() #close the connection that the tool to write queries to the db
    db.close() #close the db

    #if no matches found
    if not scores: #if the client puts in a phrase that has ZERO word that match in the symptom_keyword table
        return None

    #rank highest score first; this is the highest recommendation
    #defining a function to sort my list 
    def get_score(x):
        return x[1]
    
    #convert scores from dictionary to a sortable list. sort said list by SCORE from HIGHEST to lowest (that is what the reverse is for)
    ranked = sorted(scores.items(), key = get_score, reverse=True)
    #ranked is a list of tuples so the first [] references which tuple to look at and the second [] references which item in said tuple to look at [(massage_id, score)]
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
        (top_massage_id,) #cool way how python and mySQL are intersecting here. top_massage_id is a variable set in python by DERIVED from mySQL db
    )
    
    massage = cursor.fetchone()
    cursor.close()
    db.close()

    #this is the stored return of the def score_symptoms function. these return variables will come into play in testing and in routes for flask 
    return {
        'massage_id' : top_massage_id,
        'name' : massage['massage_name'],
        'base_price' : float(massage['massage_base_price']),
        'description' : massage['massage_description'],
        'score' : top_score,
        'rationale' : rationale,
        'all_scores': ranked
    }
