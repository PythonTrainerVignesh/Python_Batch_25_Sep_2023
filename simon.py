import csv


class Name:

    a =[]

    def __init__(self, name:str, mobile_no: int, email:str):
        assert len(name)>=3,f'{name},invalid name.'
        assert 9999999999 >mobile_no>6000000000,f'{mobile_no}invalid mobile no.'
        assert '@gmail.com' in email,f'{email},invalid email.'
        self.name = name
        self.mobile_no = mobile_no
        self.email = email


        Name.a.append(self)
    def n(self):
        return self.name


    @classmethod
    def data_initiation(cls):
        with open('data.csv','r') as file:
            data = csv.DictReader(file)
            item = list(data)
            for i in item:
                Name(i.get('name'),int(i.get('mobile_no')),i.get('email') )



    def __repr__(self):
        return f"{self.name},{self.mobile_no},{self.email}"
