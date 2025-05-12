import pandas as pd
import json

with open('test.json', "r", encoding = 'utf-8') as f:
    data = json.load(f)

all_classes = []
for entry in data:
    if entry.get("NativeClass") == "/Script/CoreUObject.Class'/Script/FactoryGame.FGRecipe'":
        all_classes.extend(entry.get("Classes", []))

df = pd.DataFrame(all_classes)

print(df.iloc[0])