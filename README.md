پروژه دانشگاه این بود که یک سیستم مدیریت دستور پخت بسازیم، من هم برای یادگیری restframework رو انتخاب کردم



میدونم هیچ وقت هیچ کس از این استفاده نمیکنه ولی خب بدون داکیومنت نمیشه ...


ابتدا یک محیط امن برای اجرای برنامه بسازید
```
python -m venv venv
source venv/bin/activate
```
نیازمندی ها را نصب کنید
```
pip install -r requirements.txt
```
سرور را اجرا کنید
```
python manage.py runserver
```


این پروژه هم زمان یک صفحه ادمین برای مدیریت و یک api را اجرا میکند

برای استفاده از ادمین صفحه زیر را در مرورگر خود باز کنید:
http://127.0.0.1:8000/admin
از admin برای یوزر و پسورد استفاده کنید

راهنمای api :


```
material data model : {
    id:int # readonly
   ,name:cahr(max:20)
}
recipe data model : {
    id:int # readonly
   ,name:char(max:20)
   ,review:char(max:100)
   ,describtion:str
   ,enerjy:int
   ,materials:[
    int # id of material
    ]
}

recipe_query data model : {
    name: str # if is in a part of name     @optional
    ,desc: str # if is in a part of describtion @optional
    ,review: str # if is in a part of review  @optional
    ,min_enerjy: int                                    @optional  
    ,max_enerjy: int                              @optional
    ,materials: [int] # if recipe contains all of materials   @optional
}

GET: /material # list all materials
GET: /material/{int:pk} # show a specefic material
DELETE: /material/{int:pk} # delete a specefic material
PUT: /material/{int:pk} data:material # change a specefic matrial
POST: /material/ data:material # create a material and shows that

GET: /recipe # list all recipes
GET: /material/{int:pk} # show a specefic recipe
DELETE: /material/{int:pk} # delete a specefic recipe
PUT: /material/{int:pk} data:recipe # change a specefic recipe
POST: /material/ data:recipe # create a recipe and shows that

GET: /material/q data:recipe_query # list recipes filtered by queryset
```