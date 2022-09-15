# from time import sleep
#
#
# class OBJECT:
#     def __init__(self, b: int) -> None:
#         self.a = b
#
#     def odd_even(self) -> str:
#         if self.a % 2 == 0:
#             return f"{str(self.a)} = Even"
#         else:
#             return f"{str(self.a)} = Odd"
#
#     def __str__(self):
#         return f'The number is {self.a}'
#
#
# if __name__ == '__main__':
#     for i in range(1, int(input("enter number : ")) + 1):
#         obj = OBJECT(i)
#         print(obj.odd_even())
#         sleep(.01)
#
