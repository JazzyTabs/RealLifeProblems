import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.model_selection import GridSearchCV
from sklearn import svm

# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

#=========================================================#
#=========== Step 1 Read file and load data ==============#
#=========================================================#

df = pd.read_csv("C:\Temp\",na_values=['NA', '?'])
print(df.head(100))

#=========================================================#
#=========== Step 2 Data =================================#
#=========================================================#

x = df["EML_CATEGORY"]
y = df["FILE_NAME"]

x_train, y_train = x[0:4457],y[0:4457]
x_test, y_test = x[4457:], y[4457:]

#=========================================================#
#=========== Step 3 Extract Features =====================#
#=========================================================#

cv = CountVectorizer()
features = cv.fit_transform(x_train)

#=========================================================#
#=========== Step 4 Build Model ==========================#
#=========================================================#

model = svm.SVC()
model.fit(features,y_train)

#=========================================================#
#=========== Step 5 Test Model ==========================#
#=========================================================#

#feautures_test = cv.transform(x_test)
#model.score(feautures_test,y_test)