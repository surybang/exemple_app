import pandas as pd 

df = pd.read_csv('./datasets/online-payments-fraud-detection-dataset.zip',usecols=['type', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig'],nrows=20)
df.to_csv('data.csv', index=False)
