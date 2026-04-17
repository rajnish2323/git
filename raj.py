def step1(data):
    return data + 2

def step2(data):
    return data * 3

def step3(data):
    return data - 1

# pipeline execution
data = 5

result = step3(step2(step1(data)))

print("rajnish")