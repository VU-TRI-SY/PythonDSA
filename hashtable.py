hs = dict()

hs2 = {
    "key1": "value1", #pair (key-value): key = "key1", value = "value1"
    1001: "Hello world", #key-value: key = 1001, value = "Hello world"
    "key2": [1,2,3,4,5],
    "key3": 5,
    "key4": 5,
    "key5": 5
}
print(hs2.get("key1", "This string will return if key not found"))
#items() will return a collection of (key, value)
# for key, val in hs2.items():
#     if type(val) == list:
#         if 5 in val:
#             print(key)
#     elif type(val) == int:
#         if 5 == val:
#             print(key)

# print(hs2.items())
# print(hs2.keys())
# print(hs2.values())
print("value1" in hs2) #operation in: check if a KEY is in dictionary or not
print("key1" in hs2)

# In hashtable, key must be unique
# to access a value, we use key
# access an element of hashtable (dictinary) --> O(1)
