# def get_masked_password(prompt):
#     user_password = ''
#     for _ in prompt:
#         print('*', end='', flush=True)
#     print('')
#     while True:
#         char = input()
#         if char == '\r' or char == '\n':
#             break
#         user_password += char
#         print('*', end='', flush=True)
#     return user_password
#
#
# password = input("Enter your password: ")
# print(get_masked_password(password))

user_password = input("Enter your password: ")
print(len(user_password) * "*")
