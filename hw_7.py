# 1
# ip_lst1 = [ "10.11.12.13", "11.12.13.14", "15.16.17.18" ]
# class Ip:
#     def __init__(self, ip_lst):
#         self._ip_lst = ip_lst
#     def print_reverse(self):
#         result_p = []
#         for i in range(len(ip_lst1)):
#             result_p.append('.'.join(ip_lst1[i].split('.')[::-1]))
#         return  result_p
#     def print_without_first(self):
#         result_p = []
#         for i in range(len(ip_lst1)):
#             result_p.append('.'.join(ip_lst1[i].split('.')[1::]))
#         return  result_p
#     def print_last(self):
#         result_p = []
#         for i in range(len(ip_lst1)):
#             result_p.append('.'.join(ip_lst1[i].split('.')[-1:]))
#         return  result_p
#

# 2
# import json
# from pprint import pprint
# class WorkJson:
#     def __init__(self, file):
#         self.file = file
#     def read_file(self):
#         with open(self.file, 'r') as file:
#             data = json.load(file)
#         return data
#     def write_file(self, out_file):
#         with open(out_file, 'w') as out_file:
#             out_file.writelines(json.dumps(self.read_file(), separators = (',', ':')))
#     def union_file(self, obj_2, union_file ):
#         data1 = self.read_file()
#         with open(obj_2.path_to_file, 'r') as file:
#             data2 = json.load(file)
#         union_data = {'file_1': data1, 'file_2': data2}
#         with open(union_file, 'w') as file:
#             file.writelines(json.dumps(union_data, separators=(',', ':')))
#         return JSONFile(union_file)
#     def relative_path(self):
#         return '/'.join(os.path.relpath(self.file).split('/')[:-1])
#     def absolute_path(self):
#         return os.path.dirname(self.file)

3
# class ConnectPhysicalUnit:
#     def __init__(self, unit_name, mac_address, ip_address, login, password):
#         self._unit_name = unit_name
#         self._mac_address = mac_address
#         self._ip_address = ip_address
#         self._login = login
#         self._password = password
#
#     @property
#     def unit_name(self):
#         return self._unit_name
#     @unit_name.setter
#     def unit_name(self, value):
#         self._unit_name = value
#
#     @property
#     def mac_address(self):
#         return self._mac_address
#     @mac_address.setter
#     def mac_address(self, value):
#         self._mac_address = value
#
#     @property
#     def ip_address(self):
#         return self._ip_address
#     @ip_address.setter
#     def ip_address(self, value):
#         self._ip_address = value
#
#     @property
#     def login(self):
#         return self._login
#     @login.setter
#     def login(self, value):
#         self._login = value
#
#     @property
#     def password(self):
#         return self._password
#     @password.setter
#     def password(self, value):
#         self._password = value
