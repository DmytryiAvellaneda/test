class Project:
    def __init__(self, project_name):
        self.__project_name=project_name
        self.__customer="customer"
        self.__customers_country="country"
        self.__project_type="type"
        self.__number_of_devs=0
        self.__number_of_qas=0
        self.__project_duration=0.0

    @property
    def project_name(self):
        return self.__project_name

    @project_name.setter
    def project_name(self, project_name):
        self.__project_name=project_name

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer=customer

    @property
    def customers_country(self):
        return self.__customers_country

    @customers_country.setter
    def customers_country(self, customers_country):
        self.__customers_country=customers_country

    @property
    def project_type(self):
        return self.__project_type

    @project_type.setter
    def project_type(self, project_type):
        self.__project_type=project_type

    @property
    def number_of_devs(self):
        return self.__number_of_devs

    @number_of_devs.setter
    def number_of_devs(self, number_of_devs):
        if number_of_devs>=0:
            self.__number_of_devs=number_of_devs
        else:
            print("Wrong value for number of devs")
            self.__number_of_devs="Error"

    @property
    def number_of_qas(self):
        return self.__number_of_qas

    @number_of_qas.setter
    def number_of_qas(self, number_of_qas):
        if number_of_qas>=0:
            self.__number_of_qas=number_of_qas
        else:
            print("Wrong value for number of QAs")
            self.__number_of_qas="Error"

    @property
    def project_duration(self):
        return self.__project_duration

    @project_duration.setter
    def project_duration(self, project_duration):
        if project_duration>0:
            self.__project_duration=project_duration
        else:
            print("Wrong value for duration")
            self.__project_duration="Error"
        
    def display(self):
        print(self.__project_name, self.__customer, self.__customers_country, self.__project_type, self.__number_of_devs, self.__number_of_qas, self.__project_duration)

    def devs_price_per_month(self):
        result=self.__number_of_devs*10000
        return result

    def qas_price_per_month(self):
        result=self.__number_of_qas*6000
        return result

    def full_price_per_year(self):
        result=(self.__number_of_devs*10000+self.__number_of_qas*6000)*12
        return result

    def full_price_per_month(self):
        result=self.__number_of_devs*10000+self.__number_of_qas*6000
        return result

    def show_project_info(self):
        if self.number_of_devs>0 and self.number_of_qas>0:
            print(self.project_type, "project", self.project_name, "from", self.customers_country, "bring us: ", self.full_price_per_month(), "every month, ", self.full_price_per_year(), "every year")
        elif self.number_of_devs>0 and self.number_of_qas==0:
            print(self.project_type, "project", self.project_name, "from", self.customers_country, "bring us: ", self.devs_price_per_month(), "every month, ", self.full_price_per_year(), "every year\nWe need to sell them several QAs!")
        elif self.number_of_devs==0 and self.number_of_qas>0:
            print(self.project_type, "project", self.project_name, "from", self.customers_country, "bring us: ", self.qas_price_per_month(), "every month, ", self.full_price_per_year(), "every year\nWe need to sell them several devs!")
   
def main():
    sa=Project("WebCool")
    print("Enter data for the project: ")
    a=1
    while a==1:
        sa.project_name=input("Project name: ")
        if sa.project_name=="":
            print("Incorrect data")
        else:
            a=0
    a=1
    while a==1:
        sa.customer=input("Customer name: ")
        if sa.customer=="":
            print("Incorrect data")
        else:
            a=0
    a=1
    while a==1:
        sa.customers_country=input("Customers country: ")
        if sa.customers_country=="":
            print("Incorrect data")
        else:
            a=0
    a=1
    while a==1:
        sa.project_type=input("Project type: ")
        if sa.project_type=="":
            print("Incorrect data")
        else:
            a=0
    a=1
    while a==1:
        sa.number_of_devs=int(input("Number of devs: "))
        if(type(sa.number_of_devs)==str):
            print("Repeat enter") 
        else:
            a=0
    a=1
    while a==1:
        sa.number_of_qas=int(input("Number of QAs: "))
        if(type(sa.number_of_qas)==str):
            print("Repeat enter")
        else:
            a=0
    a=1
    while a==1:
        sa.project_duration=float(input("Project duration in months: "))
        if(type(sa.project_duration)==str):
            print("Repeat enter")
        else:
            a=0

    sa.display()

    a=1
    while a==1:
        c=input("select operation:\na - Calculate the monthly price for all devs on the project\nb - Calculate the monthly price for all QAs the project\nc - Calculate the full (QA + dev) price per year\nd - Show project info\nAny other key - exit\n")
        match c:
            case "a":
                print(sa.devs_price_per_month())
            case "b":
                print(sa.qas_price_per_month())
            case "c":
                print(sa.full_price_per_year())
            case "d":
                sa.show_project_info()
            case _:
                break    
    
main()
