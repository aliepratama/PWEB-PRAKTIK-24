from models.events import get_event_by_id, increase_participant_by_id
from models.users import decrease_quota_by_id

bookings = [
    {
        'id': 1,
        'user_id': 1,
        'event_id': 1,
    },
]


def get_bookings() -> list[dict]:
    """
    Mendapatkan semua data booking
    """
    return bookings


def get_bookings_by_user_id(user_id: int) -> list[dict]:
    """
    Mendapatkan data booking berdasarkan user_id
    """
    temp = []
    for booking in bookings:
        if booking['user_id'] == user_id:
            temp.append(booking)
    return temp


def add_booking(user_id: int, event_id: int) -> True:
    """
    Menambahkan data booking
    """
    new_booking = {
        'id': len(bookings) + 1,
        'user_id': user_id,
        'event_id': event_id
    }
    bookings.append(new_booking)
    decrease_quota_by_id(user_id)
    increase_participant_by_id(event_id)
    return True


def display_bookings_by_user_id(user_id: int) -> list[dict]:
    """
    Menampilkan data booking berdasarkan user_id
    """
    temp = []
    for booking in bookings:
        if booking['user_id'] == user_id:
            event = get_event_by_id(booking['event_id'])
            if event is not None:
                temp.append({
                    'id': booking['id'],
                    'event_title': event['event_title'],
                    'date': event['date']
                })
    return temp
