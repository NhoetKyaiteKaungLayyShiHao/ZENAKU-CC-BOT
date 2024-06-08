from plugins.admin.gc.gc_func import *
from pyrogram import Client, filters

@Client.on_message(filters.command('gc'))
async def cmd_gc(client, message):
    user_id = str(message.from_user.id)
    CEO = "7427691214"
    
    if user_id != CEO:
        resp = "𝗥𝗲𝗾𝘂𝗶𝗿𝗲 𝗢𝘄𝗻𝗲𝗿 𝗣𝗿𝗶𝘃𝗶𝗹𝗲𝗴𝗲𝘀 ⚠️"
        await message.reply_text(resp, message.id)
    else:
        resp = "𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗶𝗻𝗴.."
        send = await message.reply_text(resp, message.id)
        
        gift_codes = []
        
        for i in range(1, 11):
            resp = f"𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗶𝗻𝗴 {i}"
            send = await client.edit_message_text(message.chat.id, send.id, resp)
            
            gc_code = f"XCC-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
            insert_pm(gc_code)
            gift_codes.append(gc_code)
        
        final_resp = "𝗚𝗶𝗳𝘁𝗰𝗼𝗱𝗲 𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗲𝗱 ✅\n𝗔𝗺𝗼𝘂𝗻𝘁: 10\n\n"
        for i, gc_code in enumerate(gift_codes, 1):
            final_resp += f"➔ <code>{gc_code}</code>\n𝗩𝗮𝗹𝘂𝗲 : 𝟭𝟬𝟬 𝗖𝗿𝗲𝗱𝗶𝘁𝘀 + 𝗣𝗿𝗲𝗺𝗶𝘂𝗺\n\n"
        
        final_resp += "𝗙𝗼𝗿 𝗥𝗲𝗱𝗲𝗲𝗺𝘁𝗶𝗼𝗻 \n𝗧𝘆𝗽𝗲 /redeem"
        
        await client.edit_message_text(message.chat.id, send.id, final_resp)
      
