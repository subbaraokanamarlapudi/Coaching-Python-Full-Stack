# s = 'abcdefghij'
# print(s[1:6:2])
# print(s[::1])
# print(s[::-1])
# print(s[::-2])
# print(s[3:7:-1])
# print(s[7:4:-1])
# print(s[0:1000:1])
# print(s[0:1000:2])
# print(s[-4:1:-1])
# print(s[-4:1:-2])
# print(s[5:0:1])
# # print(s[9:0:0])
# print(s[0:-10:-1])
# print(s[0:-11:-1])
# print(s[0:-12:-1])
# print(s[0:0:1])
# # print(s[0:0:0])
# print(s[0:-9:-2])
# print(s[-5:-9:-2])
# print(s[9:-1:-1])

# Q.w.a.p to reverse order of words

# s = input("Enter a string: ")
# words = s.split()
# reversed_words = words[::-1]
# result = ' '.join(reversed_words)
# print(result)

# # Q.W.A.P to reverse the content of each word

# s = input("Enter a string: ")
# words = s.split()
# result = '' 
# for word in words:
#     result = result + word[::-1] +''
# print(result)




# Q.w.a.p for:
# i/p:'a4k3b2'
# o/p:'aeknbd'

# s = input("Enter a string: ")
# s1 = ''
# i = 0

# while i < len(s):
#     char = s[i]
#     i += 1
    
#     num_str = ''
#     while i < len(s) and s[i].isdigit():
#         num_str += s[i]
#         i += 1

#     if num_str:
#         count = int(num_str)
#         new_char = chr(ord(char) + count)
#         s1 += new_char
#     else:
#         s1 += char

# print(s1)

# 2nd way



# Q.Remove duplicates from the given string?
# i/p:'ABCBABCBABCBDBABCB'
# o/p:'ABCD'

# s = input("Enter a string: ")
# s1 = ''
# for x in s:
#     if x not in s1:
#         s1 += x
# print(s1)

# def my_function(food):
#     for x in food:
#         print(x)

# fruits = ['apple', 'banana', 'cherry']
# my_function(fruits)

