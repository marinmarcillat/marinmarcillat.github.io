---
layout: default
---

# Elma blog

*Work in progress, testing possibilities*

## Billets de blog

[First](./new_page.md)

{% for tag in site.tags %}
  <h3>{{ tag[0] }}</h3>
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.date | date: "%B %Y" }} - {{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}

## Atelier




