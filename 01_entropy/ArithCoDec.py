from collections import Counter


def get_symbol_table(words):
    """
    build the symbol table of a given word and return it
    :param words:
    :return: a list of symbol table if form [word, lower_bound, upper_bound]
    """
    counts = Counter(words)
    symbol_table = []
    lower = 0.0
    for item in sorted(counts):
        prob = float(counts[item]) / len(words)
        symbol_table.append([item, lower, lower + prob])
        lower += prob
    for item in symbol_table:
        print item
    return symbol_table


def arith_encoder(words, symbol_table):
    """
    Use Arithmetic encode algorithm to encode a string, print out all the process and return the
    final code
    :param words: string used to encode
    :param symbol_table:
    :return: code
    """

    def get_lp(cur_word):
        for item in symbol_table:
            if item[0] == cur_word:
                return item[1], item[2]

    lower_bound = 0.0
    interval = 1.0
    print "-------------- Start of ArithMetic Encoder ------------------"
    print ('No.', 'Symbol', 'LowerBound', 'UpperBound', 'Interval')
    print (0, 'Init', '0.0', '1.0', '1.0')
    cnt = 0
    for word in words:
        word_lower, word_upper = get_lp(word)
        upper_bound = lower_bound + interval * word_upper
        lower_bound += interval * word_lower
        interval = upper_bound - lower_bound
        cnt += 1
        print (cnt, word, '{:12.10f}'.format(lower_bound),
               '{:12.10f}'.format(upper_bound), '{:12.10f}'.format(interval))
    print "The Arithmatic code of \'%s\' is %.10f" % (words, lower_bound)
    print "--------------- End of ArithMetic Encoder ----------------"
    return lower_bound


def arith_decoder(code, wordlen, symbol_table):
    """
    Use Arithmetic decode algorithm to decode a code, print out all the process and return the string
    :param code:
    :param wordlen: the length of the original string
    :param symbol_table:
    :return: the string
    """

    def get_word(cur_code):
        for item in symbol_table:
            if item[1] <= cur_code < item[2]:
                return item, symbol_table.index(item) + 1

    print "------------Start of Arithmetic Decoder ------------"
    cnt = 1
    result = ""
    arith_code = code
    print ('j', 'vj', 'i', 'cj = s')
    while len(result) < wordlen:
        cur_item, cur_idx = get_word(arith_code)
        result += cur_item[0]
        print (cnt, '{:12.10f}'.format(arith_code), cur_idx, cur_item[0])
        arith_code = (arith_code - cur_item[1]) / (cur_item[2] - cur_item[1])
        cnt += 1
    print "The arithmetic decode of %.10f is %s" % (code, result)
    print "------------End of Arithmetic Decoder ------------"
    return result


def main():
    a = 'good night'
    sym_tab = get_symbol_table(a)
    arith_code = arith_encoder(a, sym_tab)
    arith_decoder(arith_code, len(a), sym_tab)


if __name__ == '__main__':
    main()
