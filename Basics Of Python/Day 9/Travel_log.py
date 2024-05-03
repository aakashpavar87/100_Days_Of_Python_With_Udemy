# travel_log = {
#     "America":{
#         "visited_cities":["New York","California","Wall Street"],
#         "total_visits":10
#     },
#     "Things_to_carry":["Bag","Clothes","Money",
#                        {
#                            "gadgets":["Mobile","Camera"]
#                        }
#                       ]
# }
travel_log = [
    {
        "country":"France",
        "visits":12,
        "cities":["Paris","Lille","Dijon"]
    },
    {
        "country":"Germany",
        "visits":10,
        "cities":["Berlin","Hamburg","Stuttgurt"]
    }
]

def add_new_country(country,visits,cities):
    new_travel_log = travel_log
    new_travel_log.append({
        "country":country,
        "visits":visits,
        "cities":cities
    })
    print(f"After Adding :{new_travel_log}")

print(f"Before Adding : {travel_log}")
add_new_country("Russia",2,["Moscow","Saint Petersburg"])