class Order:
    part = None
    storeid = None
    storename = None
    customerid = '<null>'
    customername = None
    birthday = None
    tier = None
    club = None
    salesorder = None
    createtime = None
    salestype = None
    sku = None
    skuname = None
    itemtype = None
    marketprice = None
    revenue = None
    quantity = None
    fst = None
    fststore = None
    fstrevenue = None
    lst = None
    bcid = None
    bcname = None

    def __init__(self, list):
        self.part = list[0]
        self.storeid = list[1]
        self.storename = list[2]
        self.customerid = list[3]
        self.customername = list[4]
        self.birthday = list[5]
        self.tier = list[6]
        self.club = list[7]
        self.salesorder = list[8]
        self.createtime = list[9]
        self.salestype = list[10]
        self.sku = list[11]
        self.skuname = list[12]
        self.itemtype = list[13]
        self.marketprice = list[14]
        self.revenue = list[15]
        self.quantity = list[16]
        self.fst = list[17]
        self.fststore = list[18]
        self.fstrevenue = list[19]
        self.lst = list[20]
        self.bcid = list[21]
        self.bcname = list[22]
