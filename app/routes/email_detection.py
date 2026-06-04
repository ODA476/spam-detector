from fastapi import APIRouter, HTTPException, status, Depends
from ..schemas.email import EmailRequest
from ..utils.model_utils import clean_text
from fastapi import Request

router = APIRouter(prefix='/email', tags=['Email Detection'])

@router.post("/predict/naive_bayes")
def predict_email_Naive_Bayes(request_data: EmailRequest,
    request: Request):
    if not request_data.email or not request_data.email.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email text is required")

    models = request.app.state.models
    # 1. Clean
    cleaned = clean_text(request_data.email)
    # 2. Vectorize
    vectorized =  models["tfidf_nb"].transform([cleaned]).toarray()
    # 3. Predict
    prediction = models["nb"].predict(vectorized)[0]
    # 4. Probability
    prob = models["nb"].predict_proba(vectorized).tolist()[0]

    return {
        "label": "Spam" if prediction == 1 else "Ham",
        "confidence": round(max(prob) * 100, 2),
        "is_spam": bool(prediction)
    }

@router.post("/predict/logistic_regrssion")
def predict_email_logistic_regrssion(request_data: EmailRequest,
    request: Request):
    if not request_data.email or not request_data.email.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email text is required")

    models = request.app.state.models
    
    # 1. Clean
    cleaned = clean_text(request_data.email)
    # 2. Vectorize
    vectorized = models["tfidf_lr"].transform([cleaned]).toarray()
    # 3. Predict
    prediction = models["lr"].predict(vectorized)[0]
    # 4. Probability
    prob = models["lr"].predict_proba(vectorized).tolist()[0]

    return {
        "label": "Spam" if prediction == 1 else "Ham",
        "confidence": round(max(prob) * 100, 2),
        "is_spam": bool(prediction)
    }
