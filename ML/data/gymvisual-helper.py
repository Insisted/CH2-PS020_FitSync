import json
import re

import pandas as pd


def clean(df, gym):
    equip = df.loc[df.Equipment == 'Body weight'].to_numpy()
    temp = []

    print(len(equip), len(gym))

    for i, dataf in zip(gym, equip):
        a = re.sub(r'.*({.+}).*', r'\1', i['result'])
        b = re.sub(r'\s{2,}|\n', '', a)
        res = eval(re.sub(r'Q:.+', '', b))

        temp.append({
            'title': dataf[1],
            'type': dataf[2],
            'body_part': dataf[3],
            'gender': dataf[5],
            'desc': res['desc'],
            'level': res['level']
        })

    return temp


def get_vis(clean, vis):
    clean = pd.DataFrame(clean)
    vis = pd.DataFrame(vis)
    merged = pd.merge(clean, vis, on='title')

    print(len(clean), len(vis))

    merged.to_json('./ML/data/gymvisual-cleaned.json')


if __name__ == '__main__':
    df = pd.read_excel('./ML/data/Gym-Visual-EXERCISES-list.xlsx', sheet_name='Animated GIFs')

    with open('./ML/data/gymvisual-unclean.json', 'r') as f:
        uncleaned_gym = json.load(f)

    with open('./ML/data/gymvisual-image_urls.json', 'r') as f:
        vis = json.load(f)

    cleaned = clean(df, uncleaned_gym)

    get_vis(cleaned, vis)