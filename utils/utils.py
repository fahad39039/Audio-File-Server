"""Python file for utiiteies."""
from models.models import Song, Podcast, Audiobook

mapping_dict = {'song': Song, 'podcast': Podcast, 'audiobook': Audiobook}


def row_to_dict(row):
    """'row_to_dict' method converts query row into dictionary."""
    return {col.name: str(getattr(row, col.name)) for col in row.__table__.columns}
