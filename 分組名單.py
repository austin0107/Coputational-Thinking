project_title = 'chatbox'
name_list = ['呂昕靜', '林秉睿', '田智翔', '黃珮筑', '簡佑竹', '蔡宜玲', '王多樂', '王柏智']
number_list = ['A109260007', 'A109260017', 'A109260033', 'A109260043', 'A109260057', 'A109260071', 'A109260079', 'A109260099'] 
duty_list = ['聊天機器人自我介紹', '設計者組別介紹', '與使用者打招呼', '興趣介紹', '歷史話題', '食物話題', '心情話題', '聊天感想與道別']
load_list = ['12%', '13%', '12%', '13%', '12%', '13%', '13%', '12%']

name = name_list[2:3]
school_number = number_list[2:3]
duty = duty_list[2:3]
load = load_list[2:3]

team_leader = list((name, school_number, duty, load))

print('組長為', team_leader)

組長為 [['田智翔'], ['A109260033'], ['與使用者打招呼'], ['12%']]