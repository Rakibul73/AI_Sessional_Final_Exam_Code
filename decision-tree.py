from sklearn import tree
import pandas as pd
import pydotplus
from IPython.display import Image

golf = pd.DataFrame()
golf['Outlook'] = ['Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Sunny',
                     'Overcast', 'Rainy', 'Rainy', 'Suny', 'Rainy', 'Overcast',
                     'Overcast', 'Sunny']
golf['Temperature'] = ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool',
                         'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild']
golf['Humidity'] = ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal',
                      'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High']
golf['Windy'] = ['FALSE', 'TRUE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'TRUE',
                   'FALSE', 'FLASE', 'FALSE', 'TRUE', 'TRUE', 'FALSE', 'TRUE']
golf['Play'] = ['NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'YES', 'NO', 'YES', 'YES', 'YES',
                  'YES', 'YES', 'NO']
print(golf)

one_hot_data = pd.get_dummies(golf[ ['Outlook', 'Temperature', 'Humidity', 'Windy'] ])
clf = tree.DecisionTreeClassifier()
clf_train = clf.fit(one_hot_data, golf['Play'])
print(tree.export_graphviz(clf_train, None))
dot_data = tree.export_graphviz(clf_train, out_file=None, feature_names=list(one_hot_data.columns.values),
                                class_names=['Not_Play', 'Play'], rounded=True, filled=True)
print(dot_data)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())
prediction = clf_train.predict([[0,0,1,0,1,0,0,1,1,0]])
print(prediction)