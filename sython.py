from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
from config import *
import os
import logging
import aQYncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -
# - QYTHOM TEAM 
# -

QYthon1.start()



c = requests.session()
bot_username = '@eeobot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'
bot_usernameeeee = '@srwrot'
ownerhson_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [5755989428]




@qython1.on(events.NewMessage)
aQYnc def join_channel(event):
    try:
        await QYthon1(JoinChannelRequest("@QYTHON"))
    except BaseException:
        pass
        
@qython1.on(events.NewMessage)
aQYnc def join_channel(event):
    try:
        await QYthon1(JoinChannelRequest("@QaYTHON"))
    except BaseException:
        pass
      

        
        
        
@qython1.on(events.NewMessage(outgoing=False, pattern='.فحص'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')
        
        
@qython1.on(events.NewMessage(outgoing=False, pattern='/TEST'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')


@qython1.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⚝ مرحبا بك في اوامر سـايثـون بـوينت
 
============= • 𝐐𝐘 • ============

𝟏 - للدخول الى اوامر التجميع : .تجميع

𝟐 - للدخول الى اوامر التحـكم : .تحكم

𝟑 - للدخول الى اوامر مـمـيـزة : .مميزة

𝟒 - لـفـحص عـمـل الـســورس : .فحص

============= • 𝐐𝐘 • ============
**""")


@qython1.on(events.NewMessage(outgoing=False, pattern='.تجميع'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⚝ قـائمة جميع اوامر التجميع التي تحتاجها

============= • 𝐐𝐘 • ============

`/point1` :  تجميع نقاط بوت المليار
`/point2` : تجميع نقاط بوت الجوكر 
`/point3` :  تجميع نقاط بوت العقاب 
`/point4` :   تجميع نقاط بوت العرب 
note : تستخدم هذه الاوامر بأرسالها الى الحساب او بأرسالها الى مجموعة يوجد فيها الحساب

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/point + bot` : تجميع نقاط بوت غير موجود في القائمة

note : يوزر البوت المطلوب bot ضع مكان الـ

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/somy + bot + second` : تجميع لانهائي 

note : يوزر البوت المطلوب bot ضع مكان الـ 

note : عدد الثواني second ضع مكان الـ

note : ننصحك بوضع عدد الثواني 300

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/join` : الانضمام الى قنوات البوتات المذكورة

`/transfer` : الدخول لقائمة تحويل نقاط

`/infoacc` : الدخول لقائمة تحويل معلومات

`/lpoint` : لمغادرة جميع القنوات والمجموعات

============= • 𝐐𝐘 • ============
**""")

@qython1.on(events.NewMessage(outgoing=False, pattern='.تحكم'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⚝ قائمة اوامر التحكم بالحساب

============= • 𝐐𝐘 • ============

𝟏 - لتحويل اخر رسالة من مستخدم معين او بوت :

`/forward + يوزر الحساب او البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - لأرسال رسالة الى مستخدم معين او بوت : 

`/send + الرسالة + يوزر الحساب او البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟑 - لجعل الحساب ينقر على زر شفاف في بوت : 

`/button + رقم الزر الشفاف + يوزر البوت`

note :  قم بحساب رقم الزر الشفاف من العدد 0

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟒 - لجعل الحساب ينضم الى قناة او مجموعة

`/jn + يوزر القناة او المجموعة `

============= • 𝐐𝐘 • ============
**""")

@qython1.on(events.NewMessage(outgoing=False, pattern='.مميزة'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⚝ قائمة الاوامر المميزة 
============= • 𝐐𝐘 • ============

𝟏 - لتفعيل بوت عبر الدخول الى رابط الدعوه : 

`/bot + ايدي الحساب + يوزر البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - الامر التالي يحتوي على ملاحظات تحتاجها :

`/notes`

𝟑 - لجعل الحساب يصوت في مسابقة لايكات :

`/voice + موقع الرسالة + يوزر القناة`

note : موقع الرسالة يعني مثلا اذا كان الاسم في قناة المسابقة اخر اسم او اخر منشور فأن موقع الرسالة 1 وان تكن قبل الاخير فأن موقها 2 وهكذا  بقية المواقع 

𝟒 - لجعل الحساب يغادر قناة او مجموعة :

`/lv + يوزر القناة`

============= • 𝐐𝐘 • ============
**""")

@qython1.on(events.NewMessage(outgoing=False, pattern='/notes'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
1 - اذا كنت تريد التحكم بالحسابات في التحميع وتحويل النقاط ومعرفة معلومات كل حساب قم بأنشاء مجموعة خاصة وادخل الحسابات التي قمت بتنصيب لها السورس وارفع الحسابات الى مشرفين ثم استخدم اوامر التجميع 

2 - اذا كنت تريد جعل الحسابات تقوم بتجميع النقاط بدون توقف ونسبة قليلة من الحظر استخدم الامر : somy/ 
بأمكانك معرفة المزيد عن الامر وكيفية استخدامه في قائمة .تجميع ويستحسن عند استعمال الامر وضع عدد الثواني 300 اي يعني هذا عند حدوث خطأ في التجميع او انتهت القنوات فسوف يقوم السورس بالمحاولة في التجميع تلقائيا بعد مرور 300 اي خمس دقائق وسوف يقوم السورس بأخبارك جميع ماتم الوصول اليه من الامر ويمكنك ايقاف التجميع بأرسال .اعادة تشغيل 

3 - اذا كنت تريد تجميع نقاط بوتات التمويل بطريقة اعتيادية بدون المحاولة مرة اخرى تلقائيا يمكن استخدام الاوامر التالية [point , /point1/ , .....] يمكنك مراجعة الاوامر في القائمة .تجميع في اول قسمين من القائمة
**""")

@qython1.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
aQYnc def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")



@qython1.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
aQYnc def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗬𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗦𝗔𝗬𝗧𝗛𝗢𝗡𝗛    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟭 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗛𝗨𝗦𝗔𝗠.𝗙𝗔  ※

╰───⌯𝗦𝗬𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@qython1.on(events.NewMessage(outgoing=False, pattern='/point1'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")

        joinu = await QYthon1(JoinChannelRequest('QYTHON'))
        channel_entity = await QYthon1.get_entity(bot_username)
        await QYthon1.send_message(bot_username, '/start')
        await aQYncio.sleep(4)
        msg0 = await QYthon1.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await aQYncio.sleep(4)
        msg1 = await QYthon1.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await aQYncio.sleep(4)

            list = await QYthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await QYthon1.send_message(event.chat_id, f"تم الانتهاء من التجميع | QY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await QYthon1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await QYthon1(ImportChatInviteRequest(bott))
                msg2 = await QYthon1.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await QYthon1.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await QYthon1.send_message(event.chat_id, "تم الانتهاء من التجميع | QY")
        
@qython1.on(events.NewMessage(outgoing=False, pattern='/point2'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        joinu = await QYthon1(JoinChannelRequest('QYTHON'))
        channel_entity = await QYthon1.get_entity(bot_usernamee)
        await QYthon1.send_message(bot_usernamee, '/start')
        await aQYncio.sleep(4)
        msg0 = await QYthon1.get_messages(bot_usernamee, limit=1)
        await msg0[0].click(2)
        await aQYncio.sleep(4)
        msg1 = await QYthon1.get_messages(bot_usernamee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await aQYncio.sleep(4)

            list = await QYthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await QYthon1.send_message(event.chat_id, f"تم الانتهاء من التجميع | QY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await QYthon1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await QYthon1(ImportChatInviteRequest(bott))
                msg2 = await QYthon1.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await QYthon1.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await QYthon1.send_message(event.chat_id, "تم الانتهاء من التجميع | QY")

@qython1.on(events.NewMessage(outgoing=False, pattern='/point3'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        joinu = await QYthon1(JoinChannelRequest('QYTHON'))
        channel_entity = await QYthon1.get_entity(bot_usernameee)
        await QYthon1.send_message(bot_usernameee, '/start')
        await aQYncio.sleep(4)
        msg0 = await QYthon1.get_messages(bot_usernameee, limit=1)
        await msg0[0].click(2)
        await aQYncio.sleep(4)
        msg1 = await QYthon1.get_messages(bot_usernameee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await aQYncio.sleep(4)

            list = await QYthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await QYthon1.send_message(event.chat_id, f"تم الانتهاء من التجميع | QY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await QYthon1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await QYthon1(ImportChatInviteRequest(bott))
                msg2 = await QYthon1.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await QYthon1.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await QYthon1.send_message(event.chat_id, "تم الانتهاء من التجميع | QY")

@qython1.on(events.NewMessage(outgoing=False, pattern='/point4'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")

        joinu = await QYthon1(JoinChannelRequest('QYTHON'))
        channel_entity = await QYthon1.get_entity(bot_usernameeee)
        await QYthon1.send_message(bot_usernameeee, '/start')
        await aQYncio.sleep(4)
        msg0 = await QYthon1.get_messages(bot_usernameeee, limit=1)
        await msg0[0].click(2)
        await aQYncio.sleep(4)
        msg1 = await QYthon1.get_messages(bot_usernameeee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await aQYncio.sleep(4)

            list = await QYthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await QYthon1.send_message(event.chat_id, f"تم الانتهاء من التجميع | QY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await QYthon1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await QYthon1(ImportChatInviteRequest(bott))
                msg2 = await QYthon1.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await QYthon1.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await QYthon1.send_message(event.chat_id, "تم الانتهاء من التجميع | QY")


@qython1.on(events.NewMessage(outgoing=False, pattern='/point5'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")

        joinu = await QYthon1(JoinChannelRequest('QYTHON'))
        channel_entity = await QYthon1.get_entity(bot_usernameeeee)
        await QYthon1.send_message(bot_usernameeeee, '/start')
        await aQYncio.sleep(4)
        msg0 = await QYthon1.get_messages(bot_usernameeeee, limit=1)
        await msg0[0].click(2)
        await aQYncio.sleep(4)
        msg1 = await QYthon1.get_messages(bot_usernameeeee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await aQYncio.sleep(4)

            list = await QYthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await QYthon1.send_message(event.chat_id, f"تم الانتهاء من التجميع | QY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await QYthon1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await QYthon1(ImportChatInviteRequest(bott))
                msg2 = await QYthon1.get_messages(bot_usernameeeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await QYthon1.get_messages(bot_usernameeeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await QYthon1.send_message(event.chat_id, "تم الانتهاء من التجميع | QY")
        


@qython1.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
aQYnc def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await QYthon1(JoinChannelRequest('QYTHON'))
    channel_entity = await QYthon1.get_entity(bot_username)
    await QYthon1.send_message(bot_username, '/start')
    await aQYncio.sleep(4)
    msg0 = await QYthon1.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await aQYncio.sleep(4)
    msg1 = await QYthon1.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await aQYncio.sleep(4)

        list = await QYthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await QYthon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | QY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await QYthon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await QYthon1(ImportChatInviteRequest(bott))
            msg2 = await QYthon1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await QYthon1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await QYthon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | QY**")
    
    
    
@qython1.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
aQYnc def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await QYthon1(JoinChannelRequest('QYTHON'))
    channel_entity = await QYthon1.get_entity(bot_usernamee)
    await QYthon1.send_message(bot_usernamee, '/start')
    await aQYncio.sleep(4)
    msg0 = await QYthon1.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await aQYncio.sleep(4)
    msg1 = await QYthon1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await aQYncio.sleep(4)

        list = await QYthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await QYthon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | QY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await QYthon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await QYthon1(ImportChatInviteRequest(bott))
            msg2 = await QYthon1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await QYthon1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await QYthon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | QY**")

@qython1.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
aQYnc def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await QYthon1(JoinChannelRequest('QYTHON'))
    channel_entity = await QYthon1.get_entity(bot_usernameee)
    await QYthon1.send_message(bot_usernameee, '/start')
    await aQYncio.sleep(4)
    msg0 = await QYthon1.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await aQYncio.sleep(4)
    msg1 = await QYthon1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await aQYncio.sleep(4)

        list = await QYthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await QYthon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | QY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await QYthon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await QYthon1(ImportChatInviteRequest(bott))
            msg2 = await QYthon1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await QYthon1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await QYthon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | QY**")


@qython1.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
aQYnc def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await QYthon1(JoinChannelRequest('QYTHON'))
    channel_entity = await QYthon1.get_entity(bot_usernameeee)
    await QYthon1.send_message(bot_usernameeee, '/start')
    await aQYncio.sleep(4)
    msg0 = await QYthon1.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await aQYncio.sleep(4)
    msg1 = await QYthon1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await aQYncio.sleep(4)

        list = await QYthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await QYthon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | QY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await QYthon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await QYthon1(ImportChatInviteRequest(bott))
            msg2 = await QYthon1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await QYthon1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await QYthon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | QY**")


##########################################

@qython1.on(events.NewMessage(outgoing=False, pattern='^/point (.*)'))
aQYnc def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        
        joinu = await QYthon1(JoinChannelRequest('QYTHON'))
        channel_entity = await QYthon1.get_entity(pot)
        await QYthon1.send_message(pot, '/start')
        await aQYncio.sleep(4)
        msg0 = await QYthon1.get_messages(pot, limit=1)
        await msg0[0].click(2)
        await aQYncio.sleep(4)
        msg1 = await QYthon1.get_messages(pot, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await aQYncio.sleep(4)

            list = await QYthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await QYthon1.send_message(event.chat_id, f"تم الانتهاء من التجميع | QY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await QYthon1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await QYthon1(ImportChatInviteRequest(bott))
                msg2 = await QYthon1.get_messages(pot, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await QYthon1.get_messages(pot, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await QYthon1.send_message(event.chat_id, "تم الانتهاء من التجميع | QY")
        
@qython1.on(events.NewMessage(outgoing=False, pattern=r'^/bot (.*) (.*)'))
aQYnc def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = event.pattern_match.group(2) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await QYthon1.send_message(bots,f'/start {ids}')
     sleep(6)
    msg = await QYthon1.get_messages(bots, limit=2)
    await msg[1].forward_to(ownerhson_id)

@qython1.on(events.NewMessage(outgoing=False, pattern='^/collect (.*)'))
aQYnc def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply("**⛦ جاري بدء عملية التجميع اللانهائية ⛦**")
                joinu = await QYthon1(JoinChannelRequest('QYTHON'))
                channel_entity = await QYthon1.get_entity(pot)
                await QYthon1.send_message(pot, '/start')
                await aQYncio.sleep(2)
                msg0 = await QYthon1.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await aQYncio.sleep(2)
                msg1 = await QYthon1.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 1
                for i in range(100):
                    await aQYncio.sleep(2)

                    list = await QYthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                        await QYthon1.send_message(event.chat_id, f"**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await QYthon1(JoinChannelRequest(url))
                        except:
                            bott = url.split('/')[-1]
                            await QYthon1(ImportChatInviteRequest(bott))
                        msg2 = await QYthon1.get_messages(pot, limit=1)
                        await msg2[0].click(text='تحقق')
                        chs += 1
                        await event.edit(f"**تم الانضمام في {chs} قناة**")
                    except:
                        msg2 = await QYthon1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 1
                        await event.edit(f"**القناة رقم {chs}**")
                        await aQYncio.sleep(60)

                await QYthon1.send_message(event.chat_id, "**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            pass


@qython1.on(events.NewMessage(outgoing=False, pattern='^/somy (.*) (.*)'))
aQYnc def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            numw = int(event.pattern_match.group(2))
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply(f"**✣ حسنا سوف اقوم بعملية التجميع \n✣ عدد الثواني بين كل محاولة : {numw}\n✣ التجميع من بوت : @{pot}**")

                joinu = await QYthon1(JoinChannelRequest('QYTHON'))
                channel_entity = await QYthon1.get_entity(pot)
                await QYthon1.send_message(pot, '**جاري بدأ عملية التجميع بواسطة سايثون**')
                await QYthon1.send_message(pot, '/start')
                await aQYncio.sleep(2)
                msg0 = await QYthon1.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await aQYncio.sleep(2)
                msg1 = await QYthon1.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 0
                for i in range(100):
                    await aQYncio.sleep(2)

                    list = await QYthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                        await QYthon1.send_message(event.chat_id, f"**✣ حسنا سوف اقوم بعملية التجميع \n✣ عدد الثواني بين كل محاولة : {numw}\n✣ التجميع من بوت : @{pot}**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await QYthon1(JoinChannelRequest(url))
                        except:
                            QYth = url.split('/')[-1]
                            await QYthon1(ImportChatInviteRequest(QYth))
                        msg2 = await QYthon1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 10
                        await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")
                    except:
                        msg2 = await QYthon1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 0
                        await event.reply(f"""**✣ للأسف لم تحصل على نقاط في هذه المحاولة
✣ لأنني وجدت قناة خاصة قمت بتخطيها
✣ البوت التي حدث فيه الخطأ: {pot}**""")
                        
                await QYthon1.send_message(event.chat_id, f"**✣ عذرا نفذت قنوات البوت \n✣ لكن سوف اعاود المحاولة بعد {numw} ثانية**")
                await aQYncio.sleep(numw)
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            await aQYncio.sleep(numw)


@qython1.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        await event.reply("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")
        await QYthon1.disconnect()
        await QYthon1.send_message(event.chat_id, "تم اعادة تشغيل السورس ")
        


@qython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
aQYnc def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await QYthon1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await QYthon1.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await QYthon1.send_message(bot_username, pt)
    sleep(4)
    msg = await QYthon1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
aQYnc def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await QYthon1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await QYthon1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await QYthon1.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await QYthon1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@qython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
aQYnc def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await QYthon1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await QYthon1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await QYthon1.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await QYthon1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
aQYnc def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await QYthon1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await QYthon1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await QYthon1.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await QYthon1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await QYthon1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await QYthon1.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await QYthon1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await QYthon1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await QYthon1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await QYthon1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@qython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await QYthon1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await QYthon1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await QYthon1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await QYthon1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await QYthon1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await QYthon1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@qython1.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await QYthon1.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await QYthon1(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                




@qython1.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await QYthon1.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    
    
    

@qython1.on(events.NewMessage(outgoing=False, pattern='/transfer'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")



@qython1.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @ZMMBOT - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @MARKTEBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")


@qython1.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
aQYnc def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await QYthon1.send_message(userbt, '/start')
     sleep(2)
    msg1 = await QYthon1.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await QYthon1.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")
        

@qython1.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
aQYnc def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sing = await QYthon1.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر رسالة\n❈ من المستخدم {userbott}**")
        msgs = await QYthon1.get_messages(userbott, limit=1)
        if msgs:
            await msgs[0].forward_to(ownerhson_id)
       
@qython1.on(events.NewMessage(outgoing=False, pattern='/join'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await QYthon1.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await QYthon1(JoinChannelRequest('d3boot_7'))
        joinw = await QYthon1(JoinChannelRequest('Fvvvv'))
        joine = await QYthon1(JoinChannelRequest('DzDDDD'))
        joinr = await QYthon1(JoinChannelRequest('botbillion'))
        joint = await QYthon1(JoinChannelRequest('zzzzzz1'))
        joiny = await QYthon1(JoinChannelRequest('zzzzzz'))
        joini = await QYthon1(JoinChannelRequest('zz_MX'))
        joino = await QYthon1(JoinChannelRequest('lI7777Il'))
        joinp = await QYthon1(JoinChannelRequest('KTTTT'))
        joina = await QYthon1(JoinChannelRequest('RRXFR'))
        sendd = await QYthon1.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@qython1.on(events.NewMessage(outgoing=False, pattern='/jn (.*)'))
aQYnc def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await QYthon1.send_message(event.chat_id,f"**جاري الانضمام في القناة @{usercht}**")
        joinch = await QYthon1(JoinChannelRequest(usercht))
        sendy = await QYthon1.send_message(event.chat_id,f"**تم الانضمام في القناة @{usercht}**")

@qython1.on(events.NewMessage(outgoing=False, pattern='/lv (.*)'))
aQYnc def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await QYthon1.send_message(event.chat_id,f"**جاري مغادرة القناة  @{usercht}**")
        joinch = await QYthon1(LeaveChannelRequest(usercht))
        sendy = await QYthon1.send_message(event.chat_id,f"**تم مغادرة القناة @{usercht}**")

@qython1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await QYthon1.send_message(ownerhson_id,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await QYthon1.get_entity(chn)
        join = await QYthon1(JoinChannelRequest(chn))
        joion = await QYthon1(JoinChannelRequest('QYTHON'))
        somy = await QYthon1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await QYthon1.send_message(ownerhson_id,'**⚝ قمت بالانضمام والتصويت بنجاح**')

ownerhson_ids = 5755989428
@qython1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
aQYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_ids:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await QYthon1.send_message(ownerhson_ids,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await QYthon1.get_entity(chn)
        join = await QYthon1(JoinChannelRequest(chn))
        joion = await QYthon1(JoinChannelRequest('QYTHON'))
        somy = await QYthon1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await QYthon1.send_message(ownerhson_ids,'**⚝ قمت بالانضمام والتصويت بنجاح**')


print("💠 QYthon Userbot Running 💠")
QYthon1.run_until_disconnected()


#code skip accumulate points by t.me.QATHON thank you my bro
