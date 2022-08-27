def lin_space(min, max, samples):
    spaces = []
    for i in range(samples):
        temp = min + i * (max - min) / (samples - 1)
        spaces.append(temp)

    return spaces
