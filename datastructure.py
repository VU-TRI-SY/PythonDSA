#List
# ls = [1,2,3.5,4.5,"Hello World", [10,11,12]]
# print(ls[5])
# print(ls[-1])
# giống với array: bao gồm các cell là các ô nhớ liên tục (nằm liền kề nhau) --> indexing
# List có thể lưu các element không có cùng type
# có thể modify value của các element trong list
# có thể access vào list thông qua index âm (index của element cuối cùng trong list là -1,
# và giảm dần về đầu)
# đầu -> cuối: 0 -> n-1
# cuối -> đầu: -1 -> ...

#Tuple:
#giống với list: gồm các cell là các ô nhớ liền kề --> indexing
#tuple có thể lưu các element không có cùng type
#tuple là immmutable data structure --> Không thể modify value của các element trong tuple
# tp = (1,2,3.5,4.5,"Hello World", [10,11,12])
# print(tp)
# tp[-1][0] = 100
# print(tp)

#String:
#Trong python, string là immutable có nghĩa không thể modify value của string đó hay modify
#các character trong string
# s = "Hello"
# s[0] = 'h'
# print(s[0])

#Set
#Set là một data structure dùng để lưu data mà trong đó nó không cho phép sự lặp lại(duplicate)
#của các element
#Không thể access vào element của set bằng index
# st = {5,6,1,2,3,4,1,2,3,4}
# for val in st:
#     print(val)

#Dictionary: giống với Hashtable
#cặp key-value

dt = {
    "Hello": 1,
    "World": 2,
    "How": "1234",
    2: "How are you?"
}

print(dt)

    

