def unnest_list(list_):
    """
    Unnest arbitrary nested list. Unlike chain method, this can unnest multiple nested level
    Args:
        list_ (List): list
    Returns: unnested list
    """
    res = []
    for i in list_:
        if isinstance(i, list):
            res += unnest_list(i)
        else:
            res += [i]
    return res


if __name__ == '__main__':
    test_list = [[1, 2], [3, 4], 5, 6, [7, [8, 9]], [[[10]]], 11]

    print(test_list)
    print(unnest_list(test_list))
