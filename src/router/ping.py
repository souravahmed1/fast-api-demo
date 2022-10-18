from fastapi import FastAPI, Request, HTTPException, status, APIRouter




router = APIRouter()



@router.get("/ping")
async def ping(request: Request):
    try:
        # complex calculation
        # pi_val = 22 / 7
        return {
            "message": "Ping Hello"
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