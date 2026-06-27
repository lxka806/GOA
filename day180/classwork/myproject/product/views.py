from django.shortcuts import render

products_database = [
    {'id': 1, 'title': 'ვეფხისტყაოსანი', 'price': 12.99},
    {'id': 2, 'title': 'დიდოსტატის მარჯვენა', 'price': 9.49},
    {'id': 3, 'title': 'ჯინსების თაობა', 'price': 8.99},
    {'id': 4, 'title': 'დათა თუთაშხია', 'price': 14.99},
    {'id': 5, 'title': 'მე, ბებია, ილიკო და ილარიონი', 'price': 7.99},
    {'id': 6, 'title': 'ალუდა ქეთელაური', 'price': 4.99},
    {'id': 7, 'title': 'სტუმარ-მასპინძელი', 'price': 5.49},
    {'id': 8, 'title': 'ბაში-აჩუკი', 'price': 8.49},
    {'id': 9, 'title': 'მთვარის მოტაცება', 'price': 11.99},
    {'id': 10, 'title': 'სამოსელი პირველი', 'price': 13.99},
    {'id': 11, 'title': 'მონანიება', 'price': 9.99},
    {'id': 12, 'title': '1984', 'price': 10.99},
    {'id': 13, 'title': 'ცხოველების ფერმა', 'price': 7.49},
    {'id': 14, 'title': 'პატარა უფლისწული', 'price': 6.99},
    {'id': 15, 'title': 'ჰარი პოტერი და ფილოსოფიური ქვა', 'price': 15.99},
    {'id': 16, 'title': 'ბეჭდების მბრძანებელი', 'price': 19.99},
    {'id': 17, 'title': 'ჰობიტი', 'price': 11.49},
    {'id': 18, 'title': 'დიუნი', 'price': 17.99},
    {'id': 19, 'title': 'შერლოკ ჰოლმსი', 'price': 9.99},
    {'id': 20, 'title': 'დანაშაული და სასჯელი', 'price': 13.49},
    {'id': 21, 'title': 'ძმები კარამაზოვები', 'price': 16.99},
    {'id': 22, 'title': 'ომი და მშვიდობა', 'price': 21.99},
    {'id': 23, 'title': 'ანა კარენინა', 'price': 15.49},
    {'id': 24, 'title': 'მედეა', 'price': 8.99},
    {'id': 25, 'title': 'ოდისეა', 'price': 12.49},
    {'id': 26, 'title': 'ილიადა', 'price': 12.99},
    {'id': 27, 'title': 'კაცი, რომელიც იცინოდა', 'price': 10.49},
    {'id': 28, 'title': 'სამი მუშკეტერი', 'price': 14.49},
    {'id': 29, 'title': 'გრაფი მონტე-კრისტო', 'price': 18.99},
]


# Create your views here.
def all_products(req):
    return render(req, 'index.html', {
        'products': products_database
    })

def product_with_id(request, id):
    if 0 <= id < len(products_database):
        product = products_database[id]
    else:
        return render(request, '404page.html')

    return render(request, 'product.html', {
        'product': product
    })