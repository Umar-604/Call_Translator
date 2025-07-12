from fastapi import APIRouter
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse, Start

router = APIRouter()

@router.post("/twiml")
async def twiml():
    resp = VoiceResponse()
    start = Start()
    start.stream(url="wss://<your_server>/media")  # WebSocket endpoint
    resp.append(start)
    resp.say("You are now connected to the real-time translator.")
    return Response(content=str(resp), media_type="text/xml")
