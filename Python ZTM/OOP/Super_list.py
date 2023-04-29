class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()
super_list1.__len__

super_list1.append(5)
super_list1.append(5)
super_list1.append(7)

print(super_list1)
print(len(super_list1))
print(super_list1[2])
print(issubclass(SuperList, list))  # Should be True
