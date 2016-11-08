import queue
import sys
import math


class HuffmanNode(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def create_tree(frequencies):
    """
    Create a Huffman Tree and return the root node, base on priority queue
    :param frequencies: the tuple of words, should be in format as (frequency, word)
    :return:
    """
    pq = queue.PriorityQueue()
    for value in frequencies:
        pq.put(value)
    while pq.qsize() > 1:
        ln, rn = pq.get(), pq.get()
        node = HuffmanNode(ln, rn)
        pq.put((ln[0]+rn[0], node))
    return pq.get()


def walk_tree(node, prefix="", code={}):
    """
    walk the Huffman tree recursively, return the code dictionary which contains all the
    code of the words
    :param node: create by create tree, in form (frequency, HuffmanNode)
    :param prefix:
    :param code: dictionary in form {word, code}
    :return: code
    """
    # walk left child tree
    if isinstance(node[1].left[1], HuffmanNode):
        # recursively walk the left node: (frequency, Huffman)
        walk_tree(node[1].left, prefix + '0', code)
    else:  # leaf node
        code[node[1].left[1]] = prefix + '0'
    # walk right child tree
    if isinstance(node[1].right[1], HuffmanNode):
        walk_tree(node[1].right, prefix + '1', code)
    else:
        code[node[1].right[1]] = prefix + '1'
    # return the code
    return code


def get_frequency(filename):
    """
    get the frequency from the file, one line for one word and should be in form "Word Frequency"
    :param filename:
    :return: a frequency list
    """
    frequencies = []
    with open(filename, 'rb') as f:
        for line in f:
            tokens = [token for token in line.strip().split(' ') if token]
            frequencies.append((int(tokens[1]), tokens[0]))
    # print frequencies
    return frequencies


def print_code(frequency, code):
    """
    print the encode result of the word, in form "Word Frequency Code"
    :param frequency:
    :param code:
    :return:
    """
    for word in sorted(frequency, reverse=True):
        print word[1] + '{:4d}'.format(word[0]) + ' ' + code[word[1]]


def get_ratio(frequency, code):
    origin_per_bit = math.ceil(math.log(len(frequency), 2))
    origin_total_bit = 0
    total_bit = 0
    for word in frequency:
        total_bit += (word[0] * len(code[word[1]]))
        origin_total_bit += (word[0] * origin_per_bit)
    print (origin_per_bit, origin_total_bit, total_bit)
    return float(origin_total_bit / total_bit)


def main(argv):
    filename = 'input.txt'
    if len(argv) > 1:
        filename = argv[1]
    frequencies = get_frequency(filename)
    root_node = create_tree(frequencies)
    code = walk_tree(root_node)
    print_code(frequencies, code)
    print get_ratio(frequencies, code)


if __name__ == '__main__':
    main(sys.argv)
