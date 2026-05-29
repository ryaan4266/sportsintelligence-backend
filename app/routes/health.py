from fastapi import APIRouter


router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "Athena Sports Intelligence API",
    }
