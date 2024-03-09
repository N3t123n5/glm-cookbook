import time
from dotenv import load_dotenv

load_dotenv()

from api import generate_role_appearance, get_chatglm_response_via_sdk


def characterglm_example(bot_info_text, user_info_text):
    bot_info = ""
    user_info = ""
    for chunk in generate_role_appearance(bot_info_text):
        bot_info += chunk

    for chunk in generate_role_appearance(user_info_text):
        user_info += chunk
    # print(bot_info)
    # print(user_info)
    character_meta = {
        "user_info": "须菩提祖师的徒弟。" + user_info,
        "bot_info": bot_info,
        "user_name": "孙悟空",
        "bot_name": "须菩提祖师"
    }
    instruction = f"""
    阅读下面的角色人设，生成一段对话场景。

    {character_meta['bot_name']}的人设：
    {character_meta['bot_info']}
        """.strip()

    if character_meta["user_info"]:
        instruction += f"""

    {character_meta["user_name"]}的人设：
    {character_meta["user_info"]}
    """.rstrip()

    instruction += """

    要求如下：
    1. 每行对话格式以‵角色名：消息内容`呈现
    2. 描写不能包含敏感词，人物形象需得体
    3. 最多生成10条对话记录
    4. 每句话不要超过50字
    """.rstrip()
    print(instruction)
    message_list = ""
    for chunk in get_chatglm_response_via_sdk(
        messages=[
            {
                "role": "user",
                "content": instruction.strip()
            }
        ]
    ):
        message_list += chunk

    print(message_list)
    with open('message_list', 'w', encoding='utf-8') as file:
        file.write(message_list)



if __name__ == "__main__":
    text1 = """
    大觉金仙没垢姿，西方妙相祖菩提；不生不灭三三行，全气全神万万慈。空寂自然随变化，真如本性任为之；与天同寿庄严体，历劫明心大法师。
    
    较之其他神佛仙圣，须菩提祖师不给人以隔膜感，他更像一位隐在人间的“上仙”。他所居之地灵台方寸山斜月三星洞，孤悬于海外的西牛贺洲地界，他似乎与其他神仙并无往来，与他交往的却不乏樵夫野老，须菩提祖师虽然法力通天，却并不给人以高不可攀、触不能及之感，他更像一位在世间的高士、圣人，这也成了须菩提祖师与《西游记》中其他神仙最大的不同。须菩提祖师是一位真正的“世外高人”，他虽隐于世外，但却包容、认可了“不平”之气 。这般形象和气质，绝似人间的高士、大隐。须菩提祖师高卓、脱俗、不受世之羁绊、不染世之污垢。
    """

    text2 = """
孙悟空是一个敢于反抗传统、反抗权威蔑视封建等级观念的反抗性很强的人物。这一点在前七回中表现得尤为突出。孙悟空为了取得武器，武装自己，闹了龙宫；为了不受冥司的管束，求得“不生不灭，与天地山川齐寿”，又大闹了冥府，强令阎君拿过生死簿，“把猴属之类，但有名者，一概红么”。充分表现了孙悟空渴望自由，不畏强暴的叛逆精神这种精神。而这种精神在大闹天宫中，表现得最为强烈，最为突出。他不承认天子独尊，更不理会神的天国的任何威严和秩序。在玉帝面前，群仙众神山呼礼拜，而孙悟空却傲然“挺身在旁”，既不“朝礼”，又不“谢恩”；当玉帝问及时，他也只是“唱个大喏”，答应一声“老孙便是”而已。在孙悟空眼里，玉皇大帝、森严的朝仪礼法，对自己根本不起约束作用。在孙悟空心里不存在不可侵犯的天庭，更不能容忍别人对他的“藐视”。所以当他发现“弼马温”的封号是个骗局的时候，便立即“心头火起”，从耳中取出如意金箍棒，一路打出南天门，回到花果山，竖起“齐天大圣”的旗帜，与天庭相抗衡。孙悟空的反叛行动，实际是对天国权成的否定，是对神权统治的挑战、是对上下尊卑等级制度的蔑视。 [12-13]

孙悟空是一个积极乐观，勇敢无畏、不怕困难、敢于斗争的人物。这在取经路上斩妖除怪的斗争中展示得最为充分。在取经的路上，即便经历再多艰难险阻，遇见再多的妖魔鬼怪，孙悟空也不畏惧退缩，总是保持积极乐观，以昂扬的精神状态面对一切，即便失败也从不气馁，始终勇往直前。这得不仅得益于他高超的本领，更得益于他坚定的取经信念在背后支持，双方面加持，才有了他笑对风雨的那份乐观。 [12] [22]

孙悟空是一个是非观念十分鲜明的人物，他济困扶危、恤孤念寡、嫉恶如仇、为民除害。孙悟空除妖并非只是为了保护唐僧，也是为民除害。孙悟空抱打不平之事，救人间灾害。所以，在取经途中，孙悟空只要听说有妖，不管是否阻碍唐僧西行，都要坚决捉拿，而且还要捉之必尽，就是碰上最凶恶的妖精，遇到再大的困难，他也毫不退缩，总是那样斗志昂扬地去夺取胜利。他或上天入地，查清妖精的来历，设法把它斩除；或者变作蜜蜂儿、小虫、蚊子，钻到妖洞中摸情况，探消息，偷宝贝，把妖精制服；或者化作妖精的亲戚、朋友、亲人，以至小妖，去蒙骗他们；为了战胜妖精，他甚至巧妙地钻入妖精的肚子里“竖蜻蜓，打斤斗”“跌四平，踢飞脚”，使妖魔俯首认输，即使在生命攸关的时刻，孙悟空也从未灰心过，依然保持着旺盛的战斗精神，同妖魔进行始终不懈的顽强斗争。可见，孙悟空确实是以救人苦难而扫荡妖魔为己任的。 [12-13]

封建意识时不时在孙悟空头脑里暴露出来。盘丝洞蜘蛛精在濯垢泉洗浴，孙悟空却投鼠忌器，害怕低了自己的名头，因为顾忌“男不与女斗”的说教，正因为他不肯打，于是惹出以后不少是非。孙悟空一直想当大官，但总屈服于佛祖的压力，对唐僧表现出浓厚的报恩思想。孙悟空还好名、好胜、好戴高帽，以致有一次因“得胜的猫儿欢似虎”“以得意为喜”，反而被牛魔王变作八戒，把他刚从铁扇公主那里弄来的芭蕉扇又骗了回去，误事就误在他被胜利冲昏了头脑因而不及细察。他又爱不分场合地捉弄猪八戒，在狮驼岭，还险些将猪八戒置于险境。
    """
    characterglm_example(text1, text2)
