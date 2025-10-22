from django.shortcuts import render
from django.http import HttpResponse
from product2.models import Product, Category, Discount, Review
from django.db.models import Avg, Count
from datetime import datetime, timedelta

def test_n_1(request):

    result = ''

    product = Product.objects.get(id=1)
    reviews = Review.objects.filter(product_id=1)

    # 특정 제품의 평균 평점과 리뷰 개수 구하기

    product = Product.objects.get(id=1)
    avg_rating = product.review.aggregate(avg_rating = Avg('rating'))['avg_rating']
    review_cnt = product.review.count()

    result = f'{product.name}의 리뷰 평점 : {avg_rating} ({review_cnt}개의 리뷰)<br>'

    # 평점이 높은 리뷰(4점 이상)만 구하기

    product = Product.objects.get(id=1)
    high_rating_reviews = product.review.filter(rating__gte=4)

    for review in high_rating_reviews:
        result += f'[High Rating] {review.user_id}의 {review.comment} ({review.rating})<br>'

    # 모든 제품의 평균 평점과 리뷰 개수 구하기

    # products_with_review = Product.objects.annotate(
    #     avg_rating=Avg('review_rating'),
    #     review_count=Count('review')
    # )
    # result = ''
    # for product in products_with_review:
    #     result += f'{product.name} | 평균 평점 {product.name} | 리뷰 개수 {product.review_count}<br>'


    # 특정 기간(한달전~오늘)동안 작성된 리뷰 구하기 

    start_date = datetime.now() - timedelta(weeks=4) 
    end_date = datetime.now()

    reviews_by_date = Review.objects.filter(created_at__range=(start_date,end_date))

    for review in reviews_by_date:
        result += str(review.id) + '/' + review.product.name + '/' + str(review.user_id) + '/' + str(review.rating) + '/' + review.comment + '<br>'



    for review in reviews:
        result += str(review.id) + '/' + review.product.name + '/' + str(review.user_id) + '/' + str(review.rating) + '/' + review.comment + '<br>'

    return HttpResponse(result)

def test_1_1(request):

    result = ''

    # 1. 특정 제품의 할인 정보 구하기 

    product_id = 0

    # 1-1. Discount.objects.get()를 통해서 db에서 자료 검색
    # 1-2. 할인 정보가 있는 제품이라면 -> product 제품명 | Discount 할인율
    # 1-3. 할인 정보가 없는 제품이라면 -> product_id는 할인 안함

    try:
        discount =  Discount.objects.get(product_id = product_id)
        result = f'Product {discount.product.name} | Discount {discount.discount_percentage}'
    except Discount.DoesNotExist:
        result = f'{product_id}는 할인 안함'

    # ----------------------------------------------------------------------------------------------------------------

    # 2. 할인 중인 모든 제품 구하기

    # 2.1. 현재 시점에서 할인 중인 제품 == 조건
    # 2.2. [할인중] {제품명} ({할인율}%)

    # ----------------------------------------------------------------------------------------------------------------

    # 3. 특정 할인율(20%) 이상인 제품 구하기

    # 3-1. [파격세일!!!] {제품명} ({할인율}%)

    # ----------------------------------------------------------------------------------------------------------------

    # 4. 할인 정보와 함께 모든 제품 정보 구하기

    # 4-1. 할인 정보가 있으면 -> 제품명 ({할인율}% 세일)
    # 4-2. 할인 정보가 없으면 -> 할인 안 하는 제품명

    prodects = Product.objects.all()

    result += '<br><br><br>'

    for product in prodects:
        if hasattr(product, 'discount'):
            result += f'{product.name} ({product.discount.discount_percentage}% 세일)<br>'
        else:
            result += f'할인 안 하는 {product.name}<br>'

    # ----------------------------------------------------------------------------------------------------------------

    # 5. 할인 기간이 지난 제품 구하기

    # 5-1. [할인 종료] {제품명} ({할인율}%)


    return HttpResponse(result)

def test_prefetch(request):

    result = ''

    prodects = Product.objects.prefetch_related('discount')

    for product in prodects:
        if hasattr(product, 'discount'):
            result += f'{product.name} ({product.discount.discount_percentage}% 세일)<br>'
        else:
            result += f'할인 안 하는 {product.name}<br>'

    return HttpResponse(result)

def test_n_m(request):

    result = ''

    # 1. 특정 제품이 속한 모든 카테고리 구하기

    product_id = 9

    # 1-1. 출력 예시 Product {제품명}의 카테고리

    product = Product.objects.get(id = product_id)
    categories = product.categories.all()

    result += f'{product.name}<br>'
    for category in categories:
        result += f'{category.name}<br>'


    result += '<br><br><br>'

    # 2. 특정 카테고리에 속한 모든 제품 정보(이름, 가격, 재고량) 구하기
    category_name = '가전'

    # 2-1. 출력 예시 Category {카테고리명}의 제품
    #       - {제품명} ({가격}원 / 수량 : {재고량}개)
    #       - {제품명} ({가격}원 / 수량 : {재고량}개)

    category = Category.objects.get(name=category_name)
    products = category.products.all()

    result += f'{category.name}<br>'
    for product in products:
        result += f'{product.name}, {product.price}, {product.stock}<br>'

    result +='<br><br><br>'

    # 3. 카테고리가 없는 제품 구하기

    # 3-1. category가 null인 product 조회
    # 3-2. 출력 예시
    #       - Category 미포함 제품
    #           - {제품명} ({가격}원 / 수량 : {재고량}개)
    #           - {제품명} ({가격}원 / 수량 : {재고량}개)

    product_no_cat = Product.objects.filter(categories__isnull=True)

    result += '카테고리 미포함'
    for product in product_no_cat:
        result += f'{product.name}, {product.price}, {product.stock}<br>'

    result += '<br><br><br>'

    # 4. 특정 제품에 새 카테고리 추가하기
    product_id = 9
    new_category_name = 'Seasonal'

    # 4-1. get_or_create()와 add()
    # 4-2. 출력 예시 : {제품명} ({카테고리명1}, {카테고리명2}, ...)

    product = Product.objects.get(id=product_id)
    new_category, is_created = Category.objects.get_or_create(name=new_category_name)

    result += f'{new_category}, {is_created}<br>'

    product.categories.add(new_category)
    product_category = product.categories.all()

    result += f'{product.name},<br> ('
    for category in product_category:
        result += f'{category.name}, '
    result += ')<br>'

    result += '<br><br><br>'

    # 5. 모든 카테고리와 각 카테고리의 저품 개수 구하기
    
    # 5-1. 출력 예시
    #       - Categoty {카테고리명}에는 {제품 개수}개의 저품이
    #       - Categoty {카테고리명}에는 {제품 개수}개의 저품이
    #       - Categoty {카테고리명}에는 {제품 개수}개의 저품이

    categories_with_count = Category.objects.annotate(product_count=Count('products'))

    for category in categories_with_count:
        result += f'{category.name}, {category.product_count}<br>'

    result += '<br><br><br>'

    # 6. 여러 카테고리에 속한 제품 구하기

    # 6-1. 출력 예시
    #       - 여러 카테고리에 속한 제품 목록
    #       - {제품명} (Category 개수 : {카테고리 개수})
    #       - {제품명} (Category 개수 : {카테고리 개수})
    #       - {제품명} (Category 개수 : {카테고리 개수})

    product_with_categories = Product.objects.annotate(cat_count=Count('categories')).filter(cat_count__gt=1)

    for product in product_with_categories:
        result += f'{product.name}, {product.cat_count}<br>'


    return HttpResponse(result)