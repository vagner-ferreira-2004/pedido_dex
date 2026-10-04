from errors import NotFoundError
from models import ObjectFound


def getObjectFoundOrFail(session, id_object: int) -> ObjectFound:
    obj = session.get(ObjectFound, id_object)
    if obj is None:
        raise NotFoundError("Object found not found")
    return obj


def serializeObjectFound(obj: ObjectFound) -> dict:
    return {
        "id_object": obj.id_object,
        "id_user": obj.id_user,
        "id_category": obj.id_category,
        "id_location": obj.id_location,
        "status": obj.status,
        "found_date": obj.found_date.isoformat() if obj.found_date else None,
    }