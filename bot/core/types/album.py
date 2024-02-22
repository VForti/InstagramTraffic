import json
from typing import List, Optional, Dict, Type, Union

from aiogram.types import (
    PhotoSize, Video, Audio,
    Document, InputMediaPhoto,
    InputMediaVideo, InputMediaAudio,
    InputMediaDocument, Message
)
from pydantic import BaseModel

Media = Union[PhotoSize, Video, Audio, Document]
InputMedia = Union[
    InputMediaPhoto, InputMediaVideo,
    InputMediaAudio, InputMediaDocument
]
INPUT_TYPES: Dict[str, Type[InputMedia]] = {
    "photo": InputMediaPhoto,
    "video": InputMediaVideo,
    "audio": InputMediaAudio,
    "document": InputMediaDocument
}


class Album(BaseModel):
    photo: Optional[List[PhotoSize]] = None
    video: Optional[List[Video]] = None
    audio: Optional[List[Audio]] = None
    document: Optional[List[Document]] = None
    caption: Optional[str] = None
    messages: List[Message]

    @staticmethod
    def get_media_group(data: dict):
        return [
            INPUT_TYPES[type](media=id)
            for id, type in data.items()
        ]

    @property
    def media_types(self) -> List[str]:
        return [
            media_type for media_type in INPUT_TYPES
            if getattr(self, media_type)
        ]

    @property
    def as_media_group(self) -> List[InputMedia]:
        group = [
            INPUT_TYPES[media_type](type=media_type, media=media.file_id)
            for media_type in self.media_types
            for media in getattr(self, media_type)
        ]
        if group and self.caption:
            group[0].parse_mode = None
            group[0].caption = self.caption

        return group

    def as_media_group_2(self, caption) -> List[InputMedia]:
        group = [
            INPUT_TYPES[media_type](type=media_type, media=media.file_id)
            for media_type in self.media_types
            for media in getattr(self, media_type)
        ]
        if group:
            group[0].parse_mode = None
            group[0].caption = str(caption)

        return group

    def as_json(self):
        data = {}
        for media in self.as_media_group:
            data[media.media] = media.type._value_

        return json.dumps(data)