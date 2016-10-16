import sys


def get_uni_char_list(encoder_str):
    """
    return the sorted unique character of the input string, which can be used as the start
    of the dictionary of both encoder and decoder process
    :param encoder_str:
    :return:
    """
    return sorted(list(set(encoder_str)))


def lzw_encoder(encoder_str):
    """
    The LZW Algorithm encoder, with process shown
    :param encoder_str:
    :return: the final encode in list form
    """
    unique_char_list = get_uni_char_list(encoder_str)
    encoder_dict = {}
    print "-------------------- Start of LZW Encoder --------------------"
    for c in unique_char_list:
        idx = unique_char_list.index(c) + 1
        encoder_dict[c] = idx
        print "--\t--\t(%d)\t%s\t--" % (idx, c)
    cur_idx = 0
    next_idx = 1
    encoder_list = []
    step = 1
    while cur_idx < len(encoder_str):
        # if it is the last one element, output it and end the loop
        if cur_idx == len(encoder_str) - 1:
            encoder_list.append(encoder_dict[encoder_str[cur_idx]])
            print "%d\t--\t--\t--\t(%d)" % (step, encoder_dict[encoder_str[cur_idx]])
            break

        cur_list = encoder_str[cur_idx] + encoder_str[next_idx]
        # get the longest list which is not in the encoder dictionary
        while cur_list in encoder_dict:
            next_idx += 1
            if next_idx >= len(encoder_str):
                break
            cur_list += encoder_str[next_idx]
        # add the list to dictionary
        dsize = len(encoder_dict)
        encoder_dict[cur_list] = dsize + 1
        # add the code to encoder list
        encoder_list.append(encoder_dict[cur_list[:-1]])
        print "%d\t%d\t(%d)\t%s\t(%d)" % (step, cur_idx + 1, encoder_dict[cur_list], cur_list, encoder_dict[cur_list[:-1]])
        # update index pointer
        cur_idx = next_idx
        next_idx = cur_idx + 1
        step += 1
    # print encoder_dict
    print "The encoder list is as follow:"
    print encoder_list
    print "-------------------- End of LZW Encoder --------------------"
    return encoder_list


def lzw_decoder(code_list, uni_char):
    """
    The LZW Algorithm decoder, with process shown
    :param code_list:
    :param uni_char: the unique character as starting of dictionary
    :return: the decode string
    """
    decoder_dict = uni_char
    print "-------------------- Start of LZW Decoder --------------------"
    for item in decoder_dict:
        print "--\t--\t(%d)\t%s\t--" % (decoder_dict.index(item) + 1, item)

    old_list = decoder_dict[int(code_list[0]) - 1]
    decode_str = old_list
    step = 1
    print "%d\t(%d)\t--\t--\t%s" % (step, code_list[0], old_list)

    if len(code_list) < 2:
        print "The decode string is %s" % decode_str
        print "-------------------- End of LZW Decoder --------------------"
        return decode_str

    for code in code_list[1:]:
        dsize = len(decoder_dict)
        step += 1
        if code > dsize:
            # add old + old[0] to encoder dictionary and add it to decode string
            decoder_dict.append(old_list + old_list[0])
            decode_str += old_list + old_list[0]
            old_list = old_list + old_list[0]
            print "%d\t(%d)\t(%d)\t%s\t%s" % (step, code, code, old_list, old_list)
        else:
            # update decode string according to encoder dictionary and add old + new[0] to encoder_dict
            decode_str += decoder_dict[code - 1]
            new_dict_item = old_list + decoder_dict[code - 1][0]
            decoder_dict.append(new_dict_item)
            old_list = decoder_dict[code - 1]
            print "%d\t(%d)\t(%d)\t%s\t%s" % (step, code, len(decoder_dict), new_dict_item, decoder_dict[code - 1])
    print "The decode string is %s" % decode_str
    print "-------------------- End of LZW Decoder --------------------"
    return decode_str


def main(argv):
    input_str = 'ababcbababaaaaaaa'
    if len(argv) > 1:
        input_str = argv[1]

    code_list = lzw_encoder(input_str)
    uni_char = get_uni_char_list(input_str)
    lzw_decoder(code_list, uni_char)


if __name__ == '__main__':
    main(sys.argv)
