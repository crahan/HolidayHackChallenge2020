#!/usr/bin/env python
PLAINTEXT = ( 
    'aaaaaaaabbbbbbbbccccccccddddddddeeeeeeeeffffffffgggggggghhhhhhhhiiiiiiii'
    'jjjjjjjjkkkkkkkkllllllllmmmmmmmmnnnnnnnnooooooooppppppppqqqqqqqqrrrrrrrr'
    'ssssssssttttttttuuuuuuuuvvvvvvvvwwwwwwwwxxxxxxxxyyyyyyyyzzzzzzzzAAAAAAAA'
    'BBBBBBBBCCCCCCCCDDDDDDDDEEEEEEEEFFFFFFFFGGGGGGGGHHHHHHHHIIIIIIIIJJJJJJJJ'
    'KKKKKKKKLLLLLLLLMMMMMMMMNNNNNNNNOOOOOOOOPPPPPPPPQQQQQQQQRRRRRRRRSSSSSSSS'
    'TTTTTTTTUUUUUUUUVVVVVVVVWWWWWWWWXXXXXXXXYYYYYYYYZZZZZZZZ0000000011111111'
    '2222222233333333444444445555555566666666777777778888888899999999'
)

ENCRYPTED = (
    '9VbtacpgGUVBfWhPe9ee6EERORLdlwWbwcZQAYue8wIUrf5xkyYSPafTnnUgokAhM0sw4eOC'
    'a8okTqy1o63i07r9fm6W7siFqMvusRQJbhE62XDBRjf2h24c1zM5H8XLYfX8vxPy5NAyqmsu'
    'A5PnWSbDcZRCdgTNCujcw9NmuGWzmnRAT7OlJK2X7D7acF1EiL5JQAMUUarKCTZaXiGRehmw'
    'DqTpKv7fLbn3UP9Wyv09iu8Qhxkr3zCnHYNNLCeOSFJGRBvYPBubpHYVzka18jGrEA24nILq'
    'F14D1GnMQKdxFbK363iZBrdjZE8IMJ3ZxlQsZ4Uisdwjup68mSyVX10sI2SHIMBo4gC7VyoG'
    'Np9Tg0akvHBEkVH5t4cXy3VpBslfGtSz0PHMxOl0rQKqjDq2KtqoNicv3ehm9ZFH2rDO5LkI'
    'pWFLz5zSWJ1YbNtlgophDlgKdTzAYdIdjOx0OoJ6JItvtUjtVXmFSQw4lCgPE6x7'
)

def decrypt(passwd):
    # each character has 8 possible encrypted variations depending on its position.
    decrypted = ''
    for position, char in enumerate(passwd):
        for idx in range(position%8, len(ENCRYPTED), 8):
            if char == ENCRYPTED[idx]:
                decrypted += PLAINTEXT[idx]
    return(decrypted)


if __name__ == '__main__':
    # 'LVEdQPpBwr' decrypts to 'CandyCane1'
    print(decrypt('LVEdQPpBwr'))
