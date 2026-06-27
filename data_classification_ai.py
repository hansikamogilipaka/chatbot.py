import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=200)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=iris.target_names)

print("Accuracy:", acc)
print("Confusion Matrix:\n", cm)
print("Classification Report:\n", report)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, cmap="Blues", xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

new_data = np.array([[5.1, 3.5, 1.4, 0.2]])
new_data_scaled = scaler.transform(new_data)
prediction = model.predict(new_data_scaled)
print("Predicted Class:", iris.target_names[prediction[0]])

def train_and_evaluate(model_type):
    if model_type == "logistic":
        model = LogisticRegression(max_iter=200)
    elif model_type == "svm":
        from sklearn.svm import SVC
        model = SVC(kernel='linear')
    elif model_type == "knn":
        from sklearn.neighbors import KNeighborsClassifier
        model = KNeighborsClassifier(n_neighbors=5)
    else:
        from sklearn.tree import DecisionTreeClassifier
        model = DecisionTreeClassifier()
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    print("Model:", model_type, "Accuracy:", acc)
    return acc

models = ["logistic", "svm", "knn", "tree"]
results = {}
for m in models:
    results[m] = train_and_evaluate(m)

best_model = max(results, key=results.get)
print("Best Model:", best_model)

plt.bar(results.keys(), results.values(), color=['orange','green','blue','red'])
plt.title("Model Comparison")
plt.xlabel("Model Type")
plt.ylabel("Accuracy")
plt.show()

def predict_new(sample):
    scaled = scaler.transform(sample)
    pred = model.predict(scaled)
    return iris.target_names[pred[0]]

sample_input = np.array([[6.2, 3.4, 5.4, 2.3]])
print("New Sample Prediction:", predict_new(sample_input))

def visualize_features():
    plt.figure(figsize=(8,6))
    sns.pairplot(pd.concat([X, y.rename("target")], axis=1), hue="target", palette="Set2")
    plt.show()

visualize_features()

def evaluate_with_cross_validation():
    from sklearn.model_selection import cross_val_score
    scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
    print("Cross-validation scores:", scores)
    print("Mean CV Accuracy:", np.mean(scores))

evaluate_with_cross_validation()

def save_model():
    import joblib
    joblib.dump(model, "classification_model.pkl")
    joblib.dump(scaler, "scaler.pkl")
    print("Model and scaler saved successfully.")

save_model()

def load_model():
    import joblib
    loaded_model = joblib.load("classification_model.pkl")
    loaded_scaler = joblib.load("scaler.pkl")
    print("Model and scaler loaded successfully.")
    return loaded_model, loaded_scaler

loaded_model, loaded_scaler = load_model()

sample_test = np.array([[5.9, 3.0, 5.1, 1.8]])
sample_scaled = loaded_scaler.transform(sample_test)
pred = loaded_model.predict(sample_scaled)
print("Loaded Model Prediction:", iris.target_names[pred[0]])

def plot_feature_importance():
    if hasattr(model, "coef_"):
        importance = np.abs(model.coef_[0])
        plt.barh(iris.feature_names, importance, color='purple')
        plt.xlabel("Importance")
        plt.title("Feature Importance (Logistic Regression)")
        plt.show()

plot_feature_importance()

def summary():
    print("Project Summary:")
    print("Dataset:", "Iris")
    print("Algorithm:", "Logistic Regression")
    print("Accuracy:", acc)
    print("Best Model:", best_model)
    print("Skills Used: Data handling, supervised learning, model training")

summary()
