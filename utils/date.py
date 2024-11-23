from datetime import datetime

# Mendapatkan tanggal dan waktu saat ini
cur_date = datetime.now()

def datetime_from_string(date: str) -> datetime:
    """
    Mengubah format ke datetime dari string
    """
    return datetime.strptime(date, '%Y-%m-%d')

def check_valid_date(date: str) -> bool:
    """
    Mengecek apakah tanggal yang diberikan sudah lewat atau belum
    """
    return datetime_from_string(date) >= cur_date
