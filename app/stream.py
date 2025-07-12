import base64, json, soundfile as sf, io
from fastapi import WebSocket, APIRouter, WebSocketDisconnect

router = APIRouter()

@router.websocket("/media")
async def media_stream(ws: WebSocket):
    await ws.accept(subprotocol="audio.twilio.com")
    try:
        while True:
            msg = await ws.receive_text()
            payload = json.loads(msg)
            if payload["event"] == "media":
                # Twilio sends base64-encoded µ-law 8-kHz audio frames
                audio_bytes = base64.b64decode(payload["media"]["payload"])
                # convert to WAV in-memory for STT later
                buffer = io.BytesIO()
                sf.write(buffer, audio_bytes, 8000, format="RAW", subtype="ULAW")
                wav_data = buffer.getvalue()
                # TODO: feed to recognizer
            elif payload["event"] == "stop":
                break
    except WebSocketDisconnect:
        pass
