
class Order(object):
    details = dict(
    part = None,
    storeid = None,
    storename = None,
    customerid = '<null>',
    customername = None,
    birthday = None,
    tier = None,
    club = None,
    salesorder = None,
    createtime = None,
    salestype = None,
    sku = None,
    skuname = None,
    itemtype = None,
    marketprice = None,
    revenue = None,
    quantity = None,
    fst = None,
    fststore = None,
    fstrevenue = None,
    lst = None,
    bcid = None,
    bcname = None
    )

    def __init__(self, list):
        i = 0
        for key in self.details:
            self.details[key] = list[i]
            i+=1
            # if(key == 'createtime' or key == 'fst' or key == 'lst' or key == 'quantity' or key == 'birthday'):
            #     if(list[i] != '<null>' and list[i] != ''):
            #         self.details[key] = int(list[i])
            # elif(key == 'revenue' or key == 'marketprice' or key == 'fstrevenue'):
            #     if (list[i] != '<null>' and list[i] != ''):
            #         self.details[key] = float(list[i])
            # else:
            #     self.details[key] = list[i]
            # i += 1