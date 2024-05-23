import pandas as pd

data = {
    'Name': ['ram', 'shyam', 'hari', 'sita'],
    'Age': [21,22,23,24],
    'City': ['Kathmandu','New York','London','Dhulikhel']
}
df = pd.DataFrame(data)
print(df)