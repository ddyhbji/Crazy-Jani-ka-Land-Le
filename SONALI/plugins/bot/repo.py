from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝗧ᴇᴀᴍ 𝗣ᴜʀᴠɪ 𝗥ᴇᴘᴏs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

✰  @VIP_RAM_HACKER_PR  
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛ᴇʟᴘ", url="https://t.me/VIP_RAM_HACKER_PR"),
          InlineKeyboardButton("𐏓𐏓꯭꯭ ⃪꯭꯭꯭꯭꯭🇻꯭꯭꯭꯭꯭꯭꯭꯭꯭꯭ɪ֟፝ᴘ]꯭꯭꯭꯭᭄ ⃪꯭꯭꯭꯭꯭𝗝𝗮꯭꯭꯭꯭꯭𝗻𝗶]꯭꯭꯭꯭᭄𝅃꯭᳚𝆺꯭𝅥𝆺𝅥.🥀", url="https://t.me/VIP_RAM_HACKER_PR"),
          ],
               [
                InlineKeyboardButton("𝗝𝗮𝗻𝗶 𝗖𝗵𝗲𝘁𝗶𝗻𝗴", url=f"https://t.me/VIP_RAM_HACKER_PR"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/VIP_RAM_HACKER_PR"),

        ]]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://files.catbox.moe/u8ih4t.mp4",
        caption=start_txt,
        reply_markup=reply_markup
    )
