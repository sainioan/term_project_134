import pandas as pd

def cleanData(filePath):
  df = pd.read_csv(filePath)

  df = df.drop(['id', 'partlybad', 'date'], axis=1)

  df['class4'] = df['class4'].astype('category')
  df['class2'] = df['class4'].apply(
    lambda x: 'nonevent' if x == 'nonevent' else 'event'
    ).astype('category')
  
  return df 

cleanData('utils/npf_train.csv').to_csv(
  'utils/C_npf_train.csv', index=False
)
cleanData('utils/npf_test_hidden.csv').to_csv(
  'utils/C_npf_test_hidden.csv', index=False
)
