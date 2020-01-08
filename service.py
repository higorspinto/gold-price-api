from datetime import datetime
from flask import jsonify

def get_gold_price():

    # datetime object containing current date and time
    now = datetime.now()
 
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    response_object = {"status" : "sucess", 
                        "date" :  dt_string,
                        "items" : [{"curr": "USD",
                                    "xauPrice": 1573.78,
                                    "xagPrice": 18.4017,
                                    "chgXau": 49.28,
                                    "chgXag": 0.3337,
                                    "pcXau": 3.2325,
                                    "pcXag": 1.8469,
                                    "xauClose": 1524.5,
                                    "xagClose": 18.068
                        }]
                    }


    return jsonify(response_object)