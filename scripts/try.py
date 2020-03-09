# cd to the tests directory
import sys
sys.path.insert(1, '../tests')

from bayfordbury.api import ArchiveApi
from credentials import api_key, observer_id

api = ArchiveApi(api_key=api_key, observer_id=observer_id)

# find Andromeda galaxy images
andromeda_images = api.search(
    ra=(00 + 42./60 + 44.330/3600) * 360/24,
    dec=41 + 16./60 + 7.50/3600,
    radius=0.1)

# use first image ID
image_id = andromeda_images[0]["id"]

# download image
image = api.download(image_id)

print(image.filename())
print(image[0].header[0:20])

import matplotlib.pyplot as plt
import numpy as np
plt.imshow(np.log10(image[0].data))
plt.show()
