import random

from config import pieces, letter_scheme, buffers, pce_types

def get_buffer_index(piece_type, buffer):
    for i, piece in enumerate(pieces[piece_type]):
        if piece[0] == buffer:
            break
    return i

def gen_letter_pair(piece_type):
    pc_idx = 7 if piece_type == 'c' else 11
    buffer = random.choice(buffers[piece_type])
    bf_idx = get_buffer_index(piece_type, buffer)
    
    idx1 = random.randint(bf_idx+1, pc_idx)
    idx2 = random.randint(bf_idx+1, pc_idx)
    while idx2 == idx1:
        idx2 = random.randint(bf_idx+1, pc_idx)

    target1 = random.choice(pieces[piece_type][idx1])
    target2 = random.choice(pieces[piece_type][idx2])

    return {
        'buffer': buffer,
        'targets': [target1, target2]
    }

if __name__ == "__main__":
    for i in range(20):
        piece_type = random.choice(pce_types)
        out = gen_letter_pair(piece_type)
        print(f"{out['buffer']} {out['targets'][0]} {out['targets'][1]}")