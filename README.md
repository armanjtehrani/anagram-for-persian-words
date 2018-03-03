برای اجرای این برنامه تنها نیاز به پایتون ورژن 3 دارید که می توانید از طریق لینک زیر دانلود کنید

https://www.python.org/downloads/release/python-364/

جهت اجرای برنامه دستور زیر را اجرا کنید

python3 main.py

بانک لغات برای این تکلیف به همراه آقای امیررضا عمویی و از لینک زیر پیدا شد

https://github.com/reza1615/Persian-Spell-checker

برای پیاده سازی این تکلیف از 4روش جست و جوی خطی، یک الگوریتم مشابه بی تری، هشینگ پایتون و یک روش هش دیگر برای پیدا کردن آناگرام ها استفاده شده است که در هنگام استفاده می توان زمان ساخت و جست و جوی این الگوریتم ها را بایکدیگر مقایسه کرد

بهترین روش برای پیدا کردن آناگرام های یک کلمه، روش چهارم می باشد. در این روش، برای هر کاراکتر منحصر به فرد یک عدد اول خاص در نظر گرفته می شود و هش آن کلمه و تمامی آناگرام های آن کلمه برابر با ضرب اعداد اول است.  تمامی آناگرام های یک کلمه در یک هش جا می شوند و بجز این آناگرام ها هیچ کلمه دیگری نمی تواند در آنجا جا شود. این سریعتر روش پیدا کردن آناگرام های یک لغت است.
 این روش را بنده با آقای هادی شامغلی به نتیجه رسیدیم.
درصورت درنظر نگرفتن روش چهارم، هشینگ پایتون سریعترین روش جست و جو برای پیدا کردن یک آناگرام در میان داده ها است. اما ایندکس کردن اطلاعات این امکان را به ما می دهد تا پیش از ساخته شدن کامل یک لغت بتوان متوجه شد که آن لغت در بانک لغات وجود دارد یا خیر که درصورت عدم وجود، تعداد زیادی از درخواست ها حذف می شوند.
به طور کلی در هنگام اجرای برنامه برای لغات طولانی، الگوریتم دوم عملکرد بهتری نسبت به هشینگ پایتون ایفا می کند و درغیر این صورت هشینگ پایتون می تواند الگوریتم مناسبتری باشد. مخصوصا که زمان مورد نیاز برای ایندکس کردن اولیه اطلاعات در الگوریتم شماره 2 بسیار بیشتر از زمان موردنیاز برای هش کردن لغات است.

