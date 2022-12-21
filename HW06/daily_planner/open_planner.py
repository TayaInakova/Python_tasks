def read_daily_planner_file():
    with open('planner.txt', 'r', encoding='utf-8') as file:
        planner = file.readlines()
    day_of_week = ['Понедельник:\n', 'Вторник:\n', 'Среда:\n', 'Четверг:\n', 'Пятница:\n', 'Суббота:\n',
                   'Воскресенье:\n']
    planner_dict = {}
    a = None
    for i in range(len(planner)):
        if planner[i] in day_of_week:
            a = planner[i]
            planner_dict[a] = []
        else:
            planner_dict[a].append(planner[i])
            if i == len(planner):
                planner_dict[a][-1] += '\n'
                print(planner_dict[a][-1])
    return planner_dict


def rewrite_planner(data):
    data_convert = []
    for v in data:
        data_convert.append(v)
        for i in range(len(data[v])):
            data_convert.append(data[v][i])
    with open('planner.txt', 'w', encoding='utf-8') as file:
        for z in range(len(data_convert)):
            file.write(data_convert[z])
