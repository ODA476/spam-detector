# import joblib
# # from pathlib import Path

# # Paths to your model files (adjust if needed)
# # NB_MODEL_PATH = Path("app/Naive_Bayes/spam_model.pkl")
# # NB_VEC_PATH = Path("app/Naive_Bayes/tfidf_vectorizer.pkl")
# # LR_MODEL_PATH = Path("app/Logistic_Regression/spam_model.pkl")
# # LR_VEC_PATH = Path("app/Logistic_Regression/tfidf_vectorizer.pkl")

# NB_MODEL_PATH = "../Naive_Bayes/spam_model.pkl"
# NB_VEC_PATH = "../Naive_Bayes/tfidf_vectorizer.pkl"
# LR_MODEL_PATH = "../Logistic_Regression/spam_model.pkl"
# LR_VEC_PATH = "../Logistic_Regression/tfidf_vectorizer.pkl"

# def load_all_models():
#     """Load both model+vectorizer pairs, raise detailed errors if any fail."""
#     models = {"nb": None, "tfidf_nb": None, "lr": None, "tfidf_lr": None}

#     # Load Naive Bayes model and vectorizer
#     try:
#         models["nb"] = joblib.load(NB_MODEL_PATH)
#         models["tfidf_nb"] = joblib.load(NB_VEC_PATH)
#     except Exception as e:
#         raise RuntimeError(f"Failed to load Naive Bayes model files: {e}")

#     # Load Logistic Regression model and vectorizer
#     try:
#         models["lr"] = joblib.load(LR_MODEL_PATH)
#         models["tfidf_lr"] = joblib.load(LR_VEC_PATH)
#     except Exception as e:
#         raise RuntimeError(f"Failed to load Logistic Regression model files: {e}")

#     return models

import joblib
from pathlib import Path

# Get the directory where model_loader.py lives (app/utils)
BASE_DIR = Path(__file__).resolve().parent

# Correctly point up one level to 'app' then into the model directories
NB_MODEL_PATH = BASE_DIR.parent / "Naive_Bayes" / "spam_model.pkl"
NB_VEC_PATH = BASE_DIR.parent / "Naive_Bayes" / "tfidf_vectorizer.pkl"

LR_MODEL_PATH = BASE_DIR.parent / "Logistic_Regression" / "spam_model.pkl"
LR_VEC_PATH = BASE_DIR.parent / "Logistic_Regression" / "tfidf_vectorizer.pkl"

def load_all_models():
    """Load both model/vectorizer pairs, raising detailed errors if any fail."""
    models = {}
    
    # Check if files actually exist before loading to catch naming typos
    for name, path in [("nb_model", NB_MODEL_PATH), ("nb_vec", NB_VEC_PATH), 
                       ("lr_model", LR_MODEL_PATH), ("lr_vec", LR_VEC_PATH)]:
        if not path.exists():
            raise FileNotFoundError(f"Missing required model file: {path.absolute()}")

    try:
        # Load Naive Bayes
        models["nb"] = joblib.load(NB_MODEL_PATH)
        models["tfidf_nb"] = joblib.load(NB_VEC_PATH)
        
        # Load Logistic Regression
        models["lr"] = joblib.load(LR_MODEL_PATH)
        models["tfidf_lr"] = joblib.load(LR_VEC_PATH)
        
    except Exception as e:
        raise RuntimeError(f"Failed to load model binaries via joblib: {e}")
        
    return models
