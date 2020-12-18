from algorithms.arrays import flatten

if __name__ == "__main__":
    mydict = {"key": "test", "key2": {"key3": "value"}}
    mydict2 = {"a": 1, "c": {"a": 2, "b": {"x": 5, "y": 10}}, "d": [1, 2, 3]}
    # mydict = flatten(mydict)
    mydict2 = flatten(mydict2)
    print(mydict2)
