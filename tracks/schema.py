from datetime import datetime
import ninja

class TrackSchema(ninja.Schema):
    title: str
    artist: str
    duration: float
    last_play: datetime

class NotFoundSchema(ninja.Schema):
    message:str