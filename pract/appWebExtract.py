import pandas as pd

url = 'https://therahmacenter.org/'

table = pd.read_html(url)

print(table)