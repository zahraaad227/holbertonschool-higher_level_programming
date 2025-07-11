#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Yeni obyekt yarat
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize et və fayla yaz
obj.serialize("object.pkl")

# Fayldan oxu və deserialize et
new_obj = CustomObject.deserialize("object.pkl")

print("\nDeserialized Object:")
if new_obj:
    new_obj.display()
else:
    print("Deserialization failed.")
