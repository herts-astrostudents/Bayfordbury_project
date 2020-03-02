from bayfordbury.api import ArchiveApi
from credentials import api_key, observer_id

api = ArchiveApi(api_key=api_key, observer_id=observer_id)

andromeda_images = api.search(
    ra=(00 + 42./60 + 44.330/3600) * 360/24,
    dec=41 + 16./60 + 7.50/3600,
    radius=0.1)

print(andromeda_images[0:2])