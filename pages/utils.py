
def order_list_generator(order):#создание списка-аргумента сортировки
    
    if order:
        sort_by_dict = {
        'date':['-created_at',],
        '-date':['created_at',],
        'title':['title','-created_at'],
        '-title':['-title','-created_at'],
        'author':['author','-created_at'],
        '-author':['-author','-created_at']
        }
        order_list=sort_by_dict[order]
        
    else:
        order_list=['-created_at',]
        
    
    return order_list


    
    
    
    