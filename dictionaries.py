state_capitols = {"Ohio":"Columbus", "California":"Sacremento", "Colorado": "Denver", "Delaware":"Dover" }
speed_limits = {"School Zone":20, "Interstate":70, "County Roads":55, "Alleyways":15, "Residential":25, "Expressways":65, "Roadways":35}

Cap_of_Ohio = state_capitols.get("Ohio")
print(Cap_of_Ohio)

print(state_capitols)
print(state_capitols["California"])
print(state_capitols.items())

# place dictionary into a list
list_of_capitols = list(state_capitols)
print(f"Print by index: {list_of_capitols[0]}, {list_of_capitols[0][1]}")
print(f"Print by index: {list_of_capitols}")
print(f"Print by index: {state_capitols.values()}")

Cap_of_Ohio = state_capitols.get("Ohio")
print(Cap_of_Ohio)

for key in speed_limits:
    print(key)

for key, value in speed_limits.items():
    print(key, value)
