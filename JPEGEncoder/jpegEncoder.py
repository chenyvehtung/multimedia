import numpy as np
import math


HUE_QUANTISER = [[16, 11, 10, 16, 24, 40, 51, 61],
                 [12, 12, 14, 19, 26, 58, 60, 55],
                 [14, 13, 16, 24, 40, 57, 69, 56],
                 [14, 17, 22, 29, 51, 87, 80, 62],
                 [18, 22, 37, 56, 68, 109, 103, 77],
                 [24, 35, 55, 64, 81, 104, 113, 92],
                 [49, 64, 78, 87, 103, 121, 120, 101],
                 [72, 92, 95, 98, 112, 100, 103, 99]]
LUMINANCE_QUANTISER = [[17, 18, 24, 47, 99, 99, 99, 99],
                       [18, 21, 26, 66, 99, 99, 99, 99],
                       [24, 26, 56, 99, 99, 99, 99, 99],
                       [47, 66, 99, 99, 99, 99, 99, 99],
                       [99, 99, 99, 99, 99, 99, 99, 99],
                       [99, 99, 99, 99, 99, 99, 99, 99],
                       [99, 99, 99, 99, 99, 99, 99, 99],
                       [99, 99, 99, 99, 99, 99, 99, 99]]


def c_func(idx):
    return 1.0 if idx > 0 else 1 / math.sqrt(2)


def _hex_dec(tokens):
    result_list = []
    for token in tokens:
        result_list.append(int(token, 16))
    return result_list


def _get_matrix_str(input_matrix):
    if input_matrix.dtype == float:
        return '\n'.join(' '.join('%5.2f' %x for x in y) for y in input_matrix)
    elif input_matrix.dtype == int:
        return '\n'.join(' '.join('%d' %x for x in y) for y in input_matrix)
    else:
        return '\n'.join(' '.join('%s' %x for x in y) for y in input_matrix)


def extract_data(filename="input.txt"):
    hex_input = []
    dec_input = []
    with open(filename, 'rb') as f:
        for line in f:
            line = line.strip()
            if line:
                tokens = [token for token in line.split(' ') if token]
                hex_input.append(tokens)
                dec_input.append(_hex_dec(tokens))

    hex_input = np.array(hex_input)
    dec_input = np.array(dex_input, dtype=float)
    hex_output = []
    dec_output = []
    for row in xrange(0, 16, 8):
        for col in xrange(0, 16, 8):
            hex_output.append(hex_input[row:row + 8, col:col + 8].tolist())
            dec_output.append(dec_input[row:row + 8, col:col + 8].tolist())
    dec_output = np.array(dec_output, dtype=float)
    hex_output = np.array(hex_output)
    print dec_output.shape
    return dec_output, hex_output


def save_data(hex_data, dec_data, fdct, idct, qnt, iqnt, quantizer=HUE_QUANTISER, filename="output.txt"):
    with open(filename, 'ab') as f:
        f.write("------------------Start of Image block(8x8)------------------"
        f.write("The original data:\n" + _get_matrix_str(hex_data))
        f.write("Transform to decimal:\n" + _get_matrix_str(dec_data))
        f.write("Forward DCT:\n" + _get_matrix_str(fdct))
        f.write("Inverse DCT:\n" + _get_matrix_str(idct))
        f.write("Quantizasion:\n" + _get_matrix_str(qnt))
        f.write("Inverse Quantizasion:\n" + _get_matrix_str(iqnt))
        f.write("------------------End of Image block(8x8)-------------\n"


def forward_dct(image_block):
    """
    return the numpy array of the forward DCT of the given image block
    image_block: numpy array with float data type
    """
    def generate_cos(idx):
        return [math.cos((2 * i + 1) * idx * math.pi / 16) for i in xrange(8)]

    image_block -= 128.0
    fdct = np.zeros((8, 8))

    uv_cos = []
    for idx in xrange(8):
        uv_cos.append(generate_cos(idx))
    uv_cos = np.array(uv_cos, dtype=float)

    # I should try to remove the for loop by using matrix
    for u in xrange(8):
        for v in xrange(8):
            # get a 8x8 array using numpy broadcast
            cos_part = uv_cos[u, :].reshape((8, 1)) * uv_cos[v, :]
            # get the sum part
            sum_part = np.sum(np.multiply(image_block, cos_part))
            fdct[u, v] = 1.0 / 4 * c_func(u) * c_func(v) * sum_part

    return fdct


def inverse_dct(fdct):
    def generate_cos(idx):
        return [math.cos((2 * idx + 1) * u * math.pi / 16) for u in xrange(8)]

    c_list = [c_func(idx) for idx in xrange(8)]
    cc_part = np.array(c_list, dtype=float).reshape((8, 1)) * np.array(c_list, dtype=float)
    f_part = np.multiply(cc_part, fdct)

    ij_cos = []
    for idx in xrange(8):
        ij_cos.append(generate_cos(idx))
    ij_cos = np.array(ij_cos, dtype=float)

    idct = np.zeros((8, 8))
    for i in xrange(8):
        for j in xrange(8):
            # using numpy broadcast to get a 8x8 array
            cos_part = ij_cos[i, :].reshape((8, 1)) * ij_cos[j, :]
            idct[i, j] = 1.0 / 4 * np.sum( np.multiply(f_part, cos_part) )

    return idct


def quantisation(fdct, quantizer=HUE_QUANTISER):
    quantizer = np.array(quantizer, dtype=float)
    # well, I should find a way to fit the round type of the document :(
    sq = np.round(np.divide(fdct, quantizer))
    return sq.astype(int)


def inverse_qnt(sq, quantizer=HUE_QUANTISER):
    return np.multiply(sq, quantizer)


def test_func():
    test_image = [[139, 144, 149, 153, 155, 155, 155, 155],
                  [144, 151, 153, 156, 159, 156, 156, 156],
                  [150, 155, 160, 163, 158, 156, 156, 156],
                  [159, 161, 162, 160, 160, 159, 159, 159],
                  [159, 160, 161, 162, 162, 155, 155, 155],
                  [161, 161, 161, 161, 160, 157, 157, 157],
                  [162, 162, 161, 163, 162, 157, 157, 157],
                  [162, 162, 161, 161, 163, 158, 158, 158]]
    test_image = np.array(test_image, dtype=float)
    fdct =  forward_dct(test_image)
    print fdct
    idct = inverse_dct(fdct)
    print idct + 128.0
    sq = quantisation(fdct)
    print sq
    print inverse_qnt(sq)


def main():
    dec_output, hex_output = extract_data()
    output_file = "output.txt"
    with open(output_file, "wb") as f:
        f.write("Start of the whole program!")

    item_num = dec_output.shape[0]
    for idx in xrange(item_num):
        pass
        # TODO process one image block and write it down


if __name__ == '__main__':
    main()
