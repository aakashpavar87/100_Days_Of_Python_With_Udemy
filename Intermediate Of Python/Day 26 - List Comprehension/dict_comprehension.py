# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# list_of_words = sentence.split(" ")
# dict_words = {word: len(word) for word in list_of_words}
# print(dict_words)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
#
# weather_f = {day: temp * 9/5 + 32 for (day, temp) in weather_c.items()}
# print(weather_f)


import pandas
student_dict = {
    "student": ["Aakash", "Bhavesh", "Bharat"],
    "score": [78, 88, 93]
}
student_df = pandas.DataFrame(student_dict)
for (key,value) in student_df.iterrows():
    print(value.score)
