from dataclasses import field
from typing import List, ClassVar, Type, Optional

from marshmallow_dataclass import dataclass
from marshmallow import EXCLUDE, Schema


class MessageFrom:
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str]
    username: str

    class Meta:
        unknown = EXCLUDE


@dataclass
class MessageChat:
    id: int
    first_name: Optional[str]
    username: Optional[str]
    last_name: Optional[str]
    type: str
    title: Optional[str]

    class Meta:
        unknown = EXCLUDE


@dataclass
class Message:
    message_id: int
    from_: MessageFrom = field(metadata={'data_key': 'from'})
    chat: MessageChat
    date: int
    text: str

    class Meta:
        unknown = EXCLUDE


@dataclass
class UpdateOdj:
    update_id: int
    message: Message

    class Meta:
        unknown = EXCLUDE


@dataclass
class GetUpdatesResponse:
    ok: bool
    result: List[UpdateOdj]

    Schema: ClassVar[Type[Schema]] = Schema

    class Meta:
        unknown = EXCLUDE


@dataclass
class SendMessageResponse:
    ok: bool
    result: Message

    Schema: ClassVar[Type[Schema]] = Schema

    class Meta:
        unknown = EXCLUDE

