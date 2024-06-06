from Block import Block


class Program:
    blocks: [Block]

    def __init__(self):
        self.blocks: [Block] = []

    def add_block(self, b: Block):
        self.blocks.append(b)
