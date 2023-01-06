from dataclasses import field
from typing import List, ClassVar, Type, Optional

from marshmallow_dataclass import dataclass
from marshmallow import EXCLUDE, Schema


@dataclass
class MessageFrom:
    id: int
    is_bot: bool
    first_name: str
    username: str
    last_name: Optional[str] = field(default=None)


    class Meta:
        unknown = EXCLUDE


@dataclass
class MessageChat:
    id: int
    type: str
    first_name: Optional[str] = field(default=None)
    username: Optional[str] = field(default=None)
    last_name: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)

    class Meta:
        unknown = EXCLUDE




@dataclass
class Message:
    message_id: int
    from_: MessageFrom = field(metadata={'data_key': 'from'})
    chat: MessageChat
    date: int
    text: Optional[str] = field(default=None)

    class Meta:
        unknown = EXCLUDE


@dataclass
class UpdateObj:
    """Telegram API: https://core.telegram.org/bots/api#getting-updates"""
    update_id: int
    message: Optional[Message] = field(default=None)

    class Meta:
        unknown = EXCLUDE

@dataclass
class GetUpdatesResponse:
    ok: bool
    result: List[UpdateObj]

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