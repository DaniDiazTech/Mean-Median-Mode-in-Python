pythonic_machines_heights = [181, 187, 196, 196, 198, 203, 207, 211, 215]
after_retirement = [181, 187, 196, 198, 203, 207, 211, 215]

def median(dataset):
    data = sorted(dataset)
    index = len(data) // 2

    # If the dataset is odd  
    if len(dataset) % 2 != 0:
        return data[index]
    
    # If the dataset is even
    return (data[index - 1] + data[index]) / 2

print(median(pythonic_machines_heights))
print(median(after_retirement))