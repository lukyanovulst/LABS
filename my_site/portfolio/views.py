from django.http import HttpResponse

def render_page(title: str, content: str) -> HttpResponse:
    html = f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <title>{title} — Сергей Лукьянов</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin:0; background:#f4f6fb; color:#222; }}
    header {{ background:#1f6feb; color:white; padding:22px 15px; text-align:center; }}
    header h1 {{ margin:0; font-size:26px; }}
    nav a {{ color:white; margin: 0 8px; text-decoration:none; font-weight:600; }}
    nav a:hover {{ text-decoration:underline; }}
    .container {{ max-width:1000px; margin:28px auto; background:white; padding:22px;
                 box-shadow:0 6px 20px rgba(0,0,0,0.06); border-radius:10px; }}
    h2 {{ color:#1b3a8a; }}
    footer {{ text-align:center; padding:14px; color:#666; margin:18px 0 30px; }}
  </style>
</head>
<body>
  <header>
    <h1>Сергей Лукьянов</h1>
    <nav>
      <a href="/">Главная</a> |
      <a href="/about/">Обо мне</a> |
      <a href="/skills/">Навыки</a> |
      <a href="/projects/">Проекты</a> |
      <a href="/contacts/">Контакты</a>
    </nav>
  </header>

  <div class="container">
    {content}
  </div>

  <footer>© 2025 Сергей Лукьянов — студент УЛГТУ (ИСТбд-23)</footer>
</body>
</html>"""
    return HttpResponse(html)


def home(request):
    return render_page("Главная", """
        <h2>Добро пожаловать!</h2>
        <p>Привет! Этот сайт создан как моя личная визитка. Здесь можно узнать обо мне,
        моих интересах, учебе, навыках и проектах. Я студент УЛГТУ, и IT для меня —
        не просто учеба, а настоящее увлечение.</p>
    """)

def about(request):
    return render_page("Обо мне", """
        <h2>Обо мне</h2>
        <p>Меня зовут <b>Сергей Лукьянов</b>, мне 21 год. Учусь в <b>УЛГТУ</b>,
        группа <b>ИСТбд-23</b>. С детства увлекаюсь компьютерами, сначала играми,
        потом заинтересовался, как они устроены. Так я пришёл в программирование.</p>
    """)

def skills(request):
    return render_page("Навыки", """
        <h2>Мои навыки</h2>
        <ul>
            <li>Python (Django, алгоритмы, учебные проекты)</li>
            <li>C++ (алгоритмы, учебные проекты)</li>
            <li>C#</li>
            <li>HTML немного</li>
        </ul>
        <p>Люблю учиться новому и пробовать технологии на практике.</p>
    """)

def projects(request):
    return render_page("Проекты", """
        <h2>Мои проекты</h2>
        <ul>
            <li>Этот сайт-визитка на Django</li>
            <li>Лабораторные работы на C++ </li>
            <li>лабораторные работы (Python)</li>
            <li>Учебные программы на C#</li>
        </ul>
        <p>Хочу развиваться и участвовать в реальных коммерческих проектах.</p>
    """)

def contacts(request):
    return render_page("Контакты", """
        <h2>Контакты</h2>
        <p>Связаться со мной можно так:</p>
        <ul>
            <li>Email: sergey@mail.ru</li>
            <li>Telegram: sergey@tg.com</li>
            <li>GitHub: github.com/sergey-ulstu</li>
        </ul>
    """)

