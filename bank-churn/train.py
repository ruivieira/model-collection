import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

data = pd.read_csv('./data/train.csv')

X = data.drop(['Exited'], axis=1)
y = data['Exited']

categorical_features = ['Geography', 'Gender', 'Card Type', 'HasCrCard', 'IsActiveMember', 'Complain']
label_encoders = {}
for feature in categorical_features:
    label_encoders[feature] = LabelEncoder()
    X[feature] = label_encoders[feature].fit_transform(X[feature])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

rf_classifier.fit(X_train, y_train)

y_pred = rf_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': rf_classifier.feature_importances_})
feature_importance = feature_importance.sort_values('Importance', ascending=False)
print('Feature Importance:')
print(feature_importance)

model_file = "model.joblib"
joblib.dump(rf_classifier, model_file)
print("Model saved to", model_file)