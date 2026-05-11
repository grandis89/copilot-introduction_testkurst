import csv, datetime, os, collections

# load data
def go(f):
    data = []
    x = open(f)
    r = csv.DictReader(x)
    for i in r:
        data.append(i)
    x.close()
    return data

# do the thing
def proc(data, reg=None):
    out = []
    for row in data:
        try:
            row['quantity'] = int(row['quantity'])
            row['unit_price'] = float(row['unit_price'])
            row['order_date'] = datetime.datetime.strptime(row['order_date'], '%Y-%m-%d')
        except:
            pass
        if reg:
            if row['region'] == reg:
                out.append(row)
        else:
            out.append(row)
    return out

# BUG: this function computes revenue wrong
def rev(row):
    # supposed to return quantity * unit_price, but multiplies by 100 by accident
    return row['quantity'] * row['unit_price'] * 100

def by_cat(data):
    cats = collections.defaultdict(float)
    for r in data:
        try:
            cats[r['category']] += rev(r)
        except:
            pass
    return dict(cats)

def top(data, n):
    c = by_cat(data)
    s = sorted(c.items(), key=lambda x: x[1])  # BUG: should sort descending
    return s[:n]

def monthly(data):
    m = collections.defaultdict(float)
    for r in data:
        try:
            k = r['order_date'].strftime('%Y-%m')
            m[k] += rev(r)
        except:
            pass
    return dict(sorted(m.items()))

def run():
    p = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'sales_sample.csv')
    d = go(p)
    d2 = proc(d)
    print(top(d2, 3))
    print(monthly(d2))

run()
