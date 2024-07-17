class patient:
    def __init__(self):
        pass
    def set_name(self,name):
        self.first_name = name[0]
        self.middle_name = name[1]
        self.last_name = name[2]

    def set_address(self,housenumber,city,province,zipcode):
        self.housenumber = housenumber
        self.city = city
        self.province = province
        self.zipcode = zipcode
    def set_phone(self,phone):
        if len(phone)!=10:
            raise ValueError('Incorrect phone number format')
        else:
            self.phone = phone
        
try:
    name = input('Enter name as - first name, middle name, last name : ')
    housenumber = input('House number and street?')
    city = input('Which city do you live in? ')
    province = input('What province is that? ')
    zipcode = input('Enter ZipCode:')
    phone = input('Enter phone number as all continuous digits: ')
except ValueError as e:
    print(e)

p = patient()
p.set_name([item.strip() for item in name.split(',')])
p.set_address(housenumber,city,province,zipcode)
p.set_phone(phone)
print(p.__dict__)