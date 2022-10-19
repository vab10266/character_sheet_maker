def describe_features(features):
    out_str = ""
    titles = []
    texts = []
    max_title = 0
    max_text = 0
    text_width = 75

    for f in features:
        titles += [f.title]
        texts += [f.text]
        if len(f.title) > max_title:
            max_title = len(f.title)
        if len(f.text) > max_text:
            max_text = len(f.text)
    # Top line
    out_str += '_' + '_'*(max_title + 7 + min(max_text, text_width)) + '_\n'
    for i in range(len(titles)):
        ti = titles[i]
        te = texts[i]
        # # print(te)
        # out_str += ti + ' '*(max_title - len(ti)) + '  |  '

        # Title
        out_str += '| ' + ti + ' '*(max_title - len(ti)) + '  |'
        for j in range(len(te) // text_width +1):
            # print(te[j * 50:(j+1) * 50])
            # out_str += te[j * text_width:(j+1) * text_width]
            # out_str += '\n' + ' ' * (max_title + 2) + '|  '
            out_str += '  ' + te[j * text_width:(j+1) * text_width] + ' '*min((max_text - len(te[j * text_width:(j+1) * text_width]) + 1), (text_width - len(te[j * text_width:(j+1) * text_width]) + 1))
            if j < len(te) // text_width:
                out_str += '|\n|' + ' ' * (max_title + 3) + '|'
        # out_str += '\n'
        out_str += '|\n|' + '_' * (max_title + 3) + '|'
        out_str += '_'*(2+min(max_text, text_width)) + '_|\n'
    
    return out_str + ': '

def describe_choices(choices):
    out_str = ""
    titles = []
    texts = []
    max_title = 0
    max_text = 0
    text_width = 75

    for key in choices:
        c = choices[key].text
        titles += [key]
        texts += [c]
        if len(key) > max_title:
            max_title = len(key)
        if len(c) > max_text:
            max_text = len(c)
        

    out_str += '_' + '_'*(max_title + 7 + min(max_text, text_width)) + '_\n'
    for i in range(len(titles)):
        ti = titles[i]
        te = texts[i]
        # print(te)
        out_str += '| ' + ti + ' '*(max_title - len(ti)) + '  |'
        for j in range(len(te) // text_width +1):
            # print(te[j * 50:(j+1) * 50])
            out_str += '  ' + te[j * text_width:(j+1) * text_width] + ' '*min((max_text - len(te[j * text_width:(j+1) * text_width]) + 1), (text_width - len(te[j * text_width:(j+1) * text_width]) + 1))
            # out_str += '|\n|' + '_' * (max_title + 3) + '|'
            if j < len(te) // text_width:
                out_str += '|\n|' + ' ' * (max_title + 3) + '|'
        out_str += '|\n|' + '_' * (max_title + 3) + '|'
        out_str += '_'*(2+min(max_text, text_width)) + '_|\n'
    
    # out_str += '_'*(max_title + 7 + min(max_text, text_width)) + '\n'
    
    return out_str + ': '

def show_stats(stats):  
    out_str = ""
    out_str += '_'*(5 + 4 + 4 + 4) + '\n'
    for ti in ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']:
        te = str(stats[ti])
        mod = _beautify(stats[ti])
        # print(te)
        out_str += '| ' + ti + ' | '
        
        # print(te[j * 50:(j+1) * 50])
        out_str += ' '*(0 if stats[ti] >= 10 else 1) + te + ' |'
        out_str += ' ' + mod + ' |'
        out_str += '\n|' + '_' * (3 + 2) + '|' + '_'*(2+2) + '|' + '_'*(2+2) + '|\n'

        # out_str += '_'*(2+3) + '_|\n'
    return out_str

def _beautify(x):
    out_str = ''
    mod = x // 2 - 5
    if mod >= 0:
        out_str += '+'
    out_str += str(mod)
    return out_str