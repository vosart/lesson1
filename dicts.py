from pprint import pprint

weather = {"city": "Москва", "temperature": "20"}
pprint(weather["city"], width=1)
weather["temperature"] = str(int(weather["temperature"]) - 5)
pprint(weather, width=1)

print(weather.get("country", "Россия"))

weather["date"] = "27.05.2019"
print(len(weather))
