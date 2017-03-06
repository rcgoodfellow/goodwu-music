class CD:
    def __init__(s, title='', artists = '', pieces = []):
        s.title = title
        s.artists = artists
        s.pieces = pieces

class Piece:
    def __init__(s, title = '', composer = '', performers = [], movements = []):
        s.title = title
        s.composer = composer
        s.performers = performers
        s.movements = movements

class Movement:
    def __init__(s, number = 0, title = ''):
        s.number = number
        s.title = title

def movements(*titles):
    return list(map(lambda x: Movement(x[0]+1, x[1]), enumerate(titles)))


def tagit(cd):
    cmds = []
    cmds.append(
            "beet modify -a 'Unknown Album' album='%s' albumartist='%s' comp=True;"%(
                cd.title, cd.artists)
            )

    trk = 1
    for piece in cd.pieces:
        for movement in piece.movements:
            cmds.append(
                    ("beet modify '%s' track:%d " +
                        "piece='%s' " +
                        "composer='%s' " +
                        "movement=%d " +
                        "title='%s' " +
                        "performers='%s' " +
                        "album='%s';")%(
                            cd.title, trk,
                            piece.title,
                            piece.composer,
                            movement.number,
                            movement.title,
                            ";".join(piece.performers),
                            cd.title)
                        )
            trk += 1

    for c in cmds:
        print(c)


