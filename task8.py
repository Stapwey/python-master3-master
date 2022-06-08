def main(x):
    x = x.replace('<:<block>', '')\
        .replace('store', '')\
        .replace('.:>', '')\
        .replace('</block>', '')\
        .replace('"', '')\
        .replace('def', '')\
        .replace('\n', ' ')\
        .replace(' ', '')\
        .replace('<block>', '')
    x_parts = x.split('.')
    x_parts.pop(-1)
    x_parts1 = [i.split('|>') for i in x_parts]
    result = {}
    for i in x_parts1:
        result[i[0]] = i[1]
    return result


def main2(x):
    x = x.replace('</data>','')\
        .replace('<data>', '') \
        .replace('|', '') \
        .replace('define', '') \
        .replace('is', '') \
        .replace('(', '') \
        .replace(')', '') \
        .replace('def', '') \
        .replace('\n', ' ') \
        .replace(' ', '') \
        .replace('<block>', '')
    x_parts = x.split(';')
    x_parts.pop(-1)
    x_parts1 = [i.split('#') for i in x_parts]
    result = {}
    for match in x_parts1:
            s = []
            for j in match[1].split('.'):
                s.append(j)
            key = match[0]
            result[key] = s
    return result

# Testing
print(main('<:<block> store 258|> "tile_886" </block>. <block>store -4058 |>"biso_2" </block>. <block> store 4790 |> "teed_405" </block>. :>'))
print(main2('<data> || define iner is#( rari . esvebi_273 . xeleza ); |||| define enanti is #( rala . esma);|| </data>'))