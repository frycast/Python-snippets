# %%
# generator functions return iterable results
def square_generator(input_data):
    for num in input_data:
        res = num*num
        yield res

data = [1,2,3,4]
sg = square_generator(data)
print(sg)
print('1st result: ', next(sg))
print('2nd result: ', next(sg))
print('3nd result: ', next(sg))

