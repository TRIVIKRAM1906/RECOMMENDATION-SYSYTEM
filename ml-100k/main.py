from src.data_loader import load_movielens_100k
from src.model import train_model
from src.evaluate import evaluate_model

df = load_movielens_100k()
model, testset = train_model(df)
rmse = evaluate_model(model, testset)

print(f"Model RMSE: {rmse:.4f}")
