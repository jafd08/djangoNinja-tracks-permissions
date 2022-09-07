import ninja
from tracks.models import Track
from tracks.schema import TrackSchema, NotFoundSchema
import typing as ty

router = ninja.Router()
# http://localhost:8000/api/tracks ....

# http://localhost:8000/api/tracks?title=a

@router.get("/tracks", response=ty.List[TrackSchema])
def tracks(request, title: ty.Optional[str] = None):
    if title:
        return Track.objects.filter(title__icontains=title)
    return Track.objects.all()

@router.get("/tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def track(request, track_id:int):
    # query parameter if needed -> we place it on our parameters of function, and not on the @router.get with the {}
    # example on this -> def track(request, track_id:int , title=""). track id is on the url because of line 15 but title is only for query (after the ?)
    # so /tracks/1?title="Circles"
    try:
        track = Track.objects.get(pk=track_id)
        return track
    except Track.DoesNotExist as e:
        return 404, {"message" : "Track doesn't exist"}