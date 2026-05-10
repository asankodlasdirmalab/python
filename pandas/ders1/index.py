# pip install pandas

import pandas as pd

students = {
    "name": ["Ali", "Aysel", "Murad"],
    "age": [20, 21, 19]
}

df = pd.DataFrame(students)

print(df)
