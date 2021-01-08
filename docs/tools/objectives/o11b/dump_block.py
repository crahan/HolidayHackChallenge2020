#!/usr/bin/env python3
from Crypto.Hash import MD5, SHA256
from naughty_nice import Block, Chain

# calculate SHA256
def sha256(data):
    hash_obj = SHA256.new()
    hash_obj.update(data)
    return hash_obj.hexdigest()

if __name__ == '__main__':
    # load the blockchain file
    c2 = Chain(load=True, filename='blockchain.dat')

    # SHA256 of Jack's altered block
    sha256_ = '58a3b9335a6ceb0234c12d35a0564c4ef0e90152d0eb2ce2082383b38028a90f'

    # find Jack's altered block
    for idx, block in enumerate(c2.blocks):
        if sha256(block.block_data_signed()) == sha256_:
            # block details
            print(block)
            # save signed block data
            c2.save_a_block(idx, filename=f'{block.index}.dat')
            # save documents
            for idx in range(block.doc_count):
                block.dump_doc(idx)
            break
