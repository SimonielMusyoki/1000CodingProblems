def compute_output(list_d) -> list:
    assert isinstance(list_d, list)
    output_list = []
    for i in list_d:
        product = 1
        for j in list_d:
            if i == j:
                continue
            product *= j
        output_list.append(product)
    return output_list
