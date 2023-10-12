import re
from unidecode import unidecode

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim='-'):
    """生成仅包含ASCII字符的slug。"""
    result = []
    for word in _punct_re.split(text.lower()):
        print(word, end='&')
        result.extend(unidecode(word).lower().split())
        print(result)
    return delim.join(result)


if __name__ == '__main__':
    text = "邻家的豆豆龙"
    slug = slugify(text)
    print(slug)  # 输出: ni-hao-shi-jie-ni-hao-ma
