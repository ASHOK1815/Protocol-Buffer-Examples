import users_pb2
import os


with open("/home/mahadev/Downloads/protocalBuffer/test_protobuffer/output_binary", "rb") as f:
    bytes_data = f.read()


user = users_pb2.User()
user.ParseFromString(bytes_data)

user.name = "Ashokkumawat"

with open("/home/mahadev/Downloads/protocalBuffer/test_protobuffer/output_binary", "wb") as f:
    f.write(user.SerializeToString())
    print("Write Completed")