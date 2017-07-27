from sklearn import tree

#Decision Tree initial data
X = [[180,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[180,80,44],[171,75,42],[181,85,43]]
Y = ['male','female','female','female','female','male','male','male','male','female','male']

clasificationTree = tree.DecisionTreeClassifier()

clasificationTree = clasificationTree.fit(X,Y)

prediction = clasificationTree.predict([[190,70,40]])

print prediction


