
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
print("First five rows of dataset:")
print(df.head())
print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nUnique target values:", df['target'].unique())
plt.figure(figsize=(10, 6))
sns.countplot(x='target', data=df, palette='viridis')
plt.title('Distribution of Target Classes')
plt.show()
sns.pairplot(df, hue='target', palette='coolwarm')
plt.show()

X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\nTraining set size:", X_train.shape)
print("Testing set size:", X_test.shape)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = LogisticRegression(max_iter=200)

model.fit(X_train_scaled, y_train)
print("\nModel training complete.")
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy of the model:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='d')
plt.title('Confusion Matrix Heatmap')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
X_vis = df[['sepal length (cm)', 'sepal width (cm)']]
y_vis = df['target']

X_train_vis, X_test_vis, y_train_vis, y_test_vis = train_test_split(
    X_vis, y_vis, test_size=0.2, random_state=42, stratify=y_vis
)

scaler_vis = StandardScaler()
X_train_vis_scaled = scaler_vis.fit_transform(X_train_vis)
X_test_vis_scaled = scaler_vis.transform(X_test_vis)

model_vis = LogisticRegression(max_iter=200)
model_vis.fit(X_train_vis_scaled, y_train_vis)
x_min, x_max = X_train_vis_scaled[:, 0].min() - 1, X_train_vis_scaled[:, 0].max() + 1
y_min, y_max = X_train_vis_scaled[:, 1].min() - 1, X_train_vis_scaled[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

Z = model_vis.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
plt.scatter(X_train_vis_scaled[:, 0], X_train_vis_scaled[:, 1],
            c=y_train_vis, edgecolors='k', cmap='coolwarm')
plt.title('Decision Boundary (2D Visualization)')
plt.xlabel('Sepal Length (scaled)')
plt.ylabel('Sepal Width (scaled)')
plt.show()
import joblib
joblib.dump(model, 'iris_classifier.pkl')
print("\nModel saved as iris_classifier.pkl")
loaded_model = joblib.load('iris_classifier.pkl')
print("\nLoaded model successfully.")
sample = X_test_scaled[0].reshape(1, -1)
predicted_class = loaded_model.predict(sample)
print("\nPredicted class for first test sample:", predicted_class)
print("Actual class:", y_test.iloc[0])
from sklearn.metrics import precision_score, recall_score, f1_score

precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("\nPrecision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
from sklearn.model_selection import cross_val_score
cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
print("\nCross-validation scores:", cv_scores)
print("Mean CV Accuracy:", np.mean(cv_scores))
importance = np.abs(model.coef_).mean(axis=0)
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importance
}).sort_values(by='Importance', ascending=False)

print("\nFeature Importance:")
print(feature_importance)

plt.figure(figsize=(8, 5))
sns.barplot(x='Importance', y='Feature', data=feature_importance, palette='mako')
plt.title('Feature Importance (Logistic Regression)')
plt.show()
results = pd.DataFrame({
    'Actual': y_test,
    'Predicted': y_pred
})
results.to_csv('classification_results.csv', index=False)
print("\nResults saved to classification_results.csv")

print("\n--- PROJECT SUMMARY ---")
print("1. Dataset: Iris (150 samples, 4 features)")
print("2. Algorithm: Logistic Regression")
print("3. Accuracy:", round(accuracy, 3))
print("4. Precision:", round(precision, 3))
print("5. Recall:", round(recall, 3))
print("6. F1 Score:", round(f1, 3))
print("7. Model saved and reusable for predictions.")
print("8. Visualization and evaluation completed successfully.")
print("------------------------------------------------------------")
print("End of Project 2: Data Classification Using AI")
