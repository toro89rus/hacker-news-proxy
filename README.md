# Hacker™ News proxy

Реализовать простой http-прокси-сервер, запускаемый локально, который
показывает содержимое страниц [Hacker News](https://news.ycombinator.com).
Прокси должен модицифировать текст на страницах следующим образом: после
каждого слова из шести букв должен стоять значок «™». Пример™:

Исходный текст: `https://news.ycombinator.com/item?id=13713480`

``` text
The visual description of the colliding files, at
http://shattered.io/static/pdf_format.png, is not very helpful
in understanding how they produced the PDFs, so I took apart
the PDFs and worked it out.

Basically, each PDF contains a single large (421,385-byte) JPG
image, followed by a few PDF commands to display the JPG. The
collision lives entirely in the JPG data - the PDF format is
merely incidental here. Extracting out the two images shows two
JPG files with different contents (but different SHA-1 hashes
since the necessary prefix is missing). Each PDF consists of a
common prefix (which contains the PDF header, JPG stream
descriptor and some JPG headers), and a common suffix (containing
image data and PDF display commands).
```

Через ваш прокси™: `http://127.0.0.1:8232/item?id=13713480`

``` text
The visual™ description of the colliding files, at
http://shattered.io/static/pdf_format.png, is not very helpful
in understanding how they produced the PDFs, so I took apart
the PDFs and worked™ it out.

Basically, each PDF contains a single™ large (421,385-byte) JPG
image, followed by a few PDF commands to display the JPG. The
collision lives entirely in the JPG data - the PDF format™ is
merely™ incidental here. Extracting out the two images™ shows two
JPG files with different contents (but different SHA-1 hashes™
since the necessary prefix™ is missing). Each PDF consists of a
common™ prefix™ (which contains the PDF header™, JPG stream™
descriptor and some JPG headers), and a common™ suffix™ (containing
image data and PDF display commands).
```

Условия:

* последняя версия™ Python™
* страницы должны™ отображаться и работать полностью корректно, в точности так,
  как и оригинальные (за исключением модифицированного текста™);
* при навигации по ссылкам, которые ведут на другие™ страницы HN, браузер
  должен™ оставаться на адресе™ вашего™ прокси™;
* можно использовать любые общедоступные библиотеки, которые сочтёте нужным™;
* чем меньше™ кода, тем лучше. PEP8 — обязательно;
* если в условиях вам не хватает каких-то данных™, опирайтесь на здравый смысл.

Если задачу™ удалось сделать быстро™, и у вас еще остался энтузиазм - как
насчет™ написания тестов™?

Присылайте ваше решение в виде ссылки™ на gist или на публичный репозиторий на
GitHub™.

## Implementation

Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

Features:
Proxy for a target site (tested with <https://news.ycombinator.com>; behaviour may vary for other sites).

Modifies page text by appending a symbol (e.g. ™) to words of a configurable length.

Preserves cookies and session flow so authentication works via the proxy.

Rewrites internal absolute links to relative ones so navigation stays inside the proxy.

Serves non-HTML resources (images, JS, etc.) unchanged.

### Installation

Make sure [uv](https://docs.astral.sh/uv) is installed. If not - install uv using curl

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Download proxy and install dependencies

```bash
git clone https://github.com/toro89rus/hacker-news-proxy.git
cd hacker_news_proxy
make install
```

### Configuration

Copy the example env file and edit values as needed:

```bash
cp .env.example .env
```

Main configuration variables (in .env):

```env
# URL of the site the proxy will fetch and modify
TARGET_URL=https://news.ycombinator.com

# Symbol to append after words of given length
SYMBOL=™

# Word length to modify (integer)
WORD_LEN=6

# Port the local proxy will listen on
PORT=8000

```

You can also override them on the command line for a single run:

```bash
TARGET_URL=https://example.com SYMBOL='™' WORD_LEN=5 make start
```

### Run (development)

Start with the Makefile (uses uv/project tooling):

```bash
make start
```

After start, open the proxy should be aviable at:

```cpp
http://0.0.0.0:8000/
```

### To-Do list

-Full type-annotation and docstrings
-Docker containerization
