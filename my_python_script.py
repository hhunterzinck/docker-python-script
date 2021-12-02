import argparse
import pandas as pd

# command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--message', dest = 'message', help = 'enter a message to print')
args = parser.parse_args()

# append data frames with installed pandas package version
df1 = pd.DataFrame([[1,2],[3,4],[5,6]], columns = ['Z','A'])
df2 = pd.DataFrame([[1,2],[3,4],[5,6]], columns = ['Y','B'])
df3 = df1.append(df2)

# check for old pandas package version functionality
if df3.columns[0] == 'A':
    print(f'Old pandas version ({pd.__version__})')
else:
    print('New pandas version')

# print user supplied message
print(f'Message: {args.message}')
