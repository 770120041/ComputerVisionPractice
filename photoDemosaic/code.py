def get_mask(shape):
    masks = dict((color, np.zeros(shape)) for color in 'RGB')
    masks['R'][0::2, 0::2] = 1
    masks['G'][0::2, 1::2] = 1
    masks['G'][1::2, 0::2] = 1
    masks['B'][1::2, 1::2] = 1

    for color in 'RGB':
        masks[color] = masks[color].astype(bool)
    return tuple(masks['R']), tuple(masks['G']), tuple(masks['B'])


def get_solution_image(image):
    masks = dict((color, np.zeros(image.shape)) for color in 'RGB')
    masks['R'][0::2, 0::2] = 1
    masks['G'][0::2, 1::2] = 1
    masks['G'][1::2, 0::2] = 1
    masks['B'][1::2, 1::2] = 1

    for color in 'RGB':
        masks[color] = masks[color].astype(bool)

    R = convolve(image * masks['R'], kernel_RB, mode='constant', cval=0)
    G = convolve(image * masks['G'], kernel_G, mode='constant', cval=0)
    B = convolve(image * masks['B'], kernel_RB, mode='constant', cval=0)
    return np.stack([R, G, B], axis=2)