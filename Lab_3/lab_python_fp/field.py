
def field(items, *args):
    assert len(args) > 0
    result = []
    
    if len(args) == 1:
        key = args[0]
        for item in items:
            if key in item:
                yield item[key]
    else:
        for item in items:
           yield {key: value for key, value in item.items() if key in args}

def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    field_gen1 = field(goods, 'title')
    for i in field_gen1:
        print(i)
        
    field_gen2 = field(goods, 'title', 'price')
    for i in field_gen2:
        print(i)


if __name__ == "__main__":
    main()