from django.http import HttpResponse

# Home page
def All_laptop(req):
    return HttpResponse("""
        <h1>All Laptop Brands</h1>
        <ul>
            <li>Dell</li>
            <li>HP</li>
            <li>Lenovo</li>
            <li>Asus</li>
            <li>Apple</li>
        </ul>
    """)

# Dell
def Dell(req):
    return HttpResponse("""
        <h1>Dell Laptop</h1>
        <ul>
            <li>Model: Dell XPS 13</li>
            <li>Processor: Intel Core i7</li>
            <li>RAM: 16 GB</li>
            <li>Storage: 512 GB SSD</li>
        </ul>
    """)

# HP
def Hp(req):
    return HttpResponse("""
        <h1>HP Laptop</h1>
        <ul>
            <li>Model: HP Pavilion 15</li>
            <li>Processor: Intel Core i5</li>
            <li>RAM: 8 GB</li>
            <li>Storage: 512 GB SSD</li>
        </ul>
    """)

# Lenovo
def Lenovo(req):
    return HttpResponse("""
        <h1>Lenovo Laptop</h1>
        <ul>
            <li>Model: Lenovo IdeaPad Slim 5</li>
            <li>Processor: AMD Ryzen 7</li>
            <li>RAM: 16 GB</li>
            <li>Storage: 1 TB SSD</li>
        </ul>
    """)

# Asus
def Asus(req):
    return HttpResponse("""
        <h1>Asus Laptop</h1>
        <ul>
            <li>Model: Asus VivoBook 15</li>
            <li>Processor: Intel Core i5</li>
            <li>RAM: 8 GB</li>
            <li>Storage: 512 GB SSD</li>
        </ul>
    """)

# Apple
def Apple(req):
    return HttpResponse("""
        <h1>Apple Laptop</h1>
        <ul>
            <li>Model: MacBook Air M3</li>
            <li>Processor: Apple M3 Chip</li>
            <li>RAM: 16 GB</li>
            <li>Storage: 512 GB SSD</li>
        </ul>
    """)