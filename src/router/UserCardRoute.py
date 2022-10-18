from fastapi import FastAPI, Request, HTTPException, status, APIRouter, Depends
from src.utils.utils import JWTBearer
router = APIRouter()


@router.get("/credit-card-info")
async def UserCardAccess(request: Request, payload = Depends(JWTBearer()) ):
    try:
        # complex calculation
        # { x: 22 }
        print("jwtToken: ", payload)
        return {
            "message": "Abcd",
            "status": 200
        }

    except HTTPException as e:
        return {
            "errorMessage": [ { "exceptionMessage": "HTTPException" } ],
            "status": 500
        }
    except Exception as e:
        return {
            "status": 500,
            "errorMessage": [ { "exceptionMessage": "Unknown Exception" + str(e) } ]
        }