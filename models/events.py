events = [
    {
        'id': 1,
        'event_title': 'PyCon APAC 2024',
        'description': 'Python Conference Asia Pacific 2024 in Yogyakarta',
        'location': 'Yogyakarta, Indonesia',
        'date': '2024-11-25',
        'participants': 1,
    },
    {
        'id': 2,
        'event_title': 'PyCon Indonesia 2023',
        'description': 'Python Conference Indonesia 2023 in Bandung',
        'location': 'Bandung, Indonesia',
        'date': '2023-10-25',
        'participants': 0,
    },
    {
        'id': 3,
        'event_title': 'Python Jogja December Meetup',
        'description': 'Python Jogja Meetup Lightning Talk',
        'location': 'Universitas Teknologi Yogyakarta',
        'date': '2024-12-27',
        'participants': 0,
    },
]


def get_events() -> list[dict]:
    """
    Mendapatkan semua event yang ada
    """
    return events


def get_event_by_id(event_id: int) -> dict | None:
    """
    Mendapatkan event berdasarkan ID
    """
    for event in events:
        if event['id'] == event_id:
            return event
    return None


def increase_participant_by_id(event_id: int) -> True:
    """
    Menambahkan jumlah peserta pada event berdasarkan ID
    """
    for event in events:
        if event['id'] == event_id:
            event['participants'] += 1
    return True
