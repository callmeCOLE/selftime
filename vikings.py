from pyrogram import Client, filters,idle,errors
import os
from time import sleep
import json
VIKING = "Developed By Vikings"
api_id = 6332243
api_hash = '2cb27f7fa1f216b1494e31015dbbd8e3'
app = Client('THOR', api_id=api_id, api_hash=api_hash)
apps = {}
aDd = False
new_acc = None

with open('accs.json', 'r') as fp:
    accs = json.load(fp)
accs = {k: v for k, v in accs.items()}

with open('accs_num.json', 'r') as fp:
    accs_num = json.load(fp)
accs_num = {k: v for k, v in accs_num.items()}

with app:
    bot_name = app.get_me().first_name
    if "-vᴀικιɴԍ" not in bot_name:
        app.update_profile(first_name=f"{bot_name} -vᴀικιɴԍ")

commands = ["Set","Attack","add","Code","Stopatk","Alone"]
texts = ["Sʜᴏᴀʀᴇ titap Sᴀʙᴛ sʜᴏᴅ!","titap ɪs ᴄᴏᴍɪɴɢ ᴍᴏᴛʜᴇʀ ғᴜᴄᴋᴇʀ⚡️","تبر شما مناسب است 🪓","Bᴋᴏɴᴇ Jᴀᴅɪᴅ Bᴇ Aʀᴍʏ titap Pʏᴠᴀsᴛ!🖤","Lᴏᴛғᴀɴ Pᴀss Rᴏ Vᴀʀᴇᴅ Kᴏɴ!","Aʀᴍʏ titap Mᴏᴛᴠᴀǫғ Sʜᴏᴅ!⛔️","Cᴏᴅᴇ Rᴏ Vᴀʀᴇᴅ Kᴏɴ!","Aʙʟᴀʜ Iɴ Cʜᴇ Hᴀᴋᴛɪʏᴇ Pᴍ Aᴢ @UseTGXBot Iɴ Bᴏᴛ Fᴏʀ Bᴅᴇ","Cᴏᴅᴇ B Dᴏʀᴏsᴛɪ Vᴀʀᴅ Sʜᴅ"]
delay_each_atk = 15
delay_time = 3


Banner = {}
attacker = False
name = '';Id='';Hash=''
phhash='';phnum=''

# @app.on_message(filters.command("HeLp",prefixes=""))
# def help(c,m):
#     m.reply_text(helpMSG)

@app.on_message(filters.command([commands[5]],prefixes=""))
def ping(client,message):
    app.send_message(message.chat.id,'khafe')
    num = 0
    for acc in accs:
        accunt = Client(accs[acc][2], accs[acc][0], accs[acc][1])
        accunt.start()
        num += 1
        accunt.send_message(message.chat.id,f'{num} - khafe')

@app.on_message(filters.command("Help",prefixes=""))
def helpmsg(c,m):
    MesG = """‣ Set - ثبت بنر
‣ Get - دیدن بنر
‣ deL - پاکسازی بنر
‣ Add - افزودن اکانت
‣ Code - ارسال کد
‣ Army - بررسی اکانت ها
‣ Attack -  شروع اتک تکی
‣ stopatk - توقف اتک
‣ delAll - حذف تمام اکانت ها
‣ cLear - حذف یک اکانت
‣ Setname - تنظیم اسم اکانت ها
‣ Pass - رمز دوم

✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵

𖣔 titapppp 𖣔"""
    m.reply_text(MesG)
@app.on_message(filters.command([commands[0]],prefixes="") & filters.group)
def setBanner(client,message):
    global Banner
    if message.reply_to_message:
        Banner['chat'] = message.reply_to_message.chat.id
        Banner['message'] = message.reply_to_message.message_id
        client.send_message(message.chat.id,texts[0])
    else:
        client.send_message(message.chat.id,'لطفا این پیام را به بنر مورد نظر ریپلای کنید')

@app.on_message(filters.command(['Get'],prefixes="") & filters.group)
def banner(client,message):
    global Banner
    try:
        client.send_message(message.chat.id,'Sʜᴏᴀʀ:')
        client.forward_messages(message.chat.id,Banner['chat'],Banner['message'])
    except:
        client.send_message(message.chat.id,'Kᴏsᴋʜᴏʟ banner Sᴀʙᴛ Nᴋᴀʀᴅɪ!')

@app.on_message(filters.command([commands[1]],prefixes="") & filters.group)
def attack(client,message):
    global Banner
    global attacker,delay_each_atk,delay_time
    msg = "**افراد گاییده شده:**\n"
    if Banner == {}:
        client.send_message(message.chat.id,'Bᴀ Dᴀsᴛᴏʀᴇ **Set** Yᴇ Bᴀɴɴᴇʀ Sᴀʙᴛ Kᴏɴ😐')
    else:
        attacker = True
        delayer = 0
        success = 0
        rounds = 0
        client.send_message(message.chat.id,texts[1])
        if message.reply_to_message:
            users = [i for i in message.reply_to_message.text.split() if '@' in i]
            for acc in accs:
                accunt = Client(accs[acc][2], accs[acc][0], accs[acc][1])
                accunt.start()
                mesg = accunt.send_message(message.chat.id, msg)
                for member in users:
                    if attacker == True:
                        try:
                            accunt.copy_message(member,Banner['chat'],Banner['message'])

                            success += 1
                            delayer += 1
                            msg += f"{member}  \n"
                            mesg.edit_text(msg)
                        except Exception as e:
                            try:
                                
                                if "[420 FLOOD_WAIT_X]" in str(e):
                                    app.send_message(message.chat.id,f" {str(e)[30:33]} Sᴀɴɪʏᴇ Tᴀᴋʜɪʀ Dᴀʀ Hᴀᴍʟᴇ! ")
                                    sleep(int(str(e).split()[5]))
                                elif "[403 CHAT_WRITE_FORBIDDEN]" in str(e):
                                    app.send_message(message.chat.id,f"{member} کیرمو خورد و رفت")
                                elif "[400 USERNAME_NOT_OCCUPIED]" in str(e):
                                    app.send_message(message.chat.id, f"ID {member} Mᴏɴᴛᴢᴇʀᴇ Qᴏғʟ Sʜᴏᴅɴ Asᴛ!🚷")
                                elif "[400 USERNAME_INVALID]" in str(e):
                                    app.send_message(message.chat.id, f"{member} این آیدی کصشره خوشم نیومد")
                                elif "[400 PEER_FLOOD]" in str(e):
                                    app.send_message(message.chat.id,f"اکانت {acc} در اتک به {member} به دلیل ریپورت شدن به مشکل برخورد")
                                    break
                                else:
                                    app.send_message(message.chat.id,f"not ok for {member} because {e}")
                            except:
                                pass
                        if delayer == delay_each_atk:
                            sleep(delay_time)
                            delayer = 0
                    else:
                        return
                try:
                    app.send_message(message.chat.id,f"Gᴏʀɢ {acc} Lɪsᴛ Rᴏ Bᴀ Mᴏᴠᴀғǫɪʏᴀᴛ Tᴀᴍᴏᴍ Kᴀʀᴅ😈")
                except:
                    pass
                rounds += 1
            client.send_message(message.chat.id,'''اتک به پایان رسید :

به {} نفر {} بار اتک زده شد ({} دور)'''.format(len(users),success,rounds))

            attacker = False


@app.on_message(filters.command(['Del'],prefixes="") & filters.group)
def clear(client,message):
    global Banner
    if Banner == {}:
        client.send_message(message.chat.id,'Bᴀ Dᴀsᴛᴏʀᴇ **Set** Yᴇ Bᴀɴɴᴇʀ Sᴀʙᴛ Kᴏɴ🤝')
    else:
        Banner = {}
        client.send_message(message.chat.id,'Sʜᴏᴀʀᴇ titap Pᴀᴋ Sʜᴏᴅ🏴‍☠️')

@app.on_message(filters.command(['Army'],prefixes="") & filters.group)
def acc(client,message):
    global apps
    accounts = ''
    num = 0
    for acc in accs_num:
        num += 1
        accounts += f"{num} - <code>{accs_num[acc]}</code>\n"
    client.send_message(message.chat.id,'''**Tᴇᴅᴀᴅ Gᴏʀɢ Hᴀʏᴇ Aᴍᴀᴅᴇ titap\n {}\n**Num:**\n{}'''.format(accounts,len(apps)))

@app.on_message(filters.command([commands[4]],prefixes="") & filters.group)
def stopAttack(client,message):
    global attacker
    if attacker == True:
        client.send_message(message.chat.id,texts[5])
        attacker = False
    else:
        client.send_message(message.chat.id,'Aʀᴍʏ titap Mᴀsʜɢʜᴏʟ Ks Kʀᴅɴᴇ')

@app.on_message(filters.command([commands[2]],prefixes="") & filters.group)
def add(client,message):
    global name,Id,Hash,phhash,phnum,name,accs,new_acc,accs_num
    if message.reply_to_message and message.reply_to_message.forward_from and message.reply_to_message.forward_from.id == 542422944:
        api_text = message.reply_to_message.text.split("\n")
        phnum = api_text[0].split("Phone Number: ")[1]
        Id = api_text[3].split("APP ID: ")[1]
        Hash = api_text[4].split("API HASH: ")[1]
        name = phnum
        new_acc = Client(name, int(Id), Hash,force_sms=False)
        accs[name] = []
        accs_num[name] = phnum
        accs[name].insert(0, Id)
        accs[name].insert(1, Hash)
        with open("accs.json", "w") as fp:
            json.dump(accs, fp)
        with open('accs_num.json', 'w') as fp:
            json.dump(accs_num, fp)
        new_acc.connect()

        phhash = new_acc.send_code(phnum)
        print(phhash)
        client.send_message(message.chat.id, texts[6])
    elif message.reply_to_message and message.reply_to_message.forward_from and message.reply_to_message.forward_from.id == 1188899451:
        api_text = message.reply_to_message.text.split("\n")
        Id = api_text[1].split("APP ID: ")[1]
        Hash = api_text[2].split("API HASH: ")[1]
        phnum = message.command[1]
        name = message.command[1]
        new_acc = Client(name, int(Id), Hash,force_sms=False)
        accs[name] = []
        accs[name].insert(0, Id)
        accs[name].insert(1, Hash)
        with open("accs.json", "w") as fp:
            json.dump(accs, fp)
        new_acc.connect()
        phhash = new_acc.send_code(phnum)
        print(phhash)
        client.send_message(message.chat.id, texts[6])
    else:
        message.reply_text(texts[7])

@app.on_message(filters.command(['code'],prefixes=""))
def code(client,message):
    global phhash,new_acc_name,phnum,accs,accs_num
    code_info = message.text.split(" ")
    acc_code = code_info[1].split("-")
    code = acc_code[0] + acc_code[1]
    try:
        acc_pass = code_info[2]
    except IndexError:
        pass
    try:
        new_acc.sign_in(phnum,phhash.phone_code_hash,code)
    except errors.PhoneCodeExpired:
        message.reply_text("Cᴏᴅᴇ Nᴀᴍᴏᴛᴀʙᴀʀ Asᴛ")
        return
    except errors.PhoneCodeInvalid:
        message.reply_text("Cᴏᴅᴇ Esʜᴛᴇʙᴀʜ Vᴀʀᴇᴅ Sʜᴅᴇ Asᴛ")
        return
    except errors.SessionPasswordNeeded:
        message.reply_text("Lᴏᴛғᴀɴ Pᴀss Rᴏ Vᴀʀᴇᴅ Kɴ")
    try:
        acc_sesion = new_acc.export_session_string()
        accs[name].insert(2, acc_sesion)
        with open("accs.json", "w") as fp:
            json.dump(accs, fp)
        accs_num[name] = phnum
        with open('accs_num.json', 'w') as fp:
            json.dump(accs_num, fp)
        new_acc.update_profile(bio="TITAP")
    except:
        pass



@app.on_message(filters.command(["pass"],prefixes=""))
def paswrd(c,m):
    global new_acc,name,accs,accs_num
    acc_pass = m.text.split(" ")
    try:
        new_acc.check_password(acc_pass[1])
    except errors.SessionPasswordNeeded:
        m.reply_text("پسورد اشتباه است لطفا دوباره امتحان کنید")
    except errors.PasswordRequired:
        m.reply_text("پسورد اشتباه است لطفا دوباره امتحان کنید")
    except errors.PasswordHashInvalid:
        m.reply_text("پسورد اشتباه است لطفا دوباره امتحان کنید")
    try:
        new_acc.update_profile(bio="TITAP")
        acc_sesion = new_acc.export_session_string()
        accs[name].insert(2, acc_sesion)
        with open("accs.json", "w") as fp:
            json.dump(accs, fp)
        accs_num[name] = phnum
        with open('accs_num.json', 'w') as fp:
            json.dump(accs_num, fp)
        new_acc.update_profile(bio="TITAP")
        c.send_message(m.chat.id, texts[3])
    except:
        pass

@app.on_message(filters.command(['DelAll'],prefixes="") & filters.group)
def deleteAll(client,message):
    global accs_num,accs
    accs.clear()
    accs_num.clear()
    with open('accs_num.json', 'w') as fp:
        json.dump(accs_num, fp)
    with open("accs.json", "w") as fp:
        json.dump(accs, fp)
    client.send_message(message.chat.id,'''Pᴀᴋsᴀᴢɪ Sʜᴏᴅ!''')


@app.on_message(filters.command(['Del'],prefixes="") & filters.group)
def deleteA(client,message):
    global accs,accs_num
    try:
        del accs[message.command[1]]
        del accs_num[message.command[1]]
        with open("accs.json", "w") as fp:
            json.dump(accs, fp)
        with open('accs_num.json', 'w') as fp:
            json.dump(accs_num, fp)
        message.reply_text("Aᴄᴄᴏᴜɴᴛ Hᴀᴢғ Sʜᴏᴅ")
    except :
        client.send_message(message.chat.id,'Pᴇʏᴅᴀ Nᴀsʜᴏᴅ')

if VIKING == "Developed By Vikings":
    FARHAN = True
else:
    FARHAN = False
@app.on_message(filters.command("SetName",prefixes=""))
def setname(client,message):
    global accs,accs_num
    try:
        name = message.command[1]
        for acc in accs:
            accunt = Client(accs[acc][2],accs[acc][0],accs[acc][1])
            accunt.start()
            accunt.update_profile(first_name=name)
        message.reply_text("""Esᴍ Gᴏʀɢᴀʏᴇ TITAP Aᴠᴀᴢ Sʜᴅ""")
    except IndexError:
        message.reply_text("اسم مورد نظرتو بزن!")

@app.on_message(filters.command("GetList",prefixes="") & filters.group)
def getList(c,m):
    global name
    try:
        acc_name = m.command[2]
        gp_link = m.command[1]
    except KeyError:
        m.reply_text("یادت نره اول لینک گپ بعدش اسم اکانت رو وارد کنی.")
        return

    accunt = Client(accs[acc_name][2], accs[acc_name][0], accs[acc_name][1])
    accunt.start()
    try:
        gpe = accunt.join_chat("{}".format(gp_link))
        gpe = accunt.get_chat("{}".format(gp_link))
        gp_id = gpe.id
    except errors.UserAlreadyParticipant:
        gpe = accunt.get_chat("{}".format(gp_link))
    except errors.InviteHashExpired:
        m.reply_text('بن بودم نشد')
    except errors.Flood:
        m.reply_text('فلاد خوردم')
        return
    accunt.send_sticker(m.chat.id, "CAADBAADGggAArhpKVBYg-r8Rxp36hYE")
    members = accunt.iter_chat_members(gpe.id,limit=1000)
    number = 0
    LiNum = 1
    MesG = f"List{LiNum} - {gpe.title}"
    for member in members:
        user_name = member.user.username
        user_bot = member.user.is_bot
        user_status = member.user.status
        if user_name != None and user_bot is False and user_status != (
                "long_time_ago" or "within_month" or "within_week" or None) and member.user.is_self is False:
            number += 1
            MesG += f"{number} - @{user_name}\n"
            if number == 45:
                LiNum += 1
                accunt.send_message(m.chat.id,MesG)
                MesG = f"List{LiNum} - {gpe.title}\n"
                number = 0
    accunt.send_message(m.chat.id,MesG)

@app.on_message(filters.command("AddBzn",prefixes="") & filters.group)
def addbzn(c,m):
    global aDd
    acc = m.command[1]
    gp_id = m.command[2]
    number = 0
    msg = "okys :\n"
    aDd = True
    ids = [i for i in m.reply_to_message.text.split() if "@" in i]
    print(ids)
    accunt = Client(accs[acc][2], accs[acc][0], accs[acc][1])
    accunt.start()
    for user in ids:
        if aDd:
            sleep(5)
            try:
                accunt.add_chat_members(int(gp_id),user)
                number += 1
                msg += f"{number} - {user}\n"
            except errors.UsernameInvalid:
                m.reply_text(f"id {user} vojod ndre")
                continue
            except errors.UserBannedInChannel:
                m.reply_text(f"id {user} az gp bane")
                continue
            except errors.UsernameNotModified:
                m.reply_text(f"id {user} kasi ngrefte")
                continue
            except errors.FloodWait:
                m.reply_text(f"flood khordam")
                m.reply_text(msg)
                return
            except errors.LimitInvalid:
                m.reply_text(f"rep shodam")
                m.reply_text(msg)
                return
            except errors.Forbidden:
                m.reply_text(f"{user} addsh bastas")
                continue
            except errors.UserNotMutualContact:
                m.reply_text(f"{user} qablan left dde save nist add knish")
                continue
            except errors.Flood:
                m.reply_text(f"flood khordam engar")
                m.reply_text(msg)
                return
            except Exception as e:
                m.reply_text(f"not ok for {user} caus {e}")
                continue
            m.reply_text(msg)
    else:
        m.reply_text(msg)

@app.on_message(filters.command("StopAdd",prefixes=""))
def stopadd(client,message):
    global aDd
    aDd = False
    message.reply_text("ادد نمیزنم دیگ")


@app.on_message(filters.command("ForMasih", prefixes="") & filters.group)
def atck(client, message):
    global Banner
    global attacker, delay_each_atk, delay_time
    msg = "**افراد گاییده شده:**\n"
    if Banner == {}:
        client.send_message(message.chat.id, 'با کدوم تبر بریم جنگ؟ با دستور **Set** تبرتو ثبت کن!')
    else:
        attacker = True
        delayer = 0
        success = 0
        rounds = 0
        client.send_message(message.chat.id, texts[1])
        if message.reply_to_message:
            users = [i for i in message.reply_to_message.text.split() if '@' in i]
            for member in users:
                msg = f"start for {member}:\n"
                mesg = app.send_message(message.chat.id, msg)
                for acc in accs:
                    accunt = Client(accs[acc][2], accs[acc][0], accs[acc][1])
                    accunt.start()
                    if attacker == True:
                        try:
                            accunt.copy_message(member, Banner['chat'], Banner['message'])

                            success += 1
                            delayer += 1
                            msg += f"{acc}  \n"
                            mesg.edit_text(msg)
                        except Exception as e:
                            try:

                                if "[420 FLOOD_WAIT_X]" in str(e):
                                    app.send_message(message.chat.id, f" {str(e)[30:33]} ثانیه تاخیر در جنگ ")
                                    sleep(int(str(e).split()[5]))
                                elif "[403 CHAT_WRITE_FORBIDDEN]" in str(e):
                                    app.send_message(message.chat.id, f"{member} کونشو گزاشت کف‌ جنگو فرار کرد")
                                elif "[400 USERNAME_NOT_OCCUPIED]" in str(e):
                                    app.send_message(message.chat.id, f"آیدی  {member}  منتظر قفل شدن است❌!")
                                elif "[400 USERNAME_INVALID]" in str(e):
                                    app.send_message(message.chat.id, f"{member} این آیدی کصشره خوشم نیومد")
                                elif "[400 PEER_FLOOD]" in str(e):
                                    app.send_message(message.chat.id,
                                                     f"اکانت {acc} در اتک به {member} به دلیل ریپورت شدن به مشکل برخورد")
                                    break
                                else:
                                    app.send_message(message.chat.id, f"not ok for {member} because {e}")
                            except:
                                pass
                        if delayer == delay_each_atk:
                            sleep(delay_time)
                            delayer = 0
                    else:
                        return
                try:
                    pass
                except:
                    pass
                rounds += 1
            client.send_message(message.chat.id, '''اتک به پایان رسید :

به {} نفر {} بار اتک زده شد ({} دور)'''.format(len(users), success, rounds))
            
            attacker = False

if FARHAN:
    app.start()
    if "vᴀικιɴԍ" in app.get_me().first_name:
        print("TITAP")
        idle()
    else:
        print("tamate😂")