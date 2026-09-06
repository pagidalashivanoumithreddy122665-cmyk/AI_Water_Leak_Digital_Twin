"""
AI Leak Location Prediction
XGBoost Training
"""

import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

from xgboost import XGBClassifier


print("Loading dataset...")


df = pd.read_csv("dataset.csv")


print("Dataset shape:", df.shape)


# ------------------------------------
# Target
# ------------------------------------

target = "Leak_Junction"


X = df.drop(columns=[target])

y = df[target]


# ------------------------------------
# Encode text columns
# ------------------------------------

encoders = {}


for col in X.select_dtypes(include="object").columns:

    encoder = LabelEncoder()

    X[col] = encoder.fit_transform(
        X[col]
    )

    encoders[col] = encoder



target_encoder = LabelEncoder()

y = target_encoder.fit_transform(y)



# ------------------------------------
# Train test split
# ------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)



# ------------------------------------
# XGBoost Model
# ------------------------------------

print("Training XGBoost...")


model = XGBClassifier(

    n_estimators=300,

    max_depth=6,

    learning_rate=0.05,

    subsample=0.8,

    colsample_bytree=0.8,

    objective="multi:softmax",

    num_class=8,

    random_state=42

)



model.fit(
    X_train,
    y_train
)



# ------------------------------------
# Accuracy
# ------------------------------------

prediction = model.predict(
    X_test
)


accuracy = accuracy_score(
    y_test,
    prediction
)


print("--------------------------------")
print("Accuracy:", accuracy)
print("--------------------------------")


print(
    classification_report(
        y_test,
        prediction
    )
)



# ------------------------------------
# Save model
# ------------------------------------

pickle.dump(
    model,
    open("leak_model.pkl","wb")
)


pickle.dump(
    encoders,
    open("feature_encoders.pkl","wb")
)


pickle.dump(
    target_encoder,
    open("target_encoder.pkl","wb")
)



print("AI model saved successfully!")
