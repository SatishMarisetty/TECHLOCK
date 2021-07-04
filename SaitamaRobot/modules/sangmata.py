from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions, types

from SaitamaRobot.events import register as Eren
from SaitamaRobot import telethn as tbot
from SaitamaRobot.utils.telethonub import ubot


async def is_register_admin(chat, user):

    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):

        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerChat):

        ui = await tbot.get_peer_id(user)
        ps = (
            await tbot(functions.messages.GetFullChatRequest(chat.chat_id))
        ).full_chat.participants.participants
        return isinstance(
            next((p for p in ps if p.user_id == ui), None),
            (types.ChatParticipantAdmin, types.ChatParticipantCreator),
        )
    return None


async def silently_send_message(conv, text):
    await conv.send_message(text)
    response = await conv.get_response()
    await conv.mark_read(message=response)
    return response


@Eren(pattern="^/sg ?(.*)")
async def _(event):

    if event.fwd_from:

        return

    if event.is_group:
        if await is_register_admin(event.input_chat, event.message.sender_id):
            pass
        else:
            pass
    if not event.reply_to_msg_id:

        await event.reply("```Reply to any user message.```")

        return

    reply_message = await event.get_reply_message()

    if not reply_message.text:

        await event.reply("```reply to text message```")

        return

    chat = "Sangmatainfo_bot"
    uid = reply_message.sender_id
    reply_message.sender

    if reply_message.sender.bot:

        await event.edit("```Reply to actual users message.```")

        return
    id = f"/search_id {uid}"
    lol = await event.reply("```Processing```")

    async with ubot.conversation(chat) as conv:

        try:

            
                msg = await conv.send_message(id)
                response = await conv.get_response()
                respond = await conv.get_response()
                responds = await conv.get_response()
            except YouBlockedUserError:
                await lol.edit("Please unblock @sangmatainfo_bot and try again")
                return
            if (
                response.text.startswith("No records found")
                or respond.text.startswith("No records found")
                or responds.text.startswith("No records found")
            ):
                await lol.edit("No records found for this user")
                  return
            else:
                if response.text.startswith("🔗"):
                    await lol.edit(respond.message)
                    await lol.reply(responds.message)
                elif respond.text.startswith("🔗"):
                    await lol.edit(response.message)
                    await lol.reply(responds.message)
                else:
                    await lol.edit(respond.message)
                    await lol.reply(response.message)
    except TimeoutError:
        return await lol.edit("Error: @SangMataInfo_bot is not responding!.")
__help__ = """
 • `/sg` <reply to an user>:- Get Name history of an User.
"""

__mod_name__ = "SANGMATA"
